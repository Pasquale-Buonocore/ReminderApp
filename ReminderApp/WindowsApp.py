from kivy.app import App
from kivy.core.window import WindowBase

class ReminderApp(App):
    def build(self):
        # Window properties
        self.title = 'First App'

        parent = WindowBase(width = 100, height = 100)
        return parent
        
if __name__ == '__main__':
    # Launch the app
    ReminderApp().run()