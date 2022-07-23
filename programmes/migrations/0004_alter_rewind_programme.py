# Generated by Django 4.0.6 on 2022-07-23 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0003_alter_rewind_programme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewind',
            name='programme',
            field=models.CharField(choices=[('Rewind', 'Rewind'), ('Renew', 'Renew'), ('Restart', 'Restart')], default='Rewind', max_length=20),
        ),
    ]
