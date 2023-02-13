""" Final Project """

#################
#### READ ME ####
#################

"""
This .py script was built as part as part of the final project 
for UM | Coursera Data Collection and Processing course - part of the UM Python 3 Programming Specialization

The functions make requests to two APIs and ultimately return a sorted list 
of related movie titles by their respective Rotten Tomatoes score.

**Note: for this project we used cached .txt files and did NOT make live requests.
requests_with_caching is the stand-in module to support this functionality for the course

All the work is my own and built for academic purposes.

"""

### PART I FUNCTIONS ###

import requests_with_caching
import json

def get_movies_from_tastedive(query):

    '''
    Param: query: string of movie
    Output: Dictionary (json) of 5 similar movies
    '''
    params = {'q': query, 'type': 'movies', 'limit': 5 }
    base = "https://tastedive.com/api/similar"

    res_obj = requests_with_caching.get(base, params)
    
    text_res = res_obj.text
    
    json_res = json.loads(text_res)
    
    
    return json_res

def extract_movie_titles(json_obj):
  """
  Param: json_obj: Python object of TasteDive response
  Returns: List of movie titles
  """

  #movie_titles = [res[0]["Name"] for res in json_obj['Results']]
  movie_results = json_obj['Similar']['Results']
  movie_titles = [res['Name'] for res in movie_results]
  return movie_titles

def get_related_titles(movie_list):

  """
  param: movie list
  Return: list of movies
  
  """

  # output storage to update
  result_list = []

  for movie in movie_list:
    json_obj = get_movies_from_tastedive(movie)
    related_movies = extract_movie_titles(json_obj)

    # append if not in results list already
    for rmovie in related_movies:
      if rmovie not in result_list:
        result_list.append(rmovie)

  return result_list


### PART II FUNCTIONS ###

def get_movie_data(movie):
  """
  takes a string of movie to search
  return a dictionary with info about movie
  """

  # define base url
  base = "http://www.omdbapi.com/"
  # define params 
  params = {'t': movie, 'r': 'json'}

  # request to api
  res_obj = requests_with_caching.get(base, params)
  
  # extract json
  json_res = res_obj.json()
  # type cast dict
  dict_res = dict(json_res)
  
  # print(dict_res)
  

  return dict_res


def get_movie_rating(movie_dict):
  """
  param: movie_dict from OMBD
  return: Rotten Tomatoes rating
  """

  # Rotten tomatoes rating
  ratings_lst = movie_dict['Ratings']
  print(ratings_lst)
  rt_rating = 0

  for rating in ratings_lst:
    if rating['Source'] == 'Rotten Tomatoes':
      rt_rating = int(rating['Value'].replace('%',''))
      break
    else: rt_rating = 0

  return rt_rating

def get_sorted_recommendations(movie_list):
  """
  params: list of movie titles
  returns: sorted list of related movie titles **up to 5** for each title
  constraints: sorted in descending order by Rotten Tomatoes rating && ties broke in alpha order
  """

  # PART I -- get 5-related titles
  related_titles = get_related_titles(movie_list) # returns 5 related titles

  # Part II -- get rotten tomatoe score for each title

  # Init result dict to sort, default rt_score as 0
  res_dict = {title: get_movie_rating(get_movie_data(title)) for title in related_titles}

  # print to inspect
  print(res_dict)

  # Part III -- sort by rt_value, THEN by alpha if a tie -- specified in lambda
  sorted_lst = sorted(res_dict.items(), key = lambda x: (x[1],x[0]), reverse=True)

  # return sorted list, i.e. keys

  return [movie[0] for movie in sorted_lst]
