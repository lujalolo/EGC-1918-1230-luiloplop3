from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView

from .serializers import UserSerializer


class GetUserView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        tk = get_object_or_404(Token, key=key)
        return Response(UserSerializer(tk.user, many=False).data)


class LogoutView(APIView):
    def post(self, request):
        key = request.data.get('token', '')
        try:
            tk = Token.objects.get(key=key)
            tk.delete()
        except ObjectDoesNotExist:
            pass

        return Response({})

class IndexView(TemplateView):
    template_name="index.html"
    def get_context_date(self):
        context=super(Index, self).get_context_data()
        return context

class SigninView(TemplateView):
    template_name="signin.html"
    def get_context_date(self):
        context=super(Signin, self).get_context_data()
        return context

class SignupView(TemplateView):
    template_name="signup.html"
    def get_context_date(self):
        context=super(Signup, self).get_context_data()
        return context
