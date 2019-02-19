
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

User=settings.AUTH_USER_MODEL

@receiver(post_save,sender=User)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        password=instance.passwprd
        instance.set_password(password)
        instance.save()
        Token.objects.create(user=instance)