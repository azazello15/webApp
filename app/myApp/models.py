from django.db import models


class Channel(models.Model):
    channel_name = models.CharField(verbose_name='Название канала', max_length=200)
    channel_img = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name='Логотип')
    channel_description = models.TextField(blank=True, verbose_name='Описание')
    channel_url = models.URLField(max_length=200, null=True, verbose_name='Ссылка на канал')
    channel_stat = models.URLField(max_length=200, null=True, verbose_name='Ссылка на ТГстат')
    channel_err = models.IntegerField(verbose_name='ERR')
    channel_crm = models.IntegerField(verbose_name='CRM')
    channel_coverage = models.IntegerField(verbose_name='Охват')
    channel_category = models.CharField(verbose_name='Категория', null=True, max_length=200)

    def __str__(self):
        return self.channel_name



