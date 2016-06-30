from __future__ import print_function
import csv
import reportlab
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from sys import argv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

point = 1
inch = 72

exam_results_raw = []

data = open("exam.csv",'rb')
f = csv.reader(data)
header = f.next()

for row in f:
    exam_results_raw.append(row)

final_grad_list = [ ]

for i in range (0, len(exam_results_raw)):
    number = exam_results_raw[i][2]
    name = exam_results_raw[i][1]
    quiz = (float(exam_results_raw[i][3])*1.5)/75
    f_exam = (float(exam_results_raw[i][4])*3.50)/100
    f_grade =  round(1+quiz+f_exam,2)
    final_grad_list.append([number, name, quiz, f_exam, f_grade])

#Structure [Number, Name, Quiz Grade, Exam Grade, Final Grade]

for i in range (0, len(final_grad_list)):
#    print (final_grad_list[i])

    c = canvas.Canvas(str(final_grad_list[i][1]), pagesize=letter)

    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    c.drawString(200,750,'Business Intelligence and Analytics')

    c.drawString(120,700,'Name:')
    c.drawString(170,700,final_grad_list[i][1])

    c.drawString(120,650,'Number:')
    c.drawString(170,650,final_grad_list[i][0])

    c.drawString(120,600,'Quiz Grade/1.5:')
    c.drawString(300,600,str(final_grad_list[i][2]))

    c.drawString(120,550,'Exam Grade/3.5:')
    c.drawString(300,550,str(final_grad_list[i][3]))

    c.drawString(120,500,'Final Grade/6:')
    c.drawString(300,500,str(final_grad_list[i][4]))

    c.save()
