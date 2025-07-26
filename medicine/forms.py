from django import forms

from medicine.models import Doctor


class DoctorForm(forms.ModelForm):
    """Форма создания доктора"""
    class Meta:
        model = Doctor
        fields = ["full_name", "resume", "specialization", "work_experience"]

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите имя и фамилию доктора"}
        )
        self.fields["resume"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите резюме"}
        )
        self.fields["specialization"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Выберите специализацию",
            })
        self.fields["work_experience"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Укажите стаж работы в этой сфере",
            }
        )
