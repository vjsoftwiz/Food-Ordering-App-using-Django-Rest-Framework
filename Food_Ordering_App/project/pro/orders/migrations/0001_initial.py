# Generated by Django 3.1.7 on 2021-03-26 12:40

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0001_initial'),
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='cost')),
                ('order_date_time', models.DateTimeField(auto_now_add=True, verbose_name='order date time')),
                ('delivery_date_time', models.DateTimeField(default=None, null=True, verbose_name='order date time')),
                ('delivery_guy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employer')),
                ('food', models.ManyToManyField(to='hotels.Food')),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotels.hotel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_taken', models.BooleanField(default=False, verbose_name='on the way')),
                ('on_the_way', models.BooleanField(default=False, verbose_name='on the way')),
                ('delivered', models.BooleanField(default=False, verbose_name='food delivered')),
                ('rating', models.IntegerField(default=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='rating')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=None, verbose_name='user id')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('mobile_no', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Phone no must be enter in the format: +999999999. upto 15 digits', regex='^\\+?1?\\d{9,15}$')], verbose_name='mobile no')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='HotelOrdered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('latitude', models.DecimalField(decimal_places=16, max_digits=22, verbose_name='latitude')),
                ('longitude', models.DecimalField(decimal_places=16, max_digits=22, verbose_name='latitude')),
                ('street', models.CharField(default='', max_length=60, verbose_name='street name')),
                ('area', models.CharField(default='', max_length=60, verbose_name='area name')),
                ('city', models.CharField(default='', max_length=60, verbose_name='city name')),
                ('state', models.CharField(default='', max_length=60, verbose_name='state name')),
                ('country', models.CharField(default='', max_length=60, verbose_name='country name')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='FoodOrdered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.0'))], verbose_name='cost')),
                ('offer', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='offer')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='quantity')),
                ('total_cost', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='total cost')),
                ('major_category', models.CharField(max_length=60, verbose_name='major category')),
                ('minor_category', models.CharField(max_length=60, verbose_name='minor category')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_id', models.IntegerField(default=None, verbose_name='employer id')),
                ('name', models.CharField(max_length=60, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('mobile_no', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Phone no must be enter in the format: +999999999. upto 15 digits', regex='^\\+?1?\\d{9,15}$')], verbose_name='mobile no')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]