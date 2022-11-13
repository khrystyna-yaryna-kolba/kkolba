from drf_yasg import openapi

from .swagger import unauthorized_401, get_example, forbidden_403

container_order_schema_dict = openapi.Schema(
    title="Container Order",
    type=openapi.TYPE_OBJECT,
    properties={
        'container_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='id of the container', example = 98765),
        'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of container items', example=123),
    }
)

order_post_schema = openapi.Schema(
    title="add new container order",
    type=openapi.TYPE_OBJECT,
    properties={
        'container_id': openapi.Schema(type=openapi.TYPE_INTEGER, description='id of the container', example = 98765),
        'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of container items', example=123),

    }
)

orders_get_all = {
    "200": openapi.Response(
        description="request is valid",
        examples={
            "application/json":
                [get_example(container_order_schema_dict)],
        }),
    "401": unauthorized_401,

}
order_post_response = {
    "201": openapi.Response(
        description="Container Order was created",
        examples={
            "application/json":
                {
                    "status": "201",
                    "message": "Container Order was succesfully created and added to database",
                    "data": get_example(container_order_schema_dict),
                }
        }),
    "400": openapi.Response(
        description="Container Order was not created",
        examples={
            "application/json":
                {
                    "status": "400",
                    "message": "too big amount"
                }
        }),
    "404": openapi.Response(
        description="Container Order was not created because container was not found",
        examples={
            "application/json":
                {
                    "detail": "Not found."
                }
        }),
    "401": unauthorized_401,
}
order_get_by_id_response = {
    "200": openapi.Response(
        description="request was successful",
        examples={
            "application/json":
                get_example(container_order_schema_dict)
        }),
    "404": openapi.Response(
        description="Container Order was not created because container was not found",
        examples={
            "application/json":
                {
                    "detail": "Not found."
                }
        }),
    "401": unauthorized_401,
    "403": openapi.Response(
        description="this order id is in the order of the other user",
        examples={
            "application/json": {
                "detail": "You do not have permission to perform this action."
            }
        }),
}