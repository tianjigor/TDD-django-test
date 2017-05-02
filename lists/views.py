from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')

    # return render_to_response('home.html')

    # return render(request, 'home.html', {
    #     'new_item_text': request.POST['item_text'],
    # })

    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })