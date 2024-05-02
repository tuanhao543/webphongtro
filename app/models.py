from django.db import models

# Create your models here.


# Danh mục phong
class Danhmucquan(models.Model):
    madanhmucquan = models.CharField(primary_key=True, max_length=20)
    tendanhmucquan = models.CharField(max_length=40)
    def __str__(self):
        return self.tendanhmucquan


# Danh mục giá
class Danhmucgia(models.Model):
    madanhmucgia = models.IntegerField(primary_key=True, max_length=20)
    tendanhmucgia = models.CharField(max_length=20)
 
    def __str__(self):
        return self.tendanhmucgia


# Phòng
class Phong(models.Model):
    maphong = models.CharField(primary_key=True, max_length=20)
    tieude = models.CharField(max_length=50)
    mota = models.CharField(max_length=200)
    ttnt = models.BooleanField(verbose_name='Có Nội Thất')
    gia = models.IntegerField(max_length=5)
    diachi = models.CharField(max_length=50)
    dientich = models.IntegerField(max_length=5)
    hinhanh = models.ImageField()
    danhmucquan = models.ForeignKey(Danhmucquan, on_delete=models.CASCADE, related_name='danh_muc_quan', default=1)
    danhmucgia = models.ForeignKey(Danhmucgia, on_delete=models.CASCADE, related_name='danh_muc_giaca', default=1)
    
    def __str__(self):
        return self.maphong
    @property
    def hinhanhURL(self):
        try:
            url = self.hinhanh.url
        except:
            url = ''
        return url
    
    
# Khách Hàng
class Khachhang(models.Model):
    ma_kh = models.CharField(primary_key=True, max_length=20)
    ten_kh = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    sdt_kh = models.IntegerField(max_length=10)
    email_kh = models.EmailField()
    diachi_kh = models.CharField(max_length=20)
    cccd = models.IntegerField(max_length=20)

    
    def __str__(self):
        return self.ma_kh
    

# lịch xem phòng
class Lichxemphong(models.Model):
    malichxem = models.CharField(primary_key=True, max_length=20)
    ma_phong_xem = models.ForeignKey(Phong, on_delete=models.CASCADE, related_name='lich_xem_phong_ma_phong')
    ten_kh_xem = models.ForeignKey(Khachhang, on_delete=models.CASCADE, related_name='lich_xem_phong_ten_kh')
    gia = models.IntegerField()
    tgxem = models.DateTimeField()
    diachi_phong = models.CharField(max_length=200)
    email_kh = models.EmailField()
    sdt_kh = models.CharField(max_length=20)
    
    def __str__(self):
        return self.malichxem


