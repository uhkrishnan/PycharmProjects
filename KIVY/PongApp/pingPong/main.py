from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.1


class PongBall(Widget):
    # the coordinates require NumericProperty as we will run this on android --> Java : needs to know what var type
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    # reference list property allows to refer to (x, y) in a single go
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # LATEST POSITION = CURRENT VELOCITY + CURRENT POSITION
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# 2. create the game
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self):
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    # Update - move the ball by calling move()
    def update(self, time):
        self.ball.move()
        # out of bound control y and x axis side
        # the ball size matters. it considers the leftmost point

        if (self.ball.y < 0 or self.ball.y > self.height - 50):
            self.ball.velocity_y *= -1

        # ball bounce off left side -- increase score
        if self.ball.x < 0:
            self.ball.velocity_x *= -1
            self.player2.score += 1

        # ball bounce off right side
        if self.ball.x > self.width - 50:
            self.ball.velocity_x *= -1
            self.player1.score += 1

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width * 1/4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y

# 1. create the app
class PongApp(App):
    # 3. build the game
    def build(self):
        game = PongGame()
        game.serve_ball()
        # calls the update function in PongGame class 60 times in 1 second, i.e. 60 fps
        # Clock.schedule_interval(game.update, 1.0 / 60.0)
        Clock.schedule_interval(game.update, 1.0 / 144.0)

        return game


# 4. run th app
PongApp().run()
