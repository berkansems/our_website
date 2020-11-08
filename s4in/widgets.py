from django.contrib import messages
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings

def mailSubmit(request):

    if request.method == "POST":
        name= request.POST.get('name')
        companyName= request.POST.get('companyName')
        telephone= request.POST.get('telephone')
        email= request.POST.get('email')
        message= request.POST.get('message')
        text=f"Yeni başvuru bilgileri adı: {name} şirket ismi: {companyName} telefon numarası: {telephone} eposta adresi: {email} messagı: {message}"
        title='Yeni Başvuru Var!'
        hostEmail = settings.EMAIL_HOST_USER
        sendTo='shamsadinlo@gmail.com'

        try:
            send_mail(title, text, hostEmail ,[sendTo],fail_silently=False)
            messages.info(request, 'Mesajiniz başarılı bir şekilde gönderildi!')
        except:
            message.error(request,'Bir hata uluştu lütfen tekrar deneyiniz!')
