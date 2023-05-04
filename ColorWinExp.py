from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window

class RedWindow(Widget):
    pass

class RedWindowApp(App):
    def build(self):
        Window.size = (400, 400)
        Window.clearcolor = (1, 0, 0, 1)
        return RedWindow()

if __name__ == "__main__":
    RedWindowApp().run()
