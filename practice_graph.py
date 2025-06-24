import tkinter as tk
from tkinter import messagebox
import random


class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Камень, ножницы, бумага")

        self.user_score = 0
        self.computer_score = 0
        self.rounds_to_win = 3

        # Текст с текущим счётом
        self.score_label = tk.Label(root, text=f"Счёт: Вы 0 - 0 Компьютер", font=("Arial", 14))
        self.score_label.pack(pady=10)

        # Кнопки выбора
        self.rock_btn = tk.Button(root, text="Камень", command=lambda: self.play("камень"))
        self.rock_btn.pack(pady=5)

        self.scissors_btn = tk.Button(root, text="Ножницы", command=lambda: self.play("ножницы"))
        self.scissors_btn.pack(pady=5)

        self.paper_btn = tk.Button(root, text="Бумага", command=lambda: self.play("бумага"))
        self.paper_btn.pack(pady=5)

        # Кнопка сброса игры
        self.reset_btn = tk.Button(root, text="Сбросить игру", command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def play(self, user_choice):
        options = ['камень', 'ножницы', 'бумага']
        computer_choice = random.choice(options)

        # Определение победителя
        if user_choice == computer_choice:
            result = "Ничья!"
        elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
                (user_choice == 'ножницы' and computer_choice == 'бумага') or \
                (user_choice == 'бумага' and computer_choice == 'камень'):
            self.user_score += 1
            result = f"Вы выиграли! Компьютер выбрал {computer_choice}."
        else:
            self.computer_score += 1
            result = f"Компьютер выиграл! Он выбрал {computer_choice}."

        # Обновляем счёт
        self.score_label.config(text=f"Счёт: Вы {self.user_score} - {self.computer_score} Компьютер")

        # Проверка на победу в матче
        if self.user_score >= self.rounds_to_win:
            messagebox.showinfo("Победа!", f"Вы выиграли матч {self.user_score}:{self.computer_score}!")
            self.reset_game()
        elif self.computer_score >= self.rounds_to_win:
            messagebox.showinfo("Поражение", f"Компьютер выиграл матч {self.computer_score}:{self.user_score}!")
            self.reset_game()
        else:
            messagebox.showinfo("Результат раунда", result)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text=f"Счёт: Вы 0 - 0 Компьютер")


# Запуск игры
root = tk.Tk()
game = RockPaperScissorsGame(root)
root.mainloop()