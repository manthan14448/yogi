# Generated by Django 2.2.5 on 2020-03-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0021_order_detail_p_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_detail',
            name='price',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
