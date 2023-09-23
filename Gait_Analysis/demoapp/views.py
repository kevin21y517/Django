from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import cv2

@csrf_exempt  # 可能需要禁用CSRF保护，具体取决于您的配置和需求
def video_stream(request):

    # 開啟攝像機
    cap = cv2.VideoCapture(0)

    if request.method == 'POST':
        # 处理从树莓派发送的视频流数据
        # 解析请求体，处理视频数据并进行必要的处理
        # 将数据传递给WebRTC处理

        # 示例：将数据发送给所有连接的WebRTC客户端
        # 我们假设您已经建立了WebSocket连接，下面的示例仅用于演示。
        video_data = request.body
        # 在这里，您可以将video_data传递给连接的WebRTC客户端
        # 例如，使用WebSocket将视频数据广播给所有客户端

        # 请确保返回适当的HTTP响应
        return HttpResponse('Video stream received and processed', content_type='text/plain')
    else:
        # 处理GET请求，返回网页或其他页面
        # 在这里，您可以渲染包含WebRTC视频流的HTML页面
        # 请参考Django的模板渲染和视图功能

        # 示例：返回包含视频流的HTML页面
        return render(request, 'video_stream.html')


def index(request):
    return HttpResponse("hi")

from django.shortcuts import render

def chart_view(request):
    data = {
        'labels': ['January', 'February', 'March', 'April', 'May'],
        'data': [10, 20, 15, 25, 30]
    }
    return render(request, 'home.html', {'data': data})

def home(request):
    data = [{'title':"1"},{'title':"2"},{'title':"3"}]
    return render (request,"index.html",context={"text":"hihi", "text2":data})

def login(request):
    return render(request,'login.html')

def eye(request):
    return render(request,'eye.html')