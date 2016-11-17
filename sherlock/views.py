from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, User
from django.urls import reverse_lazy, reverse
from rest_framework.response import Response
import requests
from rest_framework.views import APIView
from sherlock.models import Profile, About
from final_project.backends import Twentythreeandme


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class IndexView(TemplateView):
    template_name = "index.html"


class ProfileDetailView(DetailView):
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.filter(id=self.kwargs['pk'])
        return context


class ProfileUpdateView(UpdateView):
    model = Profile
    # success_url = reverse_lazy('profile_detail_view')
    fields = ('picture', 'first_name', 'middle_name', 'last_name', 'gender', )

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_success_url(self, **kwargs):
        return reverse_lazy('profile_detail_view', args=[int(self.kwargs['pk'])])


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
# class AncestryAPIView(APIView):

    # def get(self, access_token, *args, **kwargs):
    #
    #     r = requests.get('https://api.23andme.com/1/ancestry/',
    #                      headers={'Authorization': 'Bearer {}'.format(access_token)})
    #     print(r)
    #     return Response(r.json())
