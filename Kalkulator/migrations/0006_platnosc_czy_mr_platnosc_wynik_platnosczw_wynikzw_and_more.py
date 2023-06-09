# Generated by Django 4.2 on 2023-05-01 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kalkulator', '0005_delete_sankcje'),
    ]

    operations = [
        migrations.AddField(
            model_name='platnosc',
            name='czy_mr',
            field=models.CharField(choices=[(1, 'tak'), (0, 'nie')], default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='platnosc',
            name='wynik',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='platnosczw',
            name='wynikzw',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='platnosczw',
            name='zmnzw',
            field=models.FloatField(default=0),
        ),
    ]
