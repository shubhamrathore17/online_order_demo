from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *

@receiver(post_save, sender=Order)
def create_order_number(sender, instance, created=False, **kwargs):
    if created:
        sequential_number = ''
        if len(str(instance.pk)) == 1:
            sequential_number =  '0000'+ str(instance.pk)
        elif len(str(instance.pk)) == 2:
            sequential_number =  '000'+ str(instance.pk)
        elif len(str(instance.pk)) == 3:
            sequential_number =  '00'+ str(instance.pk)
        elif len(str(instance.pk)) == 4:
            sequential_number =  '0'+ str(instance.pk)
        elif len(str(instance.pk)) == 5:
            sequential_number =  instance.pk

        instance.order_number = instance.order_date.date().strftime("%Y%m%d") + '-'+sequential_number
        instance.save()