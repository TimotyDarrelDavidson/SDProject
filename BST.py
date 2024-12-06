from Video import Video  

class BST:
	def __init__(self) -> None:
		self.root = None

	def insert(self, value, tag, description, duration):
		def insertDFS(current, value, tag, description, duration):
			if current is None:
				return Video(value, tag, description, duration)
			if value < current.title:
				current.left = insertDFS(current.left, value, tag, description, duration)
			elif value > current.title:
				current.right = insertDFS(current.right, value, tag, description, duration)
			return current  

		if self.root is None:
			self.root = Video(value, tag, description, duration)
		else:
			insertDFS(self.root, value, tag, description, duration)

	def printAllTree(self):
		def DFS(current: Video):
			if current is None:
				return
			# Debugging: Print current.left
			if current.left is not None:
				print(f"current.left = {current.left.title}")
			else:
				print("current.left = None")
			
			DFS(current.left)
			
			# Print the current node's title
			print(f"current.title = {current.title}", end=" ")
			
			# Debugging: Print current.right
			if current.right is not None:
				print(f"current.right = {current.right.title}")
			else:
				print("current.right = None")
			
			DFS(current.right)
		DFS(self.root)

	def search(self, value):
		def DFS(current, value):
			if current is None:
				return None
			if current.title == value:
				return current
			elif value < current.title:
				return DFS(current.left, value)
			else:
				return DFS(current.right, value)
		return DFS(self.root, value)
	
if __name__ == "__main__":
    tree = BST()
    tree.insert("Video1", ["tag1","tag2","tag3"], "desc1", 60 * 3)
    tree.insert("Video2", ["tag1","tag2","tag3"], "desc1", 60 * 3)
    tree.insert("Video3", ["tag1","tag2","tag3"], "desc1", 60 * 3)
    tree.insert("Video4", ["tag1","tag2","tag3"], "desc1", 60 * 3)
    
    tree.printAllTree()