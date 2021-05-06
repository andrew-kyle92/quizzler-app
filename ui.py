from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.iconbitmap("images\logo.ico")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="This is text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(50, 50))
        self.score_text = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "normal"))
        self.score_text.grid(row=0, column=1)
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_button)
        self.true_btn.grid(row=2, column=1)
        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_button)
        self.false_btn.grid(row=2, column=0)
        self.get_next_questions()
        self.window.mainloop()

    def get_next_questions(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz."
                     f"\nYour final score: {self.quiz.score}/{len(self.quiz.question_list)}")

    def false_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def true_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_questions)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_questions)