from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import SinhVienForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request, 'index.html')

def ctmonhoc(request, idmonhoc):
  monhoc=get_object_or_404(MonHoc, id=idmonhoc)
  nhieusinhvien = monhoc.nhieusinhvien.all()
  # nhieusinhvien = DangKyMonHoc.objects.filter(mon_hoc=monhoc)
  return render(request, 'ctmonhoc.html', {'monhoc': monhoc, 'nhieusinhvien':nhieusinhvien})

def ctsinhvien(request, idsinhvien):
  sinhvien = get_object_or_404(SinhVien, id=idsinhvien)
  nhieumonhoc = DangKyMonHoc.objects.filter(sinh_vien=sinhvien)
  somonhoc = nhieumonhoc.count() 
  tonghocphi = sum([monhoc.mon_hoc.hoc_phi for monhoc in nhieumonhoc]) 
  return render(request, 'ctsinhvien.html', {'sinhvien': sinhvien, 'somonhoc': somonhoc, 'tonghocphi': tonghocphi})

def sinhvien(request, idsinhvien=None):
  if idsinhvien:
    sinh_vien = get_object_or_404(SinhVien, id=idsinhvien)
    title = f'Sửa sinh viên {sinh_vien.ho_ten}'
    button = 'Sửa'
  else:
    sinh_vien = None
    title = 'Tạo sinh viên'
    button = 'Tạo'
  form = SinhVienForm(request.POST or None, instance=sinh_vien)
  if request.POST:
    if form.is_valid():
      sinh_vien_update = form.save(commit=False)
      if not idsinhvien:
        tai_khoan_none = [user for user in User.objects.all() if not hasattr(user, 'sinhvien')]
        sinh_vien_update.tai_khoan = tai_khoan_none[0]
      sinh_vien_update.save()
      form.save_m2m()
      if idsinhvien:
        messages.success(request, f'Sửa thành công {sinh_vien_update.ho_ten}')
      else:
        messages.success(request, f'Tạo thành công {sinh_vien_update.ho_ten}')
      return redirect('ctsinhvien', sinh_vien_update.id)
  return render(request, 'sinhvien.html', {'form': form, 'title': title, 'button': button})