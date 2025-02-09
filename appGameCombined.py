import tkinter as tk
import random
import csv

# Game logic
OPERATORS = ['+', '-', '*', '/', '^', 'root']
sqrt_symbol = "\u221A"

def generate_problem(enabled_operators):
    """Generates a math problem using only enabled operators."""
    if not enabled_operators:
        return None, None, None  # No operators enabled, return empty

    operation = random.choice(enabled_operators)

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

class MathGameApp:
    def __init__(self, root):
        """Initialize the Math Game app UI."""
        self.root = root
        self.root.title("Math Game")
        self.root.configure(bg="#008000")

        # Track enabled operators
        self.operators_enabled = {op: tk.BooleanVar(value=True) for op in OPERATORS}

        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # UI Components
        self.problem_label = tk.Label(self.root, text="Press 'New Problem' to start!", font=("Arial", 16))
        self.problem_label.pack(pady=10)

        tk.Button(self.root, text="Math Modes", command=self.show_sheet).pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10)        
        self.entry.bind("<Return>", lambda event: self.check_answer())

        self.new_problem_button = tk.Button(self.root, text="New Problem", command=self.new_problem)
        self.new_problem_button.pack(pady=5)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.feedback_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score: 0/0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.correct_answers = 0
        self.total_questions = 0
        self.current_problem = None
        self.correct_answer = None

    def show_sheet(self):
        """Show the sheet view with toggle buttons for each operator."""
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Enable/Disable Operators:", font=("Arial", 16)).pack(pady=10)

        for operator in OPERATORS:
            frame = tk.Frame(self.root)
            frame.pack(pady=5)

            # Checkbox for enabling/disabling operators
            checkbox = tk.Checkbutton(frame, text=operator, variable=self.operators_enabled[operator])
            checkbox.pack(side="left")

            # Button to toggle the operator state
            button = tk.Button(frame, text=f"Toggle {operator}", command=lambda op=operator: self.toggle_operator(op))
            button.pack(side="left")

        tk.Button(self.root, text="Back", command=self.show_main).pack(pady=20)

    def toggle_operator(self, operator):
        """Toggles an operator's enabled/disabled state."""
        current_state = self.operators_enabled[operator].get()
        self.operators_enabled[operator].set(not current_state)

    def show_main(self):
        """Return to the main screen."""
        self.__init__(self.root)

    def new_problem(self):
        """Generate and display a new math problem based on enabled operators."""
        enabled_ops = [op for op, var in self.operators_enabled.items() if var.get()]

        operation, num1, num2 = generate_problem(enabled_ops)
        if operation is None:
            self.problem_label.config(text="No operators enabled! Enable at least one.")
            return

        if operation == '+':
            self.correct_answer = str(num1 + num2)
            self.problem_label.config(text=f"What is {num1} + {num2}?")
        elif operation == '-':
            self.correct_answer = str(num1 - num2)
            self.problem_label.config(text=f"What is {num1} - {num2}?")
        elif operation == '*':
            self.correct_answer = str(num1 * num2)
            self.problem_label.config(text=f"What is {num1} * {num2}?")
        elif operation == '/':
            self.correct_answer = str(round(num1 / num2, 2))
            self.problem_label.config(text=f"What is {num1} / {num2}? (Round to 2 decimal places)")
        elif operation == '^':
            self.correct_answer = str(num1 ** num2)
            self.problem_label.config(text=f"What is {num1} ^ {num2}?")
        elif operation == 'root':
            self.correct_answer = str(num1 ** (1 / num2))
            self.problem_label.config(text=f"What is the {num2}-th root of {num1}? (Round to 2 decimal places)")

        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="")

    def check_answer(self):
        """Check if the user's answer is correct."""
        user_answer = self.entry.get()
       # try:
        if self.correct_answer in user_answer:
            self.feedback_label.config(text="Correct!", fg="green")
            self.correct_answers += 1
        else:
            self.correct_answer= int(self.correct_answer)
            self.feedback_label.config(text=f"Wrong! Correct answer: {self.correct_answer:.2f}", fg="red")


        self.total_questions += 1
        self.score_label.config(text=f"Score: {self.correct_answers}/{self.total_questions}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MathGameApp(root)
    root.mainloop()


#I need link the dictionary back to the csv file and the database to the button presses we'll figure out how that works
#I need to automate the new problem generating thing
#I wanna add difficulties that way player can do what they're in the mood for

#I'm working on my blog
#travelling but I'm learning about tkinter