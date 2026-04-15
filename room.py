class Room:
    def __init__(self, room_id, capacity, status="available"):
        self.room_id = room_id
        self.capacity = capacity
        self.status = status
    def book(self):
        self.status = "booked"
    def free(self):
        self.status = "available"
    def is_available(self):
        return self.status == "available"