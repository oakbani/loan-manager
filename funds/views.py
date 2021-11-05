from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Transaction, Participant


def process_transactions(transactions):
    all_responses = []
    cumulative_sum = 0

    for t in transactions:
        amount = t.amount
        
        if t.type == Transaction.DONATION or t.type == Transaction.LOANRETURNED:
            cumulative_sum += amount
        elif t.type == Transaction.LOANTAKEN:
            cumulative_sum -= amount
        else:
            pass

        response = {
            "date": t.date,
            "type" : getattr(Transaction, t.type),
            "amount": t.amount,
            "balance": cumulative_sum
        }

        all_responses.append(response)

    return all_responses

def index(request):
    return HttpResponse("You are at funds app")

def participant(request, participant_id):

    context = {};

    # get transactions orded by date
    all_transactions = Transaction.objects.filter(participant=participant_id).order_by("date")

    if not all_transactions:
       return HttpResponse('No transactions found for given participant ID.')

    processed_transactions = process_transactions(all_transactions)

    context['transactions'] =  processed_transactions

    # get participant name
    name = Participant.objects.filter(id=participant_id)[0].fullname
    context['name'] = name

    return render(request, 'funds/participant.html', context)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request, 'polls/index.html', context)