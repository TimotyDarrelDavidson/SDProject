'''

Yang Buat insert,  printAllTree: Anto
Yang Buat insert,  printAllTree: Anto

'''


from Video import Video  

class BSTnode:
    def __init__(self, video: Video):
        self.video = video
        self.left = None
        self.right = None

class BST:
  def __init__(self) -> None:
    self.root = None

  def insert(self, video: Video):
    def insertDFS(node: BSTnode, video: Video):
      
      if video.title < node.video.title:
        if node.left:
          insertDFS(node.left, video)
        else:
          node.left = BSTnode(video)
          
      elif video.title > node.video.title:
        if node.right:
          insertDFS(node.right, video)
        else:
          node.right = BSTnode(video)

    if self.root is None:
      self.root = BSTnode(video)
    else:
      insertDFS(self.root, video)
      
      
      

  def printAllTree(self):
    def DFS(current: BSTnode):
      if current is None:
        return
      # Debugging: Print current.left
      if current.left is not None:
        print(f"current.left = {current.left.video.title}")
      else:
        print("current.left = None")
      
      DFS(current.left)
      
      # Print the current node's title
      print(f"current.title = {current.video.title}", end=" ")
      
      # Debugging: Print current.right
      if current.right is not None:
        print(f"current.right = {current.right.video.title}")
      else:
        print("current.right = None")
      
      DFS(current.right)
    DFS(self.root)
  
  def removeVideo(self, title: str):
    if self.root is None:
        return None
    def get_successor(curr):
      curr = curr.right
      while curr is not None and curr.left is not None:
          curr = curr.left
      return curr
    
    def del_node(node: BSTnode, title: str):
      if node is None:
        return node

      if node.video.title > title:
          node.left = del_node(node.left, title)
      elif node.video.title < title:
          node.right = del_node(node.right, title)
          
      else:
        if node.left is None:
          return node.right

        if node.right is None:
          return node.left

        succ = get_successor(node)
        node.video.title = succ.video
        node.right = del_node(node.right, succ.video.title)
          
      return node
    
    return del_node(self.root, title)    
    
  def search(self, title):
    def DFS(current, title):
      if current is None:
        return None
      if current.video.title == title:
        return current.video
      elif title < current.video.title:
        return DFS(current.left, title)
      else:
        return DFS(current.right, title)
    return DFS(self.root, title)



  def __str__(self):
      def DFS(current: BSTnode):
          if current is None:
              return ""
          left_str = DFS(current.left)
          current_str = str(current.video)
          right_str = DFS(current.right)

          return left_str + current_str + right_str

      return DFS(self.root)