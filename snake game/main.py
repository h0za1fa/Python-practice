import turtle as t
import time
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

snake = Snake()
screen = t.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

def create_snake(): 
    for _ in range(3): 
        snake.make_segments()  

create_snake()
food = Food()
food.refresh()
score = ScoreBoard()

screen.onkeypress(snake.turn_left, "d")
screen.onkeypress(snake.turn_right, "a")

game_on = True
while game_on == True:
    screen.update()
    time.sleep(0.1)
    score.pl_level()
    snake.movement()
    if snake.segments[0].distance(food.xcor(),food.ycor()) < 20:
        food.refresh()
        snake.make_segments()
        score.level_up()
    if snake.self_collision() == True:
        score.update_highscore()
        snake.reset()
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290 :
        score.update_highscore()
        snake.reset()
screen.mainloop()
