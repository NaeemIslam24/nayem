# Generated by Django 3.2.5 on 2021-08-01 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_remove_portfolio_hi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='category',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='tech',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='Technology',
        ),
    ]
