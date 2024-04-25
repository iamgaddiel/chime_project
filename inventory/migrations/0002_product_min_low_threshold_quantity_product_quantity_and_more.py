# Generated by Django 5.0.4 on 2024-04-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='min_low_threshold_quantity',
            field=models.IntegerField(default=1, help_text='The minium quantity reached before product is considered low in inventory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(default=('available', 'available'), max_length=12),
        ),
    ]
