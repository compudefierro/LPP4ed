import tkinter as tk
from datetime import datetime

class AgeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Age Calculator")
        self.root.geometry("350x260")
        self.root.resizable(False, False)

        # Label for instructions
        self.label = tk.Label(root, text="Enter your birth year:", font=("Arial", 12))
        self.label.pack(pady=(20, 5))

        # Entry for birth year
        self.birth_year_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.birth_year_var, font=("Arial", 12), width=15)
        self.entry.pack(pady=5)
        self.entry.focus()

        # Button to calculate age
        self.calc_button = tk.Button(root, text="Calculate Age", command=self.start_processing, font=("Arial", 11))
        self.calc_button.pack(pady=10)

        # Animated GIF for processing
        self.thinking_gif = self.load_gif_frames("thinking.gif")
        self.gif_label = tk.Label(root)
        self.gif_label.pack(pady=5)
        self.gif_label.place(relx=0.5, rely=0.7, anchor="center")
        self.gif_label.lower()  # Hide initially

        # Label to display result or error
        self.result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        # Bind Enter key to calculate
        self.entry.bind("<Return>", lambda event: self.start_processing())

        # Animation state
        self.animating = False
        self.gif_frame = 0
        
        # Animation timing
        self.animation_duration = 4500  # milliseconds (1.5 seconds)
        self.animation_delay = 2200      # ms between frames
        self.post_animation_delay = 2000  # milliseconds (2 seconds)

    def load_gif_frames(self, filename):
        """Dynamically load all frames from an animated GIF."""
        frames = []
        idx = 0
        while True:
            try:
                frame = tk.PhotoImage(file=filename, format=f"gif -index {idx}")
                frames.append(frame)
                idx += 1
            except Exception:
                break
        if not frames:
            return None
        return frames

    def start_processing(self):
        self.result_label.config(text="", fg="black")
        if self.thinking_gif:
            self.gif_label.lift()
            self.animating = True
            self.gif_frame = 0
            self.animation_start_time = self.root.after(0, self.animate_gif)
            # Schedule to stop animation after animation_duration
            self.root.after(self.animation_duration, self.stop_animation_and_wait)
        self.calc_button.config(state="disabled")

    def animate_gif(self):
        if not self.animating or not self.thinking_gif:
            self.gif_label.lower()
            return
        frame = self.thinking_gif[self.gif_frame]
        self.gif_label.config(image=frame)
        self.gif_label.image = frame
        self.gif_label.lift()
        self.gif_frame = (self.gif_frame + 1) % len(self.thinking_gif)
        self.animation_start_time = self.root.after(self.animation_delay, self.animate_gif)

    def stop_animation_and_wait(self):
        self.animating = False
        self.gif_label.lower()
        # Wait 2 seconds before showing the result
        self.root.after(self.post_animation_delay, self.calculate_age)

    def calculate_age(self):
        self.calc_button.config(state="normal")

        birth_year_str = self.birth_year_var.get().strip()
        current_year = datetime.now().year

        if not birth_year_str.isdigit():
            self.result_label.config(text="Please enter a valid year.", fg="red")
            return

        birth_year = int(birth_year_str)
        if birth_year < 1900 or birth_year > current_year:
            self.result_label.config(
                text=f"Year must be between 1900 and {current_year}.", fg="red"
            )
            return

        age = current_year - birth_year
        self.result_label.config(
            text=f"You are {age} years old.", fg="green"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalculatorApp(root)
    root.mainloop()
