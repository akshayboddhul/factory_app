from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.db.models import Sum
from .models import *
from .forms import AddNewForm

# Create your views here.


def index(request):
    looms = powerloom.objects.all()

    # for i in range(1, 13):
    #     a = production.objects.get(plno=i)
    #     wgt = (a.pcs * a.weight) / 1000
    #     a.total_prod = wgt
    #     a.save()

    # actual_prod = production.objects.all().aggregate(Sum("total_prod"))
    # total_pcs = production.objects.all().aggregate(Sum('pcs'))['pcs__sum']
    # formatted_prod = actual_prod['total_prod__sum']
    # formatted_prod = '{:0.2f}'.format(formatted_prod)

    context = {
        'looms': looms,
        # 'formatted_prod': formatted_prod,
        # 'total_pcs': total_pcs
    }
    return render(request, 'dashboard/dashboard.html', context)


def addNew(request):
    form = AddNewForm()

    if request.method == "POST":
        form = AddNewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'dashboard/add_form.html', context)


def detailView(request):
    context = {

    }
    return render(request, 'dashboard/detail.html', context)


def error_404(request, exception):
    return render(request, 'dashboard/404.html',)
