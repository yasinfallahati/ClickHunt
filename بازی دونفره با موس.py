import tkinter as tk
from tkinter import messagebox
import math

class CursorHunt:
    def __init__(self, root):
        self.root = root
        self.root.title("Cursor Hunt - Python Edition")
        
        # اجرای بازی به صورت تمام صفحه
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="#1a1a1a")

        self.phase = "START"
        self.target_pos = None
        self.attempts = 5
        self.tolerance = 50 # شعاع خطا برای کلیک صحیح

        # رابط کاربری
        self.label = tk.Label(root, text="Cursor Hunt", font=("Arial", 48, "bold"), fg="white", bg="#1a1a1a")
        self.label.pack(pady=100)

        self.info_label = tk.Label(root, text="بازی دو نفره: نفر اول هدف را پنهان می‌کند", font=("Arial", 18), fg="#888", bg="#1a1a1a")
        self.info_label.pack(pady=10)

        self.btn = tk.Button(root, text="شروع بازی", font=("Arial", 20, "bold"), command=self.start_game, 
                             bg="#4f46e5", fg="white", padx=40, pady=20, borderwidth=0, cursor="hand2")
        self.btn.pack(pady=50)

        # اتصال رویدادها
        self.root.bind("<Double-Button-1>", self.handle_double_click)
        self.root.bind("<Button-1>", self.handle_click)
        self.root.bind("<Escape>", lambda e: self.root.destroy()) # خروج با دکمه Esc

    def start_game(self):
        self.phase = "HIDING"
        self.attempts = 5
        self.target_pos = None
        self.btn.pack_forget()
        self.label.config(text="نفر اول: دابل کلیک کنید تا ماوس پنهان شود", font=("Arial", 24))
        self.info_label.config(text="برای خروج دکمه ESC را بزنید")

    def handle_double_click(self, event):
        if self.phase == "HIDING":
            self.target_pos = (event.x, event.y)
            self.phase = "SEEKING"
            # پنهان کردن نشانگر ماوس
            self.root.config(cursor="none")
            self.label.config(text="نفر دوم: محل هدف را پیدا کنید!")
            self.info_label.config(text=f"فرصت‌های باقی‌مانده: {self.attempts}")

    def handle_click(self, event):
        if self.phase == "SEEKING" and self.target_pos:
            # محاسبه فاصله کلیک تا هدف
            dist = math.sqrt((event.x - self.target_pos[0])**2 + (event.y - self.target_pos[1])**2)
            
            if dist <= self.tolerance:
                self.win()
            else:
                self.attempts -= 1
                self.info_label.config(text=f"فرصت‌های باقی‌مانده: {self.attempts}")
                if self.attempts <= 0:
                    self.lose()

    def win(self):
        self.phase = "FINISHED"
        self.root.config(cursor="") # ظاهر شدن دوباره ماوس
        messagebox.showinfo("پیروزی!", "تبریک! نفر دوم هدف را پیدا کرد.")
        self.reset()

    def lose(self):
        self.phase = "FINISHED"
        self.root.config(cursor="") # ظاهر شدن دوباره ماوس
        messagebox.showwarning("باخت!", f"فرصت تمام شد! نفر اول برنده شد.\nهدف در مختصات {self.target_pos} بود.")
        self.reset()

    def reset(self):
        self.phase = "START"
        self.label.config(text="Cursor Hunt", font=("Arial", 48, "bold"))
        self.info_label.config(text="بازی دو نفره: نفر اول هدف را پنهان می‌کند")
        self.btn.pack(pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    game = CursorHunt(root)
    root.mainloop()
