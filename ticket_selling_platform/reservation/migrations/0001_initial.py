# Generated by Django 2.2.4 on 2019-08-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PAID', 'paid'), ('UNPAID', 'unpaid'), ('ONGOING', 'ongoing')], default='ONGOING', max_length=20)),
                ('tickets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Ticket')),
            ],
        ),
    ]
