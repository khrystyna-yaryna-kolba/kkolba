import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Containers
from .serializers import ContainerSerializer
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
# from django.core.exceptions import ValidationError
# Create your views here.


class ContainerIDView(APIView):
    def get(self, request, id):
        """
        GET METHOD
        -- get by id (in case with endpoint with specified id)
        """
        try:
            result = Containers.objects.get(ID=id)
            containers = ContainerSerializer(result)
            return Response({'status': 'success', "containers": containers.data}, status=200)
        except Containers.DoesNotExist as d:
            return Response({'status': '404', "message": "Container with id {} was not found".format(id)},
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        """
        PUT METHOD
        --put by id
        (should contain all fields(except id)!!!)
        """
        try:
            result = Containers.objects.get(ID=id)
            data = request.data
            data["ID"] = id if "ID" not in data else data["ID"]
            serializer = ContainerSerializer(result, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "message" : "Container with id {} was successfuly updated".format(id),"data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Containers.DoesNotExist as d:
            return Response({'status': '404', "message": "Container with id {} was not found".format(id)}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        """
        DELETE METHOD
        --delete by id
        """
        if id:
            result = get_object_or_404(Containers, ID=id)
            result.delete()
            return Response({"status": "success", "message": "Record with id {} deleted".format(id)})
        else:
            return Response({"status": "error", "errors": "can`t perform delete request without specified id in it"},
                            status=status.HTTP_400_BAD_REQUEST)

class ContainerView(APIView):

    def get(self, request):
        """
        GET METHOD
        -- get by params (params : sort_by (field), sort_type(asc|desc), s(search by))
        """
        sort_by, sort_type, s = request.query_params.get("sort_by"), request.query_params.get("sort_type"), request.query_params.get("s")
        print(sort_by, sort_type, s)
        res = Containers.search(sort_by, sort_type, s)
        serializers = ContainerSerializer(res, many=True)
        return Response({'status': 'success', "containers": serializers.data}, status=200)

    def post(self, request):
        """
        POST METHOD
        """
        serializer = ContainerSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({"status": "error", "message": "Can`t add Container with ID {}! It is already in the database".format(request.data["ID"])}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"status": "success", "message" : "Container was succesfully created and added to database","data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

