# Generated by Django 2.1.1 on 2018-09-14 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesTaches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='scheduled_date',
            field=models.DateField(null=True),
        ),
    ]
