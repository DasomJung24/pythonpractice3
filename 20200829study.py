
from django.http imort HttpResponse
from django.views.generic import ListView
from books.models import Book


class BookListView(ListView):
    model = book

    def head(self, *args, **kwargs):
        last_book = self.get_quesryset().latest('publication_date')
        response = HttpResponse('')
        response['Last-modified'] = last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response


from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from .forms import MyForm

class MyFormView(View):
    form_class = MyForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form':form})

