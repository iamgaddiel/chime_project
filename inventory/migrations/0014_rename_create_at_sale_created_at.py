# Generated by Django 5.0.4 on 2024-04-30 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_remove_sale_ordered_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
