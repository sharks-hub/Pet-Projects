from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.core.window import Keyboard
from kivy.graphics import Color, Rectangle


class RedWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(RedWindow, self).__init__(**kwargs)
        self.color_state = 0
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self.canvas.before.add(Color(1, 0, 0, 1))
        self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] in ('enter', 'numpadenter'):
            self.color_state = (self.color_state + 1) % 3
            if self.color_state == 0:
                self.canvas.before.clear()
                with self.canvas.before:
                    Color(1, 0, 0, 1)
                    self.rect = Rectangle(size=self.size, pos=self.pos)
            elif self.color_state == 1:
                self.canvas.before.clear()
                with self.canvas.before:
                    Color(1, 1, 1, 1)
                    self.rect = Rectangle(size=self.size, pos=self.pos)
            elif self.color_state == 2:
                self.canvas.before.clear()
                with self.canvas.before:
                    Color(0, 0, 1, 1)
                    self.rect = Rectangle(size=self.size, pos=self.pos)
            return True
        return False

class RedWindowApp(App):
    def build(self):
        Window.size = (400, 400)
        return RedWindow()

if __name__ == "__main__":
    RedWindowApp().run()
