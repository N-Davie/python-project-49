import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    number_of_questions = 3
    for _ in range(number_of_questions):
        num1 = random.randint(1, 100) # NOSONAR
        num2 = random.randint(1, 100) # NOSONAR
        correct_answer = str(gcd(num1, num2))
        print(f"Question: {num1} {num2}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

