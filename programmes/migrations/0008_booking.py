# Generated by Django 4.0.6 on 2022-07-26 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0007_rewind_status_alter_rewind_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_spaces', models.IntegerField()),
            ],
        ),
    ]