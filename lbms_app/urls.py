from django.urls import path
from . import views

app_name = "lbms_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("view_books___/", views.view____books, name="view____books"),
    path("view_students/", views.view_students, name="view_students"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    path("student_issued_books/", views.student_issued_books, name="student_issued_books"),
    path("student_registration/", views.student_registration, name="student_registration"),
    path("student_login/", views.student_login, name="student_login"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),
    path("edit_book/<int:id>/", views.bookupdate, name="bookupdate"),
    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("delete_student/<int:myid>/", views.delete_student, name="delete_student"),
    path("return_book/<int:id>", views.return_book, name="return_book"),

]