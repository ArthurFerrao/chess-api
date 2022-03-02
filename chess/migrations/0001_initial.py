# Generated by Django 4.0.3 on 2022-03-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rolls', models.PositiveIntegerField(default=8)),
                ('columns', models.PositiveIntegerField(default=8)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('king', 'King'), ('queen', 'Queen'), ('bishop', 'Bishop'), ('rook', 'Rook'), ('knight', 'Knight'), ('pawn', 'Pawn')], max_length=50)),
                ('color', models.CharField(choices=[('black', 'Black'), ('white', 'White')], max_length=50)),
            ],
        ),
    ]
