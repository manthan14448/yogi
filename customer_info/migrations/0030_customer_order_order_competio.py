# Generated by Django 2.2.5 on 2020-03-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0029_customer_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_order',
            name='order_competio',
            field=models.DateField(blank=True, null=True),
        ),
    ]
