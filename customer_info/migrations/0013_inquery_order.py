# Generated by Django 2.2.5 on 2020-02-29 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_info', '0012_auto_20200214_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquery_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_img', models.ImageField(null=True, upload_to='inq_pic')),
                ('c_Description', models.TextField(max_length=100, null=True)),
                ('a_Description', models.TextField(max_length=100, null=True)),
                ('qty', models.IntegerField(null=True)),
                ('a_status', models.TextField(max_length=100, null=True)),
                ('price', models.TextField(max_length=10)),
                ('c_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer_info.customer_detail')),
            ],
        ),
    ]
