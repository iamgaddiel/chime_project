# Generated by Django 5.0.6 on 2024-05-09 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_alter_product_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
