import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizAppUserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = tkinter.Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.score = tkinter.Label(text="Score: 0", fg="white")
        self.score.grid(column=1, row=0)
        self.score.config(bg=THEME_COLOR)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Hello", fill="black",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.correct_image = tkinter.PhotoImage(file="images/true.png")
        self.false_image = tkinter.PhotoImage(file="images/false.png")
        self.correct_image_button = tkinter.Button(image=self.correct_image, highlightthickness=0,
                                                   command=self.correct_answer)
        self.correct_image_button.grid(column=0, row=2)
        self.false_image_button = tkinter.Button(image=self.false_image, highlightthickness=0,
                                                 command=self.wrong_answer)
        self.false_image_button.grid(column=1, row=2)

        self.window.config(bg=THEME_COLOR)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        if self.quiz.still_has_questions():
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_question)
        else:
            self.canvas.itemconfig(self.question_text, text="THE END")
            self.correct_image_button.config(state="disabled")
            self.false_image_button.config(state="disabled")

    def correct_answer(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def wrong_answer(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")
            self.window.after(500, func=self.flash)
        else:
            self.canvas.config(bg="red")
            self.window.after(500, func=self.flash)

    def flash(self):
        self.canvas.config(bg="white")
        self.get_question()
