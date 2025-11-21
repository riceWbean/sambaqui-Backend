from rest_framework.pagination import PageNumberPagination

class ArtefactPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'num_artefacts'
    max_page_size = 100