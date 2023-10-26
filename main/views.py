from django.shortcuts import render
from main.models import *
import requests





# Create your views here.

def indexHandler(request):
    cases = Case.objects.all()
    feeds = Feedback.objects.all()
    blogs = Blog.objects.all()

    if request.method == 'POST':
        BOT_TOKEN = "6732637767: AAGX6rjU8U7q - x9xcB4qQqTaQAno8AgQ5kU"
        TELEGRAM_CHAT_ID = "604469732"
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        feedback = Feedback(name=name, phone=phone, comment=comment)
        feedback.save()
        if comment:
            message = f"Новый клиент\nИмя: {name}\nНомер: {phone}\nТовар: {comment}"
        else:
            message = f"Новый клиент\nИмя: {name}\nНомер: {phone}"
        response = requests.get(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
        from django.shortcuts import redirect
        return redirect('/')

    return render(request, 'index.html', {
        'cases': cases,
        'feeds': feeds,
        'blogs': blogs,
    })

