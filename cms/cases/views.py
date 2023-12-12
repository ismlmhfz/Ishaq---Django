from django.shortcuts import render, redirect
from .models import Case
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def case_list(request):
    search_term = request.GET.get('search_term', '')
    cases = Case.objects.filter(Name__icontains=search_term)

    return render(request, 'index.html', {'cases': cases, 'search_term': search_term})


def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    return render(request, 'case_detail.html', {'case': case})

def search_cases(request):
    search_term = request.GET.get('search_term', '')
    cases = Case.objects.all()

    if search_term:
        cases = cases.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term))

    return render(request, 'search_results.html', {'cases': cases, 'search_term': search_term})

@login_required
def add_case(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        case_type = request.POST.get('type')
        title = request.POST.get('title')
        finished_date = request.POST.get('finished_date')
        keyword = request.POST.get('keyword')

        # Validate and create a new Case instance
        if name and case_type and title and finished_date and keyword:
            new_case = Case(
                Name=name,
                Type=case_type,
                title=title,
                Finished_Date=finished_date,
                Keyword=keyword
            )
            new_case.save()

            # Redirect after successful form submission
            return redirect('case_list')
        else:
            # Handle form validation errors, if any
            # You can add error messages or other logic here
            pass

    type_choices = Case.typeChoice
    return render(request, 'add_case.html', {'type_choices': type_choices})
#def add_case(request):
#    type_choices = Case.typeChoice
#   return render(request, 'add_case.html', {'type_choices': type_choices})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('case_list')
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')