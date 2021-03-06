# Generated by Django 4.0.3 on 2022-04-30 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0004_remove_leavebalance_e_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonTeachingLeaveBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('Personal', 'Personal Leave'), ('Annual', 'Annual Leave'), ('Military', 'Military Leave'), ('PDL', 'Pregnancy Disability Leave')], max_length=10)),
                ('available_days', models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per employee')),
                ('allocated_days', models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per employee per year')),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.nonteaching')),
            ],
        ),
        migrations.CreateModel(
            name='NonTeachingLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('leave_type', models.CharField(choices=[('Personal', 'Personal Leave'), ('Annual', 'Annual Leave'), ('Military', 'Military Leave'), ('PDL', 'Pregnancy Disability Leave')], max_length=10)),
                ('start_date', models.DateField(help_text='Leave begin date')),
                ('end_date', models.DateField(help_text='Leave end date')),
                ('requested_days', models.PositiveIntegerField(default=0, help_text='Total no of leave days requested')),
                ('leave_Status', models.CharField(choices=[('Pending', 'Pending Status'), ('Approved', 'Approved Status'), ('Declined', 'Declined Status'), ('Cancelled', 'Cancelled Status')], default='Pending', max_length=10)),
                ('reason', models.CharField(max_length=500, null=True)),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.nonteaching')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(choices=[('Personal', 'Personal Leave'), ('Annual', 'Annual Leave'), ('Military', 'Military Leave'), ('PDL', 'Pregnancy Disability Leave')], max_length=10)),
                ('available_days', models.PositiveIntegerField(default=0, help_text='Remaining/available leave days per employee')),
                ('allocated_days', models.PositiveIntegerField(default=0, help_text='No of leave days allocated to a leave type per employee per year')),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('leave_type', models.CharField(choices=[('Personal', 'Personal Leave'), ('Annual', 'Annual Leave'), ('Military', 'Military Leave'), ('PDL', 'Pregnancy Disability Leave')], max_length=10)),
                ('start_date', models.DateField(help_text='Leave begin date')),
                ('end_date', models.DateField(help_text='Leave end date')),
                ('requested_days', models.PositiveIntegerField(default=0, help_text='Total no of leave days requested')),
                ('leave_Status', models.CharField(choices=[('Pending', 'Pending Status'), ('Approved', 'Approved Status'), ('Declined', 'Declined Status'), ('Cancelled', 'Cancelled Status')], default='Pending', max_length=10)),
                ('reason', models.CharField(max_length=500, null=True)),
                ('e_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.lecturer')),
            ],
        ),
    ]
