class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите необходимое числовое значение и нажмите Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Некорректное значение (str и/или bool)")
                ask_user = input(f'Продолжить? Д/Н ')

                if ask_user == 'Д' or ask_user == 'д':
                    print(try_except.my_input())
                elif ask_user == 'Н' or ask_user == 'н':
                    return f'Программа завершена'
                else:
                    return f'Программа завершена'

try_except = Error(1)
print(try_except.my_input())
