# Generated by Django 5.0.4 on 2024-04-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_supplier_supplier_id_alter_supplier_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
