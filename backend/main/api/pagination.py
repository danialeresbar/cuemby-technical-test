from rest_framework import response, pagination


class CustomPagination(pagination.PageNumberPagination):
    """
    Pagination subclass for custom GET and POST request pagination
    """

    page_size = 10
    page_query_param = 'Page'

    def get_page_number(self, request, paginator):
        page_number = request.data.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        return page_number

    def get_paginated_response(self, data):
        return response.Response({
            'Page': self.page.number,
            'totalPages': self.page.paginator.num_pages,
            'Items': len(data),
            'totalItems': self.page.paginator.count,
            'results': data
        })
