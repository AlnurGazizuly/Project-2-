class Reservation:
    def __init__(self, reservation_id, student, room, time_block):
        self.reservation_id = reservation_id
        self.student = student
        self.room = room
        self.time_block = time_block

    def get_details(self):
        return {
            "reservation_id": self.reservation_id,
            "student_id": self.student.student_id,
            "student_name": self.student.name,
            "room_id": self.room.room_id,
            "time_block": self.time_block
        }

    def __str__(self):
        return (
            f"Reservation({self.reservation_id}, "
            f"Student={self.student.name}, "
            f"Room={self.room.room_id}, "
            f"Time={self.time_block})"
        )