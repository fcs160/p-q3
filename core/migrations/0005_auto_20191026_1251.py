# Generated by Django 2.2.5 on 2019-10-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_aluguel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='hora_inicio',
            field=models.TimeField(verbose_name='Horário do ínicio'),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='hora_termino',
            field=models.TimeField(verbose_name='Horário do término'),
        ),
    ]