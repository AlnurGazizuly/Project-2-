# Campus Study Room Waitlist Manager

## Project Overview
This project is a campus study room reservation system that automatically manages bookings, waitlists, cancellations, and schedule tracking. The goal of the project is to make study room booking more organized and fair when rooms are full, while also showing how multiple data structures and algorithms can work together in one practical system.

Our system lets a student request a room for a specific one-hour time block. If the room is available, the reservation is confirmed. If the room is already booked for that time, the student is added to that room and time slot’s waitlist. If a reservation is canceled, the first student on that waitlist is moved into the open slot automatically.

## Main Data Structures Used
This project was designed around the data structures we learned in class.

- **Queue**
  - Used for waitlists
  - Each room/time combination has its own queue
  - This keeps the process first come, first served

- **Python List / Array**
  - Used for room inventory
  - Makes it easy to store and traverse all rooms

- **Dictionary / Hash Map**
  - Used for active reservations
  - Stores reservation ID to reservation object for fast lookup

- **Stack**
  - Used for cancellation history
  - Allows undo cancellation using LIFO behavior

- **Binary Search Tree**
  - Used to organize reservations by time block
  - Makes time-based schedule searching more efficient

## Main Features
- Book a study room for a valid one-hour time block
- Add students to a waitlist if the room is full
- Cancel reservations
- Automatically promote the next student from the waitlist after a cancellation
- Undo the most recent cancellation if the room has not already been rebooked
- View the schedule in sorted time order using BST traversal
- Use either a console demo or the GUI

## Files in This Project
- `app_gui.py`  
  Runs the Tkinter GUI for booking, canceling, and undoing reservations

- `main.py`  
  Runs a simple console demo of the system

- `student.py`  
  Defines the `Student` class

- `room.py`  
  Defines the `Room` class

- `reservation.py`  
  Defines the `Reservation` class

- `schedule_bst.py`  
  Implements the Binary Search Tree used for time slot scheduling

- `waitlist_manager.py`  
  Main logic of the system, including waitlists, bookings, cancellations, undo, and schedule management

- `test_run.py`  
  Runs the individual backend test cases one at a time

- `big_test_run.py`  
  Runs a larger combined backend test covering multiple operations in one run

## Room Setup
The system currently uses the following rooms from Bertrand Library:

### Level 2
- British Library Room
- Rothko Room
- Achilles Room
- Teahouse Room

### Lower Level 1
- Da Vinci Room
- Kahlo Room
- Warhol Room

### Lower Level 2
- Fallingwater Room
- Picasso Room
- Monet Room

## Valid Time Blocks
Reservations use one-hour time slots from 10:00 AM to 9:00 PM.

Valid start times are:
- 1000
- 1100
- 1200
- 1300
- 1400
- 1500
- 1600
- 1700
- 1800
- 1900
- 2000

## Two Ways to Run the Project
Run `python main.py` in the terminal for the console method.
or
Run `python app_gui.py` in the terminal for the GUI method.