from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.
def index(request):
    # return HttpResponse("my_to_do_app first page")
    # return render(request, 'my_to_do_app/index.html')
    todos = Todo.objects.all();
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content);

def createTodo(request):
    user_input_str = request.POST['todoContent'];
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    # return HttpResponse('createTodo를 할거야'+user_input_str)
    return HttpResponseRedirect(reverse('index'));

def deleteTodo(request):
    delete_todo_id = request.GET['todoNum']
    print("제거할 todo의 id", delete_todo_id)
    todo = Todo.objects.get(id = delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))


def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
