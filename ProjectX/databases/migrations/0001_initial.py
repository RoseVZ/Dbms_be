# Generated by Django 4.1.3 on 2022-12-26 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=100)),
                ('Addr', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Cust_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('GST_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Addr', models.TextField(max_length=500)),
                ('Mgr_name', models.CharField(max_length=100)),
                ('Mgr_no', models.IntegerField()),
                ('Descr', models.TextField()),
                ('Role_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='databases.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Satus', models.IntegerField(choices=[(1, 'Paid'), (2, 'Not paid')], max_length=1)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('Cust_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.IntegerField(choices=[(1, 'Order Accepted'), (2, 'Out for Delivery'), (3, 'Delivered')], max_length=1)),
                ('Cust_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Tag', models.CharField(max_length=100)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Photo', models.ImageField(upload_to='')),
                ('GST_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryAgent',
            fields=[
                ('DL_no', models.IntegerField(max_length=100, primary_key=True, serialize=False)),
                ('Location', models.CharField(max_length=100)),
                ('License', models.ImageField(upload_to='')),
                ('Role_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='databases.user')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='Role_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='databases.user'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('Total_No_items', models.IntegerField()),
                ('Cust_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.customer')),
                ('Food_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='databases.menu')),
            ],
        ),
    ]
