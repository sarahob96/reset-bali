# Generated by Django 4.0.6 on 2022-07-26 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmes', '0006_rewind_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='rewind',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('booked-out', 'booked-out')], default='pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='rewind',
            name='date',
            field=models.CharField(choices=[('05/05/2023-08/05/2023', '05/05/2023-08/05/2023'), ('14/05/2023-17/05/2023', '14/05/2023-17/05/2023'), ('25/05/2023-28/06/2023', '25/05/2023-28/06/2023'), ('04/06/2023-07/06/2023', '04/06/2023-07/06/2023'), ('14/06/2023-17/06/2023', '14/06/2023-17/06/2023'), ('04/07/2023-07/07/2023', '04/07/2023-07/07/2023'), ('12/07/2023-15/07/2023', '12/07/2023-15/07/2023'), ('22/07/2023-25/07/2023', '22/07/2023-25/07/2023'), ('08/08/2023-11/07/2023', '08/08/2023-11/07/2023')], default='05/05/2023-08/05/2023', max_length=25),
        ),
        migrations.AlterField(
            model_name='rewind',
            name='programme',
            field=models.CharField(choices=[('Rewind', 'Rewind'), ('Renew', 'Renew'), ('Restart', 'Restart')], default='Rewind', max_length=10),
        ),
    ]
