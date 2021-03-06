from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.contrib.auth.forms import UserCreationForm, User
from django.urls import reverse_lazy, reverse
from rest_framework.response import Response
from sherlock.forms import ContactForm, BirthdateSearchForm
from rest_framework.views import APIView
from sherlock.models import Profile, About, Relative, Image
from haystack.generic_views import FacetedSearchView
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter
from haystack.forms import SearchForm
from django.core.paginator import InvalidPage, Paginator
from django.conf import settings
from django.core.mail import send_mail


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class IndexView(TemplateView):
    template_name = "index.html"


class ProfileDetailView(DetailView):
    model = Profile


class MyProfileDetailView(ProfileDetailView):

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(UpdateView):
    model = Profile
    # success_url = reverse_lazy('profile_detail_view')
    fields = ('picture', 'first_name', 'middle_name', 'last_name', 'gender', )
    success_url = reverse_lazy('my_profile_detail_view')

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class AboutUpdateView(UpdateView):
    model = About
    success_url = reverse_lazy('profile_detail_view')
    fields = ('birthdate', 'city_of_birth', 'state_of_birth',
              'country_of_birth', 'sex_at_birth', 'eye_color', 'mother_first_name', 'mother_maiden_name',
              'mother_last_name', 'father_first_name', 'father_last_name', 'birth_hospital', 'searching_for',
              'biography',)

    def get_queryset(self):
        return About.objects.filter(user=self.request.user)

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])


class ContactUsView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["form"] = ContactForm()
        return context


class SendEmailView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class BirthdateSearchView(SearchForm):
    form_class = BirthdateSearchForm


class AboutUsView(TemplateView):
    template_name = "about.html"


class ImageAllView(TemplateView):
    template_name = "images.html"

    def get_context_data(self):
        context = super().get_context_data()
        context["image"] = Image.objects.all()
        return context


class ImageAddView(CreateView):
    model = Image
    fields = ('picture', 'description', )

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse('profile_detail_view', args=[self.request.user.profile.id])


class ImageUpdateView(UpdateView):
    model = Image
    fields = ('picture', 'description', )

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def get_success_url(self, *args, **kwargs):
        return reverse('profile_detail_view', args=[self.request.user.profile.id])


class ImageDeleteView(DeleteView):
    model = Image
    fields = ('picture', 'description', )

    def get_queryset(self):
        return Image.objects.filter(user=self.request.user)

    def get_success_url(self, *args, **kwargs):
        return reverse('profile_detail_view', args=[self.request.user.profile.id])
