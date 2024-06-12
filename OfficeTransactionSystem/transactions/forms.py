from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
         model=Transaction
         fields=['transaction_type','amount','description']
         widget={
             'transaction_type':forms.Select(choices=Transaction.TRANSACTION_TYPE_CHOICES),
             'amount':forms.NumberInput(attrs={'class':'form-control'}),
             'description':forms.TextInput(attrs={'class':'form-control'}),
         }