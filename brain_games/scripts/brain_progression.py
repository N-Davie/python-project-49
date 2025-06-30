import random

def create_progression(start, step, length):
    return [start + i * step for i in range(length)]

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for _ in range(3):
        length = random.randint(5, 10)
        start = random.randint(1, 100)
        step = random.randint(1, 25)

        progression = create_progression(start, step, length)
        index_empty = random.randint(0, length - 1)
        correct_answer = str(progression[index_empty])

        progression_display = progression.copy()
        progression_display[index_empty] = '..'
        print("Question:", ' '.join(map(str, progression_display)))
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            # Продолжаем к следующему вопросу
            continue
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

if __name__ == "__main__":
    main()
