#!/usr/bin/python3

from pymongo import MongoClient, errors
import os

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.sssb7.mongodb.net/"
client = MongoClient(uri, username='DS2022', password=MONGOPASS, connectTimeoutMS=200, retryWrites=True)

# Create new collection
thisdb = client.cxx6sw
fall2024 = thisdb.fall2024
count = fall2024.count_documents({})

# Create Documents
class_one = {
  "name": "Computational Probability",
  "course": ["DS", 2026],
  "details": {
    "day": ["Tuesday", "Thursday"],
    "time": "9:30 AM",
    "location": "Data Science Building Room 206"
  }, 
  "professor": "Thomas Stewart"
}

class_two = {
  "name": "Systems 1: Intro to Computing",
  "course": ["DS", 2022],
  "details": {
    "day": ["Tuesday", "Thursday"],
    "time": "11:00 AM",
    "location": "Data Science Building Room 306"
  }, 
  "professor": "Neal Magee"
}


class_three = {
  "name": "Writing and Critical Inquiry",
  "course": ["ENWR", 1510],
  "details": {
    "day": ["Monday", "Wednesday", "Friday"],
    "time": "9:00 AM",
    "location": "Bryan Hall 310"
  }, 
  "professor": "Jeddie Sophronius"
}

class_four = {
  "name": "Colonial Latin American History",
  "course": ["HILA", 2001],
  "details": {
    "day": ["Monday", "Wednesday"],
    "time": "1:00 PM",
    "location": "Gilmer Hall 257"
  }, 
  "professor": "Thomas Klubock", 
  "discussion": {
    "details": {
    "day": ["Thursday"],
    "time": "6:00 PM",
    "location": "New Cabell Hall 368"
    }, 
    "TA": "Aoife Hufford"
  }
}

class_five = {
  "name": "Intro to Social Psychology",
  "course": ["PSYC", 2600],
  "details": {
    "day": ["Monday", "Wednesday"],
    "time": "2:00 PM",
    "location": "Chemistry Bldg 402"
  }, 
  "professor": "Jennifer MacCormack"
}

# Insert Records
fall2024.insert_many([class_one, class_two, class_three, class_four, class_five])

# Display Documents
lookup_query = {"details.day": "Monday"}
find = fall2024.find(lookup_query)
print("I have these classes on Monday:" + find)
