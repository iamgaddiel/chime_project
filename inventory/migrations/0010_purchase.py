# Generated by Django 5.0.4 on 2024-04-27 17:52

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_rename_task_number_supplier_tax_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('purchase_id', models.CharField(max_length=20)),
                ('purchaser_name', models.CharField(max_length=20)),
                ('ordered_by', models.CharField(help_text='Name of thebperson ordering', max_length=100)),
                ('purchase_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'completed'), ('declined', 'declined')], max_length=14)),
                ('quantity', models.IntegerField()),
                ('paid', models.BigIntegerField()),
                ('create_at', models.DateField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
    ]
