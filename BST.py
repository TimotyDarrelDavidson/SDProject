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

	def search(self, title):
		def DFS(current, title):
			if current is None:
				return None
			if current.title == title:
				return current
			elif title < current.title:
				return DFS(current.left, title)
			else:
				return DFS(current.right, title)
		return DFS(self.root, title)
	
# if __name__ == "__main__":
#     tree = BST()
#     tree.insert("Video1", ["tag1","tag2","tag3"], "desc1", 60 * 3)
#     tree.insert("Video2", ["tag1","tag2","tag3"], "desc1", 60 * 3)
    
#     tree.printAllTree()