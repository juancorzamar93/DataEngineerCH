# import yagmail

# def send_alert(subject, body):
#     sender = 'pythonanaconda93@gmail.com'
#     app_password = 'tu_contraseña_de_aplicación_generada'  # Reemplazar con tu contraseña de aplicación real
    
#     yag = yagmail.SMTP(user=sender, password=app_password)
#     yag.send(to=sender, subject=subject, contents=body)
#     print("Alerta enviada")

# def check_for_alerts(data):
#     # Suponiendo que 'data' es un diccionario con las tasas de cambio y precios BTC
#     if data['rate'] > 0.05:  # Supongamos que alertamos si el cambio es mayor al 5%
#         send_alert('Alerta de Tasa de Cambio', 'La tasa de cambio ha variado significativamente.')
#     if data['btc_price_change'] > 1000:  # Supongamos que alertamos si el cambio es mayor a 1000 unidades
#         send_alert('Alerta de Precio BTC', 'El precio de BTC ha cambiado significativamente.')

# # Ejemplo de uso
# # check_for_alerts({'rate_change': 0.06, 'btc_price_change': 1500})

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)


def send_email(subject, body):
    sender_email = "pythonanaconda93@gmail.com"
    receiver_email = "pythonanaconda93@gmail.com"  
    password = os.getenv('PASSWORD_EMAIL')  
       
    # Crear el objeto del mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Agregar el cuerpo del mensaje al email
    msg.attach(MIMEText(body, 'plain'))

    # Crear la conexión segura con el servidor y enviar el email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Correo enviado exitosamente!")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

def check_for_alerts(data, rate_threshold, btc_price_threshold):
    """
    Comprueba cambios significativos en el tipo de cambio y en el precio del BTC,
    y envía alertas de correo electrónico si se superan los umbrales establecidos.
    """
    # Alerta para cambio en la tasa de cambio de divisas
    if abs(data['rate']) > rate_threshold:
        subject = "Alerta de Tasa de Cambio"
        body = f"La tasa de cambio ha variado significativamente: {data['rate']*100}%"
        send_email(subject, body)
        print("Alerta enviada debido a cambio significativo en la tasa de cambio.")

    # Alerta para cambio en el precio de compra de BTC
    if abs(data['buy_btc_ars']) > btc_price_threshold:
        subject = "Alerta de Precio BTC"
        body = f"El precio de compra de BTC ha cambiado significativamente, cambio actual: ${data['buy_btc_ars']}"
        send_email(subject, body)
        print("Alerta enviada debido a cambio significativo en el precio de BTC.")

    print("Revisión de alertas completada.")

