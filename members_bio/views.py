from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Membersinfo
from django.urls import reverse
from datetime import date, datetime, timedelta


def home(request):
    return render(request, 'yoga_app/home.html')


def register(request):
    return render(request, 'yoga_app/register.html')


def search(request):
    return render(request, 'yoga_app/search_box.html')


def allrecords(request):
    members = Membersinfo.objects.all().values()
    return render(request, 'yoga_app/all_members.html', context={'members': members})


def display(request, id=None):
    # fetching the user id based on the way view is called
    if request.method == 'POST':
        user_id = request.POST['user_id']
    else:
        user_id = request.session.get('_id')
    # calling the update function if user id exists
    member = {}
    if Membersinfo.objects.filter(id=int(user_id)).exists():
        reload(user_id)
        member = Membersinfo.objects.values().get(id=int(user_id))
    return render(request, 'yoga_app/detail.html', context={'details': member})


def addrecord(request):
    # fetching all the details from form
    first = request.POST['first_name']
    last = request.POST['last_name']
    email = request.POST['your_email']
    age = request.POST['age']
    street = request.POST['street']
    state = request.POST['state']
    zip = request.POST['zip']
    country = request.POST['country']
    phone = request.POST['phone']
    fee_status = 'unpaid'
    batch_change = ''
    date_joined = (datetime.now().date()).isoformat()
    current_batch_slot = request.POST['slot']
    # setting starting date as sys date
    batch_start_date = (datetime.now().date()).isoformat()
    # calculating end date from 30 days from date of joining
    batch_end_date = (datetime.now().date() +
                      timedelta(days=30)).isoformat()
    member = Membersinfo(firstname=first, lastname=last, email=email, age=age, street=street, state=state, zip=zip, country=country, phone=phone, date_joined=date_joined, current_batch_slot=current_batch_slot,
                         batch_start_date=batch_start_date, batch_end_date=batch_end_date, fee_status=fee_status, batch_change=batch_change)
    member.save()
    request.session['_id'] = member.id
    return HttpResponseRedirect(reverse('display'))


def reload(user_id):
    member = Membersinfo.objects.get(id=int(user_id))
    # remove member if he/she has not paid the fees on or before the end date
    if member.fee_status == 'Unpaid' and (datetime.now().date()).isoformat() > member.batch_end_date:
        member.delete()
        return
    # update member batch date if current batch subscription has ended
    if (datetime.now().date()).isoformat() > (member.batch_end_date).isoformat():
        member.batch_end_date = (
            date.today()+timedelta(days=30)).isoformat()  # o/p: 2017-06-05
        if member.batch_change:
            member.current_batch_slot = member.batch_change
            member.batch_change = ''
        member.save()
    return


def payment(request, id):
    return render(request, 'yoga_app/payment.html', context=({'id': id}))


def update_payment(request, id):
    # fetching the member details and updating their fee status
    member = Membersinfo.objects.get(id=id)
    if member.current_batch_slot != 'paid':
        member.fee_status = 'paid'
        member.save()
    request.session['_id'] = id
    return HttpResponseRedirect(reverse('display'))


def slot(request, id):
    return render(request, 'yoga_app/slot_change.html',  context=({'id': id}))


def update_slot(request, id):
    # fetching the member details and adding their requested slot change time which will be updated for the next batch
    user_id = id
    slot = request.POST['slot']
    member = Membersinfo.objects.get(id=user_id)
    if member.current_batch_slot != slot:
        member.batch_change = slot
        member.save()
    request.session['_id'] = id
    return HttpResponseRedirect(reverse('display'))

# dummy view for testing purpose


def test(request):
    return render(request, 'yoga_app/test.html')
