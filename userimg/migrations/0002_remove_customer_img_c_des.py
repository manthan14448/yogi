# Generated by Django 2.2.5 on 2020-01-04 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userimg', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_img',
            name='c_des',
        ),
    ]
