from django.db import models

# Create your models here.

class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    contact_num = models.CharField(max_length=200)

    def get_absolute_url(self):
        return "/people/%i/" % self.id

    def __str__(self):
        return f"{self.id}: '{self.fullname}'"


class Transaction(models.Model):

    DONATION = "DN"
    LOANTAKEN = "LT"
    LOANRETURNED = "LR"

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
