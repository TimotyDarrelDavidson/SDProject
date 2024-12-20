from Video import Video

class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, video: Video):
    self.queue.append(video)
    print(f"{video.title} added to queue")
    
  def deleteQueue(self, title: str):
    pass

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

# if __name__ == "__main__":
#   q = Queue()
#   q.enqueue(10)
#   q.enqueue(20)
#   q.enqueue(30)

#   print("Elemen di depan antrian:", q.peek())

#   q.dequeue()
#   q.dequeue()

#   print("Apakah antrian kosong?", q.is_empty())
#   print("Ukuran antrian:", q.size())
