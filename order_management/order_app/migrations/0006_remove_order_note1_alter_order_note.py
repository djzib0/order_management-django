# Generated by Django 4.0.6 on 2022-07-14 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0005_alter_orderproduct_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='note1',
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]