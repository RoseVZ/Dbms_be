# Generated by Django 4.0.2 on 2023-01-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0003_useraccount_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='role',
            field=models.CharField(default=False, max_length=1),
        ),
    ]
