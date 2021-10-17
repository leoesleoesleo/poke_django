# Generated by Django 3.0.8 on 2021-10-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id_table', models.AutoField(primary_key=True, serialize=False)),
                ('id_pokemon', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('height', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('evolutions', models.CharField(blank=True, max_length=150, null=True)),
                ('stat', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]