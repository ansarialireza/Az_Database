from django.shortcuts import render
from django.conf.urls import handler404
from django.views import View
from django.views.generic import ListView
from .models import Contact,HomePage ,AboutUs
from django.views.generic.edit import FormView
from .forms import ContactUsForm,NewsletterForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from itertools import chain
from blog.models import Post
from services.models import Services
from .query_manager import SearchQueryManager

class HomeView(View):
    template_name = 'website/index.html'

    def get(self, request):
        home_page = HomePage.objects.first()
        return render(request, self.template_name, {'home': home_page})

class AboutView(View):
    template_name = 'website/about.html'

    def get(self, request):
        about_us_data = AboutUs.objects.all()
        context = {'about': about_us_data}
        return render(request, self.template_name, context)
    
class ContactView(View):
    template_name = 'website/contact.html'

    def get(self, request):
        return render(request, self.template_name)

class ContactUsView(FormView):
    template_name = 'website/contact.html'
    form_class = ContactUsForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'پیام شما به موفقیت ارسال شد')
        return self.render_to_response(self.get_context_data(form=form, success=True))

    def form_invalid(self, form):
        messages.error(self.request, 'در پردازش درخواست شما خطایی رخ داده است. لطفاً دوباره امتحان کنید')
        return self.render_to_response(self.get_context_data(form=form, success=False))

class BaseView(ListView):
    model = Contact
    template_name = 'base.html'
    context_object_name = 'contacts'

class NewsletterView(FormView):
    template_name = 'website/index.html'
    form_class = NewsletterForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'ایمیل شما با موفقیت ثبت شد')
        return self.render_to_response(self.get_context_data(form=form, success=True))

    def form_invalid(self, form):
        messages.warning(self.request, 'لطفا ایمیل خود را به درستی وارد نمایید')
        return self.render_to_response(self.get_context_data(form=form, success=False))

class IndexSearchView(ListView):
    template_name = 'website/search-home.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('s')
        if query:
            posts = SearchQueryManager.search_posts(query)
            services = SearchQueryManager.search_services(query)
        else:
            posts, services = SearchQueryManager.get_all_posts_and_services()

        return posts, services

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('s', '')
        posts, services = self.get_queryset()
        context['post_list'] = posts
        context['service_list'] = services
        return context
