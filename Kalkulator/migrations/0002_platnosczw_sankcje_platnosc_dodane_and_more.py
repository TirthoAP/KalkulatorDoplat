# Generated by Django 4.2 on 2023-04-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kalkulator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatnoscZW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('pelnanazwa', models.TextField(blank=True)),
                ('stawka', models.TextField(blank=True)),
                ('dodanezw', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'PlatnoscZW',
                'verbose_name_plural': 'PlatnoscZW',
            },
        ),
        migrations.CreateModel(
            name='Sankcje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sankcjanazwa', models.CharField(max_length=50)),
                ('dodanesank', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Sankcje',
                'verbose_name_plural': 'Sankcje',
            },
        ),
        migrations.AddField(
            model_name='platnosc',
            name='dodane',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='platnosc',
            name='pelnanazwa',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='platnosc',
            name='stawka',
            field=models.TextField(blank=True),
        ),
    ]
