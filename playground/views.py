from django.shortcuts import render
from django.core.mail import mail_admins, send_mail, BadHeaderError, EmailMessage
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from rest_framework.views import APIView
import logging

logger = logging.getLogger(__name__)


@cache_page(timeout=5 * 60)
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

    #LOW LEVEL CACHING


    # key = 'httpbin_result'
    # if cache.get(key) is None:
    #     response = requests.get('https://httpbin.org/delay/2')
    #     data = response.json()
    #     cache.set(key, data, timeout=10 * 60)

    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()

    return render(request, 'hello.html', {'name': data})


#CACHING BY CACHING VIEW
# class HelloView(APIView):
#     @method_decorator(cache_page(5 * 60))
#     def get(self, request):
#         response = requests.get('https://httpbin.org/delay/2')
#         data = response.json()

#         return render(request, 'hello.html', {'name': data})


class HelloView(APIView):
    notify_customers.delay('hello')
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            data = response.json()
            logger.info('received httpbin')
            
        except request.ConnectionError:
            logger.critical('httbin is offline')

        return render(request, 'hello.html', {'name': data})
