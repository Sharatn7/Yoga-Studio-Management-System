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


def display(request, id=''):
    if id:
        user_id = id
    else:
        user_id = request.POST['user_id']
    # member = Membersinfo.objects.raw(
    # 'SELECT * FROM Members_info where id = %s', [user_id])
    reload(user_id)
    member = Membersinfo.objects.values().get(id=int(user_id))
    return render(request, 'yoga_app/table.html', context={'details': member})


def addrecord(request):
    # if request.method == "POST":
    first = request.POST['first_name']
    last = request.POST['last_name']
    email = request.POST['your_email']
    age = request.POST['age']
    street = request.POST['street']
    state = request.POST['state']
    zip = request.POST['zip']
    country = request.POST['country']
    phone = request.POST['phone']
    fee_status = 'paid'
    batch_change = ''
    # date_joined = datetime.today().strftime('%Y-%m-%d')
    date_joined = (datetime.now().date()).isoformat()
    current_batch_slot = request.POST['slot']
    # batch_start_date = datetime.today().strftime('%Y-%m-%d')
    batch_start_date = (datetime.now().date()).isoformat()
    # batch_end_date = (date.today()+timedelta(days=30)).isoformat()
    batch_end_date = (datetime.now().date() +
                      timedelta(days=30)).isoformat()
    member = Membersinfo(firstname=first, lastname=last, email=email, age=age, street=street, state=state, zip=zip, country=country, phone=phone, date_joined=date_joined, current_batch_slot=current_batch_slot,
                         batch_start_date=batch_start_date, batch_end_date=batch_end_date, fee_status=fee_status, batch_change=batch_change)
    member.save()
    # member.id
    return HttpResponseRedirect(reverse('search'))


def reload(user_id):
    member = Membersinfo.objects.get(id=int(user_id))
    # if member.fee_status == 'Unpaid' and member.datetime.date.today() > member.batch_end_date:
    if member.fee_status == 'Unpaid' and (datetime.now().date()).isoformat() > member.batch_end_date:
        member.delete()
        return
    # if datetime.date() > member.batch_end_date and member.fees_status == 'Paid':
    if (datetime.now().date()).isoformat() > (member.batch_end_date).isoformat() and member.fees_status == 'Paid':
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
    # user_id = request.POST['user_id']
    member = Membersinfo.objects.get(id=id)
    if member.current_batch_slot != 'paid':
        member.fee_status = 'paid'
        member.save()
    return HttpResponseRedirect(reverse('search'))


def slot(request, id):
    return render(request, 'yoga_app/slot_change.html',  context=({'id': id}))


def update_slot(request, id):
    user_id = request.POST['user_id']
    slot = request.POST['slot']
    member = Membersinfo.objects.get(id=user_id)
    if member.current_batch_slot != slot:
        member.batch_change = slot
        member.save()
    return HttpResponseRedirect(reverse('home'))


def test(request):
    return render(request, 'yoga_app/test.html')
