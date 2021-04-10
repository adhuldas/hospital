from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from hospitalapp.models import Deprt, Doctor



def allDoc(request, c_slug=None):
    c_page = None
    doctors_list = None
    if c_slug != None:
        c_page = get_object_or_404(Deprt, slug=c_slug)
        doctors_list = Doctor.objects.filter(deprt=c_page, available=True)
    else:
        doctors_list = Doctor.objects.all().filter(available=True)
        paginator = Paginator(doctors_list, 3)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            doctors_list=paginator.page(page)
        except (EmptyPage,InvalidPage):
            doctors_list=paginator.page(paginator.num_pages)
    return render(request, 'deptwise.html', {'Deprts': c_page, 'doctors': doctors_list})


def home(request):
    obj = Doctor.objects.all()
    obj1 =  Deprt.objects.all()
    return render(request, 'index.html', {'results': obj,'results1':obj1})


def News(request):
    i = Deprt.objects.all()
    return render(request,'news-detail.html',{'results1':i})


def doctor(request):
    doc = Doctor.objects.all()
    return render(request,'doctor.html',{'results':doc})

def dept(request):
    docdept = Deprt.objects.all()
    return render(request,'dept.html',{'results1':docdept})

def apmnt(request):
    return render(request,'appointment.html')