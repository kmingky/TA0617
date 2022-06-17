from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response

# Create your views here.
# user/views.py : rest framework의 APIView를 상속받아서 회원가입을 위한 post 메소드를 구현해보세요.
# 패스워드 해쉬는 아래 메소드 참고해서 작성할 것
class UserAPIView(APIView):
    # 로그인
    def post(self, request):
        email = request.data.get('email', '')
        password = request.data.get('password', '')

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."})
        
        login(request, user)
        return Response({"success": "로그인 성공"})

    def delete(self, request):
        logout(request)
        return Response({"success": "로그아웃 성공"})