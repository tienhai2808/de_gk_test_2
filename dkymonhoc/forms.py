from django import forms
from .models import SinhVien

class SinhVienForm(forms.ModelForm):
  class Meta:
    model = SinhVien
    exclude = ('tai_khoan',)