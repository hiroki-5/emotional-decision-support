import tkinter as tk
from tkinter import ttk

class EmotionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Emotion Input Interface")
        self.root.geometry("400x300")

        self.create_widgets()

        def create_widgets(self):
            #感情の種類を入力するラベルとテキストボックス
            self.emotion_label = tk.Label(self.root, text="Emotion:")
            self.emotion_label.pack(pady=10)

            self.emotion_entry = tk.Label(self.root, width=30)
            self.emotion_entry.pack(pady=10)

            #感情の強度を入力するラベルとスピンボックス
            self.intensity_label = tk.Label(self.root, text="Intensity (1-10):")
            self.intensity.pack(pady=10)

            self.intensity_spinbox =tk.Spinbox(self.root, from_=1, to=10, width=5)
            self.intensity_spinbox.pack(pady=10)

            #「submit」ボタンの作成
            self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_emotion)
            self.submit_button.pack(pady=20)

        def submit_emotion(self):
            #入力された感情と強度を取得して表示
            emotion = self.emotion_entry.get()
            intensity = self.intensity_spinbox.get()
            print(f"Emotion: {emotion}, Intensity: {intensity}")


            if __name__ == "__main__":
                root = tk.Tk()
                app = EmotionApp(root)
                root.mainloop()