# Generated by Django 2.2 on 2019-04-28 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=0, verbose_name='Situação'),
        ),
    ]