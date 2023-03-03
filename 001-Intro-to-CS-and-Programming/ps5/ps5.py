# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Trevor KM
# Collaborators: None
# Time: 8-hours

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
import datetime
from datetime import datetime
import pytz

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================


def process(url):
  """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
  feed = feedparser.parse(url)
  entries = feed.entries
  ret = []
  for entry in entries:
    guid = entry.guid
    title = translate_html(entry.title)
    link = entry.link
    description = translate_html(entry.description)
    pubdate = translate_html(entry.published)

    try:
      pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
      pubdate.replace(tzinfo=pytz.timezone("GMT"))
    #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
    #  pubdate.replace(tzinfo=None)
    except ValueError:
      pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

    newsStory = NewsStory(guid, title, description, link, pubdate)
    ret.append(newsStory)
  return ret


#======================
# Data structure design
#======================

# Problem 1

## MY CODE BELOW ##

## NewsStory Class ##
### COMPLETE ###


class NewsStory:
  "Processes change for single News Story (item) objects"

  ## constructor ##
  def __init__(self, guid, title, description, link, pubdate):
    self.guid = guid
    self.title = title
    self.description = description
    self.link = link
    self.pubdate = pubdate

  ## getter methods ##
  def get_guid(self):
    return self.guid

  def get_title(self):
    return self.title

  def get_description(self):
    return self.description

  def get_link(self):
    return self.link

  def get_pubdate(self):
    return self.pubdate


#======================
# Triggers
#======================


class Trigger(object):

  def evaluate(self, story):
    """
    Returns True if an alert should be generated
    for the given news item, or False otherwise.
    """
    # DO NOT CHANGE THIS!
    raise NotImplementedError


# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger
## IN PROGRESS ##


class PhraseTrigger(Trigger):

  def __init__(self, phrase):
    self.phrase = phrase.lower()  # string phrase
    ## UNIT TEST ##
    # print("Datatype of `phrase`:",type(self.phrase))
    # print("")

  def is_phrase_in(self, source_txt):  ## TESTING ALT VERSION OF FUNCTION ###

    ##### Clean source text #####

    # build string with alpha-only chars, join " " for all special chars
    txt_stripped = ""
    for char in source_txt.lower():
      txt_stripped += char if char not in string.punctuation else " "

    # split and (re)join text list elements to standardize " " chars
    txt_cleaned = " ".join(txt_stripped.split()) + " "

    ##### Clean phrase parameter text #####

    # split and (re)join text list elements to standardize " " chars
    phrase_stripped = ""
    for char in self.phrase.lower():
      phrase_stripped += char if char not in string.punctuation else " "

    phrase_cleaned = " ".join(phrase_stripped.split()) + " "

    ##### Check if phrase in source text #####

    if phrase_cleaned in txt_cleaned:
      return True
    else:
      return False


# Problem 3
# TODO: TitleTrigger
## IN PROGRESS ##
class TitleTrigger(PhraseTrigger):

  def evaluate(self, story):
    title = story.get_title()
    return super().is_phrase_in(title)


# Problem 4
# TODO: DescriptionTrigger
## IN PROGRESS ##
class DescriptionTrigger(PhraseTrigger):

  def evaluate(self, story):
    desc = story.get_description()
    return super().is_phrase_in(desc)


# TIME TRIGGERS
# Problem 5
# TODO: TimeTrigger


class TimeTrigger(Trigger):
  "Trigger objects that are triggered by time conditions"

  def __init__(self, time):
    # Constructor:
    #        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
    #        Convert time from string to a datetime before saving it as an attribute.

    # https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior
    # https://vinta.ws/code/timezone-in-python-offset-naive-and-offset-aware-datetimes.html
    # will try/except offset-aware vs offset-naive...
    # datetime objects in .evaluate methods
    format = "%d %b %Y %H:%M:%S"
    time = datetime.strptime(time, format)  # change format
    self.time = time


# Problem 6
# TODO: BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):

  def evaluate(self, story):
    pubdate = story.get_pubdate()
    try:
      condition = pubdate < self.time
    except:
      # adjust for offset aware vs offset naive incompatibility
      self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
      condition = pubdate < self.time

    ### check condition and return ###
    if condition:
      return True
    else:
      return False


class AfterTrigger(TimeTrigger):

  def evaluate(self, story):
    pubdate = story.get_pubdate()
    try:
      condition = pubdate > self.time
    except:
      # adjust for offset aware vs offset naive incompatibility
      self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
      condition = pubdate > self.time

    ### check condition and return ###
    if condition:
      return True
    else:
      return False


# COMPOSITE TRIGGERS


# Problem 7
# TODO: NotTrigger
## IN PROGRESS ##
class NotTrigger(Trigger):

  def __init__(self, T):
    """:not_trg: other Trigger object to test against"""
    self.T = T

  def evaluate(self, story):
    return not self.T.evaluate(story)


# Problem 8
# TODO: AndTrigger
class AndTrigger(Trigger):

  def __init__(self, T1, T2):
    self.T1 = T1
    self.T2 = T2

  def evaluate(self, story):
    return self.T1.evaluate(story) and self.T2.evaluate(story)


# Problem 9
# TODO: OrTrigger
class OrTrigger(Trigger):

  def __init__(self, T1, T2):
    self.T1 = T1
    self.T2 = T2

  def evaluate(self, story):
    return self.T1.evaluate(story) or self.T2.evaluate(story)


#======================
# Filtering
#======================


# Problem 10
def filter_stories(stories, triggerlist):
  """
  Takes in a list of NewsStory instances.
  Returns: a list of only the stories for which a trigger in triggerlist fires.
  """
  # TODO: Problem 10
  # https://docs.python.org/3/library/functions.html#any
  stories_filtered = []
  for story in stories:
    if any([T.evaluate(story) for T in triggerlist]):
      stories_filtered.append(story)

  return stories_filtered


print("")


#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
  """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
  # We give you the code to read in the file and eliminate blank lines and
  # comments. You don't need to know how it works for now!
  trigger_file = open(filename, 'r')
  lines = []
  for line in trigger_file:
    line = line.rstrip()
    if not (len(line) == 0 or line.startswith('//')):
      lines.append(line)

  # TODO: Problem 11
  # line is the list of lines that you need to parse and for which you need
  # to build triggers

  # Return a list of triggers specified by configuration (.txt) file

  ### DICT with trigger name keys ###
  trig_map = {
    "TITLE": TitleTrigger,
    "DESCRIPTION": DescriptionTrigger,
    "AFTER": AfterTrigger,
    "BEFORE": BeforeTrigger,
    "NOT": NotTrigger,
    "AND": AndTrigger,
    "OR": OrTrigger
  }

  ### helper function defn: line_parse ###
  trig_dict = {}  # line parsing container
  trig_list = []  # return container

  def line_parse(line):
    """takes a line from trigger config .txt file,
    builds list of triggers specified"""

    ldata = line.split(',')  # deconstruct csv line format
    if ldata[0] != "ADD":
      if ldata[1] == "OR" or ldata[1] == "AND":
        trig_dict[ldata[0]] = trig_map[ldata[1]](trig_dict[ldata[2]],
                                                 trig_dict[ldata[3]])
      else:
        trig_dict[ldata[0]] = trig_map[ldata[1]](ldata[2])
    else:
      trig_list[:] += [trig_dict[t] for t in ldata[1:]]

    ### loop with line_parse func to build return list ###
    for line in lines:
      line_parse(line)  # builds trigger list line by line

    return trig_list


SLEEPTIME = 120  #seconds -- how often we poll


def main_thread(master):
  # A sample trigger list - you might need to change the phrases to correspond
  # to what is currently in the news
  try:
    t1 = TitleTrigger("election")
    t2 = DescriptionTrigger("Trump")
    t3 = DescriptionTrigger("Clinton")
    t4 = AndTrigger(t2, t3)
    triggerlist = [t1, t4]

    # Problem 11
    # TODO: After implementing read_trigger_config, uncomment this line
    triggerlist = read_trigger_config('triggers.txt')

    # HELPER CODE - you don't need to understand this!
    # Draws the popup window that displays the filtered stories
    # Retrieves and filters the stories from the RSS feeds
    frame = Frame(master)
    frame.pack(side=BOTTOM)
    scrollbar = Scrollbar(master)
    scrollbar.pack(side=RIGHT, fill=Y)

    t = "Google & Yahoo Top News"
    title = StringVar()
    title.set(t)
    ttl = Label(master, textvariable=title, font=("Helvetica", 18))
    ttl.pack(side=TOP)
    cont = Text(master, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
    cont.pack(side=BOTTOM)
    cont.tag_config("title", justify='center')
    button = Button(frame, text="Exit", command=root.destroy)
    button.pack(side=BOTTOM)
    guidShown = []

    def get_cont(newstory):
      if newstory.get_guid() not in guidShown:
        cont.insert(END, newstory.get_title() + "\n", "title")
        cont.insert(
          END,
          "\n---------------------------------------------------------------\n",
          "title")
        cont.insert(END, newstory.get_description())
        cont.insert(
          END,
          "\n*********************************************************************\n",
          "title")
        guidShown.append(newstory.get_guid())

    while True:

      print("Polling . . .", end=' ')
      # Get stories from Google's Top Stories RSS news feed
      stories = process("http://news.google.com/news?output=rss")

      # Get stories from Yahoo's Top Stories RSS news feed
      stories.extend(process("http://news.yahoo.com/rss/topstories"))

      stories = filter_stories(stories, triggerlist)

      list(map(get_cont, stories))
      scrollbar.config(command=cont.yview)

      print("Sleeping...")
      time.sleep(SLEEPTIME)

  except Exception as e:
    print(e)


print("")

##############################################
### COMMENTED OUT FOR Replit FUNCTIONALITY ###
##############################################
if __name__ == '__main__':
  root = Tk()
  root.title("Some RSS parser")
  t = threading.Thread(target=main_thread, args=(root, ))
  t.start()
  root.mainloop()

# root = Tk()
# root.title("Some RSS parser")
# t = threading.Thread(target=main_thread, args=(root, ))
# t.start()
# root.mainloop()
