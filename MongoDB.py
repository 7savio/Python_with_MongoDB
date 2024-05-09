from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://MongoDBpy:MongoDBpy@cluster0.crrws8f.mongodb.net/")  #Not a good idea to include ID and password in code files.

print(client)

db = client["Mongo"]
video_collection = db["videos"]

print(video_collection)


def list_videos():
       for video in video_collection.find():
            print(f"ID : {video['_id']}, Name : {video['name']} and Time : {video['time']}")

def add_videos(name, time):
     video_collection.insert_one({"name":name, "time":time})       

def update_videos(video_id, new_name, new_time):
       video_collection.update_one(
            {"_id" : ObjectId (video_id)},
            {"$set" : {"name" : new_name, "time" : new_time}}
        )

def delete_videos(video_id):
     try:
        result = video_collection.delete_one({"_id" : ObjectId(video_id)})  
     except Exception as e:
          print("An error occurred: ",e) 

def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit the App")
        choice = input("Enter your Choice:- ")


        if choice == "1":
            list_videos()

        elif choice == "2":
            name = input("Enter the name of the video:- ")
            time = input("Enter the time of the video:- ")
            add_videos(name, time)

        elif choice == "3":
            video_id = input("Enter video_id to Update:- ")
            name = input("Enter the name of the video:- ")
            time = input("Enter the time of the video:- ")
            update_videos(video_id, name, time)
    
        elif choice == "4":
            video_id = input("Enter video_id to Delete:- ")
            delete_videos(video_id)
        
        elif choice == "5":
            break

        else:
            print("Invalid selected videos")        

if __name__ == "__main__":
    main()        

