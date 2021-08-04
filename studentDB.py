#import the MongoDB Library
from pymongo import MongoClient
#using this to make a delay!
import time
#connection string to MongoDB Atlas make sure you have created a cluster 
client = MongoClient("mongodb+srv://huwhuw:huwhuw@cluster0.knbmj.mongodb.net/student_db?retryWrites=true&w=majority")
#get the records currently in the DB
db = client.get_database('student_db')
records = db.student_record

print("There are currently:", records.count_documents({}), "records")

# Heres my make choice function
def makeChoice():
    result = int(input("What do you wish to do? \n\tInsert Record(1) \n\tView Records (2) \n\tDelete record(3)\n\t: "))
    if result == 1:
        insertRecord()
    else:
        print("Incorrect response, Make another choice\n")
        time.sleep(3)
        makeChoice()
        
# Heres my insert record function
def insertRecord():
    name = input("Enter name: ")
    age = input("Enter age: ")
    stuClass = input("Enter class: ")

    new_student = {
        'name': name,
        'age': age,
        'class': stuClass
    }
    records.insert_one(new_student)
    print("There are now:", records.count_documents({}), "records")
    makeChoice()

makeChoice()
#


# output = list(records.find())
# print (output)

