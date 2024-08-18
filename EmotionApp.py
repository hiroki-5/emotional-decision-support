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
            #「submit」ボタンの作成
            #入力された感情と強度を取得して表示