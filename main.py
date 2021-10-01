from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from instruction import txt_instruction
from instruction import txt_test1
from instruction import txt_test2
from instruction import txt_test3
from instruction import txt_sits
from ruffier import txt_res
from ruffier import txt_index
from ruffier import txt_nodata
from ruffier import txt_workheart

class InstrScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction)
        name = Label(text = 'Введите имя:', halign = 'right')
        self.in_name = TextInput(multiline = False)
        age = Label(text = 'Введите возраст:', halign = 'right')
        self.in_age = TextInput(text='7', multiline =False)

        self.btn = Button(text = 'Начать', size_hint= (0.3, 0.2), pos_hint = {'center_x': 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height = '30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height = '30sp')
        line1.add_widget(name)
        line1.add_widget(self.in_name)
        line2.add_widget(age)
        line2.add_widget(self.in_age)

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
        age = self.in_age.text
        self.manager.current = 'pulse1'

class PulseScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test1)
        result1 = Label(text='Введите результат:', halign='right')
        self.in_result1 = TextInput(text='75', multiline=False)

        self.btn = Button(text = 'Продолжить', size_hint= (0.3, 0.2), pos_hint = {'center_x': 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(result1)
        line1.add_widget(self.in_result1)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        self.manager.current = 'pulse2'
        global result1
        result1 = self.in_result1.text


class PulseScreen2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)

        self.btn = Button(text='Продолжить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

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
        instr = Label(text=txt_test3)
        result2 = Label(text='Результат:', halign='right')
        self.in_result2 = TextInput(text = '0', multiline=False)
        result3 = Label(text='Результат после отдыха:', halign='right')
        self.in_result3 = TextInput(text='0', multiline=False)

        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(result2)
        line1.add_widget(self.in_result2)
        line2.add_widget(result3)
        line2.add_widget(self.in_result3)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def next(self):
        global result2
        result2 = self.in_result2.text
        global result3
        result3 = self.in_result3.text
        self.manager.current = 'pulse4'


class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        name1 = Label(text='')
        ruffier = Label(text = txt_res)

        def ruffier_index(result1, result2, result3):
            return (4 * (result1 + result2 + result3) - 200) / 10

        def neud_level(age):
            norm_age = (min(age, 15) - 7) // 2
            result = 21 - norm_age * 1.5
            return result

        def ruffier_result(r_index, level):
            if r_index >= level:
                return 0
            level = level - 4
            if r_index >= level:
                return 1
            level = level - 5
            if r_index >= level:
                return 2
            level = level - 5.5
            if r_index >= level:
                return 3
            return 4

        def test(result1, result2, result3, age):
            if age < 7:
                return (txt_index + "0", txt_nodata)
            else:
                ruff_index = ruffier_index(result1, result2, result3)
                result = txt_res[ruffier_result(ruff_index, neud_level(
                    age))]
                res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
                return res

        if ruffier_result(1, 1):
            txt_res.append('''низкая. 
            Срочно обратитесь к врачу!''')
        if ruffier_result(2, 2):
            txt_res.append('''удовлетворительная. 
            Обратитесь к врачу!''')
        if ruffier_result(3, 3):
            txt_res.append('''средняя. 
            Возможно, стоит дополнительно обследоваться у врача.''')
        if ruffier_result(4, 4):
            txt_res.append('''
            выше среднего''')
        if ruffier_result(5, 5):
            txt_res.append('''
            высокая''')

        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(name1)
        line2.add_widget(ruffier)

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line1)
        outer.add_widget(line2)

        self.add_widget(outer)




class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScreen(name = 'instr'))
        sm.add_widget(PulseScreen1(name = 'pulse1'))
        sm.add_widget(PulseScreen2(name='pulse2'))
        sm.add_widget(PulseScreen3(name='pulse3'))
        sm.add_widget(Result(name='result'))
        return  sm


app = HeartCheck()
app.run()