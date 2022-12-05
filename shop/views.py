from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Purchase



def list_item(request):
    item_list = Item.objects.all()
    contex = {
        'item_list': item_list,
    }
    return render(request, 'list_item.html', contex)


def detail_item(request, id):
    item = get_object_or_404(Item, id=id)
    contex = {
        'item': item,
    }

    return render(request, 'detail_item.html', contex)


def result(request, id):
    item = get_object_or_404(Item, id=id)
    contex = {
        'item': item,
    }

    return render(request, 'result.html', contex)


def vote(request, id):
    item = get_object_or_404(Item, id=id)
    selected_purchase= request.POST.get('purchase')
    purchase = get_object_or_404(Purchase, id = selected_purchase, item=item)
    purchase.votes += 1
    purchase.save()

    return HttpResponseRedirect(reverse('result', args=(item.id,)))

