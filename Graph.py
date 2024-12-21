'''

Yang Buat addVideo, addEdge: Wilson
Yang Buat removeVideo, removeEdge, getRecommendation, printAllEdges, __str__: Darrel


'''


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
            if set(src.tags) & set(dest.tags):
                
                if src.right:
                    self.addEdge(src, dest)
                else:
                    src.right = Edge(dest)
                self.addEdge(dest, src)

        
        while temp.left:
            if (temp.title == video.title):
                print('Video title used')
                return
            link_nodes(temp,node)
            temp = temp.left
        
        link_nodes(node,temp)
        temp.left = node
        
        
        
        
        
    def removeVideo(self, video: Video):
        if self.head is None:
            return

        temp = self.head
        prev = None

        while temp:
            if temp.title == video.title:
                if prev:
                    prev.left = temp.left
                else:
                    self.head = temp.left
                
            if set(temp.tags) & set(video.tags):
                if temp.right:
                    self.removeEdge(temp, video)

            prev = temp
            temp = temp.left

    def removeEdge(self, src: Recommend, dest: Recommend):
        # Remove an edge between `src` and `dest`
        if src.right is None:
            return  # No edges to remove

        prev = None
        current = src.right

        while current:
            if current.title == dest.title:
                # Unlink the edge
                if prev:
                    prev.right = current.right
                else:
                    src.right = current.right
                return

            prev = current
            current = current.right
    
    
    def addEdge(self, Recommend: Recommend, newRecommend: Recommend):
        if(Recommend.right is None):
            Recommend.right = Edge(newRecommend)
            return
        
        temp = Recommend
        while temp.right:
            temp = temp.right
        
        temp.right = Edge(newRecommend)
            
                
    def getRecommendations(self, video: Video):
        temp = self.head
        while temp:
            if (temp.title != video.title):
                temp = temp.left
            else:
                break
            
        temp = temp.right
        s = ""
        while temp:
            s += temp.title + " -> "
            temp = temp.right
        
        return s + "None"
                
    
    def printAllEdge(self,Recommend: Edge):
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
            s += temp.title + self.printAllEdge(temp.right) + "\n"
            temp = temp.left
        
        return s