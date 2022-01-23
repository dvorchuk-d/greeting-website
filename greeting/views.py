from django.shortcuts import render
from greeting.models import MyDb
from greeting.forms import MyDbForm


def index(request):
    """Render the main paige"""
    if request.method == 'POST':
        return greeting_save(request)
    cur_form = MyDbForm()
    context = {'form': cur_form}
    return render(request, 'greeting/index.html', context)


def greeting_save(request):
    """Save greeting to the database and render greeting page"""
    cur_form = MyDbForm(request.POST)
    if cur_form.is_valid():
        if MyDb.objects.filter(email=cur_form.cleaned_data['email']):
            context = {'email': cur_form.cleaned_data['email']}
            return render(request, 'greeting/already_greeted.html', context)
        context = {'email': cur_form.cleaned_data['email']}
        cur_form.save()
        return render(request, 'greeting/first_time.html', context)
    else:
        context = {'form': cur_form}
        return render(request, 'greeting/index.html', context)


def already_greeted(request):
    """Render page with a list of emails who has already greeted"""
    emails = MyDb.objects.all()
    context = {'emails': emails}
    return render(request, "greeting/emails.html", context)
