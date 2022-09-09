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
from .serializers import employedSerializer
from .models import employed
import logging


class employedViews(APIView):
    def post(self, request, org_id=None):
        data = request.data
        logging.warning("Add customer")
        logging.warning(data)
        serializer = employedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            logging.warning(serializer.errors)
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None, org_id=None):
        if id:
            item = employed.objects.get(id=id)
            serializer = employedSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = employed.objects.all()
        serializer = employedSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None, org_id=None):
        id = request.data.get('id')
        item = employed.objects.get(id=id)
        serializer = employedSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None, org_id=None):
        item = get_object_or_404(employed, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class employedbyemployed(APIView):

    def post(self, request, user_id=None):
        logging.warning(user_id)
        if user_id:
            item = employed.objects.filter(user_id=user_id)
            serializer = employedSerializer(item, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "data": []}, status=status.HTTP_400_BAD_REQUEST)
