# Generated by Django 2.2.3 on 2019-11-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191114_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='numero',
            field=models.IntegerField(default=0, verbose_name='Numero Nota'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='desconto',
            field=models.FloatField(default=0, null=True, verbose_name='Desconto'),
        ),
    ]
