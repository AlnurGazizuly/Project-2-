from student import Student
from waitlist_manager import WaitlistManager
def main():
    manager = WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001,  "Nick")
    s2 = Student(10002,  "Alnur")
    s3 = Student(10003,  "Sarah")
    room_name = "British Library Room"
    time_block = 1300
    print(manager.request_room(s1, room_name,time_block))
    print(manager.request_room(s2, room_name,time_block))
    print(manager.request_room(s3, room_name,time_block))
    manager.show_waitlist_for_room_time(room_name,time_block)
    print("\n--- Current Schedule ---")
    manager.show_schedule()
    print("\n--- Cancel Reservation R001 ---")
    print(manager.process_cancellation("R001"))
    manager.show_waitlist_for_room_time(room_name,time_block)
    print("\n--- Updated Schedule ---")
    manager.show_schedule()
    print("\n--- Undo Cancellation ---")
    print(manager.undo_cancellation())
    print("\n--- Final Schedule ---")
    manager.show_schedule()
if __name__ == "__main__":
    main()