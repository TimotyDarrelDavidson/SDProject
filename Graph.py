class Video:

    def __init__(self,title,tags,description,duration):
        self.title = title
        self.tags = tags
        self.description = description
        self.duration = duration
        self.left = None
        self.right = None
        

class Recommend:
    def __init__(self, Video):
        self.title = Video.title
        self.tags = Video.tags
        self.right = None

class Recommendation:
    def __init__(self):
        self.head = None
    
    def addVideo(self,Video):
        
        if self.head is None:
            self.head = Video
            return
        
        temp = self.head
        while temp:
            if set(temp.tags) & set(Video.tags):
                node = Recommend(Video)
                if temp.right:
                    self.addEdge(temp.right,node)
                else:
                    temp.right = node
            temp = temp.left
        
        temp = self.head
        while temp.left:
            temp = temp.left
            
        temp.left = Video
            
                
    def addEdge(self, Recommend, newRecommend):
        temp = Recommend
        while temp.right:
            temp = temp.right
        
        temp.right = newRecommend
        
    def getAllEdge(self,Recommend):
        temp = Recommend
        s = " -> "
        while temp:
            s += temp.title + " -> "
            temp = temp.right
        
        return s + "None"
        
    def __str__(self):
        temp = self.head
        s = ""
        
        while temp:
            s += temp.title + self.getAllEdge(temp.right) + "\n"
            temp = temp.left
        
        return s
        
        
video1 = Video("Action Movie 1", ["action", "adventure"], "An exciting action movie", 120)
video2 = Video("Action Movie 2", ["action", "adventure"], "Another thrilling action movie", 125)
video3 = Video("Comedy Movie 1", ["comedy", "family"], "A funny family movie", 100)
video4 = Video("Thriller Movie 1", ["thriller", "action"], "A suspenseful action thriller", 110)

# Create the recommendation system
rec_sys = Recommendation()
rec_sys.addVideo(video1)
rec_sys.addVideo(video2)
rec_sys.addVideo(video3)
rec_sys.addVideo(video4)

print(rec_sys)