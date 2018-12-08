'''
1 def для статических данных
2 def для введеных с клавы
3 добавить бд для выбора
'''

from docxtpl import DocxTemplate
import datetime


contragents = ('Фирма 1', 'Фирма 2', 'Фирма 3')
print('Имя фирмы')
for contragent in contragents:
    print(contragent)

doc = DocxTemplate("ma.docx")
context = {'text2': 'Тестовый тест', 'text3': 'Теeee'}
doc.render(context)
# doc.save(str(datetime.date.today())+".docx")
print(datetime.date.today())

# number = input('Номер счета: ')
