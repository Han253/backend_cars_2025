from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    """
    Custom pagination class to set the default page size and maximum page size.
    """
    page_size = 10 # Valor por defecto
    page_size_query_param = 'page_size' # Parámetro de consulta para el tamaño de página
    max_page_size = 100 # Tamaño máximo de página
    page_query_param = 'page' # Parámetro de consulta para la página

