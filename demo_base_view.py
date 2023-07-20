import json
from django.http import HttpResponse
from django.views import View
from Test_project import DemoMiddleware
from products.models import Person




class MyView(View):
    def get(self, request, *args, **kwargs):
        message = request.GET["message"]
        return HttpResponse(message)
    #http://localhost:8000/mine/?message=message%20params%20here

    def post(self, request):
        #DemoMiddleware.xuly(request)
        data = request.body.decode('utf-8')
        body = json.loads(data)
        title = body['title']
        slug = body['slug']
        content = body['content']
        person = Person()
        person.itle = title
        person.slug = slug
        person.content = content
        person.save()
        return HttpResponse(request)
    
    def update(self, request):
        return HttpResponse("update method ")
    
    def delete(self, request):
        return HttpResponse(request)