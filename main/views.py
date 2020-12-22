from django.core.mail import BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Article
from .models import Category
from .models import Diplom
from main.forms import SearchForm
from main.forms import ContactForm
from django.db.models import Q
import smtplib



def articles(request):
    if request.GET:
        form = SearchForm(request.GET)
        context = {'form': form}
        if '_children' in request.GET:
            cat = Category.objects.get(id=3)
            context['article_list'] = Article.objects.filter(category=cat)
            return render(request, 'articles.html', context)
        if '_fears' in request.GET:
            cat = Category.objects.get(id=4)
            context['article_list'] = Article.objects.filter(category=cat)
            return render(request, 'articles.html', context)
        if '_complex' in request.GET:
            cat = Category.objects.get(id=5)
            context['article_list'] = Article.objects.filter(category=cat)
            return render(request, 'articles.html', context)
        if '_other' in request.GET:
            cat = Category.objects.get(id=6)
            context['article_list'] = Article.objects.filter(category=cat)
            return render(request, 'articles.html', context)
        if '_delete' in request.GET:
            context['article_list'] = []
            return render(request, 'articles.html', context)
        if form.is_valid():
            search = form.cleaned_data['search']
            print(search, Article.objects.filter(article_name__icontains=search))
            context['article_list'] = Article.objects.filter(article_name__icontains=search)
        else:
            context['error'] = form.errors
            context['article_list'] = None
        return render(request, 'articles.html', context)
    else:
        form = SearchForm(request.GET)
        context = {'form': form}
        context['article_list'] = []
        return render(request, 'articles.html', context)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def diploms(request):
    context = {}
    context['dips_list'] = Diplom.objects.all()
    return render(request, 'diploms.html', context)

def price(request):
    return render(request, 'price.html')

def services(request):
    return render(request, 'services.html')

def contact(reguest):
    #if reguest.is_ajax():
    if reguest.method == 'POST':
        form = ContactForm(reguest.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(sender, subject, message)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            #return render(reguest, 'ok.html')
            form.save()
            return HttpResponse({
                'message': 'success'
            })
    else:
        form = ContactForm()
    return render(reguest, 'contact.html', {'form': form})

def send_mail(cliaddr, subject, text, format='html'):
    fromaddr = "okorok5902@gmail.com"
    toaddr = "bifidok80@mail.ru"#"ekaterina2017-2018@mail.ru"
    mypass = "1q8j59h!"
    server = 'smtp.gmail.com'
    res_text = str(text) + u"; contact: " + str(cliaddr)
    server_port = 587
    body = "\r\n".join((
        "From: %s" % fromaddr,
        "To: %s" % toaddr,
        "Subject: %s" % subject,
        "",
        res_text
    ))
    s = smtplib.SMTP(server, server_port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(fromaddr, mypass)
    s.sendmail(fromaddr, toaddr.strip(), body)
    s.quit()

def ok(reguest):
    thanks = 'thanks'
    return render(reguest, 'ok.html', {'thanks': thanks})
