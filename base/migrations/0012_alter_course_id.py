# Generated by Django 4.0.4 on 2022-05-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_lecturer_faculty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
