# Generated by Django 3.2 on 2024-02-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0029_auto_20230829_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]