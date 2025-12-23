from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'message', 'cv']

    def clean_cv(self):
        cv = self.cleaned_data.get('cv')

        if cv:
            if not cv.name.lower().endswith(('.pdf', '.doc', '.docx')):
                raise forms.ValidationError("Faqat PDF yoki DOC/DOCX fayl mumkin")

            if cv.size > 50 * 1024 * 1024:
                raise forms.ValidationError("Fayl hajmi 50MB dan oshmasligi kerak")
        return cv


