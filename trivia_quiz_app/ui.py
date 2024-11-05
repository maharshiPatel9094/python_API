from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    # constructor
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        # labels
        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        
        # canvas
        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial",20,"italic"),
            width=280,
            )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        
        # note
        # when we write anything with self. it becomes the property for the class means that it can be accessed from anywhere inside the class
        
        
        # buttons
        right_photo = PhotoImage(file="./images/true.png") 
        self.true_button = Button(height=90,width=90,image=right_photo,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=0)
        
        wrong_photo = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(height=90,width=90,image=wrong_photo,highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2,column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    # get next question from the quizbrain class
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text= f"Q.{self.quiz.question_number} {q_text}")
        else:
            self.canvas.itemconfig(self.question_text,text="You'he reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.color_change(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.color_change(is_right)
        
    def color_change(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000,self.reset_canvas_color)
        
    def reset_canvas_color(self):
        self.canvas.config(bg="white")
        self.get_next_question()
        
    