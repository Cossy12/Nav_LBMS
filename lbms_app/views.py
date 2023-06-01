from . forms import IssueBookForm, bookupdateform, returnupdateform
from django.shortcuts import redirect, render,HttpResponse
from .models import *
from . forms import IssueBookForm
from django.contrib.auth import authenticate, login, logout
from . import forms, models
from datetime import date
from django.contrib.auth.decorators import login_required

def index(request):
    books = Book.objects.all()
    return render(request, "index.html", {'books':books})

@login_required(login_url = '/admin_login')
def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
        price = request.POST['price']

        books = Book.objects.create(name=name, author=author, isbn=isbn, category=category,price=price)
        books.save()
        alert = True
        return render(request, "add_book.html", {'alert':alert})
    return render(request, "add_book.html")


def bookupdate(request,id):
	update = Book.objects.get(id=id)

	if request.method == 'POST':
		form = bookupdateform(request.POST,request.FILES,instance=update)

		if form.is_valid():
				form.save()
				return redirect("/") 
	else:
		form = bookupdateform(instance=update)
		return render(request, 'bookupdate.html', {'form': form})





@login_required(login_url = '/admin_login')
def view_books(request):
    books = Book.objects.all()
    return render(request, "view_books.html", {'books':books})

@login_required(login_url = '/admin_login')
def view____books(request):
    books = Book.objects.all()
    return render(request, "view____books.html", {'books':books})




@login_required(login_url = '/admin_login')
def view_students(request):
    students = Student.objects.all()
    return render(request, "view_students.html", {'students':students})

@login_required(login_url = '/admin_login')
def issue_book(request):
    form = forms.IssueBookForm()
    # student = Student.objects.filter(user_id=request.user.id)
    # issuedBooks = IssuedBook.objects.filter(student_id=student[0].user_id)
    # li1 = []

    # for i in issuedBooks:
    #     books = Book.objects.filter(isbn=i.isbn)
    #     for book in books:
    #         t=(request.user.id, request.user.get_full_name, book.name,book.author,book.price)
    #         li1.append(t)
    #     total=+book.price
    #     print("Total is", total)

    #     if total <= 500:
    if request.method == "POST":
        form = forms.IssueBookForm(request.POST)
        if form.is_valid():
            obj = models.IssuedBook()
            obj.student_id = request.POST['name2']
            obj.isbn = request.POST['isbn2']
            obj.save()
            alert = True
            
            return render(request, "issue_book.html", {'obj':obj, 'alert':alert})
    return render(request, "issue_book.html", {'form':form})


@login_required(login_url = '/admin_login')
def return_book(request,id):
    update = IssuedBook.objects.get(pk=id)

    if request.method == 'POST':
        form = returnupdateform(request.POST,request.FILES,instance=update)

        if form.is_valid():
                form.save()
                return redirect("/")
    else:
        form = returnupdateform(instance=update)
        return render(request, 'return_book.html', {'form': form})



@login_required(login_url = '/admin_login')
def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(models.Book.objects.filter(isbn=i.isbn))
        students = list(models.Student.objects.filter(user=i.student_id))
        i=0
        for l in books:
            t=(students[i].user,students[i].user_id,books[i].name,books[i].isbn,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,books[i].price,issuedBooks[0].pk,issuedBooks[0].book_return)
            i=i+1
            details.append(t)
    return render(request, "view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})







@login_required(login_url = '/student_login')
def student_issued_books(request):
    student = Student.objects.filter(user_id=request.user.id)
    issuedBooks = IssuedBook.objects.filter(student_id=student[0].user_id)
    li1 = []
    li2 = []

    for i in issuedBooks:
        books = Book.objects.filter(isbn=i.isbn)
        for book in books:
            t=(request.user.id, request.user.get_full_name, book.name,book.author,book.price)
            li1.append(t)
            totals  = 0
            totals += 500
            total = totals

        days=(date.today()-i.issued_date)
        d=days.days
        fine=100
        if d>15:
            day=d-14
            fine=day*5
        t=(issuedBooks[0].issued_date, issuedBooks[0].expiry_date, fine)
        li2.append(t)


    return render(request,'student_issued_books.html',{'li1':li1, 'li2':li2,'total':total})





def delete_book(request, myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("/view_books")

def delete_student(request, myid):
    students = Student.objects.filter(id=myid)
    students.delete()
    return redirect("/view_students")



def student_registration(request):
    if request.method == "POST":
        username = request.POST['username']

        email = request.POST['email']
        branch = request.POST['branch']
        classroom = request.POST['classroom']
        roll_no = request.POST['roll_no']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            passnotmatch = True
            return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password,)
        student = Student.objects.create(user=user, branch=branch, classroom=classroom,roll_no=roll_no, )
        user.save()
        student.save()
        alert = True
        return render(request, "/", {'alert':alert})
    return render(request, "student_registration.html")

def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("/")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/add_book")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")

def Logout(request):
    logout(request)
    return redirect ("/")