import ursina as urs
import pyttsx3


app = urs.Ursina()

class Paddle(urs.Entity):
    score = 0
    def __init__(self, x, y, color, speed, is_right_paddle: bool):
        super(Paddle, self).__init__()
        self.model = "quad"
        self.color = color
        self.x = x
        self.y = y
        self.scale_x = 0.3
        self.scale_y = 1.5
        self.collider = "box"
        self.speed = speed
        self.is_right = is_right_paddle

    def update(self):
        if not self.is_right:
            self.y += urs.held_keys["w"] * self.speed * urs.time.dt
            self.y -= urs.held_keys["s"] * self.speed * urs.time.dt
        else:
            self.y += urs.held_keys["i"] * self.speed * urs.time.dt
            self.y -= urs.held_keys["k"] * self.speed * urs.time.dt



class Ball(urs.Entity):
    def __init__(self, x, y, color, speed, radius):
        super(Ball, self).__init__()
        self.model = "circle"
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = speed
        self.og_speed = speed
        self.speed_y = speed
        self.collider = "box"
        self.scale = (radius, radius)

    def update(self):
        self.x += self.speed_x * urs.time.dt
        self.y += self.speed_y * urs.time.dt

        if self.y >= 4:
            self.speed_y *= -1

        if self.y <= -4:
            self.speed_y *= -1


        if self.intersects().hit:
            # self.s
            # peed_y *= -1
            self.speed_x *= -1
            urs.Audio("ball_hit_updated.mp3")



    def reset(self):
        self.x = 0
        self.y = 0

        self.speed_x = self.og_speed
        self.speed_y = self.og_speed

left_paddle = Paddle(-7, 0, urs.color.green, 5, False)
right_paddle = Paddle(7, 0, urs.color.red, 5, True)


ball = Ball(0, 0, urs.color.blue, 5, 0.3)
# urs.Audio("audio.mp3")

def update():
    if ball.x >= 8:
        ball.speed_y = 0
        ball.speed_x = 0

    if ball.x <= -8:
        ball.speed_y = 0
        ball.speed_x = 0

app.run()

# print(right_paddle.score)
# print(left_paddle.score)