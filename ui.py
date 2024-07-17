from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain): # Go below to learn about type hints
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzz Gameee")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0",bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.ques = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )

        wrong_img = PhotoImage(file="images/false.png")
        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img,borderwidth=0, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=0)
        self.wrong_button = Button(image=wrong_img,borderwidth=0, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_ques()

        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques, text=q_text)
        else:
            self.canvas.itemconfig(self.ques, text="You've reached the end of the questions")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true_pressed(self):
        # self.quiz.check_answer('True')
        self.give_feedback(self.quiz.check_answer("True"))
    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_ques)

# Type hints where code ll tell you what kind of data you have to input while calling
        # example:
        # def police_check(age):
        #     if age > 18:
        #         can_drive = True
        #     else:
        #         can_drive = False
        # if police_check(19): # 19 is int so its ok
        #     print("You can rive")
        # else:
        #     print("Pay a fine")
        # if police_check('twelve'): # its wrong so here we are going to specify the type of data
        #     # of age while passing the argument
        #     print("You can rive")
        # else:
        #     print("Pay a fine")

        # def police_check(age: int): this is how we can do this
        #     if age > 18:
        #         can_drive = True
        #     else:
        #         can_drive = False