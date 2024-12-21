from Video import Video

class History:
    def __init__(self, video: Video):
        self.data = video
        self.next = None

class QueueHistory:
    def __init__(self):
        self.head = None

    def addHistory(self, video: Video):
        new_node = History(video)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        if not self.head:
            print("No videos have been played yet.")
        else:
            print("\n -- Play History: --")
            current = self.head
            idx = 1
            while current:
                video = current.data
                print(f"{idx}. {video.title} - {video.description} (Duration: {video.duration} minutes)")
                current = current.next
                idx += 1

    def clear(self):
        if not self.head:
            print("History is already empty.")
        else:
            self.head = None
            print("History has been cleared.")
            
# if __name__ == '__main__':
#     queueHistory = QueueHistory()
    
#     video1 = Video('Video1', ['tag1','tag2','tag3'], 'This is Video1', 60)
#     video2 = Video('Video2', ['tag2','tag3'], 'This is Video2', 60)
    
#     queueHistory.addHistory(video1)
#     queueHistory.addHistory(video2)
    
#     queueHistory.display()