from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 함수 : index
def index(request):

    # return render(request, '경로')
    return render(request, 'index.html/')