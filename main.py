from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from kivy.core.window import Window
from kivy.animation import Animation
from ruffier import test
from seconds import Seconds

name = ''
age = 7
result1 = 0
result2 = 0
result3 = 0

window_color = (0.92, 0.20, 0.34, 1)
btn_color = (0.98, 0.15, 0.27, 0.8)

def check_int(age):
    try:
        age = int(age)
    except:
        return False
    return age

class InstrScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction)
        name = Label(text = 'Введите имя:', halign = 'right')
        self.in_name = TextInput(multiline = False)
        age = Label(text = 'Введите возраст:', halign = 'right')
        self.in_age = TextInput(text='7', multiline =False)
        Window.clearcolor = window_color

        self.btn = Button(text = 'Начать', size_hint= (0.3, 0.2), pos_hint = {'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_color

        line1 = BoxLayout(size_hint=(0.8, None), height = '30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height = '30sp')
        line1.add_widget(name)
        line1.add_widget(self.in_name)
        line2.add_widget(age)
        line2.add_widget(self.in_age)
        self.btn.on_press = self.next

        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        global name
        global age
        name = self.in_name.text
        age = int(self.in_age.text)

        if age < 7 or age == False:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = 'pulse1'

class PulseScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.lbl_seconds = Seconds(15)
        self.lbl_seconds.bind(done=self.finished)
        instr = Label(text=txt_test1)
        result1 = Label(text='Введите результат:', halign='right')
        self.in_result1 = TextInput(text='75', multiline=False)
        self.in_result1.set_disabled(True)

        self.btn = Button(text = 'Начать', size_hint= (0.3, 0.2), pos_hint = {'center_x': 0.5})
        self.btn.on_press = self.next
        #self.btn.set_disabled(True)
        self.btn.on_press = self.next
        self.btn.background_color = btn_color

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(result1)
        line1.add_widget(self.in_result1)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(self.btn)
        outer.add_widget(self.lbl_seconds)
        self.add_widget(outer)

    def finished(self, *args):
        self.next_screen = True
        self.in_result1.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_seconds.start()
        else:
            global result1
            result1 = int(self.in_result1.text)
            if result1 < 7 or result1 == False:
                result1 = 0
                self.in_result1.text = str(result1)
            else:
                self.manager.current = 'pulse2'

class PulseScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)

        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_color

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        self.manager.current = 'pulse3'


class PulseScreen3(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.lbl_seconds = Seconds(15)
        self.lbl_seconds.bind(done = self.finished)
        instr = Label(text=txt_test3)
        result2 = Label(text='Результат:', halign='right')
        self.in_result2 = TextInput(text = '0', multiline=False)
        result3 = Label(text='Результат после отдыха:', halign='right')
        self.in_result3 = TextInput(text='0', multiline=False)
        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_color
        anim = Animation()

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(result2)
        line1.add_widget(self.in_result2)
        line2.add_widget(result3)
        line2.add_widget(self.in_result3)

        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def finished(self, *args):
        self.next_screen = True
        self.in_result2.set_disabled(False)
        self.in_result3.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'

    def next(self):
        global result2, result3
        result2 = int(self.in_result2.text)
        result3 = int(self.in_result3.text)
        self.manager.current = 'result'


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instructions = Label(text = '')
        self.outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        self.outer.add_widget(self.instructions)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        self.instructions = name + '/n' + test(result1, result2, result3, age)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScreen(name = 'instr'))
        sm.add_widget(PulseScreen1(name = 'pulse1'))
        sm.add_widget(PulseScreen2(name='pulse2'))
        sm.add_widget(PulseScreen3(name='pulse3'))
        sm.add_widget(Result(name='result'))
        return sm


app = HeartCheck()
app.run()