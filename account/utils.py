from django.core.mail import send_mail


def send_welcome_email(email):
    url = 'http://localhost:8000/'
    message = f'<h1>Спасибо за регистрацию на наше сайте PyShop12:</h1> {url}'
    send_mail(
        'PuShop12 Welcome!!!',
        message,
        'pyshopadmin@gmail.com',
        [email, ],
        fail_silently=False
    )






