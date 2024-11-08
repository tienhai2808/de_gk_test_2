from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MonHoc(models.Model):
  ten = models.CharField(max_length=200)
  tin_chi = models.IntegerField()
  hoc_phi = models.DecimalField(max_digits=6, decimal_places=2)
  mo_ta = models.TextField(blank=True)
  
  def __str__(self):
    return self.ten

class SinhVien(models.Model):
  ho_ten = models.CharField(max_length=150)
  gioi_tinh = models.CharField(max_length=4, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')])
  ngay_sinh = models.DateField()
  tai_khoan = models.OneToOneField(User, on_delete=models.CASCADE)
  mon_hoc = models.ManyToManyField(MonHoc, through='DangKyMonHoc')
  
  def __str__(self):
    return f'{self.ho_ten} - {self.tai_khoan}'
  
  
class DangKyMonHoc(models.Model):
  sinh_vien = models.ForeignKey(SinhVien, on_delete=models.CASCADE, related_name='nhieumonhoc')
  mon_hoc = models.ForeignKey(MonHoc, on_delete=models.CASCADE, related_name='nhieusinhvien')
  huy_dang_ky = models.BooleanField(default=False)