import random


def game():
    options = ['камень', 'ножницы', 'бумага']

    print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")
    print("Выберите один из вариантов: камень, ножницы, бумага")

    while True:
        user_choice = input("Ваш выбор: ").lower()
        if user_choice not in options:
            print("Пожалуйста, выберите камень, ножницы или бумага!")
            continue

        computer_choice = random.choice(options)
        print(f"Компьютер выбрал: {computer_choice}")

        if user_choice == computer_choice:
            print("Ничья!")
        elif (user_choice == 'камень' and computer_choice == 'ножницы') or \
                (user_choice == 'ножницы' and computer_choice == 'бумага') or \
                (user_choice == 'бумага' and computer_choice == 'камень'):
            print("Вы победили!")
        else:
            print("Компьютер победил!")

        play_again = input("Хотите сыграть ещё раз? (да/нет): ").lower()
        if play_again != 'да':
            print("Спасибо за игру! До свидания!")
            break


game()