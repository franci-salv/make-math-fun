import random

print('Hey! For when you just wanna procrastinate and don’t feel like working, you can always come play this game.')
print('Since I only have like 10 minutes, we\'ll just do some basics +, -, *, /. As I work further on my project, it will become better.')

i = 0
correct_answers = 0
totalq = 0
OPERATORS = ['+', '-', '*', '/', '^']  # This is just helpful to inspect the code


def addsubmult():
    # Generate random operator and numbers
    random_number = random.randint(1, 5)
    computational_number1 = random.randint(1, 100)
    computational_number2 = random.randint(1, 100)
    return random_number, computational_number1, computational_number2


def stopping_game(user_ans, answer):
    """
    Check if the user's answer is correct or if they want to stop the game.

    :param user_ans: The user's input as a string.
    :param answer: The correct answer as an integer.
    :return: True if the user wants to stop, False otherwise.
    """
    if user_ans.lower() == 'stop':
        return True  # Signal to stop the game
    elif user_ans.isdigit() and int(user_ans) == answer:
        print('Correct!')
        global correct_answers
        correct_answers += 1
        return False  # Continue the game
    else:
        print(f'Wrong! The correct answer is {answer}.')
        return False  # Continue the game


while i != 1:
    random_number, computational_number1, computational_number2 = addsubmult()
    print('If you wanna stop, just type "stop" and then press enter:')

    if random_number == 1:  # Addition
        answer = computational_number1 + computational_number2
        print(f'What is the answer of {computational_number1} + {computational_number2}?')
        user_ans = input('Your answer: ')
        if stopping_game(user_ans, answer):
            break

    elif random_number == 2:  # Subtraction
        answer = computational_number2 - computational_number1
        print(f'What is the answer of {computational_number2} - {computational_number1}?')
        user_ans = input('Your answer: ')
        if stopping_game(user_ans, answer):
            break

    elif random_number == 3:  # Multiplication
        answer = computational_number1 * computational_number2
        print(f'What is the answer of {computational_number1} * {computational_number2}?')
        user_ans = input('Your answer: ')
        if stopping_game(user_ans, answer):
            break

    elif random_number == 4:  # Division
        computational_number2 = random.randint(1, 100)
        computational_number1 = random.randint(1, 20) * computational_number2
        answer = computational_number1 // computational_number2  # Integer division
        print(f'What is the answer of {computational_number1} / {computational_number2}?')
        user_ans = input('Your answer: ')
        if stopping_game(user_ans, answer):
            break

    elif random_number == 5:  # Powers
        computational_number2 = random.randint(1, 6)
        computational_number1 = random.randint(1, 10)
        answer = computational_number1 ** computational_number2
        print(f'What is the answer of {computational_number1} ^ {computational_number2}?')
        user_ans = input('Your answer: ')
        if stopping_game(user_ans, answer):
            break

    totalq += 1

# Print final results
if totalq > 0:
    print(f'Out of {totalq} questions, you got {correct_answers} correct, which is {(correct_answers / totalq) * 100:.2f}%.')
else:
    print("No questions were answered.")
