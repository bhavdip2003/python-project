import tkinter as tk
import time
import winsound

class DigitalClockStopwatchAlarm:
    def __init__(self, window):
        self.window = window
        self.window.title("Digital Clock, Stopwatch, and Alarm")
        
        # Create a label for the digital clock
        self.clock_label = tk.Label(window, font=("Arial", 80), fg="black", bg="white")
        self.clock_label.pack(padx=50, pady=10)
        
        # Create a label for the stopwatch
        self.stopwatch_label = tk.Label(window, font=("Arial", 40), fg="black", bg="white")
        self.stopwatch_label.pack(padx=50, pady=10)
        
        # Create an entry field for setting the alarm time
        self.alarm_entry = tk.Entry(window, font=("Arial", 40), width=10)
        self.alarm_entry.pack(pady=10)
        
        # Create buttons to control the stopwatch and alarm
        self.start_stopwatch_button = tk.Button(window, text="Start", width=10, command=self.start_stopwatch)
        self.start_stopwatch_button.pack(pady=5)
        self.stop_stopwatch_button = tk.Button(window, text="Stop", width=10, command=self.stop_stopwatch)
        self.stop_stopwatch_button.pack(pady=5)
        self.reset_stopwatch_button = tk.Button(window, text="Reset", width=10, command=self.reset_stopwatch)
        self.reset_stopwatch_button.pack(pady=5)
        self.set_alarm_button = tk.Button(window, text="Set Alarm", width=10, command=self.set_alarm)
        self.set_alarm_button.pack(pady=5)
        
        # Initialize variables for the stopwatch and alarm
        self.start_time = 0
        self.is_running = False
        self.alarm_time = ""
        self.is_alarm_set = False
        
        # Update the clock, stopwatch, and alarm initially
        self.update_clock()
        self.update_stopwatch()
        
    def update_clock(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        self.clock_label.config(text=current_time)
        self.check_alarm(current_time)
        self.clock_label.after(1000, self.update_clock)  # Schedule the next update after 1 second
    
    def update_stopwatch(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            stopwatch_time = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))
            self.stopwatch_label.config(text=stopwatch_time)
        self.stopwatch_label.after(1000, self.update_stopwatch)  # Schedule the next update after 1 second
    
    def start_stopwatch(self):
        if not self.is_running:
            self.start_time = time.time()
            self.is_running = True
    
    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False
    
    def reset_stopwatch(self):
        self.start_time = 0
        self.is_running = False
        self.stopwatch_label.config(text="00:00:00")
    
    def set_alarm(self):
        self.alarm_time = self.alarm_entry.get()
        self.is_alarm_set = True
    
    def check_alarm(self, current_time):
        if self.is_alarm_set and current_time == self.alarm_time:
            self.play_alarm_sound()
            self.is_alarm_set = False
    
    def play_alarm_sound(self):
        # Play a sound when the alarm goes off
        frequency = 2500  # Frequency of the sound in Hz
        duration = 2000  # Duration of the sound in milliseconds
        winsound.Beep(frequency, duration)

# Create the main window
window = tk.Tk()

# Create an instance of the DigitalClockStopwatchAlarm class
app = DigitalClockStopwatchAlarm(window)

# Start the main event loop
window.mainloop()
