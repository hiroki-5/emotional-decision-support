import tkinter as tk

class EmotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Input Interface")
        self.root.geometry("400x300")
        
        self.emotion__data = []
        
        self.root
        self.create_widgets()

    def create_widgets(self):
        self.emotion_label = tk.Label(self.root, text="Emotion:")
        self.emotion_label.pack(pady=10)

        self.emotion_entry = tk.Entry(self.root, width=30)
        self.emotion_entry.pack(pady=10)

        self.intensity_label = tk.Label(self.root, text="Intensity (1-10):")
        self.intensity_label.pack(pady=10)

        self.intensity_spinbox = tk.Spinbox(self.root, from_=1, to=10, width=5)
        self.intensity_spinbox.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_emotion)
        self.submit_button.pack(pady=20)

    def submit_emotion(self):
        emotion = self.emotion_entry.get()
        intensity = self.intensity_spinbox.get()
        
        self.emotion__data.append("emotion: {emotion}, intensity: {intensity}")
        
        total_score = sum([entry["intensity"] for entry in self.emotion__data])
        
        print(f"Emotion: {emotion}, Intensity: {intensity}")
        print(f"Total Score: {total_score}")

        self.results_label.config(text=f"Total Score: {total_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()