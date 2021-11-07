from django.contrib import admin

# Register your models here.

from .models import Participant, Transaction


class ParticipantAdmin(admin.ModelAdmin):
    view_on_site = True
    list_display = ['account_num', 'fullname', 'p_type','contact_num']
    list_display_links = ['fullname']
    search_fields = ['fullname', 'contact_num']

admin.site.register(Participant, ParticipantAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date', 'type', 'participant', 'amount']
    search_fields = ['participant__fullname']


admin.site.register(Transaction, TransactionAdmin)
