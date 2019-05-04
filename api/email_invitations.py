from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_invitation():
    msg_plain = render_to_string('email/invitation_email.txt', )
    msg_html = render_to_string('email/invitation_email.html', )

    send_mail(
        'email title',
        msg_plain,
        'some@sender.com',
        ['kingbd2@gmail.com'],
        html_message=msg_html,
    )