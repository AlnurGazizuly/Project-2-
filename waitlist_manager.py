from student import Student
from room import Room
from reservation import Reservation
from schedule_bst import ScheduleBST

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
    def size(self):
        return len(self.items) - self.head
    def peek_all(self):
        return self.items[self.head:]

class WaitlistManager:
    VALID_TIME_BLOCKS = [1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000]
    DEFAULT_ROOM_NAMES = [
        "British Library Room",
        "Rothko Room",
        "Achilles Room",
        "Teahouse Room",
        "Da Vinci Room",
        "Kahlo Room",
        "Warhol Room",
        "Fallingwater Room",
        "Picasso Room",
        "Monet Room"
    ]

    def __init__(self):
        self.room_inventory = []
        self.waitlists = {}
        self.active_reservations = {}
        self.cancellation_history = []
        self.schedule_tree = ScheduleBST()
        self.next_reservation_id = 1

    def initialize_default_rooms(self):
        for room_name in self.DEFAULT_ROOM_NAMES:
            self.add_room_to_inventory(Room(room_name, capacity = 6))

    def add_room_to_inventory(self, room):
        self.room_inventory.append(room)
        for time_block in self.VALID_TIME_BLOCKS:
            self.waitlists[(room.room_id, time_block)] = CustomQueue()

    def _generate_reservation_id(self):
        reservation_id = f"R{self.next_reservation_id:03d}"
        self.next_reservation_id += 1
        return reservation_id

    def _is_valid_time_block(self, time_block):
        return time_block in self.VALID_TIME_BLOCKS

    def _find_room_by_id(self,room_id):
        for room in self.room_inventory:
            if room.room_id == room_id:
                return room
        return None

    def is_room_available(self,room_id,time_block):
        reservations_at_time = self.schedule_tree.search(time_block)
        for reservation in reservations_at_time:
            if reservation.room.room_id==room_id:
                return False
        return True

    def request_room(self, student,room_id,time_block):
        if not isinstance(student.student_id, int):
            return "Error: Student ID must be an integer."
        if not self._is_valid_time_block(time_block):
            return "Error: Invalid time block. Use 1000 through 2000 in 1-hour increments."
        room = self._find_room_by_id(room_id)
        if room is None:
            return f"Error: Room '{room_id}' not found."
        for reservation in self.active_reservations.values():
            if (
                    reservation.student.student_id == student.student_id
                    and reservation.room.room_id == room_id
                    and reservation.time_block == time_block
            ):
                return "Error: Duplicate reservation attempt."
        if self.is_room_available(room_id, time_block):
            reservation_id = self._generate_reservation_id()
            reservation =Reservation(reservation_id, student, room, time_block)

            self.active_reservations[reservation_id]=reservation
            self.schedule_tree.insert(reservation)
            return f"Reservation confirmed: {reservation}"
        else:
            self.waitlists[(room_id, time_block)].enqueue(student)
            position = self.waitlists[(room_id, time_block)].size()
            return (
                f"No availability for {room_id} at {time_block}. "
                f"{student.name} added to waitlist at position {position}."
            )

    def process_cancellation(self, reservation_id):
        if reservation_id not in self.active_reservations:
            return "Error: Reservation ID not found."
        reservation =self.active_reservations.pop(reservation_id)
        self.cancellation_history.append(reservation)
        self.schedule_tree.remove_reservation(reservation_id, reservation.time_block)
        room_id=  reservation.room.room_id
        time_block=  reservation.time_block
        queue= self.waitlists[(room_id, time_block)]
        if not queue.is_empty():
            next_student = queue.dequeue()
            new_reservation_id = self._generate_reservation_id()
            new_reservation = Reservation(
                new_reservation_id,
                next_student,
                reservation.room,
                time_block
            )
            self.active_reservations[new_reservation_id] = new_reservation
            self.schedule_tree.insert(new_reservation)
            return (
                f"Reservation {reservation_id} canceled. "
                f"{next_student.name} moved from waitlist into {room_id} at {time_block}."
            )
        return f"Reservation {reservation_id} canceled. {room_id} at {time_block} is now free."

    def undo_cancellation(self):
        if len(self.cancellation_history) == 0:
            return "Notice: There are no recent cancellations to undo."
        reservation= self.cancellation_history.pop()
        if self.is_room_available(reservation.room.room_id, reservation.time_block):
            self.active_reservations[reservation.reservation_id] = reservation
            self.schedule_tree.insert(reservation)
            return f"Undo successful: {reservation} restored."
        return (
            "Undo failed: the room/time slot is no longer available because it was already rebooked."
        )

    def find_available_room(self,time_block):
        if not self._is_valid_time_block(time_block):
            return None
        reservations_at_time=self.schedule_tree.search(time_block)
        booked_room_ids=set()
        for reservation in reservations_at_time:
            booked_room_ids.add(reservation.room.room_id)
        for room in self.room_inventory:
            if room.room_id not in booked_room_ids:
                return room
        return None

    def show_schedule(self):
        ordered= self.schedule_tree.inorder_traversal()
        if not ordered:
            print("No reservations in schedule.")
            return
        for time_block, reservations in ordered:
            print(f"\nTime Block: {time_block}")
            for reservation in reservations:
                print(f"  {reservation}")
    def show_waitlist_for_room_time(self, room_id,time_block):
        if (room_id, time_block) not in self.waitlists:
            print("Invalid room/time combination.")
            return
        queue =self.waitlists[(room_id,time_block)]
        waiting_students=queue.peek_all()
        print(f"\nWaitlist for {room_id} at {time_block}:")
        if not waiting_students:
            print("  Empty")
            return
        for i, student in enumerate(waiting_students, start=1):
            print(f"  {i}. {student.name} ({student.student_id})")