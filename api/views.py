from django.http.response import JsonResponse
from django.views.generic import ListView

from todo.models import Todo

class ApiTodoLV(ListView):
    model = Todo
    # template_name = 

    # def get(self, request, *args, **kwargs):
    #     tmpList = [
    #         {'id': 1, 'name': '박준영', 'todo': 'Django, vue.js활용한 코딩'}
    #     ]
    #     return JsonResponse(data=tmpList, safe=False)

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())
        return JsonResponse(data=todoList, safe=False)