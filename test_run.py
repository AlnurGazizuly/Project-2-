from waitlist_manager import WaitlistManager
from student import Student


def test_1_valid_booking():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001, "Nick")
    print(manager.request_room(s1, "British Library Room", 1300))


def test_2_same_room_waitlist():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001, "Nick")
    s2 = Student(10002, "Alnur")
    s3 = Student(10003, "Sarah")

    print(manager.request_room(s1, "British Library Room", 1300))
    print(manager.request_room(s2, "British Library Room", 1300))
    print(manager.request_room(s3, "British Library Room", 1300))
    manager.show_waitlist_for_room_time("British Library Room", 1300)


def test_3_invalid_student_id():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    bad_student = Student("abc", "Bad")
    print(manager.request_room(bad_student, "British Library Room", 1400))


def test_4_invalid_time_block():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001, "Nick")
    print(manager.request_room(s1, "British Library Room", 1255))


def test_5_invalid_room_name():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001, "Nick")
    print(manager.request_room(s1, "Fake Room", 1300))


def test_6_duplicate_booking():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001, "Nick")
    print(manager.request_room(s1, "British Library Room", 1300))
    print(manager.request_room(s1, "British Library Room", 1300))


def test_7_cancellation_with_waitlist():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001, "Nick")
    s2 = Student(10002, "Alnur")

    print(manager.request_room(s1, "British Library Room", 1300))
    print(manager.request_room(s2, "British Library Room", 1300))
    print(manager.process_cancellation("R001"))
    manager.show_schedule()
    manager.show_waitlist_for_room_time("British Library Room", 1300)


def test_8_cancel_nonexistent_reservation():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    print(manager.process_cancellation("R999"))


def test_9_undo_success():
    manager =WaitlistManager()
    manager.initialize_default_rooms()
    s1 = Student(10001, "Nick")

    print(manager.request_room(s1, "Monet Room", 1500))
    print(manager.process_cancellation("R001"))
    print(manager.undo_cancellation())
    manager.show_schedule()


def test_10_empty_undo_stack():
    manager = WaitlistManager()
    manager.initialize_default_rooms()
    print(manager.undo_cancellation())


if __name__ == "__main__":
    # Uncomment one test at a time

    # test_1_valid_booking()
    # test_2_same_room_waitlist()
    # test_3_invalid_student_id()
    # test_4_invalid_time_block()
    # test_5_invalid_room_name()
    # test_6_duplicate_booking()
    # test_7_cancellation_with_waitlist()
    # test_8_cancel_nonexistent_reservation()
    # test_9_undo_success()
    # test_10_empty_undo_stack()