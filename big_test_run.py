from waitlist_manager import WaitlistManager
from student import Student

manager = WaitlistManager()
manager.initialize_default_rooms()

students = [
    Student(10001, "Nick"),
    Student(10002, "Alnur"),
    Student(10003, "Sarah"),
    Student(10004, "Mike")
]

print("TEST 1:",manager.request_room(students[0], "British Library Room", 1300))
print("TEST 2:",manager.request_room(students[1], "British Library Room", 1300))
print("TEST 3:",manager.request_room(students[2], "British Library Room", 1300))
print("TEST 4:",manager.request_room(students[3], "Monet Room", 1400))
print("TEST 5:",manager.request_room(Student("abc", "Bad"), "Monet Room", 1400))
print("TEST 6:",manager.request_room(students[0], "Fake Room", 1400))
print("TEST 7:",manager.request_room(students[0], "British Library Room", 1300))
print("TEST 8:",manager.process_cancellation("R001"))
print("TEST 9:",manager.undo_cancellation())
print("TEST 10:",manager.process_cancellation("R999"))

print("\n--- WAITLIST ---")
manager.show_waitlist_for_room_time("British Library Room", 1300)

print("\n--- SCHEDULE ---")
manager.show_schedule()