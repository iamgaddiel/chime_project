# Generated by Django 5.0.4 on 2024-04-29 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_sale_delete_purchase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='sale_status',
            new_name='transaction_status',
        ),
    ]
