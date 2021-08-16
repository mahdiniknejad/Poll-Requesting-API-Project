from django.contrib import auth
from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.


class Poll(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=120, null=False,
                             blank=False, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    create = models.DateTimeField(
        auto_now_add=True, verbose_name='زمان انتشار')
    update = models.DateTimeField(auto_now=True)
    deprecate = models.DateTimeField(null=True, blank=True)
    rand_title = models.CharField(
        max_length=8, unique=True, null=True, blank=True, verbose_name='دامنه')

    def __str__(self):
        return "{} - {}".format(self.user.get_full_name(), self.title)

    class Meta:
        verbose_name = 'نظر سنجی'
        verbose_name_plural = 'نظر سنجی ها'


def create_random_title_for_instances(**kwargs):
    poll = kwargs.get('instance')
    if not poll.rand_title:
        poll.rand_title = str(uuid.uuid4())[0:8]


pre_save.connect(create_random_title_for_instances, sender=Poll)


class Responde(models.Model):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, verbose_name='نظر')
    title = models.CharField(max_length=250, verbose_name='عنوان پاسخ')

    class Meta:
        verbose_name = 'پاسخ نظر سنجی'
        verbose_name_plural = 'پاسخ نظر سنجی ها'
