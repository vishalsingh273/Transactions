from django.shortcuts import render, redirect
from .models import Transaction
from .forms import TransactionForm

def transaction_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    running_balance = 0
    for transaction in reversed(transactions):
        if transaction.transaction_type == 'CREDIT':
            running_balance += transaction.amount
        else:
            running_balance -= transaction.amount
        transaction.running_balance = running_balance
    transactions = reversed(transactions)
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/add_transaction.html', {'form': form})





