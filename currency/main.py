import requests
import inspect
from bs4 import BeautifulSoup
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = (800, 620)


class Container(GridLayout):
    first_number = None
    one_curs = ''
    two_curs = ''

    def clearAll(self):
        self.text_label.text = ''

    def setNumber(self, number):
        if number == 0 and self.text_label.text == "":
            return
        if self.first_number == None:
            self.text_label.text = ""
        self.text_label.text = self.text_label.text + str(number)
        self.first_number = self.text_label.text

    def curs(self, curs):
        if self.first_number == None:
            self.text_label.text = 'Введите число!'
            self.first_number = None

        elif self.one_curs == "":
            self.first_number = self.text_label.text
            self.one_curs = curs
            self.text_label.text = f'{self.first_number} {curs}'
        else:
            self.two_curs = curs
            self.text_label.text = curs
            try:
                url = f'https://finance.rambler.ru/calculators/converter/{self.first_number}-{self.one_curs}-{self.two_curs}'
                # print(url)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

                source = requests.get(url, headers=headers)
                main_text = source.text
                soup = BeautifulSoup(main_text, "html.parser")

                div1 = (soup.find('div', {'class': 'finance__converter-result'}))
                div2 = (div1.find('div', {'class': 'converter-change-table__result'})).text
                div2 = inspect.cleandoc(div2)[:5]

                div3 = (soup.find('div', {'class': 'finance__center'}))
                h2 = (div3.find('h2', {'class': 'finance__header'})).text

                cur = f'{h2}: {div2}'

                self.text_label.text = str(cur)
                self.first_number = None
                self.one_curs = ''
                self.two_curs = ''

            except Exception:
                self.text_label.text = "Error"


class CurrencyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Курсы валют"
        self.theme_cls.theme_style = "Light"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == "__main__":
    CurrencyApp().run()