"""
1. Create a snake body
2. Move the snake
3. Control the snake
4. Detect collision with food
5. Create a scoreboard
6. Detect collision with wall
7. Detect collision with tail

"""

import turtle as t
import time
import snake as s
import food as f
import scoreboard

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = s.Snake()
food = f.Food()  # crate the food in the screen
scoreboard = scoreboard.Scoreboard()

# able to move the snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()  # show the final position after each segment's movement
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        # update scoreboard
        scoreboard.increase_score()
        # extend the tail
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail, head collides with any segments of the body
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
