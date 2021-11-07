from django.db import models
from django.urls import reverse

# Create your models here.

def getAccountNum(p_type):
    last_account = Participant.objects.filter(p_type=p_type).order_by('-id')
    prefix = Participant.PREFIX[p_type]

    # Account being created for the first time
    if not last_account:
            return f"{prefix}1"
    else:
        new_account_int = int(last_account[0].account_num[1:]) + 1
        new_account_str = str(new_account_int)
        return f"{prefix}{new_account_str}"



class Participant(models.Model):
    DONOR = "DONOR"
    LOANER = "LOANER"

    PREFIX = {
        "DONOR": "D",
        "LOANER": "L"
    }

    P_TYPE_CHOICES =  [
        (DONOR, 'Donor'),
        (LOANER, 'Loaner')
    ]

    fullname = models.CharField(max_length=200)
    contact_num = models.CharField(max_length=200)
    p_type = models.CharField(
        "Participant Type",
        max_length = 6,
        choices = P_TYPE_CHOICES,
        default = DONOR 
    )

    account_num = models.CharField(
        "Account Number",
        max_length = 20,
        null = True,
        default = None,
        editable = False,
        unique=True
    )

    def save(self, *args, **kwargs):
        # only get a new account number when the object is being saved
        # for the first time

        if self.account_num is None:
            self.account_num = getAccountNum(self.p_type)

        super().save(*args, **kwargs)  # Call the "real" save() method.

    def get_absolute_url(self):
        return reverse('funds:participant', kwargs={'participant_id' : self.id})
        # return "/people/%i/" % self.id

    def __str__(self):
        return f"{self.account_num}: '{self.fullname}'"


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
