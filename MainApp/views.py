from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def home(request):
    # text = """<h1>"Изучаем django"</h1>
    #         <strong>Автор</strong>: <i>Иванов И.П.</i>"""
    # return HttpResponse(text)
    context = {
        "name": "Derp Johnson",
        "email": "qwerty@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    userdata = {
    "name": "Иван",
    "middle": "Petrovich",
    "surname": "Ivanov",
    "phone": "8-56-5345-4-53",
    "email": "vasya@mail.ru"

}
    result = f"""
        Имя: <b>{userdata["name"]}</b><br>
        Отчество: <b>{userdata["middle"]}</b><br>
        Фамилия: <b>{userdata["surname"]}</b><br>
        Телефон: <b>{userdata["phone"]}</b><br>
        email: <b>{userdata["email"]}</b><br>
        """
    return HttpResponse(result)

def get_item(request, id):
    try:
        item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар c id = {id} не найден')
    # items = Item.objects.all()
    # for item in items:
    #     if item.id == id:
    context = {
        "item": item
    }
    return render(request, "items.html", context)
        

def items_list(request):
    # result = "<h2>Goods list</h2><ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # result += '</ol>'
    # return HttpResponse(result)
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)