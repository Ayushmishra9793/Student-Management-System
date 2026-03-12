from django.shortcuts import render, redirect
from django.contrib import messages
from student.models import Student                                   # student app se model le ker aao "Student" name ka 
# Create your views here.


# READ :-

def student_home(request):
    
    students_data = Student.objects.all()                                                            # students_data => variable , Student => models, now database se value aygi jo ki html me pass hogi
                                                                                             # all the object from admin site (models object) it will fill in student_data variable , These are called Data Fetching , also called query set  
    
    data ={
        "student_data": students_data             
    }
    
    # "student_data" => key -> variable , = students_data => value -> variables where all the model stored
    
    
    return render(request, "student/student_home.html", data)                    # data => only dictionary which render the data in html


    


# NOTE:
    #  data ={
        # "name" : "Shree ji",                                                    # name => varible-> key ,  shreeji => value 
        # "email" : "shreeji@gmail.com",                                           # name key hai ise exact html me likhna hota hai
    # }
    
    
    
# CREATE : -


def add_student(request):                                                  #  by default yaha request (Get) hai -> ye html page de dega
    
        if request.method == "POST" :
            student_name = request.POST.get("input_name")
            student_email = request.POST.get("input_email")
            student_phone_number = request.POST.get("input_phone_number")
            student_profile_image = request.FILES.get("input_profile")       # user to upload a profile picture, Handle request.FILES in views.py
            
            Student.objects.create(
                name = student_name,
                email = student_email,
                phone_number =student_phone_number,
                student_profile = student_profile_image
                
            )
            
            messages.success(request, "Student Added Successfully ✅")
            
            return redirect("student_home")                          # form karte hi condition break and submit directly student_home page
                                                                    # student_home search karega to urls.py me jayga waha name match karega usme std url dekhega fir function call hogi views karayga student_home fir waps views me ayga student_home view kra dega sare models ko webpage per
        return render(request, "student/add_student.html")


# NOTE :
    # first check is this request is POST, if yes then......
    # student_name => isme input ki value store ho rhi hai
    # jab hum request ker rhe POST(submit) ki to get ho jay( name attributes wala input)
    
    # MOST IMPORTANT :- add token after the form tag in html  

    # NOW next step:-   put the input-data in database (admin/model) 
    
            # Student.objects.create() => Student (model) -> create objects
            # name,email,phone_number => models.py me ja ke dekh lo 
            # student_name, student_email, student_phone_number => input value jo uper store hui hai


# DELETE :


           
def delete_student(request, student_id):
     
    my_student= Student.objects.get(id = student_id)       # model ke object se id laao aur check kro ye kya student_id ke equal hai, then delete it
    
    my_student.delete()
    
    messages.error(request, "Student Deleted Successfully ❌")

    return redirect('student_home')

# UPDATE :

def update_student(request, student_id):
    student = Student.objects.get(id = student_id)
    
    if request.method =="POST":
        
        student.name =request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone_number = request.POST.get("phone")    # student.email => student = jo uper variable hai , email = model ; yaha update ka kam ho rha hai 
        if request.FILES.get("student_profile"):
            student.student_profile = request.FILES.get("student_profile")
            
        student.save()
        
        messages.success(request, "Student Updated Successfully ✅")
        
        
        return redirect('student_home')    
    
    parameters={
        "student" : student
    }
    
    return render(request, "student/update_student.html", parameters)