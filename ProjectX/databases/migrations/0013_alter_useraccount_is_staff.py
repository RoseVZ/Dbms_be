# Generated by Django 4.0.2 on 2023-01-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0012_remove_menu_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]