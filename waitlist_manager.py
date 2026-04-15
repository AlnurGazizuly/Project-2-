from student import Student
from room import Room

class CustomQueue:
    def __init__(self):
        self.items = []
        self.head = 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.items[self.head]
        self.head += 1
        return item
    def is_empty(self):
        return self.head >= len(self.items)

class WaitlistManager:
    def __init__(self):
        self.room_inventory = []
        self.waitlist = CustomQueue()
    def add_room_to_inventory(self, room):
        self.room_inventory.append(room)
    def enqueue_to_waitlist(self, student):
        self.waitlist.enqueue(student)
    def dequeue_from_waitlist(self):
        return self.waitlist.dequeue()