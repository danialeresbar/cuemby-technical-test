from rest_framework import response, pagination


class PaginationHandlerMixin:

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):

        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return response.Response({
            'Page': self.page.number,
            'totalPages': self.page.paginator.num_pages,
            'Items': len(data),
            'totalItems': self.page.paginator.count,
            'results': data
        })