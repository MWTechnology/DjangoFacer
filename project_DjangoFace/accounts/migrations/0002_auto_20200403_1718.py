# Generated by Django 3.0.5 on 2020-04-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=100, verbose_name='Номер удостоверения'),
        ),
    ]