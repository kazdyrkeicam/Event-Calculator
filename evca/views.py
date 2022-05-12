from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse


from .models import Expenses, Member, Event
from .forms import MemberForm


# Create your views here.
def index(request):
    '''
        Display all stored members and events
    '''
    all_members_list = Member.objects.all()
    all_events_list = Event.objects.all()
    context = {
        'all_members_list': all_members_list,
        'all_events_list': all_events_list,
    }
    return render(request, 'evca_home.html', context)


def add_member_form(request):
    if request.method == 'POST':
        name = request.POST['member_name']
        surname = request.POST['member_surname']
        instance = Member(name=name, surname=surname)
        instance.save()
    
    return render(request, 'member/add.html')


def member_detail(request, member_id):
    member = get_object_or_404(Member, pk=member_id)

    if request.method == "POST":
        member.delete()
        # redirect

    context = {
        'member': member
    }
    return render(request, 'member/detail.html', context)


def event_detail(request, event_id):
    expenses_list = Expenses.objects.filter(event_id=event_id)
    event = Event.objects.get(pk=event_id)

    event_members = Member.objects.exclude(id__in=expenses_list.values('member_id'))

    if request.method == 'POST':
        if 'add_event_member' in request.POST:
            mem_id = request.POST['event_member_id']
            instance = Expenses(event_id=event_id, member_id=mem_id)

            instance.save()
        # print(request.POST)

        elif 'debt_value' in request.POST:
            debt = request.POST['debt_value']
            due = request.POST['due_value']
            expens_id = request.POST['expens_id']

            instance = Expenses.objects.get(pk=expens_id)
            if debt.isdigit():
                instance.debt += float(debt)
            if due.isdigit():
                instance.due += float(due)

            instance.save()
        
        elif 'remove_member' in request.POST:
            instance = expenses_list.get(pk=request.POST['remove_member'])
            instance.delete()
        
        elif 'all_debt' in request.POST:
            debt = request.POST['all_debt']
            num_mem = len(expenses_list)
            result = float(debt) / float(num_mem)

            for expens in expenses_list.iterator():
                if debt.isdigit():
                    expens.debt += round(result, 2)
                expens.save()
        
        else:
            expenses_list.all().delete()
            event.delete()

        
    # Create new expans if not already existed with choosed member_id and event_id

    context = {
        'expenses_list': expenses_list,
        'event': event,
        'event_members': event_members
    }
    return render(request, 'event/detail.html', context)


def add_event_form(request):
    if request.method == 'POST':
        name = request.POST['event_name']
        date = request.POST['event_date']
        # print(date)
        instance = Event(name=name, date=date)
        instance.save()
    
    return render(request, 'event/add.html')