# Generated by Django 4.0.3 on 2022-03-02 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chess', '0003_alter_board_columns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='columns',
            field=models.PositiveIntegerField(default=8),
        ),
    ]
