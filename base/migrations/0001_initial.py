# Generated by Django 4.0.3 on 2022-04-30 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Orginization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orginization_name', models.CharField(max_length=200, unique=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('u_id', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('profile_pic', models.ImageField(blank=True, upload_to='base/templates/')),
                ('mobile', models.BigIntegerField()),
                ('blood', models.CharField(max_length=5)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mobile', models.BigIntegerField()),
                ('relation', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=20)),
                ('birth_place', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('nationality', models.CharField(max_length=40)),
                ('admission_date', models.DateField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.branch')),
                ('orginization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.orginization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NonTeaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('nt_e_id', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('profile_pic', models.ImageField(blank=True, upload_to='base/templates/')),
                ('mobile', models.BigIntegerField()),
                ('blood', models.CharField(max_length=5)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mobile', models.BigIntegerField()),
                ('relation', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=20)),
                ('birth_place', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('nationality', models.CharField(max_length=40)),
                ('admission_date', models.DateField()),
                ('orginization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.orginization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('e_id', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('profile_pic', models.ImageField(blank=True, upload_to='base/templates/')),
                ('mobile', models.BigIntegerField()),
                ('blood', models.CharField(max_length=5)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mobile', models.BigIntegerField()),
                ('relation', models.CharField(max_length=200)),
                ('cast', models.CharField(max_length=20)),
                ('birth_place', models.CharField(max_length=20)),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('nationality', models.CharField(max_length=40)),
                ('admission_date', models.DateField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.branch')),
                ('orginization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.orginization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Leave_Type', models.CharField(choices=[('Personal', 'Personal Leave'), ('Annual', 'Annual Leave'), ('Military', 'Military Leave'), ('PDL', 'Pregnancy Disability Leave')], max_length=10)),
                ('Available_Days', models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per employee')),
                ('Allocated_Days', models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per employee per year')),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('Leave_Type', models.CharField(choices=[('Personal', 'Personal Leave'), ('Annual', 'Annual Leave'), ('Military', 'Military Leave'), ('PDL', 'Pregnancy Disability Leave')], max_length=10)),
                ('start_date', models.DateField(help_text='Leave begin date')),
                ('end_date', models.DateField(help_text='Leave end date')),
                ('requested_days', models.PositiveIntegerField(default=0, help_text='Total no of leave days requested')),
                ('leave_Status', models.CharField(choices=[('Pending', 'Pending Status'), ('Approved', 'Approved Status'), ('Declined', 'Declined Status'), ('Cancelled', 'Cancelled Status')], max_length=10)),
                ('reason', models.CharField(max_length=500, null=True)),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('code', models.CharField(max_length=200)),
                ('semester', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.branch')),
                ('orginization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.orginization')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='orginization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.orginization'),
        ),
    ]
