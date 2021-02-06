from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


Window.size = (360, 640)


class Container(GridLayout):
    first_number = 0
    action = ''

    def setNumber(self, number):
        if number == 0 and self.text_label.text == "":
            return

        self.text_label.text = self.text_label.text + str(number)

    def setPoint(self):
        if len(self.text_label.text.split('.')) > 1:
            return

        if self.text_label.text == '':
            self.text_label.text = '0.'
        else:
            self.text_label.text = self.text_label.text + '.'

    def clearAll(self):
        self.text_label.text = ''

    def calculate(self, action):
        self.first_number = float(self.text_label.text)
        self.action = action
        self.text_label.text = ''

    def result(self):
        if self.action == '+':
            result = self.first_number + float(self.text_label.text)
        elif self.action == '-':
            result = self.first_number - float(self.text_label.text)
        elif self.action == '*':
            result = self.first_number * float(self.text_label.text)
        elif self.action == '/':
            try:
                result = self.first_number / float(self.text_label.text)
            except ZeroDivisionError:
                result = "Ошибка"

        self.text_label.text = str(result)
        self.first_number = 0
        self.action = ''


class CalculatorApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Калькулятор"
        self.theme_cls.theme_style = "Light"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == "__main__":
    CalculatorApp().run()
