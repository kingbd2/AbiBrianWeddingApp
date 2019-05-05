from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_invitation(c):
    msg_plain = render_to_string('email/wedding_invitation_email.txt', c)
    msg_html = render_to_string('email/wedding_invitation_email.html', c)

    send_mail(
        'Abiella and Brian are getting married!',
        msg_plain,
        'abiella.and.brian@gmail.com',
        ['kingbd2@gmail.com'],
        html_message=msg_html,
    )
