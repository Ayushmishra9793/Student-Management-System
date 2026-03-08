from django.shortcuts import render, redirect
from student.models import Student                                   # student app se model le ker aao "Student" name ka 
# Create your views here.


# READ :-

def student_home(request):
    
    students_data = Student.objects.all()                                                            # students_data => variable , Student => models, now database se value aygi jo ki html me pass hogi
    print(students_data)                                                                                           # all the object from admin site (models object) it will fill in student_data variable , These are called Data Fetching   
    
    data ={
        "student_data": students_data             
    }
    
    
    return render(request, "student/student_home.html", data)                    # data => dictionary which render the data in html


    


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
            
            Student.objects.create(
                name = student_name,
                email = student_email,
                phone_number =student_phone_number
                
            )
            
            return redirect("student_home")
        return render(request, "student/add_student.html")


# NOTE :
    # first check is this request is POST, if yes then......
    # student_name => isme input ki value store ho rhi hai
    # jab hum request ker rhe POST(submit) ki to get ho jay( name attributes wala input)
    
    # MOST IMPORTANT :- add token after the form tag in html  

    # NOW next step:-   put the input data in data base (admin) 
    
            # Student.objects.create() => Student (model) -> create objects
            # name,email,phone_number => models
            # student_name, student_email, student_phone_number => input value jo uper store hui hai
            
            