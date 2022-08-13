from unicodedata import name
from django.shortcuts import render
from .models import IceCream
# Create your views here.



def get_ice_cream(request,ice_cream_id,):
    iceCream = IceCream.objects.get(id=ice_cream_id)
    context ={
        "IceCream":{
            "id":ice_cream_id,
            "name":iceCream.name,
            "shop":iceCream.shop,
            "stock":iceCream.stock,

        }


    }

    return render(request, "ice_cream_detail.html",context)


def get_ice_creams(request):
    iceCreams = IceCream.objects.all()
    context = {
        "IceCreams": iceCreams
    }
    return render(request, "ice_cream_list.html", context)