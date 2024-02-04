'''
Задача №49. Решение в группах
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
'''
from csv import DictReader,DictWriter
from os.path import exists

start_info = True


def program_ifo():
    print("Все поддерживаемые команды")
    print("q - Выход из программы ")
    print("w - запись  нового контакта")
    print("r -  чтение вашего справочнике")
    print("i - информация")

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt



class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt
def get_user_data():


    flag = False
    while not flag:
        try:
            first_name = input("Введите имя")

            if len(first_name) <2:
                raise NameError("Неверная длина")
            last_name = input("Введите фамилию ")
            phone_number = int(input("Введите телефон "))
            if len(str(phone_number)) <11:
                raise LenNumberError("Неверная длина номера")

        except ValueError:
            print("Вы вводите символы вместо цифр!")
            continue
        except NameError as err:
            print(err)
            continue
        except LenNumberError as err:
            print(err)
            continue
        return first_name,last_name,phone_number

def create_file(file_name):
    with open(file_name,"w",encoding="utf-8") as date:
        f_writer = DictWriter(date,fieldnames=["Имя","Фамилия","Телефон"])
        f_writer.writeheader()

def reader_file(file_name):
    with open(file_name, "r", encoding="utf-8") as date:
        f_reader = DictReader(date)
        return list(f_reader)

file_name = "phone.csv"

reader_file(file_name)

def write_file(file_name):
  user_date = get_user_data()
  res = reader_file(file_name)
  for el in res:
    if el["Телефон"] == str(user_date[2]):
        print("Такой пользователь уже существует")
        return
  obj = {"Имя": user_date[0], "Фамилия": user_date[1], "Телефон": user_date[2]}
  res.append(obj)
  with open(file_name, "w", encoding="utf-8", newline="") as date:
      f_writer = DictWriter(date, fieldnames=["Имя", "Фамилия", "Телефон"])
      f_writer.writeheader()
      f_writer.writerows(res)

def main():

    while True:
        if start_info == True:
            program_ifo()
        command = input("Введите команду ")
        if command == "q" or command == "й":
            break
        elif command =="w" or command == "ц":
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
            print("Данные успешно записанны")
            input("Press Enter to continue...")

        elif command =="r" or command == "к":
            if not exists(file_name):
                print("Файл не найден,создайте его ")
                continue
            print(reader_file((file_name)))
        elif command == "i" or command == "ш" :
            program_ifo()
main()