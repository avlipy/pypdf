'''
1 def для статических данных
2 def для введеных с клавы
3 добавить бд для выбора

'''
'''
from mailmerge import MailMerge

template = r'/home/boomtop/PycharmProjects/pypdf/ma.docx'

document = MailMerge(template)
print(document.get_merge_fields())

document.merge(
    text1='Тестовое поле!'
)

document.write('test1.docx')'''
from docxtpl import DocxTemplate

doc = DocxTemplate("ma.docx")
context = {'text2': "Тестовый тест" }
doc.render(context)
doc.save("generated_doc.docx")