from django.db import models


class Membersinfo(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    age = models.IntegerField()
    date_joined = models.DateField()
    current_batch_slot = models.CharField(max_length=10)
    batch_start_date = models.DateField()
    batch_end_date = models.DateField()
    fee_status = models.CharField(max_length=10)
    batch_change = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.IntegerField(default=000000)
    phone = models.IntegerField(default=0000)
    # choices
    Country = (('India', 'India'), ('Malaysia', 'Malaysia'), ('USA', 'USA'))
    payment_status = (('Paid', 'Paid'), ('Unpaid', 'Unpaid'))
    Time_slots = (('6-7 AM', '6-7 AM'), ('7-8 AM', '7-8 AM'),
                  ('8-9 AM', '8-9 AM'), ('5-6 PM', '5-6 PM'))
