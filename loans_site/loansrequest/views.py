from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from requests.api import get
from .forms import LoanForm, LoanEditForm
from .models import Loan
from .services import moni_client

ROOT_ENDPOINT = f"https://api.moni.com.ar/api/v4/scoring/pre-score/"
HEADER = {"credential": ""}


def loan_application(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.approved = moni_client.validate_loan(loan.dni)
            if loan.approved:
                messages.success(request, 'Loan approved.')
            else:
                messages.error(request, 'Loan denied.')
            loan.save()
            return HttpResponseRedirect("/")
    else:
        form = LoanForm()
    return render(request, 'loansrequest/loan_application.html',{'form': form})

def loans_list(request):
    loans = Loan.objects.all().order_by('date')
    return render(request, 'loansadministration/loans_list.html',{'loans': loans})

def loans_edition(request, pk):
    loan = get_object_or_404(Loan, pk=pk)
    if request.method == "POST":
        form = LoanEditForm(request.POST, instance=loan)
        if form.is_valid():
            loan.save()
            return HttpResponseRedirect("/accounts/loans")
    else:
        form = LoanEditForm(instance=loan)
    return render(request, 'loansadministration/loans_edition.html',{'form': form, 'loandate': loan.date})

def delete_item(request, pk):
    item = Loan.objects.get(pk=pk)
    item.delete()
    return redirect("loans_list")