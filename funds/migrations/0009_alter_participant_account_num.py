# Generated by Django 3.2.8 on 2021-11-07 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0008_participant_account_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='account_num',
            field=models.IntegerField(default=0, editable=False, unique=True, verbose_name='Account Number'),
        ),
    ]