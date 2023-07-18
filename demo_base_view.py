from django.http import HttpResponse
from django.views import View



class MyView(View):
    def get(self, request, *args, **kwargs):
        message = request.GET["message"]
        return HttpResponse(message)
    #http://localhost:8000/mine/?message=message%20params%20here

    def post(self, request):
        return HttpResponse(request)
    
    def update(self, request):
        return HttpResponse("update method ")
    
    def delete(self, request):
        return HttpResponse(request)