from django.views import View
from django.shortcuts import render


# Create your views here.

class TodoView(View):
    def get(self, request):
        return render(request, 'Todo_list/todo.html')

    def post(self, request):
        pass
