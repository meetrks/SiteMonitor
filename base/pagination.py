from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10

    def paginate_queryset(self, queryset, request, view=None, page_size=10):
        paginator = self.django_paginator_class(queryset, page_size)
        self.last_page = paginator.num_pages
        page_number = request.query_params.get(self.page_query_param, 1)
        if page_number in self.last_page_strings:
            page_number = paginator.num_pages
        self.current_page = page_number
        try:
            self.page = paginator.page(page_number)
        except:
            self.page = paginator.page(1)
            self.current_page = 1

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data):
        return {
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
            "current_page": self.current_page,
            "last_page": self.last_page
        }
