from multiprocessing import AuthenticationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import User
from .serializers import  user_serializer , User_login
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
import jwt
from completeauth.settings import SECRET_KEY
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate



class User_Registration(APIView):
    def post(self,request ):
        f1=request.data
        f2=user_serializer(data=f1)

        if f2.is_valid(raise_exception=True):
            f2.save()
            return Response({
                    'Msg':'Registrations successfully'
                })
        return Response(f2.errors,status=status.HTTP_400_BAD_REQUEST)

class login(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']

        user_data1=User.objects.filter(email=email).first()
        # pwd1=user_data1.check_password(password)
        # print(pwd1)
        user_data=authenticate(email=email, password=password)
        # user_data=

        print(user_data,'******************')

        if user_data1.check_password(password) is False:
            raise AuthenticationFailed({
                "Status":"Incorrect Password"
            })
        if user_data1.check_password(password) is True:
             return Response({
                    'Msg':'Loggedin successfully'
                })

        # if user_data is not None:
        #     raise AuthenticationFailed({
        #         "Status":"Incorrect Password"
        #     })

        # encoded_jwt = jwt.encode(Payload, SECRET_KEY, algorithm=ALGORITHM)

        # if serializer.is_valid(raise_exception=True):
        #     email=serializer.data.get('email')
        #     password=serializer.data.get('password')

        #     print(email, "\n" , password)

        #     authenticate()

        # f1=User.objects.filter(email=email).first()

