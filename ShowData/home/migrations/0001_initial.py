# Generated by Django 4.1 on 2022-09-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biliniars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brank', models.CharField(max_length=10)),
                ('bname', models.CharField(max_length=100)),
                ('bnetworth', models.CharField(max_length=100)),
                ('bage', models.CharField(max_length=2)),
                ('bsource', models.CharField(max_length=200)),
                ('bcountry', models.CharField(max_length=50)),
            ],
        ),
    ]