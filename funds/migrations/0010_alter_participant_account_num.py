# Generated by Django 3.2.8 on 2021-11-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0009_alter_participant_account_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='account_num',
            field=models.CharField(default=None, editable=False, max_length=20, null=True, unique=True, verbose_name='Account Number'),
        ),
    ]
