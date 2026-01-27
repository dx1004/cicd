from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    # Clear session when user comes from success page (new session)
    if request.GET.get('new_session') == '1':
        request.session.flush()
    
    context = {}
    if 'login' not in request.session:
        request.session['login'] = 0
        
    if request.method == 'POST':
        if request.POST.get('username') == "admin" and request.POST.get('password') == "1234":
            request.session['login'] = 0
            request.session['success'] = True
            return redirect('success') 
        else:
            request.session['login'] += 1
            context = {'error': "Invalid Credentials"}
    
    # Pass session values to context
    context['login'] = request.session.get('login', 0)
    context['success'] = request.session.get('success', False)
    
    # Clear success message after displaying it
    if request.session.get('success'):
        del request.session['success']
    
    return render(request, 'login.html', context)


def success(request):
    return render(request, 'success.html')
    