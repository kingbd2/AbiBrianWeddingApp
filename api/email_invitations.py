from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_invitation(c, email):
    msg_plain = render_to_string('email/wedding_invitation_email.txt', c)
    msg_html = render_to_string('email/wedding_invitation_email.html', c)
    print("This is a real email to " + email)
    
    send_mail(
        'Abiella and Brian are getting married!',
        msg_plain,
        'abiella.and.brian@gmail.com',
        [email],
        html_message=msg_html,
    )
