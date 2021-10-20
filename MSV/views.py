from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from MSV.forms import ProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from MSV.models import Templates, Video, UserProfile


def Home(request):
    return render(request, "home.html")


def Aboutus(request):
    return render(request, "aboutus.html")


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def Logout(request):
    auth.logout(request)
    return redirect('/YFI/login/')


def Register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('user created')
                return redirect('/YFI/home/')
        else:
            messages.info(request, 'password not matching')
            return render(request, "Register.html")
        return redirect('/')
    else:
        return render(request, 'Register.html')


@login_required(login_url="/YFI/login/")
def Profile(request):
    return render(request, "profile.html")


@login_required(login_url="/YFI/login/")
def UpdateProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            p_image = request.user.userprofile.image
            print(p_image)
            u_form.save()
            p_form.save()
            p_im = request.user.userprofile.image
            print(p_im)
            if p_im != p_image:
                p_image.url.delete(delete=True)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'update profile.html', {'u_form': u_form, 'p_form': p_form})


def Temp(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Templates.objects.filter(Q(category__icontains=srch) | Q(description__icontains=srch))
            if match:
                temp = Templates.objects.all()
                return render(request, 'templates.html', {'sr': match, 'temp': temp})
            else:
                messages.error(request, 'No result found')
        else:
            return render('/YFI/templates/')
    temp = Templates.objects.all()
    return render(request, 'templates.html', {'temp': temp})


def Search(request):
    if request.method == "POST":
        che = request.POST['che']
        if che == 'Video':
            srch = request.POST['srh']
            if srch:
                match = Video.objects.filter(Q(category__icontains=srch) | Q(description__icontains=srch))
                if match:
                    temp = Video.objects.all()
                    return render(request, 'videos.html', {'sr': match, 'temp': temp})
                else:
                    messages.error(request, 'No ' + srch + ' video found')
        else:
            if request.method == "POST":
                che = request.POST['che']
                if che == 'Template':
                    srch = request.POST['srh']
                    if srch:
                        match = Templates.objects.filter(Q(category__icontains=srch) | Q(description__icontains=srch))
                        if match:
                            temp = Templates.objects.all()
                            return render(request, 'templates.html', {'sr': match, 'temp': temp})
                        else:
                            if (srch == 'all') or (srch == 'All'):
                                return redirect('/YFI/all/')
                            else:
                                messages.error(request, 'No ' + srch + ' template found')
    return render(request, 'master.html')


def Celebrity(request):
    cat = 'celebrity'
    temp = Templates.objects.filter(Q(category__icontains=cat))
    return render(request, 'templates.html', {'temp': temp, 'cat': cat})


def Popular(request):
    cat = 'Popular'
    temp = Templates.objects.filter(Q(category__icontains=cat))
    return render(request, 'templates.html', {'temp': temp, 'cat': cat})


def Web_series(request):
    cat = 'Web series'
    temp = Templates.objects.filter(Q(category__icontains=cat))
    return render(request, 'templates.html', {'temp': temp, 'cat': cat})


def Cartoon(request):
    cat = 'Cartoon'
    temp = Templates.objects.filter(Q(category__icontains=cat))
    return render(request, 'templates.html', {'temp': temp, 'cat': cat})


def Anime(request):
    cat = 'Anime'
    temp = Templates.objects.filter(Q(category__icontains=cat))
    return render(request, 'templates.html', {'temp': temp, 'cat': cat})


def New(request):
    cat = 'New'
    temp = Templates.objects.filter(Q(category__icontains=cat))
    return render(request, 'templates.html', {'temp': temp, 'cat': cat})


def Random(request):
    cat = 'Random'
    temp = Templates.objects.filter(Q(category__icontains=cat))
    return render(request, 'templates.html', {'temp': temp, 'cat': cat})


def All(request):
    temp = Templates.objects.all()
    return render(request, 'templates.html', {'temp': temp})


def Videos(request):
    if request.method == 'POST':
        srch = request.POST['srh']
        if srch:
            match = Video.objects.filter(Q(category__icontains=srch) | Q(description__icontains=srch))
            if match:
                temp = Video.objects.all()
                return render(request, 'videos.html', {'sr': match, 'temp': temp})
            else:
                messages.error(request, 'No result found')
        else:
            return render('/YFI/videos/')
    temp = Video.objects.all()
    return render(request, 'videos.html', {'temp': temp})


def v_Celebrity(request):
    cat = 'celebrity'
    temp = Video.objects.filter(Q(category__icontains=cat))
    return render(request, 'videos.html', {'temp': temp, 'cat': cat})


def v_Popular(request):
    cat = 'Popular'
    temp = Video.objects.filter(Q(category__icontains=cat))
    return render(request, 'videos.html', {'temp': temp, 'cat': cat})


def v_Web_series(request):
    cat = 'Web series'
    temp = Video.objects.filter(Q(category__icontains=cat))
    return render(request, 'videos.html', {'temp': temp, 'cat': cat})


def v_Funny(request):
    cat = 'Funny'
    temp = Video.objects.filter(Q(category__icontains=cat))
    return render(request, 'videos.html', {'temp': temp, 'cat': cat})


def v_Abusive(request):
    cat = 'Abusive'
    temp = Video.objects.filter(Q(category__icontains=cat))
    return render(request, 'videos.html', {'temp': temp, 'cat': cat})


def v_New(request):
    cat = 'New'
    temp = Video.objects.filter(Q(category__icontains=cat))
    return render(request, 'videos.html', {'temp': temp, 'cat': cat})


def v_Random(request):
    cat = 'Random'
    temp = Video.objects.filter(Q(category__icontains=cat))
    return render(request, 'videos.html', {'temp': temp, 'cat': cat})


def v_All(request):
    temp = Video.objects.all()
    return render(request, 'videos.html', {'temp': temp})


def vserch(request):
    import SpeechRecognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('speak :')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('you said :{}'.format(text))
        except:
            print('sorry, could not recognize your voice')


'''
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request,'change_password.html')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
'''
