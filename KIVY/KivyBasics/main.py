from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (1,0,0,1)

class MainApp(App):
    def build(self):
        label = Label(text='I am IronMan', bold=True, italic=True, font_size='30sp', color=(1, 1, 1, 1))

        return label

    # # trying random code
    # def build(self):
    #     label = Label(text='*')
    #     for i in range (0,20):
    #         return label


MainApp().run()
