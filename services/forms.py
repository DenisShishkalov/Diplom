from django import forms

from services.models import Service


class ServiceForm(forms.ModelForm):
    """Форма создания услуг"""

    class Meta:
        model = Service
        fields = [
            "name",
            "description",
            "price",
        ]

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите услугу"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Укажите описание услуги"}
        )
        self.fields["price"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Укажите цену",
            }
        )
