import random

def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    for _ in range(3):
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)

        operations = ['+', '-', '*']
        operation = random.choice(operations)

        print(f'Question: {number_1} {operation} {number_2}')
        answer = input('Your answer: ')

        if operation == '+':
            correct_answer = number_1 + number_2
        elif operation == '-':
            correct_answer = number_1 - number_2
        else:
            correct_answer = number_1 * number_2

        if int(answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()

