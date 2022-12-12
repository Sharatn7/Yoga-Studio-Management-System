# Generated by Django 4.1.4 on 2022-12-11 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membersinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('age', models.IntegerField()),
                ('date_joined', models.DateField()),
                ('current_batch_slot', models.CharField(choices=[('6-7 AM', '6-7 AM'), ('7-8 AM', '7-8 AM'), ('8-9 AM', '8-9 AM'), ('5-6 PM', '5-6 PM')], max_length=10)),
                ('batch_start_date', models.DateField()),
                ('batch_end_date', models.DateField()),
                ('fee_status', models.CharField(choices=[('paid', 'paid'), ('unpaid', 'unpaid')], max_length=10)),
                ('batch_change', models.CharField(choices=[('6-7 AM', '6-7 AM'), ('7-8 AM', '7-8 AM'), ('8-9 AM', '8-9 AM'), ('5-6 PM', '5-6 PM')], max_length=10)),
            ],
        ),
    ]
