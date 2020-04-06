from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import CreatePoll
from .models import Poll
def home(request):
    polls = Poll.objects.all()
    return render(request,"home.html",{'polls':polls})

def create(request):
    if request.method=="POST":
        form=CreatePoll(request.POST)
        if form.is_valid():
            print(form.cleaned_data['question'])
            form.save()
            
            return redirect('/')

    else:
        form=CreatePoll()
    
    return render(request,"create.html",{'form':form})

def vote(request,poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.count_op1 += 1
        elif selected_option == 'option2':
            poll.count_op2 += 1
        elif selected_option == 'option3':
            poll.count_op3 += 1
        else:
            return HttpResponse(400, 'Invalid form option')

        poll.save()
        return redirect(f"/results/{poll.id}/")
    return render(request,"vote.html",{'poll':poll})

def results(request,poll_id):
    polls = Poll.objects.get(pk=poll_id)
    return render(request,"results.html",{'polls':polls})

