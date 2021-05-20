# Generated by Django 3.2 on 2021-05-20 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('last_name', models.CharField(max_length=64, verbose_name='last_name')),
                ('nationality', models.CharField(blank=True, max_length=64, verbose_name='nationality')),
                ('position', models.CharField(blank=True, max_length=32, verbose_name='position')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team', verbose_name='team')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
    ]