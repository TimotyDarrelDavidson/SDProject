from Video import Video

class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, video: Video):
    self.queue.append(video)
    print(f"{video.title} added to queue")
    
  def delete(self, title):
    for i, item in enumerate(self.queue):
      if item.title == title:  # Compare based on title
        del self.queue[i]
        print(f"Video '{title}' removed from the queue.")
        return
    print(f"Video '{title}' not found in the queue.")

  def dequeue(self):
    if self.is_empty():
      print("queue is empty")
      return None
    video: Video = self.queue[0]
    self.queue = self.queue[1:]
    print(f"{video.title} deleted from queue")
    return video

  def peek(self):
    if self.is_empty():
      print("queue is empty")
      return None
    return self.queue[0]

  def is_empty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)