import datetime
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from forms import NameForm

#tao class route thong qua view cua django
#goi ham get tra so tuoi x 2
#them param vao method get or post va verify


def getTime(request):
    # if this is a POST request we need to process the form data
    if request.method == "GET":
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
      now = datetime.datetime.now()
    template = f"""
        <html>
            <body>day la get method.
            </body>
        </html>
    """

    # if a GET (or any other method) we'll create a blank form

    return HttpResponse(template)


def getPost(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
    # if a GET (or any other method) we'll create a blank form
      template = "day la post method"
    # if a GET (or any other method) we'll create a blank form
    return HttpResponse(template)





