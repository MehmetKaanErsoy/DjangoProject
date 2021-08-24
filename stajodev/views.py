from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from stajodev.models import fakulteeekle, bolumekle, sorumlu_ekle, ünvan_model
from stajodev.forms import FakulteEklee, BolumEkle, SorumluEkle, UserLoginForm
from django.contrib import messages
from django.core.mail import send_mail
from stajodev.filters import Fakulte,Bolum,Sorumlu


@login_required()
def home(request):
    data = fakulteeekle.objects.all()
    data2 = bolumekle.objects.all()
    data3 = sorumlu_ekle.objects.all()
    data4 = User.objects.all()

    return render(request, 'dashboard.html', {'data': data, 'data2': data2, 'data3': data3, 'data4': data4})


@login_required()
def fakultee_ekle(request):
    form = FakulteEklee()
    if request.method == 'POST':
        form = FakulteEklee(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, messages.SUCCESS, "asdkfmasdf")
            return redirect('fakultekle')
        else:
            form = FakulteEklee()
    else:
        form = FakulteEklee()
    return render(request, 'fakulteekle.html', {'form': form})


@login_required()
def fakulte_listele(request):
    data = fakulteeekle.objects.all()
    fakulte_listelee = Fakulte(request.GET, queryset=data)
    data = fakulte_listelee.qs
    return render(request, 'fakultelistele.html', {'data': data,'fakulte_listelee':fakulte_listelee})


@login_required()
def bolum_ekle(request):
    data = fakulteeekle.objects.all()
    form = BolumEkle()
    if request.method == 'POST':
        form = BolumEkle(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, messages.SUCCESS, "asdkfmasdf")
            return redirect('bolumekle')
    else:
        form = BolumEkle()
    return render(request, 'bolumekle.html', {'form': form, 'data': data})


@login_required()
def bolum_listele(request):
    data2 = bolumekle.objects.all()
    bolum_listelee = Bolum(request.GET, queryset=data2)
    data2 = bolum_listelee.qs
    return render(request, "bolumlistele.html", {'data2': data2,'bolum_listele':bolum_listelee})


@login_required()
def sorumlu_eklee(request):
    data = fakulteeekle.objects.all()
    data2 = bolumekle.objects.all()
    data3 = ünvan_model.objects.all()
    form = SorumluEkle()
    if request.method == 'POST':
        form = SorumluEkle(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, messages.SUCCESS, "afsadf")
            return redirect('sorumluekle')
    else:
        form = SorumluEkle()
    return render(request, "Sorumluekle.html", {'form': form, 'data': data, 'data2': data2, 'data3': data3})


@login_required()
def sorumlu_listele(request):
    data = sorumlu_ekle.objects.all()
    sorumlu_listelee = Sorumlu(request.GET, queryset=data)
    data = sorumlu_listelee.qs
    return render(request, "sorumlulistele.html", {'data': data,'sorumlu_listelee':sorumlu_listelee})


@login_required()
def güncelle_sorumlu(request, pk):
    data = ünvan_model.objects.all()
    data2 = fakulteeekle.objects.all()
    data3 = bolumekle.objects.all()
    getir = sorumlu_ekle.objects.get(id=pk)
    form = SorumluEkle(instance=getir)
    if request.method == 'POST':
        form = SorumluEkle(request.POST, instance=getir)
        if form.is_valid():
            recipient = form.cleaned_data.get('email')

            send_mail(
                'Subject here',
                'Here is the message.',
                'hesapacmakicin23@gmail.com',
                [recipient],
                fail_silently=False,
            )
            form.save()
            return redirect('sorumlulistele')

    return render(request, 'güncellesorumlu.html', {'form': form, 'data': data, 'data2': data2, 'data3': data3})


@login_required()
def admin_liste(request):
    data = User.objects.all()
    return render(request, 'admin_liste.html', {'data': data})


@login_required()
def cikisyap(request):
    logout(request)
    messages.success(request, messages.SUCCESS, "ksadf")
    return redirect('login')
