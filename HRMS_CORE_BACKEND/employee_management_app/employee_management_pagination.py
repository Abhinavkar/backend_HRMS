from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response




class CustomPagination(PageNumberPagination):
    page_size = 2  # Default number of records per page
    page_size_query_param = 'page_size'  # You can change the page size via this query parameter
    max_page_size = 100  # Maximum number of records per page

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,  # Total number of records
            'next': self.get_next_link(),  # URL to the next page of results
            'previous': self.get_previous_link(),  # URL to the previous page of results
            'results': data  # Paginated data
        })
