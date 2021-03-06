# Generated by Django 4.0.4 on 2022-05-16 22:20

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_action_contract_alter_contract_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='contract',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='contract',
            name='shares',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='contract',
            name='type',
            field=models.CharField(default='BUY', max_length=5),
        ),
        migrations.AlterField(
            model_name='contract',
            name='symbol',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.DeleteModel(
            name='Action',
        ),
    ]
