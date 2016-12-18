from model.group import Group
import random
import string
import os.path #для работы с путями до файлов
import jsonpickle
import getopt # для использования опций из командной строки
import sys #для получения доступа к этим опциям


# описание получение опций из оф. документации питона
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

# указываем дефольные значения
n = 2
f = "data/groups.json"

for o, a in opts:
    if o == "-n": #если название опции равно -n
        n = int(a) #значит в ней задается количество групп
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
    for i in range(n) #цикл для генерации случайных данных. 5 раз. то есть все данные для теста будут состоять из одной пустой группы и 5 групп со случ. данными

]

# сохраняем сгенерированные данные в фаил
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)  # путь к файлу

# открываем фаил
with open(file, "w") as out:
    # dumps - превращает данные в строку вида json
    #out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2)) #т.к. json не знает как преобразовывать объъекты типа group в словарь, мы ему подскажем - лямбда функцией. он сначала выполнит ее, а потом будет преобразовывать
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
