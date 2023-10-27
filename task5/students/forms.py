from django import forms
from django.forms import NumberInput
import phonenumbers

from students.models import Student


class StudentForm(forms.ModelForm):
    birth_date = forms.DateField(widget=NumberInput(attrs={"type": "date"}))
    year_of_admission = forms.IntegerField(max_value=2023, min_value=1999)

    class Meta:
        model = Student
        fields = ["first_name", "last_name", "birth_date", "year_of_admission", "phone"]

    def clean(self):
        birth_date = self.cleaned_data["birth_date"]
        year_of_admission = self.cleaned_data["year_of_admission"]
        phone = self.cleaned_data["phone"]
        age_of_admission = birth_date.year + 15

        if year_of_admission <= age_of_admission:
            raise forms.ValidationError("Year of admission more than age of admission")

        if not phone:
            raise forms.ValidationError("Empty phone number")
        try:
            phonenumbers.parse(phone, None)
            if len(phone) < 10:
                raise forms.ValidationError("Phone too small")
            elif not phone[1:].isdigit():
                raise forms.ValidationError("Phone number is digit")
        except phonenumbers.NumberParseException as parse:
            raise forms.ValidationError(parse.args[0])
