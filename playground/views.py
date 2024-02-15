from django.shortcuts import render
from django.core.mail import mail_admins, send_mail, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests

def say_hello(request):
    # try:
    #     message = EmailMessage('subject', 'message', 'lgurjidze@gmail.com', ['luka.gurjidze04@gmail.com'])
    #     message.attach_file('playground/static/images/channel-2.jpeg')
    #     message.send()
    # except BadHeaderError:
    #     pass

    notify_customers.delay('hello')

    # try:
    #     message = BaseEmailMessage(template_name='emails/hello.html', context={'name': 'Gurjika'})
    #     message.send(['gurjika@gmail.com'])
    # except BadHeaderError:
    #     pass

    requests.get('https://httpbin.org/delay/2')
    
    return render(request, 'hello.html', {'name': 'Mosh'})
