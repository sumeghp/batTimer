import tkinter as tk
import time
import json

class BatmanStopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Batman Stopwatch")
        self.root.geometry("300x500")  # Increased height to fit the new entry field
        self.root.configure(bg="#191970")  # Dark blue background color
        self.root.resizable(False, False)

        self.is_running = False
        self.start_time = 0
        self.elapsed_time = 0
        self.task_name = ""

        self.label = tk.Label(root, text="00:00:00.000", font=("Arial", 28), fg="yellow", bg="#191970")
        self.label.pack(pady=50)

        self.task_entry = tk.Entry(root, font=("Arial", 12), bg="white", fg="black", width=30)
        self.task_entry.pack(pady=10)

        self.start_button = tk.Button(root, text="Start", command=self.start_stopwatch, font=("Arial", 14), bg="yellow")
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_stopwatch, font=("Arial", 14), bg="yellow")
        self.stop_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_stopwatch, font=("Arial", 14), bg="yellow")
        self.reset_button.pack(pady=10)

        self.update()

        # Make the window semi-transparent (80% opacity)
        self.root.attributes("-alpha", 0.8)

    def update(self):
        if self.is_running:
            current_time = time.time()
            self.elapsed_time += current_time - self.start_time
            self.start_time = current_time
            self.label.configure(text=self.format_time(self.elapsed_time))
        self.root.after(50, self.update)

    def format_time(self, elapsed_time):
        minutes, seconds = divmod(int(elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        microseconds = int((elapsed_time - int(elapsed_time)) * 1000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{microseconds:03d}"

    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time()

    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.log_task()

    def reset_stopwatch(self):
        self.is_running = False
        self.elapsed_time = 0
        self.label.configure(text="00:00:00.000")

    def log_task(self):
        self.task_name = self.task_entry.get()
        task_data = {
            "task_name": self.task_name,
            "elapsed_time": self.format_time(self.elapsed_time)
        }
        with open("task_log.json", "a") as file:
            json.dump(task_data, file)
            file.write("\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BatmanStopwatchApp(root)
    root.mainloop()
