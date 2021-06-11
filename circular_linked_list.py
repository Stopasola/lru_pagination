from node import Node


class CircularList:
    def __init__(self, frame_size):
        self.head = None
        self.count = 0
        self.page_victim = 0
        self.frame_size = frame_size

    def __repr__(self):
        string = ""

        if self.head is None:
            string += "Circular Linked List Empty"
            return string

        string += f"Circular Linked List:\n{self.head.data}"
        temp = self.head.next
        while temp != self.head:
            string += f" -> {temp.data}"
            temp = temp.next
        return string

    def shift_page_victim(self):
        self.page_victim = (self.page_victim + 1) % self.frame_size

    def append(self, data):
        self.insert(data, self.count)
        return

    def insert(self, data):
        reference_bit = 1
        if self.head is None:
            self.head = Node(data, reference_bit)
            self.count += 1
            self.shift_page_victim()
            return

        temp = self.head
        for _ in range(self.count - 1 if self.page_victim - 1 == -1 else self.page_victim - 1):
            temp = temp.next

        aftertemp = temp.next
        temp.next = Node(data, reference_bit)
        temp.next.next = aftertemp
        if self.page_victim == 0:
            self.head = temp.next
        self.count += 1
        self.shift_page_victim()
        return

    def set_page_bit(self, data):
        temp = self.head
        for i in range(self.count):
            if temp.data == data:
                temp.reference_bit = 1
                break
            temp = temp.next

    def remove(self):

        if self.count == 1:
            self.head = None
            self.count = 0
            return

        before = self.head
        for _ in range(self.count - 1 if self.page_victim - 1 == -1 else self.page_victim - 1):
            before = before.next
        after = before.next.next

        before.next = after
        if self.page_victim == 0:
            self.head = after
        self.count -= 1
        return

    def find(self, data):
        temp = self.head
        for i in range(self.count):
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def index(self, idx):
        temp = self.head
        for i in range(self.count):
            if i == idx:
                return temp
            temp = temp.next

    def size(self):
        return self.count

    def display(self):
        print(self)