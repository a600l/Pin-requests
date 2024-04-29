from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RequestForm, ActionTakenForm
from .models import RequestModel
from django.shortcuts import get_object_or_404

@login_required
def new_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            request_instance = form.save(commit=False)
            request_instance.created_by = request.user
            request_instance.save()
            return redirect('new-request')
    else:
        form = RequestForm()
    return render(request, 'new_request.html', {'form': form})


@login_required
def open_request_detail(request, request_id):
    request_instance = get_object_or_404(RequestModel, pk=request_id)
    if request.method == 'POST':
        form = ActionTakenForm(request.POST)
        if form.is_valid():
            request_instance.remarks = form.cleaned_data['remarks']  # Updated field name
            request_instance.save()
            return redirect('all-open-requests')
    else:
        form = ActionTakenForm()
    return render(request, 'open-request-detail.html', {'request_instance': request_instance, 'form': form})

@login_required
def all_open_requests(request):
    open_requests = RequestModel.objects.filter(remarks__isnull=True)
    return render(request, 'all-open-requests.html', {'open_requests': open_requests})

@login_required
def closed_requests(request):
    closed_requests = RequestModel.objects.filter(remarks__isnull=False)  # Updated field name
    return render(request, 'closed-requests.html', {'closed_requests': closed_requests})
