from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path
from .city.city import City
from .models import Containers

schema_view = get_schema_view(
   openapi.Info(
      title="Containers API",
      default_version='v1',
      description="Working with containers database",
      #terms_of_service="https://www.restapicontainers.com/policies/terms/",
      contact=openapi.Contact(email="khrystyna-yaryna.kolba@lnu.edu.ua"),
      #license=openapi.License(name="TEST License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

url_patterns = [
   #swagger
    #path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

def get_example(schema):
    res ={}
    for i in schema.properties.keys():
        res[i] = schema.properties[i].example
    return res

container_schema_dict = openapi.Schema(
    title="Container",
    type=openapi.TYPE_OBJECT,
    properties={
        'ID': openapi.Schema(type=openapi.TYPE_INTEGER, description='id of the container', example = 98765),
        'number': openapi.Schema(type=openapi.TYPE_STRING, description='Container number', example="AA-12345", pattern=r"^[A-Z]{2}-[0-9]{5}$"),
        'departure_city': openapi.Schema(type=openapi.TYPE_STRING, description='Departure city', example="Paris", enum=City.list_values()),
        'arrival_city': openapi.Schema(type=openapi.TYPE_STRING, description='Arrival city', example="Toronto", enum=City.list_values()),
        'departure_date': openapi.Schema(type=openapi.TYPE_STRING, description='Departure date', example="2022-05-27", format="YYYY-MM-DD"),
        'arrival_date': openapi.Schema(type=openapi.TYPE_STRING, description='Arrival date', example="2022-05-30", format="YYYY-MM-DD"),
        'amount_of_items': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of container items', example=123),
    }
)

sort_by = openapi.Parameter(name='field to sort by', description='number(default)', enum = Containers.default_props(), in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)
sort_type = openapi.Parameter(name="sort_type", description='desc or asc(default)',enum=["asc", "desc"], in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)
s = openapi.Parameter(name="s", description='value to search', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_STRING)
offset = openapi.Parameter(name="offset", description='offset (number of items to skip(limit*offset))', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_INTEGER)
limit = openapi.Parameter(name="limit", description='limit (number of items to return)', in_=openapi.IN_QUERY,
                           type=openapi.TYPE_INTEGER)

response_get_all = {
    "200": openapi.Response(
        description="request is valid, status: status code, data: list of results (list of containers objects), "
                    "count(total number of items (may be different than a length of data list when offset and limit "
                    "is used))",
        examples={
            "application/json": {
                "status": "200",
                "data": [get_example(container_schema_dict)],
                "count" : 2,
            }
        }
    ),
    "400": openapi.Response(
        description="bad limit or offset parameter",
        examples={
            "application/json": {
                "status": "400",
                "massage": "That page number is less than 1",
            }
        }
    ),
}

response_get_by_id = {
    "200": openapi.Response(
        description="request is valid",
        examples={
            "application/json": {
                "status": "200",
                "data": get_example(container_schema_dict),
            }
        }
    ),
    "400": openapi.Response(
        description="bad id in the request (not integer)",
        examples={
            "application/json": {
                "status": "400",
                "message": "invalid url (id)"
            }
        }
    ),
    "404": openapi.Response(
        description="element with requested id was not found",
        examples={
            "application/json": {
                'status': '404',
                "message": "Container with id 98765 was not found"
            }
        }
    ),
}


response_post = {
    "201": openapi.Response(
        description="element was created and added to database",
        examples={
            "application/json": {
                "status": "201",
                "message" : "Container was succesfully created and added to database",
                "data": get_example(container_schema_dict)}
        }
    ),
    "400": openapi.Response(
        description="Validation errors in request body",
        examples={
            "application/json": {
                "status": "400",
               "message":  {
                   "ID": ["A valid integer is required." ],
                   "number": ["invalid format of container number"],
                   "arrival_city": ["invalid representation of city"]
               }
            }
        }
    ),
    "409": openapi.Response(
        description="ID conflict (trying to add element with ID that is already in database)",
        examples={
            "application/json": {
                "status": "409",
                "message": "Can`t add Container with ID 98765! It is already in the database"
            }
        }
    ),
}

response_put = {
    "201": openapi.Response(
        description="element was created and added to database",
        examples={
            "application/json": {
                "status": "201",
                "message" : "Container with ID 11111 was successfuly updated",
                "data": get_example(container_schema_dict)}
        }
    ),
    "400": openapi.Response(
        description="Validation errors in request body or bad id in the request (not integer)",
        examples={
            "application/json": {
                "status": "400",
                "message":  {
                   "ID": ["A valid integer is required." ],
                   "number": ["invalid format of container number"],
                   "arrival_city": ["invalid representation of city"]
               }
            }
        }
    ),
    "409": openapi.Response(
        description="ID conflict (trying to add element with ID that is already in database)",
        examples={
            "application/json": {
                "status": "409",
                "message": "Can`t add Container with ID 98765! It is already in the database"
            }
        }
    ),
    "404": openapi.Response(
        description="element that we want to update was not found, if you want to create an item, use POST method "
                    "instead",
        examples={
            "application/json": {
                'status': '404',
                "message": "Container with id 98765 was not found"
            }
        }
    ),
}

response_delete = {
    "200": openapi.Response(
        description="deleting was successful",
        examples={
            "application/json": {
                "status": "200",
                "message": "Container with id 98765 deleted"
                }
            }
    ),
    "400": openapi.Response(
        description="bad id in the request (not integer)",
        examples={
            "application/json": {
                "status": "400",
                "message": "invalid url (id)"
            }
        }
    ),
    "404": openapi.Response(
        description="element that we want to delete was not found",
        examples={
            "application/json": {
                'status': '404',
                "message": "Container with id 98765 was not found, can`t delete"
            }
        }
    ),
}