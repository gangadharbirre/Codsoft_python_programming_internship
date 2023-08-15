import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "What is the largest planet in our solar system?",
                "options": ["Earth", "Mars", "Jupiter", "Saturn"],
                "correct_answer": "Jupiter"
            },
            {
                "question": "Which gas do plants use for photosynthesis?",
                "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                "correct_answer": "Carbon Dioxide"
            },
            # Add more questions...
            {
                "question": "Which programming language is known for its readability and clean code?",
                "options": ["Python", "Java", "C++", "Ruby"],
                "correct_answer": "Python"
            },
            {
                "question": "What does HTML stand for?",
                "options": ["Hyper Text Markup Language", "High Tech Modern Language", "Hyperlink and Text Markup Language", "Hyper Transfer Text Language"],
                "correct_answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Venus", "Jupiter", "Mars", "Uranus"],
                "correct_answer": "Mars"
            },
            {
                "question": "Which of the following is a loop in Python?",
                "options": ["if-else", "switch-case", "for-in", "try-except"],
                "correct_answer": "for-in"
            },
            {
                "question": "What is the chemical symbol for the element Oxygen?",
                "options": ["O", "Ox", "Oy", "Om"],
                "correct_answer": "O"
            },
            {
                "question": "Which country is known as the Land of the Rising Sun?",
                "options": ["China", "Japan", "South Korea", "Thailand"],
                "correct_answer": "Japan"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_answer": "Blue Whale"
            },
            {
                "question": "In which year did the Titanic sink?",
                "options": ["1902", "1912", "1922", "1932"],
                "correct_answer": "1912"
            },
            {
                "question": "Which scientist developed the theory of general relativity?",
                "options": ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"],
                "correct_answer": "Albert Einstein"
            },
            {
                "question": "Which gas forms about 78% of the Earth's atmosphere?",
                "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                "correct_answer": "Nitrogen"
            },
            {
                "question": "What is the largest organ in the human body?",
                "options": ["Heart", "Liver", "Lungs", "Skin"],
                "correct_answer": "Skin"
            },
            {
                "question": "Which famous scientist developed the laws of motion and universal gravitation?",
                "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Marie Curie"],
                "correct_answer": "Isaac Newton"
            },
            {
                "question": "Which continent is known as the 'Dark Continent'?",
                "options": ["Africa", "Asia", "Europe", "South America"],
                "correct_answer": "Africa"
            },
            {
                "question": "What is the smallest prime number?",
                "options": ["0", "1", "2", "3"],
                "correct_answer": "2"
            },
            {
                "question": "What is the chemical symbol for the element Gold?",
                "options": ["Au", "Go", "Gd", "Gl"],
                "correct_answer": "Au"
            },
            {
                "question": "Which famous play was written by William Shakespeare?",
                "options": ["Romeo and Juliet", "War and Peace", "To Kill a Mockingbird", "1984"],
                "correct_answer": "Romeo and Juliet"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "correct_answer": "Pacific Ocean"
            },
            {
                "question": "Which element is represented by the chemical symbol 'Fe'?",
                "options": ["Iron", "Iodine", "Fluorine", "Francium"],
                "correct_answer": "Iron"
            },
            {
                "question": "Which famous scientist developed the theory of evolution?",
                "options": ["Isaac Newton", "Albert Einstein", "Charles Darwin", "Galileo Galilei"],
                "correct_answer": "Charles Darwin"
            },
            {
                "question": "Which gas do humans breathe in?",
                "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
                "correct_answer": "Oxygen"
            }
        ]

        self.label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12))
        self.score_label.pack()

        self.question_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.question_label.pack(pady=10)

        self.option_var = tk.StringVar()
        self.option_var.set("")

        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(root, text="", variable=self.option_var, value="", font=("Helvetica", 10))
            self.option_buttons.append(button)
            button.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_answer, font=("Helvetica", 12))
        self.submit_button.pack(pady=20)

        self.next_question_button = tk.Button(root, text="Next Question", command=self.next_question, font=("Helvetica", 12))
        self.next_question_button.pack()
        self.next_question_button.pack_forget()

        self.load_question(0)

    def load_question(self, question_index):
        if question_index < len(self.questions):
            question_data = self.questions[question_index]
            self.question_label.config(text=question_data["question"])
            self.option_var.set("")
            for i, option in enumerate(question_data["options"]):
                self.option_buttons[i].config(text=option, value=option)
            self.submit_button.config(state=tk.NORMAL)
            self.next_question_button.pack_forget()
        else:
            self.show_results()

    def submit_answer(self):
        user_answer = self.option_var.get()
        correct_answer = self.questions[self.current_question]["correct_answer"]
        if user_answer == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", "Your answer is correct.")
        else:
            messagebox.showinfo("Incorrect!", f"Your answer is incorrect.\nCorrect answer: {correct_answer}")
        self.submit_button.config(state=tk.DISABLED)
        self.next_question_button.pack()

    def next_question(self):
        self.current_question += 1
        self.load_question(self.current_question)

    def show_results(self):
        result_message = f"Your final score is: {self.score}\n"
        if self.score == len(self.questions):
            result_message += "Congratulations! You answered all questions correctly."
        elif self.score == 0:
            result_message += "Oops! Better luck next time."
        else:
            result_message += f"Good job! You answered {self.score} out of {len(self.questions)} questions correctly."
        messagebox.showinfo("Quiz Results", result_message)
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    quiz = QuizGame(root)
    root.mainloop()
