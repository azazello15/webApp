# Generated by Django 4.1.1 on 2022-09-22 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_name', models.CharField(max_length=200, verbose_name='Название канала')),
                ('channel_img', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Логотип')),
                ('channel_description', models.TextField(blank=True, verbose_name='Описание')),
                ('channel_url', models.URLField(null=True, verbose_name='Ссылка на канал')),
                ('channel_stat', models.URLField(null=True, verbose_name='Ссылка на ТГстат')),
                ('channel_err', models.IntegerField(verbose_name='ERR')),
                ('channel_crm', models.IntegerField(verbose_name='CRM')),
                ('channel_coverage', models.IntegerField(verbose_name='Охват')),
                ('channel_category', models.CharField(max_length=200, null=True, verbose_name='Категория')),
            ],
        ),
    ]
