from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.core.window import Keyboard

class RedWindow(Widget):
    def __init__(self, **kwargs):
        super(RedWindow, self).__init__(**kwargs)
        self.color_state = 0
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in ('enter', 'numpadenter'):
            self.color_state = (self.color_state + 1) % 3
            if self.color_state == 0:
                Window.clearcolor = (1, 0, 0, 1)
            elif self.color_state == 1:
                Window.clearcolor = (1, 1, 1, 1)
            elif self.color_state == 2:
                Window.clearcolor = (0, 0, 1, 1)
            return True
        return False

class RedWindowApp(App):
    def build(self):
        Window.size = (400, 400)
        Window.clearcolor = (1, 0, 0, 1)
        return RedWindow()

if __name__ == "__main__":
    RedWindowApp().run()
