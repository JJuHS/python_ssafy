from django.shortcuts import render

# Create your views here.
def todos(request):
    return render(request, 'todos.html')

def create_todo_view(request):
    return render(request, 'todos/create_todo.html')