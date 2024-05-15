import pymongo

client = pymongo.MongoClient("mongodb+srv://gourab:722133@cluster0.zxpcqgz.mongodb.net/")
db = client["Youtube_Manager"]
video_Collection = db["videos"]

def list_all_videos():
    print("\nListing all favorite videos:")
    for video in video_Collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video():
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    video_Collection.insert_one({"name": name, "time": time})
    print("Video added successfully!")

def update_video():
    video_id = input("Enter video ID to update: ")
    name = input("Enter updated video name: ")
    time = input("Enter updated video time: ")
    video_Collection.update_one({'_id': video_id}, {'$set': {"name": name, "time": time}})
    print("Video updated successfully!")

def delete_video():
    video_id = input("Enter video ID to delete: ")
    video_Collection.delete_one({"_id": video_id})
    print("Video deleted successfully!")

def main():
    while True:
        print("\n ----------YOUTUBE MANAGER----------")
        print('1. List all favorite videos')
        print('2. Add a video to the list')
        print('3. Update a video in the list')
        print('4. Delete a video from the list')
        print('5. EXIT')
        print('Enter the number of your choice:')
        selection = input("> ")

        if selection == '1':
            list_all_videos()
        elif selection == '2':
            add_video()
        elif selection == '3':
            update_video()
        elif selection == '4':
            delete_video()
        elif selection == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print('Invalid input. Please enter a valid option.')

if __name__ == "__main__":
    main()
