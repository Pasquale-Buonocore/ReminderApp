from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
import random

class MyPaintWidget(Widget):
    
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
            d = random.uniform(0.,100.)
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
        print(touch)
    
    def on_touch_move(self, touch):
        print((touch.x, touch.y))
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self):
        # Define the parent widget
        parent = Widget()
        self.painter = MyPaintWidget()

        # Define the clear button
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)

        # Add all widget to the parent
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)

        # Return parent
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    MyPaintApp().run()