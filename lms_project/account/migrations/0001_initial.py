# Generated by Django 5.0.7 on 2024-08-23 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAttendanceCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Attendance_cherry', models.IntegerField(default=0)),
                ('Attendance_date', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'account_attendance_check',
            },
        ),
        migrations.CreateModel(
            name='AccountCherry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cherry', models.IntegerField(default=99999)),
            ],
            options={
                'db_table': 'account_cherry',
            },
        ),
        migrations.CreateModel(
            name='AccountLoginType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loginType', models.CharField(choices=[('NORMAL', 'Normal'), ('GOOGLE', 'Google')], default='NORMAL', max_length=10)),
            ],
            options={
                'db_table': 'account_login_type',
            },
        ),
        migrations.CreateModel(
            name='AccountPaidMemberType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paidmemberType', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'account_paid_member_type',
            },
        ),
        migrations.CreateModel(
            name='AccountTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticket', models.IntegerField(default=99999)),
            ],
            options={
                'db_table': 'account_ticket',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('AttendanceCheck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountattendancecheck')),
                ('Cherry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountcherry')),
                ('loginType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountlogintype')),
                ('paidmemberType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountpaidmembertype')),
                ('Ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.accountticket')),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(default='n', max_length=64)),
                ('nickname', models.CharField(default='n', max_length=64)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
