from django import forms
from django.core.mail import send_mail
from haystack.forms import SearchForm


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        message = self.cleaned_data["message"]
        subject = "Contact Submission Form!"
        body = """
        Hey Guys! You got a new contact form submission:
        From: {}
        At: {}
        Message: {}
        """.format(name, email, message)
        recipient_list = ["tdhdesapp@gmail.com"]
        send_mail(subject, body, 'Do Not Reply <do_not_replay@domain.com>', recipient_list)


class BirthdateSearchForm(SearchForm):
    birthdate = forms.DateField(required=False)

    def search(self):
        sqs = super(BirthdateSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        if self.cleaned_data['birthdate']:
            sqs = sqs.filter(birthdate=self.cleaned_data['birthdate'])

        return sqs
