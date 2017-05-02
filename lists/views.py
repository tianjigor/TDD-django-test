from django.shortcuts import render
from lists.models import Item
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    #
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text', ''),
    # })
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
    else:
        new_item_text=''

    return render(request, 'home.html', {
        'new_item_text': new_item_text,
    })