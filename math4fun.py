import random
import re

print('Hey! For when you just wanna procrastinate and don’t feel like working, you can always come play this game.')
print('We\'ll just do some basics +, -, *, /, ^, and roots.')

correct_answers = 0
totalq = 0
OPERATORS = ['+', '-', '*', '/', '^', 'root']  # Adding root operation

def generate_problem():
    operation = random.choice(OPERATORS)
    if operation in ['+', '-']:
        num1 = random.randint(10, 1000)
        num2 = random.randint(10, 1000)
    elif operation == '*':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    elif operation == '/':
        num2 = random.randint(1, 20)
        num1 = num2 * random.randint(1, 10)  # Ensure divisibility
    elif operation == '^':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 5)
    elif operation == 'root':
        num2 = random.randint(2, 4)
        num1 = random.randint(2, 20) ** num2  # Ensure perfect roots
    return operation, num1, num2

def extract_number(input_text):
    """
    Extracts the first valid number from the user's input.
    :param input_text: The user's input as a string.
    :return: The extracted number as a float, or None if no valid number is found.
    """
    numbers = re.findall(r'[-+]?\d*\.?\d+', input_text)  # Regex to find numbers
    if numbers:
        return float(numbers[-1])  # Return the last number (assumes it is the user's final answer)
    return None

def check_answer(user_ans, correct_ans, tolerance=0.01):
    # Extract the last number in the input
    extracted_number = extract_number(user_ans)
    if extracted_number is not None:
        if abs(extracted_number - correct_ans) <= tolerance:
            print('Correct!')
            return False, True  # Continue and mark as correct
        else:
            print(f'Wrong! The correct answer is {correct_ans:.2f}.')
            return False, False
    else:
        if user_ans.lower() == 'stop':
            return True, False  # Stop the game
        print('Invalid input! Please provide a valid number.')
        return False, False

while True:
    operation, num1, num2 = generate_problem()
    if operation == '+':
        answer = num1 + num2
        print(f'What is {num1} + {num2}?')
    elif operation == '-':
        answer = num1 - num2
        print(f'What is {num1} - {num2}?')
    elif operation == '*':
        answer = num1 * num2
        print(f'What is {num1} * {num2}?')
    elif operation == '/':
        answer = round(num1 / num2, 2)
        print(f'What is {num1} / {num2}? (Round to 2 decimal places)')
    elif operation == '^':
        answer = num1 ** num2
        print(f'What is {num1} ^ {num2}?')
    elif operation == 'root':
        answer = round(num1 ** (1 / num2), 2)
        print(f'What is the {num2}-th root of {num1}? (Round to 2 decimal places)')

    user_ans = input('Your answer: ')
    stop_game, is_correct = check_answer(user_ans, answer)
    if stop_game:
        break
    if is_correct:
        correct_answers += 1
    totalq += 1

# Print final results
if totalq > 0:
    print(f'Out of {totalq} questions, you got {correct_answers} correct, which is {(correct_answers / totalq) * 100:.2f}%.')
else:
    print("No questions were answered.")


#https://wumbo.net/operators/ here are ideas of other operators we can add
#create a file on computer to see user preferences that way everytime they play they dont have to deactivate certain modes
#make an app on windows in the future with some UI

#just wanna add my daily repos



#pyinstaller --onefile --windowed math4fun.py
#since im tired today I'm just gonna read about app development with python to try to learn how it works
#I should really implement nonhomogenuous equations
#implement algorithm that makes problems go from easy to hard
#grinding for exams right now lol
