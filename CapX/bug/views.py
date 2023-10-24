from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from .models import Bug
from .forms import BugForm

def view_bug(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug/view_bug.html', {'bug': bug})

def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bugs')
    else:
        form = BugForm()
    return render(request, 'bug/register_bug.html', {'form': form})

def list_bugs(request):
     bugs = Bug.objects.all()
     return render(request, 'bug/list_bugs.html', {'bugs': bugs})
