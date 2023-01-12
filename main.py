from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle


class Prin(BoxLayout):

    def __init__(self, **kwargs):
        super(Prin, self).__init__(**kwargs)

        with self.canvas.before:
            Rectangle(source='gradient_pict.png', pos=self.pos, size=Window.size)


class MainApp(App):

    def canonical_form(self, num):
        lis = []
        if int(num ** 0.5) == num ** 0.5:
            lis = [int(num ** 0.5)]
        for d in range(int(num ** 0.5) - 1, 0, -1):
            if num % d == 0:
                lis.append(num // d)
                lis.insert(0, d)

        can = []
        for d in lis:
            for n in range(len(can)):
                while d % can[n][0] == 0:
                    can[n][1] += 1
                    d //= can[n][0]
            if d != 1:
                can.append([d, 1])
        for i in can:
            i[1] *= 2
            i[1] //= len(lis)
        return f'{num} = {" * ".join([str(i[0]) + "^" + str(i[1]) for i in can])}'

    def __init__(self):
        super().__init__()
        self.intro_label = Label(text='[b][i][size=70][u]Canonical factorization[/u][/size][size=60]\n>>> Write down your number\n[/size][/i][/b]', markup=True,
                                 font_size='40sp')

        self.btn = Button(text='Submit')
        self.input_num = TextInput(hint_text='Number:', multiline=False)
        self.btn.bind(on_press=self.btn_pressed)
        self.data = Label(text='[b][i][size=40]1357 = 23^1 * 59^1[/size][/i][/b]', font_size='30sp', markup=True)

    def btn_pressed(self, *args):
        if self.input_num.text.isdigit():
            self.data.text = f'[b][i][size=40]{self.canonical_form(int(self.input_num.text))}[/size][/i][/b]'
            self.input_num.text = ''

    def build(self):
        self.title = 'UniqueNumber'

        box = BoxLayout(orientation='vertical')

        box.add_widget(Prin())

        box.add_widget(self.intro_label)
        box.add_widget(self.input_num)
        box.add_widget(self.btn)
        box.add_widget(self.data)

        return box


if __name__ == "__main__":
    MainApp().run()
