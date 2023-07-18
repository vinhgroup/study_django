from django.http import Http404


class DemoMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # BT: lay thong tin trong request ra
        
        response = self.get_response(request)

        age = request.headers['age']
        print(age)
        if int(age) < 5:
            raise Http404
        else:
            print("xxxxxxxxxxxx")
   
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        pass
