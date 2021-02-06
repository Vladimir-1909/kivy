from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window

Window.size = (350, 600)


class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0

        self.label_hours.text = str(number * 24)
        self.label_minutes.text = str(number * 24 * 60)
        self.label_seconds.text = str(number * 24 * 60 * 60)
        self.label_m_seconds.text = str(number * 24 * 60 * 60 * 60)
        self.label_weeks.text = str("%.2f" % round(number / 7, 2))


class DuckyApp(App):
    def build(self):
        return Container()


if __name__ == "__main__":
    DuckyApp().run()