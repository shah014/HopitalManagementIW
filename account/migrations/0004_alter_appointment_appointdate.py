# Generated by Django 3.2.3 on 2021-05-23 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_appointment_appointdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
