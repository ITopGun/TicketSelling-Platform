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
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField()),
                ('tickets', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Ticket')),
            ],
        ),
    ]
