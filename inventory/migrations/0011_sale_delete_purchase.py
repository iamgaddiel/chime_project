# Generated by Django 5.0.4 on 2024-04-29 21:38

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sale_id', models.CharField(max_length=20)),
                ('buyer_name', models.CharField(max_length=20)),
                ('ordered_by', models.CharField(help_text='Name of thebperson ordering', max_length=100)),
                ('sale_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'completed'), ('declined', 'declined')], max_length=14)),
                ('quantity', models.IntegerField()),
                ('paid', models.BigIntegerField()),
                ('create_at', models.DateField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.supplier')),
            ],
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
