from random import randint
import tkinter
from tkinter import *


class SettingBalls:
    def __init__(self, canvas, scrnwidth, scrnheight):

        self.xpos = randint(10, int(scrnwidth))
        self.ypos = randint(10, int(scrnheight))
        self.canvas = canvas

        self.xvelocity = randint(6, 12)
        self.yvelocity = randint(6, 12)


        self.radius = randint(40, 70)


        r = lambda : randint(0, 255)


        self.color = "#%02x%02x%02x" % (r(), r(), r())


        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight


    def create_ball(self):


        x1 = self.xpos - self.radius

        y1 = self.ypos - self.radius

        x2 = self.xpos + self.radius

        y2 = self.ypos + self.radius


        self.ball = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = self.color)


    def move_ball(self):

        self.xpos += self.xvelocity
        self.ypos += self.yvelocity


        if self.ypos >= self.scrnheight - self.radius:
            self.yvelocity = -self.yvelocity



        if self.ypos <= self.radius:
            self.yvelocity = abs(self.yvelocity)


        if self.xpos >= self.scrnwidth - self.radius:
            self.xvelocity = -self.xvelocity


        if self.xpos <= self.radius:
            self.xvelocity = abs(self.xvelocity)


        self.canvas.move(self.ball, self.xvelocity, self.yvelocity)

class MoreBalls:

    balls = []


    def __init__(self, num):


        self.root = Tk()


        scrnw, scrnh = self.root.winfo_screenwidth(), self.root.winfo_screenheight()


        self.root.overrideredirect(1)
        #self.root.iconbitmap("test.ico")

        self.root.attributes("-alpha", 0.4)


        self.canvas = Canvas(self.root, width = scrnw, height = scrnh)


        self.canvas.pack()


        for i in range(num):

            ball = SettingBalls(self.canvas, scrnwidth = scrnw, scrnheight = scrnh)


            ball.create_ball()


            self.balls.append(ball)


        self.run_ball()


        self.root.mainloop()

    def run_ball(self):
        for ball in self.balls:
            ball.move_ball()

        self.canvas.after(20, self.run_ball)


    def myquit(self, event):
        self.root.destroy()

if __name__ == "__main__":
    ball = MoreBalls(20)

