# Generated by Django 4.0.6 on 2022-07-26 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_review_title_alter_review_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='programme_attended',
            field=models.CharField(choices=[('Rewind', 'Rewind'), ('Renew', 'Renew'), ('Restart', 'Restart')], max_length=20),
        ),
    ]
