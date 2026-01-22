import tkinter as tk
import turtle

def launch_turtle_game():
    splash.destroy()  # Close splash window

    # Start turtle game
    t = turtle.Turtle()
    s = turtle.Screen()
    s.title("Turtle Game!")

    def move_forward(): t.forward(10)
    def move_backward(): t.backward(10)
    def turn_left(): t.left(15)
    def turn_right(): t.right(15)
    def draw_circle(): t.circle(50)
    def go_home(): t.home(); t.setheading(90)
    def erase(): t.clear()
    def quit_game(): print("Thank you for playing!"); s.bye()
    def black(): t.pencolor("black")
    def red(): t.pencolor("red")
    def blue(): t.pencolor("blue")
    def yellow(): t.pencolor("yellow")
    def green(): t.pencolor("green")
    def square():
        for _ in range(4):
            t.forward(50)
            t.right(90)

    s.listen()
    s.onkey(move_forward, "Up")
    s.onkey(move_backward, "Down")
    s.onkey(turn_left, "Left")
    s.onkey(turn_right, "Right")
    s.onkey(draw_circle, "c")
    s.onkey(go_home, "h")
    s.onkey(erase, "e")
    s.onkey(quit_game, "q")
    s.onkey(black, "1")
    s.onkey(red, "2")
    s.onkey(blue, "3")
    s.onkey(yellow, "4")
    s.onkey(green, "5")
    s.onkey(square, "s")

    s.mainloop()

# Create splash screen
splash = tk.Tk()
splash.title("Welcome!")
splash.geometry("300x150")
splash.configure(bg="lightblue")

label = tk.Label(splash, text="🐢 Welcome to Turtle Game!", font=("Arial", 16), bg="lightblue")
label.pack(expand=True)

# Launch turtle game after 2 seconds
splash.after(5000, launch_turtle_game)
splash.mainloop()
