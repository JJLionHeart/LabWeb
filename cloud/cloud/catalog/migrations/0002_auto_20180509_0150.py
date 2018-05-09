# Generated by Django 2.0.2 on 2018-05-09 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
            ],
            options={
                'ordering': ('Nombre',),
            },
        ),
        migrations.CreateModel(
            name='Folio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateTimeField()),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Descripcion', models.CharField(default='none', max_length=40)),
                ('Precio', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('En_Existencia', models.IntegerField(default=0)),
                ('Codigo', models.CharField(max_length=128)),
                ('Categorias', models.ManyToManyField(to='catalog.Categoria')),
            ],
            options={
                'ordering': ('Nombre',),
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cantidad', models.IntegerField()),
                ('folio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Folio')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Producto')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.DeleteModel(
            name='wea',
        ),
        migrations.AddField(
            model_name='folio',
            name='Productos',
            field=models.ManyToManyField(through='catalog.Venta', to='catalog.Producto'),
        ),
    ]
