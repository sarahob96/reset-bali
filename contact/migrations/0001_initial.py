# Generated by Django 4.0.6 on 2022-07-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('your_message', models.TextField(max_length=400)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
