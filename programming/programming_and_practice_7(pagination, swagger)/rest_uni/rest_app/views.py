import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Containers
from .serializers import ContainerSerializer
from django.db import IntegrityError
from django.core.paginator import Paginator, InvalidPage
# from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from .swagger import container_schema_dict, limit, offset, sort_type, sort_by, s
from .swagger import response_get_all, response_get_by_id, response_post, response_put, response_delete
from rest_framework import generics, filters
from .custom_filters import SortBySortType
from .custom_pagination import CustomPagination
# Create your views here.

class ContainerListCreateApiView(generics.ListCreateAPIView):
    queryset = Containers.objects.all()
    serializer_class = ContainerSerializer
    pagination_class = CustomPagination
    filter_backends = [SortBySortType, filters.SearchFilter]
    ordering_fields = Containers.default_props()
    ordering = "number"
    search_fields = Containers.default_props()
    http_method_names = ['get', 'post']
    @swagger_auto_schema(
        manual_parameters=[sort_by, sort_type, s, offset, limit],
        responses=response_get_all
    )
    def get(self, request, *args, **kwargs):
        """
        get from whole collection of containers
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        responses=response_post,
        request_body=container_schema_dict,
    )
    def post(self, request, *args, **kwargs):
        """
        add new container to database
        """
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({"status": "409",
                                 "message": "Can`t add Container with ID {}! It is already in the database".format(
                                     request.data["ID"])}, status=status.HTTP_409_CONFLICT)
            return Response({"status": "201", "message": "Container was succesfully created and added to database",
                             "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "400", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class ContainerIDView(APIView):
    serializer_class = ContainerSerializer
    http_method_names = ['get', 'put', 'delete']

    @swagger_auto_schema(
        responses=response_get_by_id
    )
    def get(self, request, id):
        """
        GET METHOD
        -- get by id (in case with endpoint with specified id)
        """
        try:
            int(id)
            result = Containers.objects.get(ID=id)
            containers = ContainerSerializer(result)
            return Response({'status': '200', "data": containers.data}, status=status.HTTP_200_OK)
        except Containers.DoesNotExist as d:
            return Response({'status': '404', "message": "Container with id {} was not found".format(id)},
                            status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"status": "400", "message": "invalid url (id)"}, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        responses=response_put,
        request_body=container_schema_dict,
    )
    def put(self, request, id):
        """
        PUT METHOD
        --put by id
        request body should contain all fields (maybe without id if you don`t want to change it)
        !!!can change id
        """
        try:
            result = Containers.objects.get(ID=id)
            #to prevent query dict error
            request.data._mutable = True
            data = request.data
            data["ID"] = id if "ID" not in data else data["ID"]
            #if we want to change id:
            if int(id) != int(data["ID"]):
                duplicat = Containers.objects.filter(ID=data["ID"])
                if duplicat:
                    return Response({"status": "409",
                                     "message": "Can`t put Container with ID {}! It is already in the database".format(
                                         request.data["ID"])}, status=status.HTTP_409_CONFLICT)
            serializer = ContainerSerializer(result, data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "200", "message" : "Container with id {} was successfuly updated".format(id),"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "400", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Containers.DoesNotExist as d:
            return Response({'status': '404', "message": "Container with id {} was not found".format(id)}, status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"status": "400", "message": "invalid url (id)"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses=response_delete
    )
    def delete(self, request, id):
        """
        DELETE METHOD
        --delete by id
        """
        try:
            int(id)
            result = Containers.objects.get(ID=id)
            result.delete()
            return Response({"status": "200", "message": "Container with id {} deleted".format(id)}, status=status.HTTP_200_OK)
        except Containers.DoesNotExist as d:
            return Response({'status': '404', "message": "Container with id {} was not found, can`t delete".format(id)},
                            status=status.HTTP_404_NOT_FOUND)
        except ValueError:
            return Response({"status": "400", "message": "invalid url (id)"}, status=status.HTTP_400_BAD_REQUEST)


"""class ContainerView(APIView):
    @swagger_auto_schema(
        manual_parameters=[sort_by, sort_type, s, offset, limit],
        responses=response_get_all
    )
    def get(self, request):
        
        GET METHOD
         -- get by params (params : sort_by (field), sort_type(asc|desc), s(search by), offset(number of items to skip(limit*offset)), limit(number of items to return))
        
        sort_by, sort_type, s = request.query_params.get("sort_by"), request.query_params.get(
            "sort_type"), request.query_params.get("s")
        offset, limit = request.query_params.get("offset"), request.query_params.get("limit")
        res = Containers.search(sort_by, sort_type, s)
        count = len(res)
        if offset is not None and limit is not None:
            p = Paginator(res, limit)
            try:
                serializers = ContainerSerializer(p.page(int(offset) + 1), many=True)
            except InvalidPage as e:
                return Response({'status': '400', "message": str(e)},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            serializers = ContainerSerializer(res, many=True)
        return Response({'status': '200', "data": serializers.data, "count": count}, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        responses=response_post,
        request_body=container_schema_dict,
    )
    def post(self, request):
        
        POST METHOD
        add new container to database
        
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({"status": "409", "message": "Can`t add Container with ID {}! It is already in the database".format(request.data["ID"])}, status=status.HTTP_409_CONFLICT)
            return Response({"status": "201", "message" : "Container was succesfully created and added to database","data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "400", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)"""

