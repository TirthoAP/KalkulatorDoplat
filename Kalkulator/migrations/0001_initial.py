# Generated by Django 4.2 on 2023-04-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platnosc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('pelnanazwa', models.TextField()),
                ('stawka', models.TextField()),
            ],
            options={
                'verbose_name': 'Platnosc',
                'verbose_name_plural': 'Platnosc',
            },
        ),
    ]
