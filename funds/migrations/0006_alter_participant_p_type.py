# Generated by Django 3.2.8 on 2021-11-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0005_participant_p_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='p_type',
            field=models.CharField(choices=[('DONOR', 'Donor'), ('LOANER', 'Loaner')], default='DONOR', max_length=6, verbose_name='Participant Type'),
        ),
    ]
