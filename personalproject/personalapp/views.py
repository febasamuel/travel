from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# import operator

# # Create your views here.
# def home(request):
#     return render(request, "index.html")

def demo(request):
        obj = Place.objects.all()
        obj1 = Team.objects.all()
        return render(request, "index.html", {'result': obj, 'result1': obj1})

# def home(request):
#
#         return render(request, "index.html", {'result1': obj})

# def addition(request):
#     x = int(request.GET.get('num1'))
#     y = int(request.GET.get('num2'))
#     res1 = x+y
#     res2 = x - y
#     res3 = x * y
#     res4 = x / y
#     return render(request, "result.html", {'result1': res1, 'result2': res2, 'result3': res3, 'result4':res4})












# # def contact(request):
# #     return HttpResponse("i am contact")
# #
# # def detail(request):
# #     return render(request, "detail.html")
# #
# # def thanks(request):
# #     return HttpResponse("i am thanks page")
