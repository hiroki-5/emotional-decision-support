import tkinter as tk
import json
class EmotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Input Interface")
        self.root.geometry("400x300")
        
        self.decision_sets = []
        self.current_set = []
        
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

        self.new_set_button = tk.Button(self.root, text="Create New Set", command=self.create_new_set)
        self.new_set_button.pack(pady=5)
        
        self.compare_button = tk.Button(self.root, text="Compare Sets", command=self.compare_sets)
        self.compare_button.pack(pady=5)
        
        self.save_button = tk.Button(self.root, text="Save Data", command=self.save_data)
        self.save_button.pack(pady=5)
        
        self.load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack(pady=5)
        
        self.results_label = tk.Label(self.root, text="")
        self.results_label.pack(pady=20)
        
    def submit_emotion(self):
        emotion = self.emotion_entry.get()
        intensity = int(self.intensity_spinbox.get())
        
        self.current_set.append({"emotion": emotion, "intensity":  intensity})
        
        print("Current Emotion Set:", self.current_set)
        
        total_score = sum([int(entry["intensity"]) for entry in self.current_set])
        
        print(f"Emotion: {emotion}, Intensity: {intensity}")
        print(f"Total Score: {total_score}")

        self.results_label.config(text=f"Total Score: {total_score}")

    def create_new_set(self):
        if self.current_set:
            self.decision_sets.append(self.current_set)
            print("Decision Sets:", self.decision_sets)
            self.current_set = []
            self.results_label.config(text="New set created. Start adding emotions.")

    def compare_sets(self):
        if not self.decision_sets:
            self.results_label.config(text="No sets to compare")
            return

        set_scores = [sum(int(entry["intensity"]) for entry in decision_set)for decision_set in self.decision_sets]
        
        best_score = max(set_scores)
        best_set_index = set_scores.index(best_score)
        
        print(f"Set Scores: {set_scores}")
        self.results_label.config(text=f"Best set is Set {best_set_index + 1} with a score of {best_score}")
    def save_data(self):
        data = {
            "decision_sets": self.decision_sets,
            "current_set": self.current_set
        }
        with open("emotion_data.json", "w") as file:
            json.dump(self.emotion_data, file)
        print("Data saved successfully.")
        
    def load_data(self):
        try:
            with open("emotion_data.json", "r") as file:
                data = json.load(file)
                self.decision_sets = data.get("decision_sets", [])
                self.current_set = data.get("current_set", [])
                print("Data loaded successfully.")
                self.results_label.config(text="data loaded successfully.")
        except FileNotFoundError:
                print("No data file found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmotionApp(root)
    root.mainloop()