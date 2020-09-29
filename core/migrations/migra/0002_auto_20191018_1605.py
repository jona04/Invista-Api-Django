# Generated by Django 2.2.3 on 2019-10-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapa',
            name='estoque',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade em Estoque'),
        ),
        migrations.AlterField(
            model_name='chapa',
            name='marca',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='chapa',
            name='obs',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Obs'),
        ),
    ]