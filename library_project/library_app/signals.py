from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from .models import *


@receiver(pre_save, sender=Book)
def on_create_book(sender, instance, **kwargs):
    if instance.id is None:
        print('A new Book instance created: %s, %s\n' % (instance.title, instance.authors))


@receiver(pre_save, sender=Reader)
def on_change_reader_card_number(sender, instance, **kwargs):
    if instance.id is not None:
        previous = Reader.objects.get(id=instance.id)
        if previous.card_number != instance.card_number:
            instance.card_number_old = previous.card_number
            print('Reader card number updated: old = %s, new = %s\n' %
                  (instance.card_number_old, instance.card_number))


@receiver(pre_delete, sender=Book)
def on_delete_book(sender, instance, **kwargs):
    with open('delete_log.txt', 'a') as log_file:
        log_file.write('Deleted Book instance: %s, %s\n' % (instance.title, instance.authors))
