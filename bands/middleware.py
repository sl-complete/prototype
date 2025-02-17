from django.db import connection

class SQLPrintingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        for query in connection.queries:
            print(f"Query: {query['sql']}")
            print(f"Time: {query['time']}")
        
        return response