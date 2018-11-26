from tkinter import *
import time
import random

root = Tk()

root.title("Bounce")

root.resizable(0,0)
#cannot resize the window

root.wm_attributes("-topmost", 1)
#puts the window in front of all windows

canvas = Canvas(root, width=500, height=400, bd=0, highlightthickness=0)

canvas.config(bg="black")
#canvas is black
canvas.pack()

canvas.create_line(250,0,250,400,fill="white")
#border down the middle

score0 = 0
score1 = 0
goTo = 5
ballSpeed = 6
paddleSpeed = 3

root.update()

class Ball:
    def __init__(self, canvas, paddle0, paddle1, color):
        self.canvas = canvas
        
        self.id = canvas.create_oval(10,10,25,25,fill = color)
        self.paddle0 = paddle0
        self.paddle1 = paddle1
        
        self.canvas.move(self.id,235,200)
        #centers the ball
        
        start = [-ballSpeed,ballSpeed]
        random.shuffle(start)
        self.x = start[0]
        #random x starting movement
        
        self.y = -3
        #Starts by going up
        
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        #stores the width and the height of the canvas as variables

        self.score0 = 0
        self.score1 = 0


    def score(self, val):
        global score0
        global score1
        if val == True:
            a = self.canvas.create_text(125,40,text=score0,font= ("Ariel", "60"), fill = "white")
            canvas.itemconfig(a,fill="black")
            score0+=1
            a = self.canvas.create_text(125,40,text=score0,font= ("Ariel", "60"), fill = "white")
        else:
            a = self.canvas.create_text(375,40,text=score1,font= ("Ariel", "60"), fill = "white")
            canvas.itemconfig(a,fill="black")
            score1+=1
            a = self.canvas.create_text(375,40,text=score1,font= ("Ariel", "60"), fill = "white")
        

        
    def hit_paddle0(self, pos):
        paddle_pos = self.canvas.coords(self.paddle0.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False

    def hit_paddle1(self, pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False

        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        
        pos = self.canvas.coords(self.id)
        #returns an array of (x1,y1,x2,y2)(left,up,right,down)
        
        if pos[1] <= 0:
            #if ball is less than zero the ball will move down
            self.y = 3
        if pos[3] >= self.canvas_height:
            #if the ball is more than the screen height, the ball will move up
            self.y = -3

            
        if pos[0] <= 0:
            #if ball is past the left the ball will move right
            self.x = ballSpeed
            self.score(False)
        if pos[2] >= self.canvas_width:
            #if the ball is more than right of the screen height, the ball will move left
            self.x = -ballSpeed
            self.score(True)

        if self.hit_paddle0(pos) == True:
            self.x = ballSpeed
        if self.hit_paddle1(pos) == True:
            self.x = -ballSpeed

       

            
class Paddle0:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,10,100, fill = color)
        self.canvas.move(self.id,30,200)
        self.y=0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width
        ()
        self.canvas.bind_all("<w>",self.turn_left)
        self.canvas.bind_all("<s>",self.turn_right)

    def turn_left(self,evt):
        self.y = -paddleSpeed
    def turn_right(self,evt):
        self.y = paddleSpeed
        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0
        #paddle stops when it hits left or right

class Paddle1:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,10,100, fill = color)
        self.canvas.move(self.id,470,200)
        self.y=0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Up>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Down>",self.turn_right)

    def turn_left(self,evt):
        self.y = -paddleSpeed
    def turn_right(self,evt):
        self.y = paddleSpeed
        
    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= self.canvas_height:
            self.y = 0

        

        

paddle0 = Paddle0(canvas, "blue")
paddle1 = Paddle1(canvas, "yellow")
ball = Ball(canvas, paddle0, paddle1, "green")



time.sleep(1)
while score0 < goTo and score1 < goTo:

    if score0 == goTo:
        ball.x = 0
        ball.y = 0
        paddle0.y = 0
        paddle1.y = 0
        tkinter.messagebox.showinfo("GAME OVER", "Player 1 wins!")
        #canvas.create_text(250,200, text = "Player 1 wins!", font = 60, fill = "blue")

    if score1 == goTo:
        ball.x = 0
        ball.y = 0
        paddle0.y = 0
        paddle1.y = 0
        tkinter.messagebox.showinfo("GAME OVER", "Player 2 wins!")
        #canvas.create_text(250,200, text = "Player 2 wins!", font = 60, fill = "blue")                  

    ball.draw()
    paddle0.draw()
    paddle1.draw()
    root.update_idletasks()
    root.update()
    time.sleep(0.01)



  
