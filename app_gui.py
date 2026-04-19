import tkinter as tk
from tkinter import messagebox
from waitlist_manager import WaitlistManager
from student import Student


class BookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Campus Study Room Waitlist Manager")
        self.root.geometry("450x650")

        self.manager = WaitlistManager()
        self.student_history = {}

        self.library_data = self.manager.get_library_data()
        self.manager.initialize_default_rooms()

        tk.Label(root, text="Student ID (5 digits):").pack(pady=5)
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        tk.Label(root, text="Student Name:").pack(pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Time Block (e.g., 1300):").pack(pady=5)
        self.time_entry = tk.Entry(root)
        self.time_entry.pack()

        tk.Label(root, text="Select Building:").pack(pady=5)
        self.building_var = tk.StringVar()
        self.building_dropdown = tk.OptionMenu(root, self.building_var, *self.library_data.keys(),
                                               command=self.update_floors)
        self.building_dropdown.pack()

        tk.Label(root, text="Select Floor:").pack(pady=5)
        self.floor_var = tk.StringVar()
        self.floor_dropdown = tk.OptionMenu(root, self.floor_var, "")
        self.floor_dropdown.pack()

        tk.Label(root, text="Select Rooms:").pack(pady=5)
        self.rooms_frame = tk.Frame(root)
        self.rooms_frame.pack(pady=5)

        self.room_vars = {}

        self.submit_btn = tk.Button(root, text="Submit Request", command=self.process_booking)
        self.submit_btn.pack(pady=10)

        self.cancel_btn = tk.Button(root, text="Cancel Latest Booking", command=self.process_cancellation)
        self.cancel_btn.pack(pady=5)

        self.undo_btn = tk.Button(root, text="Undo Cancellation", command=self.process_undo)
        self.undo_btn.pack(pady=5)

        buildings = list(self.library_data.keys())
        if buildings:
            self.building_var.set(buildings[0])
            self.update_floors(buildings[0])

    def update_floors(self, building_selection):
        floors = list(self.library_data[building_selection].keys())
        menu = self.floor_dropdown["menu"]
        menu.delete(0, "end")
        for floor in floors:
            menu.add_command(label=floor, command=lambda value=floor: self.update_rooms(building_selection, value))
        if floors:
            self.floor_var.set(floors[0])
            self.update_rooms(building_selection, floors[0])

    def update_rooms(self, building, floor):
        self.floor_var.set(floor)
        for widget in self.rooms_frame.winfo_children():
            widget.destroy()
        self.room_vars= {}
        rooms = self.library_data[building][floor]
        for room_name in rooms:
            self.room_vars[room_name] =tk.BooleanVar()
            chk = tk.Checkbutton(self.rooms_frame, text=room_name, variable=self.room_vars[room_name])
            chk.pack(anchor="w")

    def process_booking(self):
        student_id = self.id_entry.get()
        student_name = self.name_entry.get()

        try:
            time_block = int(self.time_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Time block must be an integer.")
            return
        student = Student(student_id, student_name)

        selected_rooms = [r_name for r_name, var in self.room_vars.items() if var.get()]
        if not selected_rooms:
            messagebox.showwarning("Warning", "Please select at least one room.")
            return
        results = []
        for room in selected_rooms:
            result_message = self.manager.request_room(student, room, time_block)
            results.append(result_message)

            if "Reservation confirmed:" in result_message:
                try:
                    res_id = result_message.split("Reservation(")[1].split(",")[0]
                    if student_id not in self.student_history:
                        self.student_history[student_id] = []
                    self.student_history[student_id].append(res_id)
                except IndexError:
                    pass
        final_output = "\n\n".join(results)
        messagebox.showinfo("Booking Results", final_output)

    def process_cancellation(self):
        student_id = self.id_entry.get()
        if not student_id:
            messagebox.showwarning("Warning", "Please enter a Student ID.")
            return
        if student_id not in self.student_history or len(self.student_history[student_id]) == 0:
            messagebox.showwarning("Warning", f"No recent bookings found for Student ID {student_id}.")
            return
        res_id = self.student_history[student_id].pop()
        result_message = self.manager.process_cancellation(res_id)
        messagebox.showinfo("Cancellation Results", result_message)

    def process_undo(self):
        result_message = self.manager.undo_cancellation()
        messagebox.showinfo("Undo Results", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = BookingApp(root)
    root.mainloop()