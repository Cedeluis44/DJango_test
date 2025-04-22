from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm

def client_list(request):
    clients = Client.objects.all()
    form = ClientForm()
    client = None  
    message = None  

    if request.method == 'POST' and 'add_client' in request.POST:
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')

    if request.method == 'GET' and 'email' in request.GET:
        email = request.GET.get('email')
        try:
            client = Client.objects.get(email=email)
        except Client.DoesNotExist:
            message = 'No client found with that email.'

    return render(request, 'client.html', {'clients': clients, 'form': form, 'client': client, 'message': message})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'client.html', {'clients': Client.objects.all(), 'form': form, 'editing': client})  

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('client_list')
