from django.contrib import admin
from django.urls import path
from . import views
from .views import AiAssistantView, chat_view
urlpatterns = [
    # trang chu
    path('', views.trangchu, name='trangchu'),
    # dang nhap
    path('dangnhap/', views.dangnhap, name='dangnhap'),
    # dang ky
    path('dangky/', views.dangky, name='dangky'),
    # trang chu da dang nhap  
    path('trangchudadangnhap/<ma_kh>/', views.trangchudadangnhap, name='trangchudadangnhap'),
    # tim kiem
    # path('trangchudadangnhap/<str:ma_kh>/timkiem/', views.timkiem, name='timkiem'),
    # danh muc quan
    path('danhmucquan/<str:madanhmucquan>/<str:ma_kh>/', views.danhmucquan, name="danhmucquan"),
    # danh muc gia
    path('danhmucgia/<str:madanhmucgia>/<str:ma_kh>/', views.danhmucgia, name="danhmucgia"),
    # thong tin khach hang
    path('thongtinkhachhang/<ma_kh>/', views.thongtinkh, name='thongtinkhachhang'),
    # danh sach phong
    path('danhsachphong/<ma_kh>/', views.trangdanhsachphong, name='danhsachphong'),
    # chi tiet phong
    path('phong/<str:ma_kh>/<str:ma_phong>/', views.chitietphong, name='chitietphong'),
    # dat lich
    path('phong/<str:ma_kh>/<str:ma_phong>/datlich/', views.datlichxemphong, name='datlichxemphong'),
    # lưu lịch
    path('phong/<str:ma_kh>/<str:ma_phong>/datlich/luu/', views.luulichxemphong, name='luulichxemphong'),
    # xem lich xem phong
    path('khachhang/<str:ma_kh>/lichxemphong/', views.xemlichxemphong, name='xemlichxemphong'),
    # huy lich xem phong
    path('khachhang/<str:ma_kh>/lichxemphong/huylich/<str:malichxem>/', views.huylichxemphong, name='huylichxemphong'),
    # tro ly ao
    path('ai_assistant/', AiAssistantView.as_view(), name='ai_assistant'),
    path('chat/', views.chat_view, name='chat'),
    path('timkiem/', views.timkiem, name='timkiem'),
    
]