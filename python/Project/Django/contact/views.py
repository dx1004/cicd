from django.shortcuts import render

# Create your views here.
def contact(request):
    context = {}
    if request.method == 'POST':
        context = {
            'name' : request.POST.get('name', ''),
            'email' : request.POST.get('email', ''),
            'phone' : request.POST.get('phone', ''),
            'subject' : request.POST.get('subject', ''),
            'message' : request.POST.get('message', '').upper()
        }      
    return render(request, 'form.html', context)
    