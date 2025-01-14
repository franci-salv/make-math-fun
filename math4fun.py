import random

print('Hey! For when you just wanna procrastinate and don’t feel like working, you can always come play this game.')
print('Since I only have like 10 minutes, we\'ll just do some basics +, -, *, /. As I work further on my project, it will become better.')

i = 0
correct_answers = 0
totalq = 0
OPERATORS = ['+', '-', '*', '/']  # This is just helpful to inspect the code


def addsubmult():
    # Generate random operator and numbers
    random_number = random.randint(1, 4)
    computational_number1 = random.randint(1, 100)
    computational_number2 = random.randint(1, 100)
    return random_number, computational_number1, computational_number2


while i != 1:
    random_number, computational_number1, computational_number2 = addsubmult()
    print('If you wanna stop, just type "stop" and then press enter:')

    if random_number == 1:  # Addition
        answer = computational_number1 + computational_number2
        print(f'What is the answer of {computational_number1} + {computational_number2}?')
        user_ans = input('Your answer: ')
        if user_ans.lower() == 'stop':
            break
        elif int(user_ans) == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'Wrong! The correct answer is {answer}.')
    
    elif random_number == 2:  # Subtraction
        answer = computational_number2 - computational_number1
        print(f'What is the answer of {computational_number2} - {computational_number1}?')
        user_ans = input('Your answer: ')
        if user_ans.lower() == 'stop':
            break
        elif int(user_ans) == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'Wrong! The correct answer is {answer}.')
    
    elif random_number == 3:  # Multiplication
        answer = computational_number1 * computational_number2
        print(f'What is the answer of {computational_number1} * {computational_number2}?')
        user_ans = input('Your answer: ')
        if user_ans.lower() == 'stop':
            break
        elif int(user_ans) == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'Wrong! The correct answer is {answer}.')
    
    elif random_number == 4:  # Division
        computational_number2 = random.randint(1, 100)
        computational_number1 = random.randint(1, 20) * computational_number2
        answer = computational_number1 // computational_number2  # Use integer division
        print(f'What is the answer of {computational_number1} / {computational_number2}?')
        user_ans = input('Your answer: ')
        if user_ans.lower() == 'stop':
            break
        elif int(user_ans) == answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'Wrong! The correct answer is {answer}.')
    totalq += 1


print(f'Out of {totalq} questions, you got {correct_answers} correct, which is {(correct_answers / totalq) * 100:.2f}%.')




#potential improvement call the numbers by function (so specific parameters per operator)  cuz no one finna be doing 99*45 in their head for fun
#obiously add more shit like to the power of, roots, matrices, vectors etc.
#make a choice menu
#somehow find a way to 'show' like integration signs and that shit cuz it makes it a lot easier to read
