from django.shortcuts import render
from greeting.models import MyDb
from greeting.forms import MyDbForm


def index_and_save(request):
    if request.method == 'POST':
        cur_form = MyDbForm(request.POST)
        if cur_form.is_valid():
            if MyDb.objects.filter(email=cur_form.cleaned_data['email']):
                context = {'email': cur_form.cleaned_data['email']}
                return render(request, 'greeting/already_greeted.html', context)
            else:
                context = {'email': cur_form.cleaned_data['email']}
                cur_form.save()
                return render(request, 'greeting/first_time.html', context)
        else:
            context = {'form': cur_form}
            return render(request, 'greeting/index.html', context)
    else:
        cur_form = MyDbForm()
        context = {'form': cur_form}
        return render(request, 'greeting/index.html', context)


def already_greeted(request):
    emails = MyDb.objects.all()
    context = {'emails': emails}
    return render(request, "greeting/emails.html", context)
