from django.shortcuts import render, get_object_or_404, redirect
from .models import Mobil, Service
from .forms import MobilForm, ServiceForm
from django.db.models import Q

def list_mobil(request):
    query = request.GET.get('q')  # ambil nilai dari input "q"
    if query:
        mobil_list = Mobil.objects.filter(
            Q(merk__icontains=query) | Q(model__icontains=query)
        )
    else:
        mobil_list = Mobil.objects.all()
    return render(request, 'showroom/list_mobil.html', {'mobil_list': mobil_list, 'query': query})

def tambah_mobil(request):
    if request.method == 'POST':
        form = MobilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_mobil')
    else:
        form = MobilForm()
    return render(request, 'showroom/tambah_mobil.html', {'form': form})

def detail_mobil(request, pk):
    mobil = get_object_or_404(Mobil, pk=pk)
    services = Service.objects.filter(mobil=mobil)
    return render(request, 'showroom/detail_mobil.html', {
        'mobil': mobil,
        'services': services
    })

def tambah_service(request, mobil_id):
    mobil = get_object_or_404(Mobil, pk=mobil_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.mobil = mobil
            service.save()
            return redirect('detail_mobil', pk=mobil.id)
    else:
        form = ServiceForm(initial={'mobil': mobil})
    return render(request, 'showroom/tambah_service.html', {'form': form, 'mobil': mobil})

def hapus_mobil(request, pk):
    mobil = get_object_or_404(Mobil, pk=pk)
    mobil.delete()
    return redirect('list_mobil')
