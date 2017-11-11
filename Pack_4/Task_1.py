def TimeToSec(time):  # Переводим время в секунды
    time_list = time.split(':')  # Для этого разделяем строку по : и записываем в список
    return float(time_list.pop()) + int(time_list.pop()) * 60 + int(time_list.pop()) * 3600
  # Считываем сначала милисекунды, потом секунды и т. д.


def cell(line_table):  # Теперь будем считывать по биржам
    list_line = line_table.split(',')  # Разделяем по ,
    time = TimeToSec(list_line[0])  # присваиваем значение времени
    exchange = list_line[3][0]  # присваиваем значение биржи
    trade_add(time, exchange)  # записываем в функцию


trades = {'V': [], 'D': [], 'X': [], 'Y': [], 'B': [], 'J': [], 'Q': [], 'Z': [], 'K': [], 'P': [], 'All': []}   # Делаем словарик для бирж
max = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}  # Обнуляем максимумы
times = {'V': 0, 'D': 0, 'X': 0, 'Y': 0, 'B': 0, 'J': 0, 'Q': 0, 'Z': 0, 'K': 0, 'P': 0, 'All': 0}  # обнуляем время


def trade_add(time, exchange):  # вот, наша основная функция
    trades[exchange].append(time)  # Добавляем время
    while time - trades[exchange][0] >= 1:  # необходимое условие, чтобы время было в пределахмодной секунды
        trades[exchange].pop(0)  # если больше, то выкидываем первый элемент и снова проверяем
    if len(trades[exchange]) > max[exchange]:  # теперь элементарно выбираем наибольшее
        max[exchange] = len(trades[exchange])
        times[exchange] = trades[exchange][0]  # Сохраняем начальную позицию времени, чтобы потом вывести
    if exchange != 'All':  # Этот блок необходим, чтобы каждый элемент проверять на всеобщую величину
        exchange = 'All'  # то есть присваиваем all и повторяем процедуру для него
        trade_add(time, exchange)  # вызывая эту же функцию! очень хитро!


def SecToTime(time):  # Обратный перевод вромени
    zero_min = ''  # Нужно, чтобы праильно вывести 06, а не 6
    zero_hours = ''
    zero_sec = ''
    hour = int(time // 3600)
    time = time - hour * 3600
    minutes = int(time // 60)
    seconds = int((time - minutes * 60) * 1000) / 1000
    if hour < 10: zero_hours = '0'  # Вот, если меньше десяти, то еще ноль вперед добавим
    if minutes < 10: zero_min = '0'
    if seconds < 10: zero_sec = '0'
    return zero_hours + str(hour) + ':' + zero_min + str(minutes) + ':' + zero_sec + str(seconds)  # такое присваиваем


def output():
    for a in max:
        print(a + ':' + str(max[a]) + '  ' + SecToTime(times[a]))


with open("TRD2.csv") as f:
    f.readline()
    for line in f.readlines():
        cell(line)
output()
