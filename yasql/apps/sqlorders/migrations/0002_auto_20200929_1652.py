# Generated by Django 2.2.16 on 2020-09-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlorders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releaseversions',
            name='expire_time',
            field=models.DateField(verbose_name='截止上线日期'),
        ),
    ]
