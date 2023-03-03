from django import forms
from .models import DataExcel

class FileForm(forms.ModelForm):
    excel_file= forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model=DataExcel
        fields=['excel_file']
        # widgets = {
        #     'excel_file': forms.ClearableFileInput(attrs={'multiple': True})
        # }
    def clean_excel_file(self):
        print("karan")
        file = self.cleaned_data['excel_file']
        print(file.name,'form clean data')
        # if not file.name.endswith('.csv'):
        #     print("karan")
        #     raise forms.ValidationError('Invalid file type. Only CSV files are allowed.')
        return file
