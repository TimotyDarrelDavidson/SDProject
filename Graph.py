from Video import Video

class Recommend:
    def __init__(self, Video: Video):
        self.title = Video.title
        self.tags = Video.tags
        self.left = None
        self.right = None

class Edge:
    def __init__(self, recommend: Recommend):
        self.title = recommend.title
        self.left = recommend
        self.right = None

class Recommendation:
    def __init__(self):
        self.head = None
    
    def addVideo(self,video: Video):
        
        if self.head is None:
            self.head = Recommend(video)
            return
        
        node = Recommend(video)
        temp = self.head
        
        def link_nodes(src: Recommend, dest: Recommend):
            if set(src.tags) & set(dest.tags):  # Check for common tags
                if src.right:
                    self.addEdge(src, dest)
                else:
                    src.right = Edge(dest)
                self.addEdge(dest, src)
        
        while temp.left:
            link_nodes(temp,node)
            temp = temp.left
        
        link_nodes(node,temp)
        temp.left = node
            
                
    def addEdge(self, Recommend: Recommend, newRecommend: Recommend):
        if(Recommend.right is None):
            Recommend.right = Edge(newRecommend)
            return
        
        temp = Recommend
        while temp.right:
            temp = temp.right
        
        temp.right = Edge(newRecommend)
                
    def getAllEdge(self,Recommend: Edge):
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
        
        
# video1 = Video("Action Movie 1", ["action", "adventure"], "An exciting action movie", 120)
# video2 = Video("Action Movie 2", ["action", "adventure"], "Another thrilling action movie", 125)
# video3 = Video("Comedy Movie 1", ["comedy", "family"], "A funny family movie", 100)
# video4 = Video("Thriller Movie 1", ["thriller", "action"], "A suspenseful action thriller", 110)

# # Create the recommendation system
# rec_sys = Recommendation()
# rec_sys.addVideo(video1)
# rec_sys.addVideo(video2)
# rec_sys.addVideo(video3)
# rec_sys.addVideo(video4)

# print(rec_sys)