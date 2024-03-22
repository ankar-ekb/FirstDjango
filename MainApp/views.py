from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

userdata = {
    "name": "Иван",
    "middle": "Petrovich",
    "surname": "Ivanov",
    "phone": "8-56-5345-4-53",
    "email": "vasya@mail.ru"

}

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]



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
    result = f"""
        Имя: <b>{userdata["name"]}</b><br>
        Отчество: <b>{userdata["middle"]}</b><br>
        Фамилия: <b>{userdata["surname"]}</b><br>
        Телефон: <b>{userdata["phone"]}</b><br>
        email: <b>{userdata["email"]}</b><br>
        """
    return HttpResponse(result)

def get_item(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                "item": item
            }
            return render(request, "items.html", context)
        
    return HttpResponseNotFound(f'<h1>Товар c id = {id} не найден</h1>')

def items_list(request):
    # result = "<h2>Goods list</h2><ol>"
    # for item in items:
    #     result += f"<li><a href='/item/{item['id']}'>{item['name']}</a></li>"
    # result += '</ol>'
    # return HttpResponse(result)
    context = {
        "items": items
    }
    return render(request, "items-list.html", context)