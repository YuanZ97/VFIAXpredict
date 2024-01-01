# Generated by Django 4.2.5 on 2024-01-01 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='StockEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('date', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stocks', to='backend.dateentry')),
            ],
        ),
        migrations.CreateModel(
            name='PriceEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('close', models.FloatField()),
                ('adj_close', models.FloatField()),
                ('stock', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='price', to='backend.stockentry')),
            ],
        ),
    ]
