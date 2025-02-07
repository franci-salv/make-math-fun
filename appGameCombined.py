import tkinter as tk
import random
import re
import csv


# Game logic
OPERATORS = ['+', '-', '*', '/', '^', 'root']

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
        num1 = num2 * random.randint(1, 10)
    elif operation == '^':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 5)
    elif operation == 'root':
        num2 = random.randint(2, 4)
        num1 = random.randint(2, 20) ** num2
    return operation, num1, num2


import csv

def read_csv_to_dict(filename):
    """ Reads a CSV file and stores two lists into a dictionary. """
    data_dict = {}

    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        # Read the raw header row
        first_line = file.readline().strip()
        headers = first_line.replace('"', '').split(',')  # Clean quotes and split
        print("Processed Headers:", headers)  # Debugging step

        # Rewind file and read the remaining data with corrected headers
        file.seek(0)
        reader = csv.DictReader(file, fieldnames=[headers[0], headers[1]])

        # Initialize empty lists
        operators = []
        validate = []

        # Skip the header row since we manually processed it
        next(reader)

        for row in reader:
            operators.append(row[headers[0]].strip())  # Strip spaces
            validate.append(int(row[headers[1]].strip()))  # Convert to int and strip spaces

        # Store both lists in a dictionary
        for i in range(0,len(operators)):
            data_dict[operators[i]] = validate[i]


    return data_dict
#Issue right now is the format of the dictionary each column cell in column 1 should be coupled with the adjacent one

# Example usage
csv_file = r"C:\Users\franc\OneDrive\Bureaublad\codespace\Githubcode\Myprojects\Lets make math fun\make-math-fun-1\problems.csv"
data = read_csv_to_dict(csv_file)

print(data)



class MathGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Game")
        root.configure(bg="#008000")
        
        self.problem_label = tk.Label(root, text="Press 'New Problem' to start!", font=("Arial", 16))
        self.problem_label.pack(pady=10)

        
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)        
        self.entry.bind("<Return>", lambda event: self.check_answer())

        self.new_problem_button = tk.Button(root, text="New Problem", command=self.new_problem)
        self.new_problem_button.pack(pady=5)
        
        self.feedback_label = tk.Label(root, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=10)
        
        self.score_label = tk.Label(root, text="Score: 0/0", font=("Arial", 14))
        self.score_label.pack(pady=10)
        
        self.correct_answers = 0
        self.total_questions = 0
        self.current_problem = None
        self.correct_answer = None

    def new_problem(self):
        operation, num1, num2 = generate_problem()
        if operation == '+':
            self.correct_answer = num1 + num2
            self.problem_label.config(text=f"What is {num1} + {num2}?")
        elif operation == '-':
            self.correct_answer = num1 - num2
            self.problem_label.config(text=f"What is {num1} - {num2}?")
        elif operation == '*':
            self.correct_answer = num1 * num2
            self.problem_label.config(text=f"What is {num1} * {num2}?")
        elif operation == '/':
            self.correct_answer = round(num1 / num2, 2)
            self.problem_label.config(text=f"What is {num1} / {num2}? (Round to 2 decimal places)")
        elif operation == '^':
            self.correct_answer = num1 ** num2
            self.problem_label.config(text=f"What is {num1} ^ {num2}?")
        elif operation == 'root':
            self.correct_answer = round(num1 ** (1 / num2), 2)
            self.problem_label.config(text=f"What is the {num2}-th root of {num1}? (Round to 2 decimal places)")

        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        user_input = self.entry.get()
        try:
            user_answer = float(user_input)
            if abs(user_answer - self.correct_answer) <= 0.01:
                self.feedback_label.config(text="Correct!", fg="green")
                self.correct_answers += 1
            else:
                self.feedback_label.config(text=f"Wrong! Correct answer: {self.correct_answer:.2f}", fg="red")
        except ValueError:
            self.feedback_label.config(text="Invalid input! Enter a number.", fg="red")

        self.total_questions += 1
        self.score_label.config(text=f"Score: {self.correct_answers}/{self.total_questions}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MathGameApp(root)
    root.mainloop()

#rest day
#right now if i type the answer in the bar it doesn't recognise the answer is there
#another rest day cuz im w pooks