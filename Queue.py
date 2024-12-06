class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)
    print(f"{item} added to queue")

  def dequeue(self):
    if self.is_empty():
      print("queue is empty")
      return None
    item = self.queue[0]
    self.queue = self.queue[1:]
    print(f"{item} deleted from queue")
    return item

  def peek(self):
    if self.is_empty():
      print("queue is empty")
      return None
    return self.queue[0]

  def is_empty(self):
    return len(self.queue) == 0

  def size(self):
    return len(self.queue)

if __name__ == "__main__":
  q = Queue()
  q.enqueue(10)
  q.enqueue(20)
  q.enqueue(30)

  print("Elemen di depan antrian:", q.peek())

  q.dequeue()
  q.dequeue()

  print("Apakah antrian kosong?", q.is_empty())
  print("Ukuran antrian:", q.size())
