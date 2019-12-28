from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

from difflib import HtmlDiff


# Create your views here.
@api_view(["POST"])
def api(request):
    form_data = request.data
    before_text = form_data['before'].split('\r')
    after_text = form_data['after'].split('\r')
    return HttpResponse(HtmlDiff().make_file(before_text, after_text))


@api_view(["Get"])
def form(request):
    return render(request, 'form.html')
