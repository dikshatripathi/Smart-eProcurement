from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.Press_Release import Press
from .models.tender import Tender
from .models.Bidder import User
from .models.filetender import etender
from .models.administration import administrater
from django.contrib.auth.hashers import make_password, check_password

tEN = Tender.get_all_Tender()
error = None
User_Count = User.objects.all()
Etdr = etender.objects.all()
Etdrs = etender


# Create your views here.
def index(request):
    PR=Press.get_all_Press();

    return render(request,'index.html' ,{'Press':PR , 'Tendr':tEN}  )

def Uindex(request):
    PR=Press.get_all_Press();

    return render(request,'U.index.html' ,{'Press':PR , 'Tendr':tEN}  )

def filetender(request):
    if request.method == 'GET':
        return render(request,'filetender.html')
    elif request.method == 'POST':
        Biddername = request.POST.get('Biddername')
        Bid_ID = request.POST.get('Bid_ID')
        Bid_Type = request.POST.get('Bid_Type')
        Bid_Category = request.POST.get('Bid_Category')
        Total_Projects_Worked = request.POST.get('Total_Projects_Worked')
        Total_Success_Projects = request.POST.get('Total_Success_Projects')
        Org_size = request.POST.get('Organization_size')
        Org_est = request.POST.get('orgy')
        Value_of_Last_Project = request.POST.get('Value_of_Last_Project')
        Proposed_Cost_of_Project = request.POST.get('Proposed_Cost_of_Project')

        etender2 = etender(
            Biddername = Biddername,
            Bid_ID = Bid_ID,
            Bid_Type = Bid_Type,
            Bid_Category = Bid_Category,
            Total_Projects_Worked = Total_Projects_Worked,
            Total_Success_Projects = Total_Success_Projects,
            Value_of_Last_Project = Value_of_Last_Project,
            Proposed_Cost_of_Project = Proposed_Cost_of_Project
            )

        etender2.save()
        l= 'Successfully Submitted'
        return render(request, 'filetender.html', {'Success' : l})



def about(request):
    return render(request, 'about.html')

def AdminShowUser(request):
    return render(request, 'AdminShowUser.html', {'User_Count': User_Count})

def AdminReq(request):

    return render(request, 'AdminReq.html', {'Tender':tEN} )

def AdminAddReq(request):
    if request.method == 'GET':
        return render(request, 'AdminAddReq.html' )
    elif request.method == 'POST':
        Subject = request.POST.get('Subject')
        Reference_Number = request.POST.get('Reference_Number')
        Identification_No = request.POST.get('Identification_No')
        Budget = request.POST.get('Budget')
        Time_Duration = request.POST.get('Time_Duration')
        EMD = request.POST.get('EMD')
        Eligible_Class = request.POST.get('Eligible_Class')

        Tender_Show = Tender(
        Subject = Subject,
        Reference_Number = Reference_Number,
        Identification_No = Identification_No,
        Budget = Budget,
        Time_Duration = Time_Duration,
        EMD = EMD,
        Eligible_Class = Eligible_Class)

        Tender_Show.save()
        return render(request, 'AdminAddReq.html')




def adminlogin(request):
    if request.method == 'GET':
        return render(request, 'adminlogin.html')
    elif request.method == 'POST':
        AEmail = request.POST.get('AEmail')
        APassword = request.POST.get('APassword')

        Administrater = administrater.get_user_by_email(AEmail)
        if Administrater:

            if (Administrater.APassword == administrater.APassword):
                return redirect('U.index')
            else:
                error = 'Invalid Password'
                return render(request, 'adminlogin.html', {'error': error})

        else:
            error = 'Invalid Email'
        print(error)
        return render(request, 'A_index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')

        user= User.get_user_by_email(Email)
        if user:
            flag = check_password(Password, user.Password)
            if flag:
                return redirect('U.index')
            else:
                error = 'Invalid Password'
                return render(request, 'login.html', {'error':error})

        else:
            error = 'Invalid Email'
        print(error)
        return render(request, 'login.html', {'error':error})

    elif request.method == 'put':
        return render(request, 'U.base.html')

def adminsignup(request):
    if request.method == 'GET':
        return render(request, 'adminsignup.html')
    elif request.method == 'POST':
        AName = request.POST.get('AName')
        AUID = request.POST.get('AUID')
        AEmail = request.POST.get('AEmail')
        APassword = request.POST.get('APassword')
        AMobile = request.POST.get('AMobile')

        Aemailerror = None

        x = administrater.isExists(AEmail)
        if (x):
            Aemailerror = 'Email already Registered'
            print(Aemailerror)

        if not Aemailerror:
            Administrater = administrater(
            AName = AName,
            AUID = AUID,
            AEmail = AEmail,
            APassword = APassword,
            AMobile = AMobile)


        Administrater.save()


        return render(request, 'adminlogin.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Bidder_Mobile = request.POST.get('Bidder_Mobile')
        Password = request.POST.get('Password')
        Company_Name = request.POST.get('Company_Name')
        Registration_Number = request.POST.get('Registration_Number')
        Registered_Address = request.POST.get('Registered_Address')
        Partners_or_Directors = request.POST.get('Partners_or_Directors')
        City = request.POST.get('City')
        State = request.POST.get('State')
        Postal_Code = request.POST.get('Postal_Code')
        PAN_TAN_Number = request.POST.get('PAN_TAN_Number')
        Estd_Year = request.POST.get('Estd_Year')
        Nature_of_Business = request.POST.get('Nature_of_Business')
        Legel_Status = request.POST.get('Legel_Status')

        emailerror = None

        x= User.isExists(Email)
        if (x):
            emailerror = 'Email already Registered'
            print(emailerror)

        if not emailerror:
            user = User(
                Name=Name,
                Email =  Email,
                Bidder_Mobile=Bidder_Mobile,
                Password= make_password(Password),
                Company_Name=Company_Name,
                Registration_Number=Registration_Number,
                Registered_Address=Registered_Address,
                Partners_or_Directors=Partners_or_Directors,
                City=City,
                State=State,
                Postal_Code=Postal_Code,
                PAN_TAN_Number=PAN_TAN_Number,
                Estd_Year=Estd_Year,
                Nature_of_Business=Nature_of_Business,
                Legel_Status=Legel_Status

            )

            print("Running")
            user.save()
            return redirect('login')

        else:
            return render(request, 'signup.html', {'emailerror': emailerror})



def activetender(request):
    return render(request, 'activetender.html', {'Tender':tEN})

def cancelledtender(request):
    return render(request, 'cancelledtender.html')

def recruitment(request):
    return render(request, 'recruitment.html')

def circular(request):
    return render(request, 'circular.html')

def events(request):
    return render(request, 'events.html')

def contactus(request):
    return render(request, 'contactus.html')

def media(request):
    return render(request, 'media.html')
t=0
def Compare_Bids(request):

    if request.method == 'GET':
        return render(request,'Compare_Bids.html' , {'Etendr':Etdr} )
    elif request.method == 'POST':
        sel = int(request.POST.get('sel'))
        t=sel
        print(t)
        if (t == 1):
            print("if........")
            k = Etdrs.objects.all().order_by('Proposed_Cost_of_Project', '-Total_Projects_Worked',
                                             '-Total_Success_Projects', '-Value_of_Last_Project')
        elif (t == 0):
            print("else")

            k = Etdrs.objects.all().order_by('Proposed_Cost_of_Project')
        #print(k).
        if (t == 1):
            print("if........")
            k = Etdrs.objects.all().order_by('Proposed_Cost_of_Project', '-Total_Projects_Worked',
                                             '-Total_Success_Projects', '-Value_of_Last_Project')
        elif (t == 0):
            print("else")

            k = Etdrs.objects.all().order_by('Proposed_Cost_of_Project')
        print(k)
        return render(request, 'Compare_Bids.html',{'Etendr':k})
'''
if
l1=etdr.objects.all().order_by('Proposed_Cost_of_Project').values()
print(l1)
print('\n\nQCBS\n\n')

QCBS=etender.objects.all().order_by('Organization_established_Year','Proposed_Cost_of_Project','-Total_Projects_Worked','-Total_Success_Projects','-Value_of_Last_Project').values()
print(QCBS)

'''
