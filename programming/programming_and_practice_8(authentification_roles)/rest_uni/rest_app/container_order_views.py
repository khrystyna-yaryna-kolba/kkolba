from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ContainerOrder, Containers
from .serializers import ContainerOrderSerializer, ContainerOrderForUserSerializer
from .swagger.container_order_swagger import orders_get_all, order_post_schema, order_post_response, order_get_by_id_response


class ContainerOrderViewSet(viewsets.ModelViewSet):
    serializer_class = ContainerOrderSerializer
    queryset = ContainerOrder.objects.all()
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        responses=orders_get_all,
    )
    def list(self, request, *args, **kwargs):
        if self.request.user.is_admin():
            return super().list(request, *args, **kwargs)
        else:
            queryset = ContainerOrder.objects.filter(user_id=self.request.user)
            serializer = ContainerOrderForUserSerializer(queryset, many=True)
            return Response(serializer.data)

    @swagger_auto_schema(
        request_body=order_post_schema,
        responses=order_post_response,
    )
    def create(self, request, *args, **kwargs):
        data = request.data
        data["user_id"] = self.request.user.id
        serializer = ContainerOrderSerializer(data=data)
        container = get_object_or_404(Containers, ID=data["container_id"])
        if serializer.is_valid():

            if data["amount"] > container.quantity:
                return Response({"status": "400", "message": "too big amount"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                container.quantity = container.quantity - data["amount"]
                container.save(update_fields = ["quantity"])
                serializer.save()
            return Response({"status": "201", "message": "ContainerOrder was succesfully created and added to database",
                             "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "400", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        responses=order_get_by_id_response,
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        if self.request.user.is_admin():
            return super().retrieve(request, pk, *args, **kwargs)
        else:
            order = get_object_or_404(ContainerOrder, id=pk)
            if self.request.user.id != order.user_id:
                return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
            serializer = ContainerOrderSerializer(order)
            return Response(serializer.data)
