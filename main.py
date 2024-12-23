'''

Yang Buat: Mary

'''


from BST import BST
from Video import Video
from Queue import Queue
from Graph import Recommendation
from QueueHistory import QueueHistory

def main_menu():
    current_video = None  # Current video placeholder

    videos = BST()
    recommendation = Recommendation()
    queue = Queue()
    queueHistory = QueueHistory()

    # Sample video data
    video1 = Video('Video1', ['tag1','tag2','tag3'], 'This is Video1', 60)
    video2 = Video('Video2', ['tag2','tag3'], 'This is Video2', 60)
    video3 = Video('Video3', ['tag1'], 'This is Video3', 60)

    # Insert sample videos into BST and Recommendation graph
    videos.insert(video1)
    videos.insert(video2)
    videos.insert(video3)
    recommendation.addVideo(video1)
    recommendation.addVideo(video2)
    recommendation.addVideo(video3)

    print(videos)
    print(recommendation)

    while True:
        title = None
        print("WELCOME TO STREAMTREE")
        print("\nMenu:")
        print("1. Add video")                   #nambah video ke videos(BST) dan recommendation(Graph)
        print("2. Remove video")                #remove video dari videos(BST) dan recommendation(Graph)
        print("3. Play Video")                  #search from videos(BST) dan save ke current_video
        print("4. Play next")                   #Play next in queue
        print("5. Find recommended")            #From current_video display recommended
        print("6. Add video ke Queue")          #nambah video dalam queue
        print("7. Remove video dari Queue")     #bisa remove video apapun dari queue
        print("8. Display Queue")               #diplay semua video dalam queue
        print("9. Display All Video")           #diplay semua video dalam videos(BST)
        print("10. Display All history")  #diplay semua video dalam queueHistory
        print("11. Clear history")  #diplay semua video dalam queueHistory
        print("0. Exit")
        print()
        if(current_video):
            print(f"\nNow playing: {current_video.title}")
        
        
        try:
            choice = int(input("Pilih menu (Enter the number): "))

            if choice == 1:
                print("\n -- Fungsi Add video ke StreamTree. --")
                title = input("Enter the title of the video: ")
                tags = list(map(str, input("Enter tags for the video (separate tags with space): ").split()))
                description = input("Enter the description of the video: ")
                duration = int(input("Enter the duration of the video (in minutes): "))

                new_video = Video(title, tags, description, duration)

                video = videos.search(title)
                if(video is None):
                    videos.insert(new_video)
                    recommendation.addVideo(new_video)
                    print("\nVideo added successfully!")
                else:
                    print('\nVideo failed to add')
                videos.printAllTree()
                print(recommendation)

            elif choice == 2:
                print("\n -- Fungsi Remove video dari StreamTree. --")
                title = input("Enter the title of the video to remove: ")
                video = videos.search(title)
                if(video):    
                    videos.printAllTree()
                    videos.removeVideo(title)
                    print()
                    videos.printAllTree()
                    recommendation.removeVideo(video)
                    if(current_video is not None and current_video.title == title):
                        current_video = None
                    queue.delete(title,True)
                    
                    print(f"\n{title} removed successfully!")
                    print(videos)
                    
                else:
                    print(f"\n{title} not found in database")

            elif choice == 3:
                print("\n -- Fungsi Play Video. --")
                title = input("Enter the title of the video to play: ")
                current_video = videos.search(title)
                if current_video is None:
                    print("Video not found.")
                    
                    
            elif choice == 4:
                if(queue.is_empty()):
                    print('Queue is still empty!!!')
                    continue
                
                video = queue.dequeue()
                queueHistory.addHistory(video)
                current_video = video


            elif choice == 5:
                print("\n -- Fungsi Find recommended. --")
                if current_video:
                    print(f"\nRecommendations for {current_video.title}:")
                    print(recommendation.getRecommendations(current_video))
                else:
                    print("No video selected. Please play a video first.")

            elif choice == 6:
                print("\n -- Fungsi Add video ke Queue. --")
                title = input("Enter the title of the video to add to the queue: ")
                # Add video to queue (implement your queue logic here)
                video = videos.search(title)
                if (video):
                    queue.enqueue(video)
                else:
                    print(f"{title} not found!!")
                

            elif choice == 7:
                print("\n -- Fungsi Remove video dari Queue. --")
                title = input("Enter the title of the video to remove from the queue: ")
                # Remove video from queue (implement your queue logic here)
                queue.delete(title)
                
            elif choice == 8:
                print("\n -- Displaying queue: --")
                print(queue)

            elif choice == 9:
                print("\n -- Displaying all Video: --")
                print(videos)
                
            elif choice == 10:
                print("\n -- Displaying queue History: --")
                queueHistory.display()
                
            elif choice == 11:
                queueHistory.clear()

            elif choice == 0:
                print(" -- Terima kasih sudah menggunakan StreamTree. Sampai jumpa! -- ")
                break

            else:
                print("\n !!! Pilihan tidak valid. Silakan coba lagi. !!!")

        except ValueError:
            print("Input tidak valid. Please enter a number.")

if __name__ == "__main__":
    main_menu()