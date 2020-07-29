# background colour
# on touch down
# colour
# draw elipse, circle using code

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Ellipse, Color, Line

import random

# RGBA (R,G,B, opacity) : usually RGB is in 255. KIVY multiplies each value by 255.
Window.clearcolor = (1, 1, 1, 1)


class PaintWindow(Widget):
    def on_touch_down(self, touch):
        coloR = random.randint(0, 255)
        coloG = random.randint(0, 255)
        coloB = random.randint(0, 255)

        self.canvas.add(Color(rgb=(coloR / 255.0, coloG / 255.0, coloB / 255.0)))
        d = 10
        self.canvas.add(Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d)))
        # kivy dictionary and its name | KEY = 'LINE', VALUE = line()
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


# Root window = paint window + button
class PaintApp(App):
    def build(self):
        rootwindow = Widget()
        self.painter = PaintWindow()
        clrbutton = Button(text = 'Clear')
        clrbutton.bind(on_release = self.clear_canvas)
        rootwindow.add_widget(self.painter)
        rootwindow.add_widget(clrbutton)

        return rootwindow

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

PaintApp().run()
