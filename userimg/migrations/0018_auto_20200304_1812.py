# Generated by Django 2.2.5 on 2020-03-04 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userimg', '0017_auto_20200304_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_img',
            name='img_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer_info.customer_detail'),
        ),
    ]
