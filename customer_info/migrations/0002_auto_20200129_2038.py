# Generated by Django 2.2.5 on 2020-01-29 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_order',
            name='amt_status',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='d_a_status',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='pay_status',
        ),
    ]
