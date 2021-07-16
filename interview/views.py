
from .models import Interview
from .forms import InterviewForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.conf import settings
from django.forms.models import model_to_dict
from django.db.models import Sum, Count
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import PageTemplate, Frame, NextPageTemplate, BaseDocTemplate, SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_RIGHT, TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor
import requests
import re
from urllib.request import urlopen
from evaluation.models import Test_Assign


PartnerLogo = "https://raw.githubusercontent.com/JorgeScp/randomfiles/main/logo_E2E.png"
#PartnerLogo = "https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=png&cs=fFNQTw&docid=https%3A%2F%2Flinkam-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!tb30pSTWMkSXMivGJmJNbpMzxD32bjdHlSgKAhwQmR7c8pEJKiKZTqNc4Nxxoc94%2Fitems%2F01O6MELQB6SB4MDO465JCJVJTX3QS4OD3K%3Fversion%3DPublished&encodeFailures=1&ctag=%22c%3A%7BC178903E-9EBB-44EA-9AA6-77DC25C70F6A%7D%2C1%22&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvbGlua2FtLW15LnNoYXJlcG9pbnQuY29tQGVjMDA4MmE5LWU5YzItNGQ2NS1hODFkLTdjM2U2YmRjZjczMyIsImlzcyI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMCIsIm5iZiI6IjE2MjQ2NDM5OTkiLCJleHAiOiIxNjI0NjY1NTk5IiwiZW5kcG9pbnR1cmwiOiJldzUrNk50KzM2a1VXVm5kRVhkQmQwRHFYY2FlYzFTeHJOZUUwZURvdzQ4PSIsImVuZHBvaW50dXJsTGVuZ3RoIjoiMTE2IiwiaXNsb29wYmFjayI6IlRydWUiLCJ2ZXIiOiJoYXNoZWRwcm9vZnRva2VuIiwic2l0ZWlkIjoiWVRWbU5HSmtZalV0WkRZeU5DMDBORE15TFRrM016SXRNbUpqTmpJMk5qSTBaRFpsIiwibmFtZWlkIjoiMCMuZnxtZW1iZXJzaGlwfHVybiUzYXNwbyUzYWFub24jZmUxMWY2MTY1MjhmZTcwMmFiODJiMjc0OTZhODI0NTM0ODFkOTA3OGFlZTIwNzMyNjg2ZTM2YmZmZDM0YWYzMCIsIm5paSI6Im1pY3Jvc29mdC5zaGFyZXBvaW50IiwiaXN1c2VyIjoidHJ1ZSIsImNhY2hla2V5IjoiMGguZnxtZW1iZXJzaGlwfHVybiUzYXNwbyUzYWFub24jZmUxMWY2MTY1MjhmZTcwMmFiODJiMjc0OTZhODI0NTM0ODFkOTA3OGFlZTIwNzMyNjg2ZTM2YmZmZDM0YWYzMCIsInNoYXJpbmdpZCI6Ikk1MWFNUmxGdGtLRUxlQ2NyVXVUQ1EiLCJ0dCI6IjAiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjoiMiJ9.Tm9oaDVnWkQ2UkMvNzZkMC9qQWl1QVYxT1h1MDZtK21XRkJJU2RDUkp6TT0&prooftoken=undefined&srcWidth=&srcHeight=&width=1366&height=581&action=Access"
def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url)
   if image_formats in r.headers.get("content-type",""):
      return True
   return False

def x__chopLine(line, maxline):
    if len(line) < int(maxline):
        return line
    else:
        cant = len(line) / int(maxline)
        cant += 1
        strline = ""
        index = int(maxline)
        for i in range(1,int(cant)):
            index = int(maxline) * i
            strline += "%s\n" %(line[(index-int(maxline)):index])
        strline += "%s\n" %(line[index:])
        return strline[0:255]

def x__chopLine2(line, maxline):
    if len(line) < int(maxline):
        return line
    else:
        cant = len(line) / int(maxline)
        cant += 1
        strline = ""
        index = int(maxline)
        for i in range(1,int(cant)):
            index = int(maxline) * i
            strline += "%s\n" %(line[(index-int(maxline)):index])
        strline += "%s\n" %(line[index:])
        return strline[0:255]

def export_pdf(request,id):
    
    
    interview = Interview.objects.get(pk=id)
    itdate = str(interview.dated)[0:10]
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="ED-{interview.evaluated.last_name} {interview.evaluated.first_name}-{itdate}.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    line_x_start = 10
    line_width = 100
    line_y = 520

    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='header white', fontName ='Arial',fontSize=14, leading=16,backColor = colors.black, textColor=colors.white, alignment=TA_LEFT))
    styles.add(ParagraphStyle(name='Table Top Red Back', fontName ='Arial',fontSize=9, leading=12, backColor = colors.red, textColor=colors.black, alignment=TA_LEFT))
    p.setTitle("Evaluación de Desempeño E2E")
    #header
    p.drawImage(PartnerLogo, line_x_start, line_y, width=line_width, 
                 preserveAspectRatio=True, mask='auto') 
    #title
    p.setFillColor(HexColor("#b7d53a"))
    p.setStrokeColor(HexColor("#b7d53a"))
    p.rect(140,790,300,50,fill=1)

    p.setFillColor(colors.white)
    p.setStrokeColor(colors.white)
    p.setFont("Helvetica-Bold", 12)
    
    p.drawCentredString(290, 810, "EVALUACIÓN DE DESEMPEÑO")

    p.setFillColor(colors.black)
    p.setStrokeColor(colors.black)
    p.setFont("Helvetica-Bold", 10)
    
    p.drawCentredString(520, 810, "PÁGINA 1 DE 2")

    #=====================================================
    #Date / assessment
    p.setFillColor(HexColor("#b7d53a"))
    p.setStrokeColor(HexColor("#b7d53a"))
    p.rect(0,745,200,20,fill=1)

    p.setFillColor(colors.white)
    p.setStrokeColor(colors.white)
    p.setFont("Helvetica-Bold", 10)

    p.drawString(20, 750, "FECHA EVALUACIÓN")

    #Name title - a
    p.setFillColor(HexColor("#5c5c5b"))
    p.setStrokeColor(HexColor("#5c5c5b"))
    p.setFont("Helvetica-Bold", 10)
    date2 = interview.dated
    p.drawAlignedString(300, 750, str(date2)[0:10])
    #=====================================================

    #=====================================================
    #Header 1 / Data of the employee
    p.setFillColor(HexColor("#b7d53a"))
    p.setStrokeColor(HexColor("#b7d53a"))
    p.rect(0,715,755,20,fill=1)

    p.setFillColor(colors.white)
    p.setStrokeColor(colors.white)
    p.setFont("Helvetica-Bold", 10)

    p.drawString(20, 720, "DATOS DEL EVALUADO")

    data2 = [
        ['NOMBRE', interview.evaluated.last_name + ' ' + interview.evaluated.first_name],
        ['CARGO', str(interview.evaluated.jobname)],
        ['TEAM', str(interview.evaluated.team)],
        ['CARGO', str(interview.evaluated.jobname)],
        ['NOMBRE JEFE INMEDIATO', str(interview.evaluated.boss_name)],
        ['CARGO JEFE INMEDIATO', str(interview.boss_job_name)],
    ]

    width = 600
    height = 200
    x = 20
    y = 595
    f = Table(data2)
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 8),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #set fond
                       ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
                       #('BACKGROUND',(-2,-2),(-1,-1), colors.pink),
                       
                       ('BACKGROUND',(0,0),(1,0), HexColor("#bcc2cf")),
                       #second
                       ('BACKGROUND',(0,2),(1,2), HexColor("#bcc2cf")),
                       #third
                       ('BACKGROUND',(0,4),(1,4), HexColor("#bcc2cf")),

                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)

    p.setFillColor(colors.white)
    p.setStrokeColor(colors.white)
    p.setFont("Helvetica-Bold", 10)

    p.drawString(320, 720, "DATOS DEL EVALUADOR")

    data2 = [
        ['NOMBRE', interview.evaluator.last_name + ' '+ interview.evaluator.first_name],
        ['CARGO', str(interview.evaluator.jobname)],
        ['RELACIÓN', str(interview.relation)],
    ]

    width = 600
    height = 200
    x = 320
    y = 650
    f = Table(data2)
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 8),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #('BACKGROUND',(-2,-2),(-1,-1), colors.pink),
                       #set fond
                       ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
                       #('BACKGROUND',(-2,-2),(-1,-1), colors.pink),
                       
                       ('BACKGROUND',(0,0),(1,0), HexColor("#bcc2cf")),
                       #second
                       ('BACKGROUND',(0,2),(1,2), HexColor("#bcc2cf")),
                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)
    #====================================================
    #Header 1 / Data of the employee
    #====================================================

    p.setFillColor(HexColor("#b7d53a"))
    p.setStrokeColor(HexColor("#b7d53a"))
    p.rect(0,585,690,5,fill=1)

    #Calification Table

    data2 = [
        ['CALIFICACIÓN','','','',''],
        ['Deficiente', 'Regular','Aceptable','Muy Bueno','Excelente'],
        ['De 1 a 20', 'De 21 a 40','De 41 a 65','De 66 a 85','De 86 a 100'],
    ]

    width = 600
    height = 200
    x = 160
    y = 525
    f = Table(data2)
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 8),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       ('ALIGN', (0, 0), (4, 0), "CENTER"),
                       ('SPAN', (0, 0), (4, 0)),
                       ('BACKGROUND',(0,0),(4,0), HexColor("#b7d53a")),
                       ('TEXTCOLOR', (0, 0), (4, 0), colors.white)
                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)


    data2 = [
        ['COMPETENCIAS A EVALUAR','CALIFICACIÓN'],

        ['COMUNICACIÓN', interview.comunicacion_r],
        ['TRABAJO EN EQUIPO', interview.trabajo_equipo_r],
        ['SERVICIO AL CLIENTE', interview.servicio_cliente_r],
        ['RESOLUCIÓN DE PROBLEMAS', interview.resolucion_problemas_r],
        ['LIDERAZGO', interview.resolucion_problemas_r],
        ['ADMINISTRACIÓN DEL TIEMPO', interview.admon_tiempo_r],
        ['PENSAMIENTO ESTRATÉGICO', interview.pensamiento_estrategico_r],
        ['ENFOQUE A RESULTADOS', interview.enfoque_resultados_r],
    ]

    width = 600
    height = 200
    x = 180
    y = 355
    f = Table(data2)
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 8),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #TITLE
                       ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                       ('BACKGROUND',(0,0),(2,0), HexColor("#b7d53a")),
                       ('TEXTCOLOR', (0, 0), (2, 0), colors.white),
                       #COMUNICATION
                       #set fond
                       ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
                       #('BACKGROUND',(-2,-2),(-1,-1), colors.pink),
                       ('BACKGROUND',(0,1),(1,1), HexColor("#bcc2cf")),
                       #second
                       ('BACKGROUND',(0,3),(1,3), HexColor("#bcc2cf")),
                       #third
                       ('BACKGROUND',(0,5),(1,5), HexColor("#bcc2cf")),
                        #four
                       ('BACKGROUND',(0,7),(1,7), HexColor("#bcc2cf")),

                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)

    #general calification
    data2 = [
        ['CALIFICACIÓN GENERAL'],
        [str(interview.result)[0:6]],
    ]

    width = 600
    height = 200
    x = 400
    y = 430
    f = Table(data2)
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 8),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #TITLE
                       ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('BACKGROUND',(0,0),(2,0), HexColor("#b7d53a")),
                       ('TEXTCOLOR', (0, 0), (2, 0), colors.white),
                       #COMUNICATION
                       #('SPAN', (0, 1), (1, 1)),
                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)

    #other


    p.setFillColor(HexColor("#b7d53a"))
    p.setStrokeColor(HexColor("#b7d53a"))
    p.rect(0,342,650,5,fill=1)


    data2 = [
        ['FORTALEZAS Y ÁREAS DE OPORTUNIDAD',''],
        ['Indica algunas fortalezas y áreas de oportunidad particulares que identifiques en el evaluado', ''],
        ['FORTALEZAS', x__chopLine(interview.strengths,int(105))],
        ['', ''],
        ['ÁREAS DE OPORTUNIDAD', x__chopLine(interview.oportunities_areas,int(105))],
        ['', ''],
    ]

    width = 300
    height = 300
    x = 10
    y = 205
    f = Table(data2,colWidths=[150,415],rowHeights=(18, 18, 22,22,22,28))
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 10),
                       ('FONTSIZE', (0, 1), (1, 1), 6),
                       ('FONTSIZE', (0, 2), (-1, -1), 8),
                       
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #TITLE
                       ('ALIGN', (0, 0), (1, 1), "CENTER"),
                       ('ALIGN', (2, 0), (3, 0), "CENTER"),
                       ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                       ('BACKGROUND',(0,0),(2,0), HexColor("#b7d53a")),
                       ('TEXTCOLOR', (0, 0), (2, 0), colors.white),
                       ('SPAN', (0, 0), (1, 0)),
                       #Message
                       ('SPAN', (0, 1), (1, 1)),
                       #strengths
                       ('SPAN', (0, 2), (0, 3)),
                            #second column
                       ('SPAN', (1, 2), (1, 3)),
                       #oportunities
                       ('SPAN', (0, 4), (0, 5)),
                            #second column
                       ('SPAN', (1, 4), (1, 5)),
                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)

    #Data
    data2 = [
        ['¿Qué le sugerirías al evaluado para mejorar su desempeño profesional y personal?'],
        [x__chopLine2(interview.general_question,int(150))],
        [''],
    ]

    width = 300
    height = 300
    x = 10
    y = 145
    f = Table(data2,colWidths=[565],rowHeights=(18,18,18))
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 10),
                       ('FONTSIZE', (0, 1), (1, 1), 8),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #TITLE
                       ('ALIGN', (0, 0), (2, 0), "CENTER"),
                       ('BACKGROUND',(0,0),(2,0), HexColor("#b7d53a")),
                       ('TEXTCOLOR', (0, 0), (2, 0), colors.white),
                       #Message
                       ('SPAN', (0, 1), (0, 2)),

                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)

    #Observations
    #Data
    data2 = [
        ['Observaciones:',x__chopLine(interview.observations,int(80))],
    ]

    width = 300
    height = 300
    x = 10
    y = 120
    f = Table(data2,colWidths=[75,490],rowHeights=(20))
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 8),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #TITLE
                       ('ALIGN', (0, 0), (2, 0), "CENTER"),
                       ('FONTNAME', (0,0), (0,1), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,0),(0,1), HexColor("#bcc2cf")),

                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)
    tem_file_path = "interview.url_signature"
    
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


    #signature
    checked_url = re.match(regex, tem_file_path)
    is_match = bool(checked_url)
    #Validate if image is ok
    if is_match == True:
        image_formats = ("image/png", "image/jpeg", "image/gif")
        url = tem_file_path
        try:
            site = urlopen(url)
            meta = site.info()  # get header of the http request
            if meta["content-type"] in image_formats:  # check if the content-type is a image
                print("it is an image")
                I = Image(tem_file_path)
            else:
                I = Image("https://raw.githubusercontent.com/JorgeScp/randomfiles/main/bg.png") 
        except:
                I = Image("https://raw.githubusercontent.com/JorgeScp/randomfiles/main/bg.png") 
    else:
        I = Image("https://raw.githubusercontent.com/JorgeScp/randomfiles/main/bg.png") 
    
    
    I.drawHeight = 40*I.drawHeight / I.drawWidth
    I.drawWidth = 170

    #Data
    data2 = [
        [I,'',''],
        ['Firma Evaluador','','Firma Evaluado'],
    ]

    width = 300
    height = 300
    x = 10
    y = 50
    f = Table(data2,colWidths=[170,225,170],rowHeights=(40,18))
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 8),
                       ('LINEABOVE', (0,1), (0,1), 0.25, colors.black),
                       ('LINEABOVE', (2,1), (2,1), 0.25, colors.black),
                       #('INNERGRID', (1,1), (2,2), 0.25, colors.black),
                       #('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #TITLE
                       ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                       #('BACKGROUND',(0,0),(0,1), HexColor("#b7d53a")),
                       #('TEXTCOLOR', (0, 0), (0, 1), colors.white),
                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)

    p.showPage()


    #========================================================================
    #SECOND PAGE -----------------------------------
    #========================================================================
    #skills to evaluate
    #========================================================================
    #header
    p.drawImage(PartnerLogo, line_x_start, line_y, width=line_width, 
                 preserveAspectRatio=True, mask='auto') 
    #title
    p.setFillColor(HexColor("#b7d53a"))
    p.setStrokeColor(HexColor("#b7d53a"))
    p.rect(140,780,300,50,fill=1)

    p.setFillColor(colors.white)
    p.setStrokeColor(colors.white)
    p.setFont("Helvetica-Bold", 14)

    p.drawCentredString(290, 800, "EVALUACIÓN DE DESEMPEÑO")
    
    p.setFillColor(colors.black)
    p.setStrokeColor(colors.black)
    p.setFont("Helvetica-Bold", 10)
    
    p.drawCentredString(520, 810, "PÁGINA 2 DE 2")

    p.setFillColor(colors.grey)
    p.setStrokeColor(colors.grey)
    p.setFont("Helvetica-Bold", 12)

    p.drawCentredString(290, 760, "DETALLE DE CALIFICACIONES")
    #=====================================================


    data2 = [
        ['COMPETENCIAS A EVALUAR','CALIFICACIÓN'],
        ['COMUNICACIÓN', interview.comunicacion_r],
        ['La información que comparte es clara y asertiva.', interview.comunicacion_1],
        ['Es receptivo a las opiniones y sugerencias de los demás. ', interview.comunicacion_2],
        ['Escucha y presta atención a las conversaciones.', interview.comunicacion_3],
        ['Su comunicación escrita es clara, concisa y efectiva.', interview.comunicacion_4],
        ['Expresa sus ideas con claridad y respeto a los demás.', interview.comunicacion_5],
 
        ['TRABAJO EN EQUIPO', interview.trabajo_equipo_r],
        ['Se desempeña como un miembro activo del equipo.', interview.trabajo_equipo_1],
        ['Motiva y guía al equipo para el logro de los objetivos establecidos.', interview.trabajo_equipo_2],
        ['Fomenta el diálogo de manera abierta y directa. ', interview.trabajo_equipo_3],
 
        ['SERVICIO AL CLIENTE', interview.servicio_cliente_r],
        ['Es cortes y amable en el trato que tiene con el cliente', interview.servicio_cliente_1],
        ['Se gestionan correctamente las solicitudes para dar respuesta de manera oportuna. ', interview.servicio_cliente_2],
        ['Realiza de manera oportuna, feedback a los procesos', interview.servicio_cliente_3],
  
        ['RESOLUCIÓN DE PROBLEMAS', interview.resolucion_problemas_r],
        ['Busca la información suficiente para la toma de decisiones.', interview.resolucion_problemas_1],
        ['Es flexible al cambio en las diferentes situaciones que se presentan.', interview.resolucion_problemas_2],
        ['Considera las implicaciones antes de llevar a cabo una acción.', interview.resolucion_problemas_3],
        ['Conserva la calma en situaciones complicadas.', interview.resolucion_problemas_4],
        ['Es propositivo en las diferentes situaciones que requieran soluciones o toma de decisiones de impacto. ', interview.resolucion_problemas_5],

        ['LIDERAZGO', interview.liderazgo_r],
        ['Se adapta a trabajar con nuevos procesos y tareas. ', interview.liderazgo_1],
        ['No muestra resistencia a las ideas de las demás personas.', interview.liderazgo_2],
        ['Comparte su conocimiento, habilidades y experiencia.', interview.liderazgo_3],
        ['Comparte el reconocimiento de logros con el resto del equipo.', interview.liderazgo_4],
        ['Busca reforzar sus habilidades y trabajar en sus áreas de oportunidad.', interview.liderazgo_5],

        ['ADMINISTRACIÓN DEL TIEMPO', interview.admon_tiempo_r],
        ['Establece prioridades en sus actividades laborales cumpliento con las metas y objetivos establecidos.', interview.admon_tiempo_1],
        ['Cumple con los tiempo y forma los proyectos asignados', interview.admon_tiempo_2],
        ['Utiliza eficientemente los recursos asignados para llevar a cabo sus actividades. ', interview.admon_tiempo_3],

        ['PENSAMIENTO ESTRATÉGICO', interview.pensamiento_estrategico_r],
        ['Comprende las implicaciones de sus decisiones en el negocio a corto y largo plazo.', interview.pensamiento_estrategico_1],
        ['Determina objetivos y establece prioridades para lograrlos. ', interview.pensamiento_estrategico_2],
        ['Tiene visión a largo plazo y busca oportunidades paracumplir con las metas de organización desde su área.', interview.pensamiento_estrategico_3],
        ['Es percibido por el cliente como una persona confiable que representa a la empresa. ', interview.pensamiento_estrategico_4],

        ['ENFOQUE A RESULTADOS', interview.enfoque_resultados_r],
        ['Reconoce y aprovecha las oportunidades que se presentan en las diferentes situaciones.', interview.enfoque_resultados_1],
        ['Mantiene altos niveles de estándares de desempeño ', interview.enfoque_resultados_2],
        ['Sus resultados son sobresalientes y generan valor a la empresa. ', interview.enfoque_resultados_3],
        ['Es detallista con la información que presenta y en pocas ocasiones se detectan inconsistencias o errores. ', interview.enfoque_resultados_4],

    ]

    width = 600
    height = 200
    x = 70
    y = 10
    f = Table(data2)
    f.setStyle(TableStyle([
                       ('FONTSIZE', (0, 0), (-1, -1), 7),
                       ('FONTNAME', (0,0), (1,2), 'Helvetica-Bold'),
                       ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                       ('BOX', (0,0), (-1,-1), 0.25, colors.black),
                       #TITLE
                       ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                       ('BACKGROUND',(0,0),(2,0), HexColor("#b7d53a")),
                       ('TEXTCOLOR', (0, 0), (2, 0), colors.white),
                       #COMUNICATION
                       ('FONTNAME', (0,1), (1,1), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,1),(1,1), HexColor("#bcc2cf")),
                       #2
                       ('FONTNAME', (0,7), (8,7), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,7),(8,7), HexColor("#bcc2cf")),
                        #3
                       ('FONTNAME', (0,11), (12,11), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,11),(12,11), HexColor("#bcc2cf")),
                       #4
                       ('FONTNAME', (0,15), (16,15), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,15),(16,15), HexColor("#bcc2cf")),
                       #5
                       ('FONTNAME', (0,21), (22,21), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,21),(22,21), HexColor("#bcc2cf")),
                       #6
                       ('FONTNAME', (0,27), (28,27), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,27),(28,27), HexColor("#bcc2cf")),
                       #7
                       ('FONTNAME', (0,31), (32,31), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,31),(32,31), HexColor("#bcc2cf")),
                       #8
                       ('FONTNAME', (0,36), (37,36), 'Helvetica-Bold'),
                       ('BACKGROUND',(0,36),(37,36), HexColor("#bcc2cf")),
                       ]))

    f.wrapOn(p, width, height)
    f.drawOn(p, x, y)

    # Close the PDF object cleanly, and we're done.
    p.showPage()

   
    p.save()
    return response





@login_required(login_url="/login/")
def int_list(request):
    if request.user.is_superuser:
        created_by_user = Interview.objects.all()
    else:
        created_by_user = Interview.objects.filter(evaluator=request.user)
    context = {'int_list': created_by_user}
    
    return render(request, "ui-tables-abs.html", context)


@login_required(login_url="/login/")
def int_form(request, id=0,pk=0):
    User_at = get_user_model()
    if request.method == "GET":
        if id == 0:
            form = InterviewForm()
        else:
            interview = Interview.objects.get(pk=id)
            employee_list = User_at.objects.all()
            form = InterviewForm(instance=interview)
            contextabs = {'form': form, 'employee_list': employee_list}
        return render(request, "abs_form.html", {'form': form, 'employee_list': User_at.objects.all()})
    else:
        if id == 0:
            form = InterviewForm(request.POST)
            assessment = form.save(commit=False)
        else:
            interview = Interview.objects.get(pk=id)
            form = InterviewForm(request.POST,instance= interview)
            assessment = form.save(commit=False)

        if form.is_valid():
            
            if pk != 0:
                prefill_data = Test_Assign.objects.get(pk=pk)
                prefill_data.done = "Completada"
                prefill_data.save()

                assessment.evaluated = prefill_data.evaluated
                assessment.evaluator = prefill_data.evaluator
                assessment.relation = prefill_data.relation
            else:
                emp_data = Interview.objects.get(pk=id)
                assessment.evaluated = emp_data.evaluated
                assessment.evaluator = emp_data.evaluator
                assessment.relation = emp_data.relation
                
            print(assessment.dated)
            assessment.comunicacion_r = (assessment.comunicacion_1 + assessment.comunicacion_2 + assessment.comunicacion_3 +assessment.comunicacion_4 +assessment.comunicacion_5) / (5)
            assessment.trabajo_equipo_r = (assessment.trabajo_equipo_1 + assessment.trabajo_equipo_2 + assessment.trabajo_equipo_3) / (3)
            assessment.servicio_cliente_r = (assessment.servicio_cliente_1+assessment.servicio_cliente_2+assessment.servicio_cliente_3) / (3)
            assessment.resolucion_problemas_r = (assessment.resolucion_problemas_1 + assessment.resolucion_problemas_2 +assessment.resolucion_problemas_3 +assessment.resolucion_problemas_4+assessment.resolucion_problemas_5) / (5)
            assessment.liderazgo_r = (assessment.liderazgo_1+assessment.liderazgo_2+assessment.liderazgo_3+assessment.liderazgo_4+assessment.liderazgo_5) / (5)
            assessment.admon_tiempo_r = (assessment.admon_tiempo_1+assessment.admon_tiempo_2+assessment.admon_tiempo_3) / (3)
            assessment.pensamiento_estrategico_r = (assessment.pensamiento_estrategico_1+assessment.pensamiento_estrategico_2+assessment.pensamiento_estrategico_3+assessment.pensamiento_estrategico_4) / (4)
            assessment.enfoque_resultados_r = (assessment.enfoque_resultados_1+assessment.enfoque_resultados_2+assessment.enfoque_resultados_3+assessment.enfoque_resultados_4) / (4)

            assessment.result = (assessment.comunicacion_r+assessment.trabajo_equipo_r+assessment.servicio_cliente_r+assessment.resolucion_problemas_r+assessment.liderazgo_r+assessment.admon_tiempo_r+assessment.pensamiento_estrategico_r+assessment.enfoque_resultados_r) / (8)
            assessment.save()
            return redirect('/int_list')
        else:
            return render(request,"abs_form.html",{'form':form})

@login_required(login_url="/login/")
def int_delete(request,id):
    interview = Interview.objects.get(pk=id)
    interview.delete()
    return redirect('/int_list')
# @login_required(login_url="/login/")
# class int_list(self, request):
#     """Generic class-based view listing books on loan to current user."""
#     model = Interview
#     template_name ='ui-tables-abs.html'
#     paginate_by = 10
    
#     def get_queryset(self):
#         return Interview.objects.filter(toUser=self.request.user)
