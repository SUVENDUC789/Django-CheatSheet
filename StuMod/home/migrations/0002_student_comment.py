# Generated by Django 4.1 on 2022-09-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comment',
            field=models.CharField(default='None', max_length=70),
        ),
    ]