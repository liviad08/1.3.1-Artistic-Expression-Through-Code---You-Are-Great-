import turtle
import random

# --- Setup Configuration ---
screen = turtle.Screen()
screen.bgcolor("#121212")
screen.title("The Growing Celebration")
screen.setup(width=700, height=700)
screen.tracer(0) 

# This asks a question before the animation starts
user_choice = screen.textinput("Theme Picker", "Choose a vibe: 'fire', 'ice', or 'party':")
if user_choice:
    user_choice = user_choice.lower().strip()

# Logic to change variables based on the answer
if user_choice == "fire":
    bg_color = "#300000"  # Dark Red
    colors = ["#FF4500", "#FFD700", "#FF0000", "#FFA500"]
    star_type = "sharp"
elif user_choice == "ice":
    bg_color = "#E0F7FA"  # Light Blue
    colors = ["#00BFFF", "#1E90FF", "#ADD8E6", "#87CEEB"]
    star_type = "round"
else:
    bg_color = "#121212"  # Original dark theme
    colors = ["#FF3385", "#33FFF5", "#FFFB33", "#8D33FF", "#33FF8D", "#FF4500"]
    star_type = "mixed"

screen.bgcolor(bg_color)

artist = turtle.Turtle()
artist.hideturtle()

# Global counter for user input
press_count = 0

def draw_star(t_obj, size, color):
    """Iteration: Creates a star shape."""
    t_obj.color(color)
    t_obj.begin_fill()
    # Logic change: Use different shapes based on the user's answer
    points = 5 if star_type != "round" else 8
    angle = 144 if star_type != "round" else 135
    
    for _ in range(points):
        t_obj.forward(size)
        t_obj.right(angle)
    t_obj.end_fill()

def draw_smiley(size):
    """Creates a smiley face that grows in size."""
    artist.penup()
    artist.goto(0, -size) 
    artist.setheading(0)
    artist.pendown()
    artist.color("#FFFB33") 
    artist.begin_fill()
    artist.circle(size)
    artist.end_fill()

    # Eyes
    for x_pos in [-size/3, size/3]:
        artist.penup()
        artist.goto(x_pos, size/4)
        artist.color("black")
        artist.begin_fill()
        artist.circle(size/10)
        artist.end_fill()

    # Smile
    artist.penup()
    artist.goto(-size/2, -size/10)
    artist.setheading(-60)
    artist.width(5)
    artist.pendown()
    artist.circle(size/1.8, 120)
    artist.width(1)

# --- Star Rain Setup ---
star_rain_list = []
for _ in range(20):
    p = turtle.Turtle()
    p.hideturtle()
    p.penup()
    p.goto(random.randint(-350, 350), random.randint(-350, 350))
    star_rain_list.append([p, random.randint(4, 10), random.choice(colors)])

def run_animation():
    """Triggers when Space is pressed."""
    global press_count
    press_count += 1
    artist.clear()
    
    # 1. Background Art
    for i in range(12):
        x, y = random.randint(-250, 250), random.randint(-250, 250)
        artist.penup()
        artist.goto(x, y)
        artist.pendown()
        
        # Logic change: Draw based on theme
        if star_type == "round":
             artist.color(random.choice(colors))
             artist.circle(random.randint(10, 25))
        else:
             draw_star(artist, random.randint(20, 40), random.choice(colors))
    
    # 2. Conditional Logic for Smiley
    if press_count >= 5:
        growth_size = 50 + (press_count * 5)
        draw_smiley(growth_size)
        text_y_position = -300
    else:
        text_y_position = -20

    # 3. Write message
    artist.penup()
    artist.goto(0, text_y_position)
    artist.color(random.choice(colors)) 
    artist.write("YOU ARE GREAT!", align="center", font=("Verdana", 42, "bold"))

def update_star_rain():
    """Continuous movement for the star rain."""
    for item in star_rain_list:
        p_turtle, speed, p_color = item
        p_turtle.clear()
        p_turtle.sety(p_turtle.ycor() - speed)
        if p_turtle.ycor() < -350:
            p_turtle.goto(random.randint(-350, 350), 350)
        p_turtle.pendown()
        draw_star(p_turtle, 10, p_color)
        p_turtle.penup()

    screen.update()
    screen.ontimer(update_star_rain, 30)

# --- Events ---
screen.listen()
screen.onkey(run_animation, "space")

run_animation()
update_star_rain()

print("⭐ You are great! Hit [SPACE] 4 times for a surprise.")

turtle.done()
