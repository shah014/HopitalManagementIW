# Generated by Django 3.2.3 on 2021-05-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_appointment_appointdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointDate',
            field=models.DateField(null=True),
        ),
    ]
