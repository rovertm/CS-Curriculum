
### The Assignment ###


"""

Write Python code that processes a .zip file of newspaper images,
identifies faces and text with OCR tools, then enables a text search function
that renders contact sheet images with relevant results.

e.g. searching the keyword 'Mark' would display contact sheets
with faces identified on a newspaper clipping where the keyword 'Mark' was found.

This project was my submission for the Python 3 Programming specialization capstone
for the University of Michigane | Coursera program.

"""

#### Project code below - adapted from .ipynb ####


# In[1]:


from zipfile import ZipFile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np
import math
import itertools

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

# In[2]:


###########################################
### get_text helper function ###
###########################################

def get_text(img_pil):
    """extracts text from opened PIL image via pytesseract"""
    return pytesseract.image_to_string(img_pil)


# In[3]:


###########################################
### get_faces helper function ###
###########################################

def get_faces(cv_image, gs_image):
    """
    extracts faces via bounding boxes, pastes them to a contact sheet
    
    :param: cv_image, PIL image 
    :param: grayscaled_image, converted image to grayscale
    :returns: contact sheet object
    
    """
    
    # get bounding boxes - cv package's detectMultiScale
    bounding_boxes = face_cascade.detectMultiScale(gs_image, 1.3, 5)
    
    # face image thumbnail container
    faces = []
    # crop images - if not empty
    if len(bounding_boxes)>0:
        # init contact sheet to paste to
        contact_sheet = Image.new(cv_image.mode, (100 * 5, 100 * int(math.ceil(len(bounding_boxes)/5.0))))
        boxes_positions = zip(bounding_boxes, itertools.product(range(0,contact_sheet.height,100),range(0,contact_sheet.width,100)))  
        # loop through each face, i.e. bounding box in bounding_boxes
        for [x,y,w,h], position in boxes_positions:
            # crop face via box coordinates
            face = cv_image.crop((x,y,x+w,y+h))
            # create thumbnail for face
            face.thumbnail((100,100),Image.ANTIALIAS)
            # append face thumbnail image to list storage
            faces.append(face)
            # past face to contact sheet
            contact_sheet.paste(face, position[::-1])
        
        
    # return contact sheet of faces
    return contact_sheet
            


# In[6]:



###################################
####### process_zip_images #######
###################################


def process_zip_images(zip_file):
    
    """

    :param: zip_file >> a single zip file
    :returns: list(dict()) >> single list of nested dictionaries for each image file
    :example: >> [ {"file_name": f_name, "file_image": f_image, "file_text": f_text} ]

    """
    
    # init list to return list of dicts
    image_data = []

    # process zip file
    with ZipFile(zip_file, 'r') as zfile:
        # https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.infolist
        img_files = zfile.infolist()
        # loop through all files 
        for img_file in img_files:
            # open the each image file
            with zfile.open(img_file.filename) as img_raw:

                # 1 -- pre-process image with PIL, numpy array and cv
                img_pil = Image.open(img_raw) # open image with PIL
                img_array = np.asarray(img_pil)
                img_array_gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY) # greyscale # https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html                
                
                
                # 2 -- nested text and image extraction functions
                ## get text
                try:
                    text_data = get_text(img_pil)
                except:
#                     print("ExceptionError with get_text function")
                    text_data = None
     
                ## get face images
                try:
                    # get face images, returns contact sheet
                    face_sheet = get_faces(img_pil, img_array_gray)
                except:
#                     print("ExceptionError with get_faces function")
                    face_sheet = None



                # append dict of image data to list
                image_data.append({"file_name": img_file.filename,
                                   "face_images": face_sheet, 
                                   "image_text": text_data})

    
    return image_data


# In[7]:


###################################
####### search_image_text #######
###################################

def search_image_text(file_data, keyword):
    
    """
    return contact sheets for news files where "keyword" was found

    :param: image_file_data : list of dictionaries of parsed image file data, including contact sheets
    :param: keyword: str word to search for in image file
    :returns: prints result file name, displays contact sheet, returns NONE
    """
    
    for file_dict in file_data:
        if keyword in file_dict["image_text"]:
            # print out response
            print(f"Result found in file {file_dict['file_name']}")
            # check if image AND text were found
            if file_dict["face_images"] == None:
                  print("But there were no faces in that file!")
            else: display(file_dict["face_images"])
                  

###########################            
##### Results Testing #####
###########################

# ### Output test on small_img.zip -- "Christopoher" keyword

# In[59]:


sample_file = "readonly/small_img.zip"
sample_output = process_zip_images(sample_file)


# In[62]:


search_image_text(sample_output, "Christopher")


# ### Output test on images.zip -- "Mark" keyword

# In[8]:


full_file = "readonly/images.zip"
full_output = process_zip_images(full_file)


# In[9]:


search_image_text(full_output, "Mark")


################################
###### End project code ######
################################




