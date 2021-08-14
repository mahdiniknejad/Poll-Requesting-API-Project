from django.contrib import auth
from django.db import models
from django.contrib.auth import get_user_model

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

    def __str__(self):
        return "{} - {}".format(self.user.get_full_name(), self.title)

    class Meta:
        verbose_name = 'نظر سنجی'
        verbose_name_plural = 'نظر سنجی ها'


class Responde(models.Model):
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, verbose_name='نظر')
    title = models.CharField(max_length=250, verbose_name='عنوان پاسخ')

    class Meta:
        verbose_name = 'پاسخ نظر سنجی'
        verbose_name_plural = 'پاسخ نظر سنجی ها'
