from rest_framework.filters import OrderingFilter
from rest_framework.compat import coreapi, coreschema
from django.utils.encoding import force_str

class SortBySortType(OrderingFilter):

    def get_ordering(self, request, queryset, view):
        sort_by = request.query_params.get("sort_by")
        sort_type = request.query_params.get("sort_type")
        ordering = None
        if sort_by:
            fields = [param.strip() for param in sort_by.split(',')]
            ordering = [f for f in fields if f in view.ordering_fields]
        if sort_type == "desc":
            ordering = ['-' + f for f in ordering]
        if ordering:
            return ordering

        # No ordering was included, or all the ordering fields were invalid
        return self.get_default_ordering(view)


    def get_schema_fields(self, view):
        return []