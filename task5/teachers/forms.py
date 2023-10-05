from django import forms
from django.forms import NumberInput

from teachers.models import Teacher


SUBJECTS_LICT = [
    ("math", "Math"),
    ("biology", "Biology"),
    ("drawing", "Drawing"),
    ("chemistry", "Chemistry"),
    ("geography", " Geography"),
    ("history", "History"),
    ("literature", "Literature"),
    ("technology", "Technology"),
    ("physics", "Physics"),
    ("music", "Music"),
]


class TeacherForm(forms.Form):
    name = forms.CharField(label="First name", max_length=20)
    middle_name = forms.CharField(label="Middle", max_length=20, required=False)
    surname = forms.CharField(label="Surname", max_length=20)
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    email = forms.EmailField(label="Email", max_length=30)
    subject = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=SUBJECTS_LICT
    )


class GroupForm(forms.Form):
    curator = forms.ModelChoiceField(queryset=Teacher.objects.all())
    group_name = forms.CharField(label="Group name", max_length=30)
