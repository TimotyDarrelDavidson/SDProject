import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class History:
    def __init__(self, max_size=sys.maxsize):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

        #kalo ukuran stack>batas stack, hapus nilai paling bawah
        if self.size > self.max_size:
            self.remove_bottom()

    def remove_bottom(self):
        prev = self.top
        current = self.top.next
        while current.next and prev.next:
            prev = current
            current = current.next
        #hapus nilai terakhir kalo misalnya penuh
        prev.next = None
        self.size -= 1

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def empty(self):
        return self.top is None
    
    def to_list(self):
        result = []
        current = self.top
        while current is not None:
            result.append(current.data)
            current = current.next
        return result[::-1]

    # Print biasa, biar lebih enak lihat e
    def __str__(self):
        s = ""
        current = self.top
        while current is not None:
            s += f"[{current.data}] ->"
            current = current.next
        s += "None"
        return s

history = History(max_size=3)#angka bisa diganti untuk mengganti batasnya
history.push("video a")
history.push("video b")
history.push("video c")
history.push("video d")
history.push("video e")

print(str(history))
