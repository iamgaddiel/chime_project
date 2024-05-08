# Generated by Django 5.0.4 on 2024-04-30 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_alter_sale_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='transaction_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('declined', 'Declined')], max_length=14),
        ),
    ]
