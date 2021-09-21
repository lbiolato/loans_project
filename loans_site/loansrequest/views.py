from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import LoanForm, LoanEditForm
from .models import Loan


def loan_application(request):
    if request.method == "POST":
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.aprobado = True
            loan.save()
            messages.success(request, 'Su prestamo fue aprobado.')
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