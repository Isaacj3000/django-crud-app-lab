from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Plant, WateringRecord, CareTask
from django.contrib.auth import login, authenticate, logout

def home(request):
    """Landing page view"""
    if request.user.is_authenticated:
        return redirect('my_app:plant_list')
    return render(request, 'my_app/home.html')

@login_required
def plant_list(request):
    """List all plants for the current user"""
    plants = Plant.objects.filter(user=request.user)
    return render(request, 'my_app/plant_list.html', {'plants': plants})

@login_required
def plant_detail(request, pk):
    """Show details of a single plant"""
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    watering_records = plant.watering_records.all()[:5]  # Get last 5 watering records
    return render(request, 'my_app/plant_detail.html', {
        'plant': plant,
        'watering_records': watering_records
    })

@login_required
def plant_create(request):
    """Create a new plant"""
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        watering_frequency = request.POST.get('watering_frequency')
        notes = request.POST.get('notes')
        
        plant = Plant.objects.create(
            user=request.user,
            name=name,
            species=species,
            watering_frequency=watering_frequency,
            notes=notes
        )
        return redirect('my_app:plant_detail', pk=plant.pk)
    
    return render(request, 'my_app/plant_form.html')

@login_required
def plant_edit(request, pk):
    """Update an existing plant"""
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    
    if request.method == 'POST':
        plant.name = request.POST.get('name')
        plant.species = request.POST.get('species')
        plant.watering_frequency = request.POST.get('watering_frequency')
        plant.notes = request.POST.get('notes')
        plant.save()
        return redirect('my_app:plant_detail', pk=plant.pk)
    
    return render(request, 'my_app/plant_form.html', {'plant': plant})

@login_required
def plant_delete(request, pk):
    """Delete a plant"""
    plant = get_object_or_404(Plant, pk=pk, user=request.user)
    
    if request.method == 'POST':
        plant.delete()
        return redirect('my_app:plant_list')
    
    return render(request, 'my_app/plant_confirm_delete.html', {'plant': plant})

# Watering Record Views
@login_required
def watering_record_create(request, plant_pk):
    """Create a new watering record"""
    plant = get_object_or_404(Plant, pk=plant_pk, user=request.user)
    
    if request.method == 'POST':
        notes = request.POST.get('notes', '')
        WateringRecord.objects.create(
            plant=plant,
            notes=notes
        )
        # Update plant's last_watered date
        plant.last_watered = timezone.now().date()
        plant.save()
        return redirect('my_app:plant_detail', pk=plant.pk)
    
    return render(request, 'my_app/watering_record_form.html', {'plant': plant})

@login_required
def watering_record_list(request, plant_pk):
    """List all watering records for a plant"""
    plant = get_object_or_404(Plant, pk=plant_pk, user=request.user)
    watering_records = plant.watering_records.all()
    return render(request, 'my_app/watering_record_list.html', {
        'plant': plant,
        'watering_records': watering_records
    })

@login_required
def watering_record_delete(request, plant_pk, record_pk):
    """Delete a watering record"""
    plant = get_object_or_404(Plant, pk=plant_pk, user=request.user)
    record = get_object_or_404(WateringRecord, pk=record_pk, plant=plant)
    
    if request.method == 'POST':
        record.delete()
        return redirect('my_app:watering_record_list', plant_pk=plant.pk)
    
    return render(request, 'my_app/watering_record_confirm_delete.html', {
        'plant': plant,
        'record': record
    })

# Care Task Views
@login_required
def care_task_list(request):
    """List all care tasks for the current user"""
    care_tasks = CareTask.objects.filter(user=request.user)
    return render(request, 'my_app/care_task_list.html', {'care_tasks': care_tasks})

@login_required
def care_task_detail(request, pk):
    """Show details of a single care task"""
    care_task = get_object_or_404(CareTask, pk=pk, user=request.user)
    return render(request, 'my_app/care_task_detail.html', {'care_task': care_task})

@login_required
def care_task_create(request):
    """Create a new care task"""
    if request.method == 'POST':
        name = request.POST.get('name')
        task_type = request.POST.get('task_type')
        frequency = request.POST.get('frequency')
        notes = request.POST.get('notes')
        
        care_task = CareTask.objects.create(
            user=request.user,
            name=name,
            task_type=task_type,
            frequency=frequency,
            notes=notes
        )
        return redirect('my_app:care_task_detail', pk=care_task.pk)
    
    return render(request, 'my_app/care_task_form.html', {'task_types': CareTask.TASK_TYPES})

@login_required
def care_task_edit(request, pk):
    """Update an existing care task"""
    care_task = get_object_or_404(CareTask, pk=pk, user=request.user)
    
    if request.method == 'POST':
        care_task.name = request.POST.get('name')
        care_task.task_type = request.POST.get('task_type')
        care_task.frequency = request.POST.get('frequency')
        care_task.notes = request.POST.get('notes')
        care_task.save()
        return redirect('my_app:care_task_detail', pk=care_task.pk)
    
    return render(request, 'my_app/care_task_form.html', {
        'care_task': care_task,
        'task_types': CareTask.TASK_TYPES
    })

@login_required
def care_task_delete(request, pk):
    """Delete a care task"""
    care_task = get_object_or_404(CareTask, pk=pk, user=request.user)
    
    if request.method == 'POST':
        care_task.delete()
        return redirect('my_app:care_task_list')
    
    return render(request, 'my_app/care_task_confirm_delete.html', {'care_task': care_task})

@login_required
def care_task_complete(request, pk):
    """Mark a care task as completed"""
    care_task = get_object_or_404(CareTask, pk=pk, user=request.user)
    care_task.last_completed = timezone.now().date()
    care_task.save()
    return redirect('my_app:care_task_detail', pk=care_task.pk)

@login_required
def plant_care_tasks(request, plant_pk):
    """Manage care tasks for a specific plant"""
    plant = get_object_or_404(Plant, pk=plant_pk, user=request.user)
    available_tasks = CareTask.objects.filter(user=request.user).exclude(plants=plant)
    
    if request.method == 'POST':
        task_pk = request.POST.get('task_pk')
        action = request.POST.get('action')
        
        if action == 'add':
            task = get_object_or_404(CareTask, pk=task_pk, user=request.user)
            plant.care_tasks.add(task)
        elif action == 'remove':
            task = get_object_or_404(CareTask, pk=task_pk, user=request.user)
            plant.care_tasks.remove(task)
            
        return redirect('my_app:plant_care_tasks', plant_pk=plant.pk)
    
    return render(request, 'my_app/plant_care_tasks.html', {
        'plant': plant,
        'available_tasks': available_tasks
    })

def register(request):
    """Handle user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Ensure new users don't have admin privileges
            user.is_staff = False
            user.is_superuser = False
            user.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('admin:login')
    else:
        form = UserCreationForm()
    return render(request, 'my_app/registration/register.html', {'form': form})

def user_login(request):
    """Handle user login"""
    if request.user.is_authenticated:
        return redirect('my_app:plant_list')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_staff:
                    messages.error(request, 'Please use the Admin Login for staff accounts.')
                else:
                    login(request, user)
                    messages.success(request, f'Welcome back, {username}!')
                    return redirect('my_app:plant_list')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'my_app/registration/login.html', {'form': form})

def user_logout(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('my_app:home')
