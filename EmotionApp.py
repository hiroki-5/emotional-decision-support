import tkinter as tk
import json
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

        self.save_button = tk.Button(self.root, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=5)
        
        self.load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack(pady=5)
        
        self.results_label = tk.Label(self.root, text="")
        self.results_label.pack(pady=20)
        
    def submit_emotion(self):
        emotion = self.emotion_entry.get()
        intensity = int(self.intensity_spinbox.get())
        
        self.emotion__data.append({"emotion": emotion, "intensity":  intensity})
        
        print("Current Emotion Data List:", self.emotion__data)
        
        total_score = sum([entry["intensity"] for entry in self.emotion__data])
        
        print(f"Emotion: {emotion}, Intensity: {intensity}")
        print(f"Total Score: {total_score}")

        self.results_label.config(text=f"Total Score: {total_score}")

    def save_data(self):
        with open("emotion_data.json", "w") as file:
            json.dump(self.emotion__data, file)
        print("Data saved successfully.")
        
    def load_data(self):
        try:
            with open("emotion_data.json", "r") as file:
                self.emotion__data = json.load(file)
                print("Data loaded successfully.")
                self.results_label.config(text="data loaded successfully.")
        except FileNotFoundError:
                print("No data file found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()