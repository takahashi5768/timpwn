from django.http import JsonResponse
from .models import Profile
# Create your views here.

def get_(request):
    
    #Getting Data from users
    if request.method == "GET":
        
        #check if we get the required GET data else return an invalid data response
        try:
            email = request.GET['email']
            password = request.GET['password']
        except:
            out = {
                "response" : "Invalid Data"
            }
            return JsonResponse(out)
        
    elif request.method == "POST":
        
        #check if we get the required POST data else return an invalid data response
        try:
            email = request.GET['email']
            password = request.GET['password']
        except:
            out = {
                "response" : "Invalid Data"
            }
            return JsonResponse(out)
        
    #Default output
    out = {}
        
    #Checking if the profile exists if it does then reponding with the data else responding with invalid data
    try:
        obj = Profile.objects.get(email=email,password=password)
        
        out = {
            "first_name": obj.first_name,
            "last_name": obj.last_name,
            "phone": obj.phone,
            "email_address": obj.email,
            "dob": obj.date_of_birth,
            "bio": obj.bio,
            "verification_question_and_answer": obj.verification_question
        }  
    except:
        out = {
            "response" : "Invalid Data"
        }
        
        return JsonResponse(out)
    
    return JsonResponse({"response" : out})

def put_(request):
    
    #Getting Data from get requests
    if request.method == "GET":
    
        email = request.GET['email']
        password = request.GET['password']
        first_name = request.GET['first_name']
        last_name = request.GET['last_name']
        phone = request.GET['phone']
        bio = request.GET['bio']
        verification_question = request.GET['verification_question']
        date_of_birth = request.GET['date_of_birth']
        
    #Getting Data from post requests
    elif request.method == "POST":
    
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        bio = request.POST['bio']
        verification_question = request.POST['verification_question']
        date_of_birth = request.POST['date_of_birth']

    Profile(
            first_name=first_name,last_name=last_name,phone=phone,email=email,password=password,bio=bio,
            verification_question=verification_question,
            date_of_birth=date_of_birth
        ).save()
    
    return JsonResponse({"response" : "Success"})
