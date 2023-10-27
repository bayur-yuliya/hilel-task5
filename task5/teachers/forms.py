from django import forms
from django.forms import NumberInput

from students.models import Student
from teachers.models import Teacher, Group

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


class TeacherForm(forms.ModelForm):
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    subject = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=SUBJECTS_LICT
    )

    class Meta:
        model = Teacher
        fields = ["name", "middle_name", "surname", "birth_date", "email"]


class GroupForm(forms.Form):
    curator = forms.ModelChoiceField(queryset=Teacher.objects.all())
    group_name = forms.CharField(label="Group name", max_length=30)


class StudentGroupForm(forms.ModelForm):
    group = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Student
        fields = ["group"]
