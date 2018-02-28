# Generated by Django 2.0.2 on 2018-02-26 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180226_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('PasswordHash', models.CharField(max_length=40)),
                ('Admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Administrators')),
            ],
        ),
    ]