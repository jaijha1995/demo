# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from rest_framework.decorators import action
from django.contrib.auth.forms import PasswordResetForm
from .serializers import loginSerializer
from .models import login
import logging


class loginViews(APIView):
    def post(self, request, org_id=None):
        data = request.data
        logging.warning("Add customer")
        logging.warning(data)
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            logging.warning(serializer.errors)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            item = login.objects.get(id=id)
            serializer = loginSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = login.objects.all()
        serializer = loginSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        id = request.data.get('id')
        item = login.objects.get(id=id)
        serializer = loginSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None, org_id=None):
        item = get_object_or_404(login, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})



class ListCustomerViews(APIView):
    def get(self, request, org_id=None):
        items = login.objects.filter(org_id=org_id)
        serializer = loginSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class LoginCustomer(APIView):
    def post(self, request,org_id=None):
        email = request.data['email']
        password = request.data['password']
        # logging.warning(email, password)
        try:
            item = login.objects.filter(email=email).first()
            serializer = loginSerializer(item)
            dpassword = serializer.data['password']
            if password == dpassword:
                data = serializer.data
                return Response({"status": "success", "data": data, "msg": "True"})
            else:
                return Response({"status": "passworderror", "msg": "Passwords do not match, try again"})
        except employed.DoesNotExist:
            return Response({"status": "emailerror", "msg": "User Does not match, try again"})


class CreateCustomer(APIView):
    def post(self, request, org_id=None):
        logging.warning("Add customer")
        request.data['org_id'] = org_id
        data = request.data
        logging.warning(org_id)
        logging.warning(data)
        serializer = loginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            logging.warning(serializer.errors)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


