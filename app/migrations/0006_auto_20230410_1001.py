# Generated by Django 2.2.14 on 2023-04-10 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20230410_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
    ]
