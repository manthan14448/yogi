# Generated by Django 2.2.5 on 2020-03-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0009_custom_product_p_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_product',
            name='p_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
