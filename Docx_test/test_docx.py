from docxtpl import DocxTemplate

name = input('name')
year = input('year')
mark = input('mark')

doc = DocxTemplate("test.docx")
context = {
    'name': name,
    'year': year,
    'mark': mark
}

doc.render(context)
doc.save('otchet.docx')