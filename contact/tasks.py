from django.conf import settings
from django.core.mail import EmailMessage

from gemotest.celery import app


@app.task
def send_info(
        name: str, lastName: str, patronymic: str,
        phone: str, email: str, dateOfBirth: str, 
        passNumber: str, address: str, analysisDate: str,
        completeDate: str):
    message = f"""
    name: {name}
    lastName: {lastName}
    patronymic: {patronymic}
    phone: {phone}
    email: {email}
    dateOfBirth: {dateOfBirth}
    passNumber: {passNumber}
    address: {address}
    analysisDate: {analysisDate}
    completeDate: {completeDate}
    """
    email = EmailMessage(
        "гемотест сайт",
        message, settings.EMAIL_HOST_USER,
        ['edznproger@gmail.com', 'megabmx4477@gmail.com'],
    )
    email.send(fail_silently=False)


