from django.contrib import admin
from .models import *

# Register your models here.
class SinhVienAdmin(admin.ModelAdmin):
  list_display = ('ho_ten', 'gioi_tinh', 'ngay_sinh')
  list_filter = ('ho_ten', 'gioi_tinh')
  search_fields = ('ho_ten', 'gioi_tinh')

admin.site.register(SinhVien, SinhVienAdmin)
admin.site.register(MonHoc)
admin.site.register(DangKyMonHoc)