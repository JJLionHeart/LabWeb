# Generated by Django 2.0.2 on 2018-02-26 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('PasswordHash', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('PasswordHash', models.CharField(max_length=40)),
                ('IDAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Administrators')),
            ],
        ),
        migrations.CreateModel(
            name='Products_Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TotalPayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('SaleDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='Description',
            field=models.CharField(default='none', max_length=40),
        ),
        migrations.AddField(
            model_name='products',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='products',
            name='Quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='sales_products',
            name='IDProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Products'),
        ),
        migrations.AddField(
            model_name='sales_products',
            name='IDSale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Sales'),
        ),
        migrations.AddField(
            model_name='products_categories',
            name='IDProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Products'),
        ),
        migrations.AlterUniqueTogether(
            name='sales_products',
            unique_together={('IDSale', 'IDProduct')},
        ),
        migrations.AlterUniqueTogether(
            name='products_categories',
            unique_together={('IDProduct', 'IDCategory')},
        ),
    ]
