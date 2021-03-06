# Generated by Django 3.1.7 on 2021-03-26 12:40

import account.managers
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('mobile_no', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Phone no must be enter in the format: +999999999. upto 15 digits', regex='^\\+?1?\\d{9,15}$')], verbose_name='mobile no')),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('user_type', models.CharField(max_length=10, verbose_name='user type')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', account.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PasswordUpdation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reset_counter', models.IntegerField(default=0, verbose_name='reset counter')),
                ('secret_key', models.BinaryField(null=True, verbose_name='secret key')),
                ('otp_sent', models.BooleanField(default=False, verbose_name='otp sent')),
                ('otp_accepted', models.BooleanField(default=False, verbose_name='otp accepted')),
                ('last_otp_datetime', models.DateTimeField(null=True, verbose_name='last otp grnerated')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22, verbose_name='latitude')),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22, verbose_name='longitude')),
                ('area', models.CharField(default='', max_length=60, verbose_name='area name')),
                ('city', models.CharField(default='', max_length=60, verbose_name='city name')),
                ('state', models.CharField(default='', max_length=60, verbose_name='state name')),
                ('country', models.CharField(default='', max_length=60, verbose_name='country name')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
