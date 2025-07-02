import random
import operator


def get_question_and_answer():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    num1 = random.randint(1, 50)  # NOSONAR
    num2 = random.randint(1, 50)  # NOSONAR
    op_symbol, operation = random.choice(list(operations.items()))  # NOSONAR
    question = f"{num1} {op_symbol} {num2}"
    answer = str(operation(num1, num2))
    return question, answer


def main():
    print("Welcome to the Brain Games!")
    global NAME
    NAME = input("May I have your name? ")
    print(f"Hello, {NAME}!")
    print("What is the result of the expression?")

    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {NAME}!")
            return
    print(f"Congratulations, {NAME}!")


if __name__ == "__main__":
    main()

