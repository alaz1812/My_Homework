import requests
from lxml import html
import csv
import time

proxies = {
    'http': 'http://51.15.64.186:3128',
    'https': 'http://10.10.1.10:1080',
}


def get_link_arhiv(site):  # функция парсинга ссылок на архивные страницы статистики сайта
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    r = requests.get(site, headers=header, proxies=proxies)
    parsed_body = html.fromstring(r.text)
    arhiv = parsed_body.xpath('//p[@align="center"]//a/@href')  # парсим на ссылки в архиве
    arhiv = ['http://football.kulichki.net/trans/' + i for i in arhiv]
    arhiv.append(site)  # добавляем главную ссылку с текущими результатми за текущий год
    return (arhiv)


def parsing_arhive(site, command_name):  # функция парсинга архивных страниц статистики сайта
    # site='http://football.kulichki.net/trans/2008/index.htm'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    header1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144'}
    r = requests.get(site, headers=header, proxies=proxies)
    # print(r.text)
    parsed_body = html.fromstring(r.text)

    commands = parsed_body.xpath('//table/tr/td/p/font/b/a/text()')  # парсим на название команд

    commands = [i.replace('\n', '') for i in commands]  # убираем лишнее из названий
    commands = [i.replace('\t', '') for i in commands]  # убираем лишнее из названий
    # commands=[i.capitalize() for i in commands] #Переводим первый символ строки в верхний регистр, а все остальные в нижний
    date = parsed_body.xpath('//table/tr/td[1]/font/text()')  # берем дату игры команд
    # избавляемся от лишнего
    date = [i.replace('\n', '') for i in date]
    date = [i.replace('\t', '') for i in date]
    date = [i.replace('\xa0', '') for i in date]
    date = [i.replace('\n\t', '') for i in date]
    date = [i.replace('    ', '') for i in date]
    date = [i for i in date if i != '']
    time = parsed_body.xpath('//table/tr/td[2]/font/text()')  # берем время игры
    time = [i.replace('\xa0', '') for i in time]
    time = [i.replace('\n\t', '') for i in time]
    o = []
    result = (zip(date, time, commands))  # объеденяем вместе (дату игры + время игры + команды)
    for rows in result:  # для каждой строки
        for row in rows:  # для каждого значения строки
            if command_name in row:  # если в строке встречается словосочитание 'Наполи - Манчестер Сити'
                print(rows)
                # print(rows) # вывести строку с датой временем и названием команд


def parsing_current_page(site, command_name):  # функция парсинга главной страницы Наверняка можно было обойтись одним кодом,но я не придумал
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    header1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.1144'}
    r = requests.get(site, headers=header, proxies=proxies)
    # print(r.text)
    parsed_body = html.fromstring(r.text)
    # time=parsed_body.xpath('//table/tr/td/font/text()')
    # commands=parsed_body.xpath('//table/tr/td/p/font/b/a/text()')
    table = parsed_body.xpath('//table')[3]  # берем таблицу "КАЛЕНДАРЬ ОНЛАЙН-ТРАНСЛЯЦИЙ."
    commands = table.xpath('tr/td/p/font/b/a/text()')  # парсим на название команд
    commands = [i.replace('\n', '') for i in commands]  # убираем лишнее из названий
    commands = [i.replace('\t', '') for i in commands]  # убираем лишнее из названий
    # commands=[i.capitalize() for i in commands] Переводим первый символ строки в верхний регистр, а все остальные в нижний
    date = table.xpath('tr/td[1]/font/text()')  # берем дату игры команд
    # избавляемся от лишнего
    date = [i.replace('\n', '') for i in date]
    date = [i.replace('\t', '') for i in date]
    date = [i.replace('\xa0', '') for i in date]
    date = [i.replace('\n\t', '') for i in date]
    date = [i.replace('    ', '') for i in date]
    date = [i for i in date if i != '']
    time = table.xpath('tr/td[2]/font/text()')  # берем время игры
    result = (zip(date, time, commands))  # объеденяем вместе (дату игры + время игры + команды)
    for rows in result:  # для каждой строки
        for row in rows:  # для каждого значения строки
            if command_name in row:  # если в строке встречается словосочитание 'Наполи - Манчестер Сити'
                print(rows)  # вывести строку с датой временем и названием команд


a = input(str('Доброго времени суток! Хотите узнать результат футбольного матча? Введите название команд с заглавной буквы через дефис: '))  # например, Зенит - Бенфика
site = 'http://football.kulichki.net/trans/'
links = get_link_arhiv(site)
for i in links:
    if i == 'http://football.kulichki.net/trans/':
        parsing_current_page(i, a)
    else:
        (parsing_arhive(i, a))