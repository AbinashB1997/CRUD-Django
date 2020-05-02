from django.http import HttpResponse
from ..views import car_detail
from django.utils.deprecation import MiddlewareMixin

class ExceptionMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    def process_response(self, request, response):
        print('process responce middleware is running')
        print('resp = ', response)
        pass
    def process_exception(self, request, exception):
        print(exception)
        return HttpResponse("in exception")

    def process_view(self, request, car_detail, *view_args, **view_kargs):
        print('View middleware is running')
        pass
    def process_request(self, request):
        print('****************************')
        print('process request middleware running')
        print('****************************')
        pass
    def process_template_response(self, request, response):
        """
        Runs when view returns any TemplateResponse which is imported from the django.template.response
        """
        print('process_template_response middleware running')
        pass