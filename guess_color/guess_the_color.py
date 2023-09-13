import random

COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = [random.choice(COLORS) for _ in range(CODE_LENGTH)]
    return code

def guess_code():
    while True:
        guess = input("Угадай: ").upper().split(" ")
    
        if len(guess) != CODE_LENGTH:
            print(f"Ты должен угадать {CODE_LENGTH} цвета")
            continue
    
        for color in guess:
            if color not in COLORS:
                print(f'Недопустимый цвет {color}')
                break
        else:
            return guess
    
def check_code(guess, real_code):
    correct_pos = sum(1 for g, r in zip(guess, real_code) if g == r)
    incorrect_pos = sum(min(guess.count(color), real_code.count(color)) for color in set(guess))
    return correct_pos, incorrect_pos

def game():
    print(f'Попробуй угадать цвета за {TRIES} попыток')
    print("Цвета: ", *COLORS)
    code = generate_code()
    
    for i in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        print(f'Правильные позиции: {correct_pos}, Не правильные {incorrect_pos}')
        
        if correct_pos == CODE_LENGTH:
            print(f'Поздравляем! Ты угадал код за {i} попыток')
            break
        else:
            print(f'У тебя осталось {TRIES - i} попыток')
        
    else:
        print(f'Закончились попытки. Загаданный код был:', *code)

if __name__ == "__main__":
    game()
