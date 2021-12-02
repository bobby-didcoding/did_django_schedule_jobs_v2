
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection
from django.contrib.auth.models import User
 
from celery import shared_task
from celery.utils.log import get_task_logger
 
logger = get_task_logger(__name__)
 
@shared_task()
def thirty_second_func():
    logger.info("I run every 30 seconds using Celery Beat")
    return "Done"
 
@shared_task(bind=True)
def create_email(self, user_id: int, **kwargs):
   
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return 'Failed'
    email_account = kwargs.get("email_account")
    subject = kwargs.get("subject", "")
    email = kwargs.get("email")
    template = kwargs.get("template")
    cc_email = kwargs.get("cc_email")
    context = kwargs.get("context", {})
 
    context["username"] = user.username
 
    email_accounts = {
        "do not reply": {
            'name': settings.EMAIL_HOST_USER,
            'password':settings.DONOT_REPLY_EMAIL_PASSWORD,
            'from':settings.EMAIL_HOST_USER,
            'display_name': settings.DISPLAY_NAME},
    }
 
    html_content = render_to_string(template, context ) # render with dynamic value
    text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.
 
    with get_connection(
            host= settings.EMAIL_HOST,
            port= settings.EMAIL_PORT,
            username=email_accounts[email_account]["name"],
            password=email_accounts[email_account]["password"],
            use_tls=settings.EMAIL_USE_TLS,
        ) as connection:
            msg = EmailMultiAlternatives(
                subject,
                text_content,
                f'{email_accounts[email_account]["display_name"]} <{email_accounts[email_account]["from"]}>',
                [email],
                cc=[cc_email],
                connection=connection)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    return "Done"
 
 