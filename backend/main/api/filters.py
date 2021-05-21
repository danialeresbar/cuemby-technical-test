from rest_framework import filters


class NameFilterBackend(filters.BaseFilterBackend):
    """

    """

    def filter_queryset(self, request, queryset, view):
        name = request.query_params.get('search', '')
        filter_queryset = queryset.filter(name__icontains=name)
        return filter_queryset


class OrderFilterBackend(filters.BaseFilterBackend):
    """

    """

    def filter_queryset(self, request, queryset, view):
        order = request.query_params.get('order', 'asc')
        if order == 'dsc':
            filter_queryset = queryset.order_by('-name')
            return filter_queryset

        return queryset
