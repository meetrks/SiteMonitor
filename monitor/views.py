# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.text import slugify
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from base.pagination import Pagination
from monitor.models import SiteDetail
from monitor.serializers import SiteDetailSerializer


class SiteDetailView(ListAPIView):
    serializer_class = SiteDetailSerializer
    model = SiteDetail
    pagination_class = Pagination

    def get(self, request, id=None):
        if id:
            query = SiteDetail.objects.get(pk=id)
            serializer = self.get_serializer(query)
            return Response(serializer.data, status=status.HTTP_200_OK)
        queryset = SiteDetail.objects.all()
        paginator = self.pagination_class()
        result = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = self.get_serializer(result, many=True)
        response_data = serializer.data
        response = paginator.get_paginated_response(response_data)
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            data = request.data
            data['site_slug'] = slugify(data.get('site_name'))
            serializer = self.get_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                key = next(iter(serializer.errors))
                error = serializer.errors[key][0].replace('slug', 'name')
                return Response({"detail": error.title()}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Error while adding site"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        instance = SiteDetail.objects.get(pk=id)
        try:
            data = request.data
            data['site_slug'] = slugify(data.get('site_name'))
            serializer = self.get_serializer(instance, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                key = next(iter(serializer.errors))
                error = serializer.errors[key][0].replace('slug', 'name')
                return Response({"detail": error.title()}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": "Error while adding site"}, status=status.HTTP_400_BAD_REQUEST)