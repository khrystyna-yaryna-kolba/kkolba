from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from .models import Containers
from .serializers import ContainerSerializer
from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from .swagger.swagger import container_schema_dict, limit, offset, sort_type, sort_by, s
from .swagger.swagger import response_get_all, response_get_by_id, response_post, response_put, response_delete
from .custom_filters import SortBySortType
from .custom_pagination import CustomPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser


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

    def get_permissions(self):
        method = self.request.method
        if method == 'POST':
            return [IsAuthenticated() and IsAdminUser()]
        else:
            return [IsAuthenticated()]

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

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            return [IsAuthenticated()]
        else:
            return [IsAuthenticated() and IsAdminUser()]

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
            # to prevent query dict error
            request.data._mutable = True
            data = request.data
            data["ID"] = id if "ID" not in data else data["ID"]
            # if we want to change id:
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


