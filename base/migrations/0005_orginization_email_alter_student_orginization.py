# Generated by Django 4.0.3 on 2022-05-01 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_leavebalance_e_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orginization',
            name='email',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='orginization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.orginization'),
        ),
    ]