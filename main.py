from BST import BST
from Video import Video
import History
import Queue
from Graph import Recommendation

def main_menu():
  print("WELCOME TO STREAMTREE")
  print("\nMenu:")
  print("1. Add video")               #nambah video ke videos(BST) dan recommendation(Graph) 
  print("2. Remove video")            #remove video dari videos(BST) dan recommendation(Graph) 
  print("3. Play Video")              #search from videos(BST) dan save ke current_video 
  print("4. Find recommended")        #From current_video display recommended
  print("5. Add video ke Queue")      #nambah video dalam queue
  print("6. Remove video dari Queue") #bisa remove video apapun dari queue
  print("7. Display All Video")       #diplay semua video dalam videos(BST)
  print("0. Exit")
  print()
  
  current_video = None;         '''<-----  CURRENT VIDEO'''
  
  videos = BST()
  recommendation = Recommendation()
  
  video1 = Video('Video1', ['tag1','tag2'], 'This is Video1', 60)
  video2 = Video('Video2', ['tag1','tag2'], 'This is Video2', 60)
  video3 = Video('Video3', ['tag2','tag3'], 'This is Video3', 60)
  video4 = Video('Video4', ['tag3','tag4'], 'This is Video4', 60)
  
  videos.insert(video1)
  videos.insert(video2)
  videos.insert(video3)
  videos.insert(video4)
  recommendation.addVideo(video1)
  recommendation.addVideo(video2)
  recommendation.addVideo(video3)
  recommendation.addVideo(video4)
  

  videos.printAllTree()
  print(recommendation)

  while(True):
    try:
      choice = int(input("Pilih menu : "))
      if choice == 1:
        print("Fungsi Add video ke StreamTree.")
        title = input()
        tags = list(map(str, input().split(' ')))
        description = input()
        duration = int(input())
        
        video = Video(title,tags,description,duration)
        
        videos.insert(video)
        recommendation.addVideo(video)
        
        videos.printAllTree()
        print(recommendation)
        
      elif choice == 2:
        print("Fungsi Remove video SreamTree.")
      elif choice == 3:
        print("Fungsi Find recommended dari video.")
      elif choice == 4:
        print("Fungsi Add video ke Queue.")
      elif choice == 5:
        print("Fungsi Remove video dari Queue.")
      elif choice == 0:
        print("Terima kasih sudah menggunakan StreamTree. Sampai jumpa!")
        return False
      else:
        print("Pilihan tidak valid. Silakan coba lagi.")
    except ValueError:
      print("Input tidak valid")

if __name__ == "__main__":
  main_menu()
  