from django.db import models
from django.urls import reverse

# Create your models here.

class Participant(models.Model):
    DONOR = "DONOR"
    LOANER = "LOANER"

    P_TYPE_CHOICES =  [
        (DONOR, 'Donor'),
        (LOANER, 'Loaner')
    ]

    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    contact_num = models.CharField(max_length=200)
    p_type = models.CharField(
        "Participant Type",
        max_length = 6,
        choices = P_TYPE_CHOICES,
        default = DONOR 
    )

    def get_absolute_url(self):
        return reverse('funds:participant', kwargs={'participant_id' : self.id})
        # return "/people/%i/" % self.id

    def __str__(self):
        return f"{self.id}: '{self.fullname}'"


class Transaction(models.Model):

    DONATION = "DN"
    LOANTAKEN = "LT"
    LOANRETURNED = "LR"

    # Adding reverse as well for views todo: see this later
    DN = "Donation"
    LT = "Loan Taken"
    LR = "Loan Returned"

    TRANS_TYPE_CHOICES =  [
        (DONATION, 'Donation'),
        (LOANTAKEN, 'Loan Taken'),
        (LOANRETURNED, 'Loan Returned')
    ]

    type = models.CharField(
        max_length = 2,
        choices = TRANS_TYPE_CHOICES,
        default = DONATION
    )
    amount = models.IntegerField()
    date = models.DateField()
    participant = models.ForeignKey(
        'Participant',
        on_delete=models.PROTECT
    )
