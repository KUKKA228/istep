#Класс Компьютер
class Computer:
    def __init__(self, model, *args, **kwargs):
        #Метод super()
        super().__init__(*args, **kwargs)
        #Переменная (Модель,Память)
        self.model = model
        self.memory = 128
#Класс Дисплей
class Display:
    def init (self, *args, **kwargs):
        #Метод super()
        super().__init__(*args, **kwargs)
        #Переменная (Разрешение)
        self.resolution = "4k"
#Класс Смартфон
class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.resolution)
        print(self.memory)
iphone = SmartPhone(model = "Last")
iphone.print_info()

