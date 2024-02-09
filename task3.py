# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:


import random

number_to_guess = random.randint(0, 1000)

attempts = 10

print("Загадано число от 0 до 1000. Необходимо угадать его за 10 попыток.")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Попытка {attempt}. Введите число: "))

    if guess < number_to_guess:
        print("Загаданное число больше.")
    elif guess > number_to_guess:
        print("Загаданное число меньше.")
    else:
        print("Вы угадали число!")
        break
else:
    print(f"Вы не угадали число за {attempts} попыток. Правильное число {number_to_guess}.")