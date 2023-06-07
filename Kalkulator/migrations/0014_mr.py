# Generated by Django 4.2 on 2023-05-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kalkulator', '0013_delete_mr'),
    ]

    operations = [
        migrations.CreateModel(
            name='MR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
                ('czy_mlody', models.CharField(choices=[('tak', 'tak'), ('nie', 'nie')], default='nie', max_length=3)),
            ],
            options={
                'verbose_name': 'MR',
                'verbose_name_plural': 'MR',
            },
        ),
    ]