from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView

# views.py
import csv
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from .models import CompanyData


# Create your views here.


def index(request):
    # my_dict = {"insert_me": "I am from views.py contex"}
    return render(request, 'login.html')


def home(request):
    # my_dict = {"insert_me": "I am from views.py contex"}
    return render(request, 'home.html')

def logout(request):
    print("Logout called")
    # logout(request)
    # Redirect to the logout page
    return render(request, 'login.html')



@csrf_exempt
def login_api(request):
    print("login_api called...")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return JsonResponse({'status': 'success'})
            return JsonResponse({'status': 'success', 'redirect_url': 'home'})  # Redirect URL to the user page
        else:
            return JsonResponse({'status': 'success', 'redirect_url': 'home'})  # Redirect URL to the user page
            # return JsonResponse({'status': 'success'})
            # return JsonResponse({'status': 'fail', 'message': 'Invalid credentials'}, status=400)
    return JsonResponse({'status': 'fail', 'message': 'Only POST method is allowed'}, status=405)


def user_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return JsonResponse({'status': 'fail', 'message': 'User already exist'}, status=412)

        User.objects.create(username=username,email=email)
        return JsonResponse({'status': 'success', 'msg': 'user added successfully'},status=201)  # Redirect URL to the user page
    

# def logout(request):
#     if request.method == 'POST':
#         return JsonResponse({'status': 'success', 'redirect_url': ''})  # Redirect URL to the user page



class LogoutPageView(TemplateView):
    print("Logout called")
    template_name = 'login.html'


# class GetUsers(TemplateView):
#     print("Logout called")
#     template_name = 'user.html'

def get_users(request):
    template_name = 'user.html'
    # Run your query
    results = User.objects.all()
    # Prepare data for the template
    context = {
        'results': results
    }
    
    return render(request, template_name, context)


class QueryBuilder(TemplateView):
    print("Logout called")
    template_name = 'query_build.html'


class Upload(TemplateView):
    print("Logout called")
    template_name = 'home.html'



@csrf_exempt
def upload_chunk(request):
    file = request.FILES['file']
    filename = request.POST['filename'] 
    #"companies_sorted.csv"
    chunk_number = int(request.POST['chunk_number'])
    total_chunks = int(request.POST['total_chunks'])
    print(filename)    
    # Save chunk
    file_path = filename # os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
    
    with open(file_path, 'ab') as f:
        f.write(file.read())

    if chunk_number == total_chunks:
        process_file(file_path)
        # Process the file when all chunks are uploaded
        os.remove(file_path)
        return JsonResponse({'message': 'File upload and processing complete'}, status=201)
    return JsonResponse({'message': 'Chunk uploaded successfully'}, status=200)



def process_file(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                CompanyData.objects.create(
                    keyword=row.get('keyword'),
                    name=row.get('name'),
                    domain=row.get('domain'),
                    industry=row.get('industry'),
                    year_founded=row.get('year_founded'),
                    locality=row.get('locality'),
                    size_range=row.get('size_range'),
                    city=row.get('city'),
                    state=row.get('state'),
                    country=row.get('country'),
                    linked_url=row.get('linked_url'),
                    current_emplyee_estimate=row.get('current_emplyee_estimate'),
                    total_emplyee_estimate=row.get('total_emplyee_estimate')
                )
    except Exception as e:
        print(e)


# @csrf_exempt
# def upload_chunk(request):
#     if request.method == 'POST':
#         try:
#             # Get the chunk number and filename from the request
#             chunk_number = request.POST['chunk_number']
#             total_chunks = request.POST['total_chunks']
#             filename = request.POST['filename']

#             # Ensure directory exists
#             upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
#             os.makedirs(upload_dir, exist_ok=True)

#             # Save the chunk
#             chunk_file_path = os.path.join(upload_dir, f'{chunk_number}.part')
#             with open(chunk_file_path, 'wb') as chunk_file:
#                 for chunk in request.FILES['file'].chunks():
#                     chunk_file.write(chunk)

#             # If all chunks are uploaded, combine them into the final file
#             if int(chunk_number) == int(total_chunks) - 1:
#                 final_file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
#                 with open(final_file_path, 'wb') as final_file:
#                     for i in range(int(total_chunks)):
#                         chunk_file_path = os.path.join(upload_dir, f'{i}.part')
#                         with open(chunk_file_path, 'rb') as chunk_file:
#                             final_file.write(chunk_file.read())

#                 # Optionally, remove the chunk files and directory
#                 for i in range(int(total_chunks)):
#                     os.remove(os.path.join(upload_dir, f'{i}.part'))
#                 os.rmdir(upload_dir)

#             return JsonResponse({'message': 'Chunk uploaded successfully.'})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method.'}, status=405)