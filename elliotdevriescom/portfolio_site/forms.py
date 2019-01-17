from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    organization = forms.CharField(
        label='Organization', max_length=50, required=False)
    location = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    subject = forms.CharField(label='Subject', max_length=150)
    body = forms.CharField(label='Message', widget=forms.Textarea)
    urgency = forms.ChoiceField(choices=(
        ((1, '1 - not time dependent'), (2, '2'), (3, '3'), (4, '4'), (5, '5 - critically urgent'))))

    error_css_class = 'contact-form-error'
