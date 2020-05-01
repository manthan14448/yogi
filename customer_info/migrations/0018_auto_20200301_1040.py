# Generated by Django 2.2.5 on 2020-03-01 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_delete_gadge'),
        ('customer_info', '0017_auto_20200229_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquery_order',
            name='i_color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='inquery_order',
            name='i_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Product_Type'),
        ),
    ]
