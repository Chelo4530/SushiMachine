# Generated by Django 2.2.7 on 2019-11-18 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('sushi', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.TextField()),
                ('hora', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
