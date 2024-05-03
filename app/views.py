from django.shortcuts import get_object_or_404, render,redirect
from django.http import JsonResponse
from .models import *
import random
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import render
from django.views import View
from .models import Phong
import google.generativeai as genai
from django.http import JsonResponse
from django.views import View

# Create your views here.


# trang chu
def trangchu(request):  
    return render(request, 'app/trangchu.html',)


# đăng nhập
def dangnhap(request):
    if request.method == "POST":
        ma_kh = request.POST.get('ma_kh')
        password = request.POST.get('password')
        khachhang = Khachhang.objects.filter(ma_kh=ma_kh).first()
        if khachhang and khachhang.password == password:
        # Đăng nhập thành công
            request.session['khachhang_id'] = khachhang.ma_kh
            trangchudadangnhap_url = reverse('trangchudadangnhap', kwargs={'ma_kh': khachhang.ma_kh})
            return redirect(trangchudadangnhap_url)
        else:
            messages.info(request, 'Mã khách hàng hoặc Mật Khẩu của bạn không đúng!')
    return render(request, 'app/dangnhap.html') 


# đăng ký
def dangky(request):
    if request.method == "POST":
        ma_kh = request.POST.get('ma_kh')
        ten_kh = request.POST.get('ten_kh')
        password = request.POST.get('password')
        sdt_kh = request.POST.get('sdt_kh')
        email_kh = request.POST.get('email_kh')
        diachi_kh = request.POST.get('diachi_kh')
        cccd = request.POST.get('cccd')

        khachhang = Khachhang(ma_kh=ma_kh, ten_kh=ten_kh, password=password, sdt_kh=sdt_kh, email_kh=email_kh, diachi_kh=diachi_kh, cccd=cccd)
        khachhang.save()
        return redirect('dangnhap')

    return render(request, 'app/dangky.html')

 
# trang chu da dang nhap
def trangchudadangnhap(request, ma_kh):
    if 'khachhang_id' not in request.session:
        return redirect('dangnhap')
    
    if request.method == 'POST':
        search_title = request.POST.get('search_title')
        request.session['khachhang_id'] = ma_kh
        # Thực hiện tìm kiếm sản phẩm với tiêu đề trùng
        phong_list = Phong.objects.filter(tieude=search_title)
        return redirect('ketquatimkiem', ma_kh=ma_kh, search_title=search_title)
    
    ma_kh = request.session.get('khachhang_id')
    khachhang = Khachhang.objects.get(ma_kh=ma_kh)
    danhmucquans = Danhmucquan.objects.all()
    danhmucgias = Danhmucgia.objects.all()
    context = {
        'khachhang': khachhang,
        'danhmucquans': danhmucquans,
        'danhmucgias': danhmucgias,
    }
    return render(request, 'app/trangchudadangnhap.html', context)


# # tim kiém
def timkiem(request, ma_kh):
    if request.method == 'POST':
        search_title = request.POST.get('search_title', '')
        # Thực hiện tìm kiếm sản phẩm với tiêu đề trùng
        phong_list = Phong.objects.filter(tieude=search_title)
        context = {
            'phong_list': phong_list
        }
        return render(request, 'app/ketquatimkiem.html', context)
    
    return redirect('trangchudadangnhap', ma_kh=ma_kh)


# danh mục quan
def danhmucquan(request, madanhmucquan, ma_kh):
    danhmucquans = Danhmucquan.objects.all()
    ma_kh = request.session.get('khachhang_id')
    khachhang = Khachhang.objects.get(ma_kh=ma_kh)
    danhmucquanp = request.GET.get('danhmucquan', '')
    if danhmucquanp:
        phongs = Phong.objects.filter(danhmucquanhuyen=danhmucquanp)
    else:
        phongs = Phong.objects.all()
    context = {'danhmucquans': danhmucquans, 'phongs': phongs, 'danhmucquanp': danhmucquanp, 'khachhang': khachhang}
    return render(request, 'app/danhmucquan.html', context)


# danh muc giá
def danhmucgia(request, madanhmucgia, ma_kh):
    danhmucgias = Danhmucgia.objects.all()
    ma_kh = request.session.get('khachhang_id')
    khachhang = Khachhang.objects.get(ma_kh=ma_kh)
    danhmucgiap = request.GET.get('danhmucgia', '')
    if danhmucgiap:
        phongs = Phong.objects.filter(danhmucgiaca=danhmucgiap)
    else:
        phongs = Phong.objects.all()
    context = {'danhmucgias': danhmucgias, 'phongs': phongs, 'danhmucgiap': danhmucgiap, 'khachhang': khachhang}
    return render(request, 'app/danhmucgia.html', context)


# trang thong tin khach hang
def thongtinkh(request, ma_kh):
    ma_kh = request.session.get('khachhang_id')
    khachhang = Khachhang.objects.get(ma_kh=ma_kh)
    context = {
        'khachhang': khachhang
        }
    return render(request, 'app/thongtinkhachhang.html', context)


# trang danh sach phong
def trangdanhsachphong(request, ma_kh):
    ma_kh = request.session.get('khachhang_id')
    phongs = Phong.objects.all()
    khachhang = Khachhang.objects.get(ma_kh=ma_kh)
    context = {
        'phongs': phongs,
        'khachhang': khachhang
        }
    return render(request, 'app/danhsachphong.html', context)


# chi tiet phong
def chitietphong(request, ma_kh, ma_phong):
    phong = get_object_or_404(Phong, maphong=ma_phong)
    context = {
        'phong': phong,
        'ma_kh': ma_kh,
    }
    return render(request, 'app/chitietphong.html', context)


# ramdon ma lich xem
def generate_random_code():
    code = random.randint(1000, 9999)  # Tạo một số ngẫu nhiên từ 1000 đến 9999
    while Lichxemphong.objects.filter(malichxem=code).exists():  # Kiểm tra xem số đã tồn tại trong cơ sở dữ liệu chưa
        code = random.randint(1000, 9999)  # Nếu đã tồn tại, tạo số mới
    return str(code)


# dat lich
def datlichxemphong(request, ma_kh, ma_phong):
    phong = get_object_or_404(Phong, maphong=ma_phong)
    khachhang = get_object_or_404(Khachhang, ma_kh=ma_kh)
    malichxem = generate_random_code()
    context = {
        'phong': phong,
        'khachhang': khachhang,
        'malichxem': malichxem,
    }
    return render(request, 'app/datlichxemphong.html', context)


# luu lich xem phòng
def luulichxemphong(request, ma_kh, ma_phong):
    if request.method == 'POST':
        phong = get_object_or_404(Phong, maphong=ma_phong)
        khachhang = get_object_or_404(Khachhang, ma_kh=ma_kh)
        thoigianxem = request.POST.get('thoigianxem')
        malichxem = generate_random_code()
        lichxemphong = Lichxemphong.objects.create(
            malichxem=malichxem,
            ma_phong_xem=phong,
            ten_kh_xem=khachhang,
            gia=phong.gia,
            tgxem=thoigianxem,
            diachi_phong=phong.diachi,
            email_kh=khachhang.email_kh,
            sdt_kh=khachhang.sdt_kh
        )
        lichxemphong.save()
        return redirect('danhsachphong', ma_kh=ma_kh)

# xem lich xem phong
def xemlichxemphong(request, ma_kh):
    khachhang = get_object_or_404(Khachhang, ma_kh=ma_kh)
    lichxemphong = Lichxemphong.objects.filter(ten_kh_xem=khachhang)
    context = {
        'khachhang': khachhang,
        'lichxemphong': lichxemphong,
    }
    return render(request, 'app/xemlichxemphong.html', context)


# huy lich xem phong
def huylichxemphong(request, ma_kh, malichxem):
    lichxemphong = get_object_or_404(Lichxemphong, malichxem=malichxem)
    lichxemphong.delete()
    return redirect('xemlichxemphong', ma_kh=ma_kh)




# ... (các import khác của bạn) ...

# Cấu hình API key (thay thế bằng API key của bạn)
genai.configure(api_key="AIzaSyBCjnxRI0H8l-z3JfTNtHbqMquBv6DaipA")

def get_chat_history(request):
    # Lấy lịch sử trò chuyện từ session
    # (bạn cần xử lý trường hợp session chưa có dữ liệu)
    return request.session.get('chat_history', [])

def save_chat_history(request, history):
    # Lưu lịch sử trò chuyện vào session
    request.session['chat_history'] = history

class AiAssistantView(View): 
    def get(self, request):
        return render(request, 'app/chattrolyao.html')

    def post(self, request):
        NguoiDung = request.POST.get('q', '')
        ma_kh = request.POST.get('ma_kh')
        response = self.process_input(NguoiDung, request)
        if isinstance(response, str):
            return JsonResponse({'response': response})
        else:
            return JsonResponse({'response': response['response'], 'redirect_url': response['redirect_url']})

    def process_input(self, NguoiDung, request):
        if 'chào' in NguoiDung:
            response = 'Chào bạn, tôi là trợ lý ảo của web, tôi có thể giúp gì cho bạn?'
            return response
        elif NguoiDung == '':
            response = 'Tôi không hiểu bạn đang nói gì, hãy lặp lại'
            return response
        elif 'tìm kiếm phòng ở' in NguoiDung:
            search_keyword = NguoiDung.split('tìm kiếm phòng ở', 1)[1].strip()
            ma_kh = request.POST.get('ma_kh')
            redirect_url = f'/trolyaotimkiemquan/{ma_kh}/?search_quan={search_keyword}'
            return {'response': f'Đây là kết quả tìm kiếm phòng ở "{search_keyword}" của bạn', 'redirect_url': redirect_url}
        elif 'tìm kiếm phòng có giá' in NguoiDung:
            search_keyword = NguoiDung.split('tìm kiếm phòng có giá', 1)[1].strip()
            ma_kh = request.POST.get('ma_kh')
            redirect_url = f'/trolyaotimkiemgia/{ma_kh}/?search_gia={search_keyword}'
            return {'response': f'Đây là kết quả tìm kiếm phòng có giá "{search_keyword}" của bạn', 'redirect_url': redirect_url}
        elif 'tìm kiếm ' in NguoiDung:
            search_keyword = NguoiDung.split('tìm kiếm', 1)[1].strip()
            ma_kh = request.POST.get('ma_kh')
            redirect_url = f'/trolyaotimkiem/{ma_kh}/?search_title={search_keyword}'
            return {'response': f'Đây là kết quả tìm kiếm phòng có tiêu đề là "{search_keyword}" của bạn', 'redirect_url': redirect_url}
        else:
            # Lấy lịch sử trò chuyện
            history = get_chat_history(request)

            # Gọi Gemini API
            response = call_gemini_api(NguoiDung, history)

            # Lưu lịch sử trò chuyện mới
            history.append({"role": "user", "parts": [NguoiDung]})
            history.append({"role": "model", "parts": [response]})
            save_chat_history(request, history)

            return response

def call_gemini_api(query, history=[]):
    # Thiết lập mô hình
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    }

    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        # ... (các cài đặt an toàn khác) ...
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    # Khởi tạo cuộc trò chuyện và gửi tin nhắn
    convo = model.start_chat(history=history)
    convo.send_message(query)
    return convo.last.text

def trolyaotimkiem(request, ma_kh):
    if request.method == 'GET':
        search_title = request.GET.get('search_title', '')
        phong_list = Phong.objects.filter(tieude=search_title)
        context = {
            'phong_list': phong_list,
             'ma_kh': ma_kh
        }
        return render(request, 'app/ketquatimkiem.html', context)
    return redirect('trangchudadangnhap', ma_kh=ma_kh)


def trolyaotimkiemquan(request, ma_kh):
    if request.method == 'GET':
        search_quan = request.GET.get('search_quan', '')
        phong_list = Phong.objects.filter(diachi=search_quan)
        context = {
            'phong_list': phong_list,
             'ma_kh': ma_kh
        }
        return render(request, 'app/ketquatimkiem.html', context)
    return redirect('trangchudadangnhap', ma_kh=ma_kh)


def trolyaotimkiemgia(request, ma_kh):
    if request.method == 'GET':
        search_gia = request.GET.get('search_gia', '')
        phong_list = Phong.objects.filter(gia=search_gia)
        context = {
            'phong_list': phong_list,
             'ma_kh': ma_kh
        }
        return render(request, 'app/ketquatimkiem.html', context)
    return redirect('trangchudadangnhap', ma_kh=ma_kh)


def chat_view(request, ma_kh):
    return render(request, 'app/chattrolyao.html', {'ma_kh': ma_kh})


