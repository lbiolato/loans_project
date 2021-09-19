from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import LoanForm


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
