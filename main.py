import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

Y_POSITION = [-70, -40, -10, 20, 50, 80]

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross the road")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.player_up, "Up")
screen.onkey(player.player_down, "Down")
screen.onkey(player.player_left, "Left")
screen.onkey(player.player_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



    if player.is_at_finish():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score_level_up()

screen.exitonclick()