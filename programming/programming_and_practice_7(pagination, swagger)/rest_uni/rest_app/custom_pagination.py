from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomPagination(LimitOffsetPagination):
    offset_query_description = 'offset*limit is the initial index from which to return the results.'

    def paginate_queryset(self, queryset, request, view=None):
        self.limit = self.get_limit(request)
        if self.limit is None:
            self.count = self.get_count(queryset)
            return list(queryset[:])
        self.count = self.get_count(queryset)
        self.offset = self.get_offset(request)
        self.request = request
        if self.count == 0 or self.offset > self.count:
            return []
        return list(queryset[self.offset:self.offset + self.limit])

    def get_offset(self, request):
        offset = super().get_offset(request)
        return self.get_limit(request) * offset

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('status', "200"),
            ('count', self.count),
            ('data', data)
        ]))
