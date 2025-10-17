from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from mybook.forms import BookForm,BookUpdateForm,SignupForm,SignInForm

from mybook.models import Book

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.models import User

from django.db.models import Q



# Create your views here.

class BookView(View):
    
    template_name="book.html"
    
    form_class=BookForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data,files=request.FILES)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            print(data)
            
            Book.objects.create(**data)
            
            return redirect("book_list")
            
        return render(request,self.template_name,{"form":form_instance})
        
class BookListView(View):
    
    template_name="book_list.html"
    
    def get(self,request,*args,**kwargs):
        
        search_text=request.GET.get("filter")
        
        qs=Book.objects.all()
        
        if search_text:
            
            qs=qs.filter(
                
                 Q(name__contains=search_text)|Q(author__contains=search_text)|Q(category__contains=search_text)
            )
        
        return render(request,self.template_name,{"data":qs})


class BookDetailView(View):
    
    template_name="book_detail.html"
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        qs=Book.objects.get(id=id)
        
        return render(request,self.template_name,{"data":qs})
    
class BookDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        Book.objects.get(id=id).delete()
        
        return redirect("book_list")

class BookUpdateView(View):
    
    template_name="book_update.html"
    
    form_class=BookUpdateForm
    
    def get(self,request,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        book_object=get_object_or_404(Book,id=id)
        
        form_instance=self.form_class(instance=book_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,requset,*args,**kwargs):
        
        id=kwargs.get("pk")
        
        book_object=get_object_or_404(Book,id=id)
        
        form_data=requset.POST
        
        form_instance=self.form_class(form_data,requset.FILES,instance=book_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("book_list")
        
        return render(requset,self.template_name,{"form":form_instance})
    
class SignupView(View):
    
    template_name="register.html"
    
    form_class=SignupForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            User.objects.create_user(**data)
            
            return redirect("book_list")
        
        return render(request,self.template_name,{"form":form_instance})
    
class SignInView(View):
    
    template_name="signin.html"
    
    form_class=SignInForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance=self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data=request.POST
        
        form_instance=self.form_class(form_data)
        
        if form_instance.is_valid():
            
            data=form_instance.cleaned_data
            
            uname=data.get("username")
            
            pwd=data.get("password")
            
            user_object=authenticate(request,username=uname,password=pwd)
            
            if user_object:
                
                login(request,user_object)
                
                return redirect("book_list")
            
            return render(request,self.template_name,{"form":form_instance})
        
        
class SignOutView(View):
    
    def get(self,request,*args,**kwargs):
        
        logout(request)
          
        return redirect("signin")