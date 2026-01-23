from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Autobus, Ruta, Conductor
from .forms import AutobusForm, RutaForm, ConductorForm

@login_required
def home(request):
    return render(request, 'core/home_modern.html')


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')


# CRUD Views for Autobus
@login_required
def autobus_list(request):
    autobuses = Autobus.objects.all().order_by('matricula')
    paginator = Paginator(autobuses, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'title': 'Gestión de Autobuses'
    }
    return render(request, 'core/autobus/autobus_list.html', context)


@login_required
def autobus_create(request):
    if request.method == 'POST':
        form = AutobusForm(request.POST)
        if form.is_valid():
            autobus = form.save()
            messages.success(request, f'Autobus {autobus.matricula} creado exitosamente.')
            return redirect('autobus_list')
    else:
        form = AutobusForm()
    
    context = {
        'form': form,
        'title': 'Crear Autobus',
        'action': 'Crear'
    }
    return render(request, 'core/autobus/autobus_form.html', context)


@login_required
def autobus_edit(request, pk):
    autobus = get_object_or_404(Autobus, pk=pk)
    
    if request.method == 'POST':
        form = AutobusForm(request.POST, instance=autobus)
        if form.is_valid():
            autobus = form.save()
            messages.success(request, f'Autobus {autobus.matricula} actualizado exitosamente.')
            return redirect('autobus_list')
    else:
        form = AutobusForm(instance=autobus)
    
    context = {
        'form': form,
        'autobus': autobus,
        'title': 'Editar Autobus',
        'action': 'Actualizar'
    }
    return render(request, 'core/autobus/autobus_form.html', context)


@login_required
def autobus_delete(request, pk):
    autobus = get_object_or_404(Autobus, pk=pk)
    
    if request.method == 'POST':
        matricula = autobus.matricula
        autobus.delete()
        messages.success(request, f'Autobus {matricula} eliminado exitosamente.')
        return redirect('autobus_list')
    
    context = {
        'autobus': autobus,
        'title': 'Eliminar Autobus'
    }
    return render(request, 'core/autobus/autobus_confirm_delete.html', context)


@login_required
def autobus_detail(request, pk):
    autobus = get_object_or_404(Autobus, pk=pk)
    rutas = autobus.rutas.all().order_by('-hora_salida')
    
    context = {
        'autobus': autobus,
        'rutas': rutas,
        'title': f'Detalles del Autobus {autobus.matricula}'
    }
    return render(request, 'core/autobus/autobus_detail.html', context)


# CRUD Views for Ruta
@login_required
def ruta_list(request):
    rutas = Ruta.objects.all().order_by('-hora_salida')
    paginator = Paginator(rutas, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'title': 'Gestión de Rutas'
    }
    return render(request, 'core/ruta/ruta_list.html', context)


@login_required
def ruta_create(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid():
            ruta = form.save()
            messages.success(request, f'Ruta {ruta.origen} → {ruta.destino} creada exitosamente.')
            return redirect('ruta_list')
    else:
        form = RutaForm()
    
    context = {
        'form': form,
        'title': 'Crear Ruta',
        'action': 'Crear'
    }
    return render(request, 'core/ruta/ruta_form.html', context)


@login_required
def ruta_edit(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    
    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid():
            ruta = form.save()
            messages.success(request, f'Ruta {ruta.origen} → {ruta.destino} actualizada exitosamente.')
            return redirect('ruta_list')
    else:
        form = RutaForm(instance=ruta)
    
    context = {
        'form': form,
        'ruta': ruta,
        'title': 'Editar Ruta',
        'action': 'Actualizar'
    }
    return render(request, 'core/ruta/ruta_form.html', context)


@login_required
def ruta_delete(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    
    if request.method == 'POST':
        ruta_info = f"{ruta.origen} → {ruta.destino}"
        ruta.delete()
        messages.success(request, f'Ruta {ruta_info} eliminada exitosamente.')
        return redirect('ruta_list')
    
    context = {
        'ruta': ruta,
        'title': 'Eliminar Ruta'
    }
    return render(request, 'core/ruta/ruta_confirm_delete.html', context)


@login_required
def ruta_detail(request, pk):
    ruta = get_object_or_404(Ruta, pk=pk)
    billetes = ruta.billetes.all().order_by('-fecha_compra')
    
    context = {
        'ruta': ruta,
        'billetes': billetes,
        'title': f'Detalles de la Ruta {ruta.origen} → {ruta.destino}'
    }
    return render(request, 'core/ruta/ruta_detail.html', context)


# CRUD Views for Conductor
@login_required
def conductor_list(request):
    conductores = Conductor.objects.all().order_by('nombre')
    paginator = Paginator(conductores, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'title': 'Gestión de Conductores'
    }
    return render(request, 'core/conductores/conductor_list.html', context)


@login_required
def conductor_create(request):
    if request.method == 'POST':
        form = ConductorForm(request.POST)
        if form.is_valid():
            conductor = form.save()
            messages.success(request, f'Conductor {conductor.nombre} creado exitosamente.')
            return redirect('conductor_list')
    else:
        form = ConductorForm()

    context = {
        'form': form,
        'title': 'Crear Conductor',
        'action': 'Crear'
    }
    return render(request, 'core/conductores/conductor_form.html', context)


@login_required
def conductor_edit(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)

    if request.method == 'POST':
        form = ConductorForm(request.POST, instance=conductor)
        if form.is_valid():
            conductor = form.save()
            messages.success(request, f'Conductor {conductor.nombre} actualizado exitosamente.')
            return redirect('conductor_list')
    else:
        form = ConductorForm(instance=conductor)

    context = {
        'form': form,
        'conductor': conductor,
        'title': 'Editar Conductor',
        'action': 'Actualizar'
    }
    return render(request, 'core/conductores/conductor_form.html', context)


@login_required
def conductor_delete(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)

    if request.method == 'POST':
        nombre = conductor.nombre
        conductor.delete()
        messages.success(request, f'Conductor {nombre} eliminado exitosamente.')
        return redirect('conductor_list')

    context = {
        'conductor': conductor,
        'title': 'Eliminar Conductor'
    }
    return render(request, 'core/conductores/conductor_confirm_delete.html', context)


@login_required
def conductor_detail(request, pk):
    conductor = get_object_or_404(Conductor, pk=pk)

    context = {
        'conductor': conductor,
        'title': f'Detalles del Conductor {conductor.nombre}'
    }
    return render(request, 'core/conductores/conductor_detail.html', context)
