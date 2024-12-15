import random

def lottery():
    print("=== Лотерея чисел ===")
    print("Випадкові числа для вашої лотереї:")

    numbers = random.sample(range(1, 50), 6)  # Генерує 6 випадкових чисел від 1 до 49
    print("Ваші числа:", sorted(numbers))

if __name__ == "__main__":
    lottery()
