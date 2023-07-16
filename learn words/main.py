# установка библиотек
# pip install tk
import random
import tkinter as tk
# Слова
words = {
    "apple": "яблоко", "banana": "банан", "orange": "апельсин",
    "grape": "виноград", "pear": "груша", "pineapple": "ананас",
    "watermelon": "арбуз", "cherry": "вишня", "lemon": "лимон",
    "strawberry": "клубника"
}

def show_word():
    global correct_answer
    word = random.choice(list(words.keys()))
    correct_answer = words[word]
    word_label.config(text=word)

    options = list(words.values())
    options.remove(correct_answer)
    options = random.sample(options, 3)
    options.append(correct_answer)
    random.shuffle(options) # перемешиваем варианты ответов

    for i in range(4):
        answer_buttons[i].config(text=options[i])

def check_answer(answer):
    if answer == correct_answer:
        result_label.config(text="Правильно!")
    else:
        result_label.config(text="Неправильно!")

window = tk.Tk()
window.title("Изучение английских слов")
window.geometry("300x250")

word_label = tk.Label(window, font=("Arial", 20))
word_label.pack(pady=10)

# Создаем кнопки
answer_buttons = []
for i in range(4):
    button = tk.Button(window, font=("Arial", 14), width=20,
                       command=lambda x=i: check_answer(answer_buttons[x].cget("text")))
    button.pack(pady=5)
    answer_buttons.append(button)

result_label = tk.Label(window, font=("Arial", 16))
result_label.pack(pady=10)

tk.Button(window, text="Новое слово", command=show_word).pack(pady=10)

show_word()
window.mainloop()