from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    # constructor
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        # labels
        self.score_label = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        
        # canvas
        self.canvas = Canvas(height=250,width=300,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Some Question Text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        # buttons
        right_photo = PhotoImage(file="./images/true.png") 
        self.true_button = Button(height=90,width=90,image=right_photo,highlightthickness=0)
        self.true_button.grid(row=2,column=0)
        
        wrong_photo = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(height=90,width=90,image=wrong_photo,highlightthickness=0)
        self.wrong_button.grid(row=2,column=1)
        
        
        
        self.window.mainloop()