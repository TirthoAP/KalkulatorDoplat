# Generated by Django 4.2.1 on 2023-05-25 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kalkulator', '0021_alter_platnosctyton_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platnoscvirginia',
            name='uzytkownik',
        ),
        migrations.RemoveField(
            model_name='sankcjaefa',
            name='uzytkownik',
        ),
        migrations.RemoveField(
            model_name='sankcjaniezadekl',
            name='uzytkownik',
        ),
        migrations.DeleteModel(
            name='PlatnoscTyton',
        ),
        migrations.DeleteModel(
            name='PlatnoscVirginia',
        ),
        migrations.DeleteModel(
            name='SankcjaEFA',
        ),
        migrations.DeleteModel(
            name='SankcjaNiezadekl',
        ),
    ]