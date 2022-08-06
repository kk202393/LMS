from tkinter import TRUE
from tkinter.tix import LabelEntry
from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from LOAN.forms import *
from LOAN.forms import customerKYCform
from django.contrib import messages
from LOAN.models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Max


# Create your views here.


@login_required(login_url="")
def Region_field(request):
    fm = haed_officeform()
    if request.method == "POST":
        re = request.POST.get("Region")
        ce = request.POST.get("created_by")
        messages.success(request, "Region is created successfully")
        return redirect("/region_view")
    return render(request, "Region.html", {"form": fm})


@login_required(login_url="")
def region_view(request):
    dest1 = region.objects.all()
    messages.success(request, "Region is created successfully")
    return render(request, "region_view.html", {"dest1": dest1})


@login_required(login_url="")
def one(request):
    fm = circleform()
    if request.method == "POST":
        gn = request.POST.get("region")
        re = request.POST.get("Zone")
        ce = request.POST.get("created_by")

        messages.success(request, "Zone is created successfully")
        return redirect("/zone_view")
    return render(request, "zone.html", {"form": fm})


@login_required(login_url="")
def zone_view(request):
    dest1 = zone.objects.all()
    messages.success(request, "Zone is created successfully")
    return render(request, "zone_view.html", {"dest1": dest1})


@login_required(login_url="")
def Center(request):
    fm = zoneform()
    if request.method == "POST":
        gn = request.POST.get("region")
        re = request.POST.get("Zone")
        ce = request.POST.get("created_by")
        kk = region.objects.get(pk=gn)
        rk = zone.objects.get(pk=re)

        return redirect("/zone_view")
    return render(request, "center.html", {"form": fm})


@login_required(login_url="")
def Agents(request):
    form = agentform(request.POST)
    if form.is_valid():
        User_ID = form.cleaned_data["user_Id"]
        Agents_Name = form.cleaned_data["agents_Name"]
        branchName = form.cleaned_data["branch_Name"]
        Agent(user_Id=User_ID, agents_Name=Agents_Name, branch_Name=branchName).save()
        messages.success(request, "Branch is Assigned successfully to the Agent")
    form = agentform()
    return render(
        request,
        "agent.html",
        {
            "form": form,
        },
    )


@login_required(login_url="")
def center_ID(request):
    form = centerIdform(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "centerID.html", {"form": form})


@login_required(login_url="")
def Agent_user(request):
    form = customerRegistraionForm(request.POST)
    if form.is_valid():
        form.save()
    return render(
        request,
        "useragent.html",
        {
            "form": form,
        },
    )


@login_required(login_url="")
def change_password(request):
    sm = PasswordResetForm(auto_id=TRUE)
    messages.success(
        request, "Password Reset Link has been send to your Registerd Email-id"
    )
    return render(request, "index2.html", {"form": sm})


@login_required(login_url="")
def desbord(request):
    user = request.user
    if request.user.is_superuser == True:
        return render(request, "home.html", {"user": user})
    else:
        return render(request, "home1.html", {"user": user})


@login_required(login_url="")
def center_meeting(request):
    return render(request, "center_meeting.html")


@login_required(login_url="")
def addCenterMeeting(request):
    return render(request, "addCenterMeeting.html")


@login_required(login_url="")
def collection_reverse(request):
    return render(request, "collection_reverse.html")


@login_required(login_url="")
def cross_sell_cash_sell(request):
    return render(request, "cross_sell_cash_sell.html")


@login_required(login_url="")
def add_cross_sell_cash_sell(request):
    return render(request, "add_cross_sell_cash_sell.html")


@login_required(login_url="")
def Credit_Bureau_Check(request):
    return render(request, "Credit_Bureau_Check.html")


@login_required(login_url="")
def branchDayClose(request):
    return render(request, "branchDayClose.html")


@login_required(login_url="")
def loan(request):
    return render(request, "loan.html")


@login_required(login_url="")
def loanCalculator(request):
    fm = calculatorForm()
    finalAmount = 0
    if request.method == "POST":
        calculationType = request.POST.get("calculation_type")
        loanMode = request.POST.get("loanMode")
        rateOfIntrest = request.POST.get("rateOfIntrest")
        loan_amount = request.POST.get("loan_amount")
        terms = request.POST.get("terms")
        print(rateOfIntrest)
        if (calculationType == "REDUCING") & (loanMode == "WEEKLY"):
            principleapmount = int(loan_amount) / int(terms)
            intrest = int(principleapmount) * int(rateOfIntrest) / 100
            finalAmount = int(principleapmount) + int(intrest)
    return render(
        request, "loanCalculator.html", {"form": fm, "finalAmount": finalAmount}
    )


@login_required(login_url="")
def CustomerKYC(request):
    if request.user.is_superuser == True:
        AppID = commonfield.objects.all()
        return render(request, "customerKYC.html", {"AppID": AppID})
    else:
        return redirect("/AgentCustomer")


def AgentCustomerKYC(request):
    user = request.user
    AppID = commonfield.objects.all()
    LoanDetail = LoanDetails.objects.all()
    Branch = branch.objects.all()
    AgentDetails = Agent.objects.filter(user_Id=user)
    CenterId = Center_ID.objects.filter(agents_Name=user)
    if request.method == "POST":
        fm = customerKYCform(request.POST)
        if fm.is_valid():
            AadhaarNumber = fm.cleaned_data["Aadhaar"]
            VoterCard = fm.cleaned_data["VoterCard"]
            KycIdType = fm.cleaned_data["OtherKYCIdtype"]
            kycId = fm.cleaned_data["OtherKYCId"]
            # custimg = request.POST["Custimage"]
            FirstName = fm.cleaned_data["FirstName"]
            LastName = fm.cleaned_data["LastName"]
            Gender = fm.cleaned_data["Gender"]
            DateOfBirth = fm.cleaned_data["DateOfBirth"]
            Age = fm.cleaned_data["Age"]
            MaritalStatus = fm.cleaned_data["MaritalStatus"]
            FsName = fm.cleaned_data["FSName"]
            FsType = fm.cleaned_data["FSType"]
            FsDOB = fm.cleaned_data["FSDateOfBirth"]
            FsAdhaar = fm.cleaned_data["FSAdhaar"]
            MotherName = fm.cleaned_data["MothersName"]
            Caste = fm.cleaned_data["Caste"]
            Religion = fm.cleaned_data["Religion"]
            Qualification = fm.cleaned_data["Qualification"]
            Occupation = fm.cleaned_data["Occupation"]
            PhoneNumber = fm.cleaned_data["PhoneNumber"]
            AddLine1 = fm.cleaned_data["AddressLine1"]
            AddLine2 = fm.cleaned_data["AddressLine2"]
            AddLine3 = fm.cleaned_data["AddressLine3"]
            Language = fm.cleaned_data["PreferredLanguage"]
            Village = fm.cleaned_data["Village"]
            # District = request.POST["District"]
            # State = request.POST["State"]
            PinCode = fm.cleaned_data["Pincode"]
            confirmAddressLine1 = fm.cleaned_data["confirmAddressLine1"]
            confirmAddressLine2 = fm.cleaned_data["confirmAddressLine2"]
            confirmAddressLine3 = fm.cleaned_data["confirmAddressLine3"]
            confirmVillage = fm.cleaned_data["confirmVillage"]
            # confirmDistrict = request.POST["confirmDistrict"]
            # confirmState = request.POST["confirmState"]
            confirmPincode = fm.cleaned_data["confirmPincode"]
            HouseType = fm.cleaned_data["HouseType"]
            LandInAcre = fm.cleaned_data["LandInAcre"]
            PovertyLine = fm.cleaned_data["PovertyLine"]
            NoOfAnimals = fm.cleaned_data["NumberofAnimals"]
            BankName = fm.cleaned_data["BankName"]
            BankAccountNo = fm.cleaned_data["BankAccountNo"]
            ConfirmbankAccountNo = fm.cleaned_data["ConfirmBankAccountNo"]
            BankIFSCcode = fm.cleaned_data["BankIFSCCode"]
            ConfirmbankIFSCcode = fm.cleaned_data["ConfirmBankIFSCCode"]
            Branch = request.POST.get("branch")
            CenterId = request.POST.get("centerId")
            CategoryType = fm.cleaned_data["CategoryType"]
            ProductCategory = request.POST.get("productCategory")
            Product = request.POST.get("product")
            PurposeId = fm.cleaned_data["PurposeId"]
            LoanAmount = fm.cleaned_data["LoanAmount"]
            IntRate = fm.cleaned_data["InterestRate"]
            RepayFreq = fm.cleaned_data["RepayFrequency"]
            GroupName = fm.cleaned_data["GroupName"]
            CoInsurerRelation = fm.cleaned_data["CoInsurerRelation"]
            CoInsurerName = fm.cleaned_data["CoInsurerName"]
            CoOccupation = fm.cleaned_data["CoOccupation"]
            CoInsurerdob = fm.cleaned_data["CoInsurerDOB"]
            CoInsurerage = fm.cleaned_data["CoInsurerAge"]
            CokycIdType = fm.cleaned_data["KYCIDType"]
            KycId = fm.cleaned_data["KYCID"]
            RemarkComments = fm.cleaned_data["RemarkComments"]
            NomineeRelation = fm.cleaned_data["NomineeRelation"]
            NomineeName = fm.cleaned_data["NomineeName"]
            NomineeDob = fm.cleaned_data["NomineeDateOfBirth"]
            NomineeAge = fm.cleaned_data["NomineeAge"]
            print(NomineeAge)
            customerKYC(
                Aadhaar=AadhaarNumber,
                VoterCard=VoterCard,
                OtherKYCIdtype=KycIdType,
                OtherKYCId=kycId,
                # Custimage=custimg,
                FirstName=FirstName,
                LastName=LastName,
                Gender=Gender,
                DateOfBirth=DateOfBirth,
                Age=Age,
                MaritalStatus=MaritalStatus,
                FSName=FsName,
                FSType=FsType,
                FSDateOfBirth=FsDOB,
                MothersName=MotherName,
                FSAdhaar=FsAdhaar,
                Caste=Caste,
                Religion=Religion,
                Qualification=Qualification,
                Occupation=Occupation,
                PhoneNumber=PhoneNumber,
                AddressLine1=AddLine1,
                AddressLine2=AddLine2,
                AddressLine3=AddLine3,
                PreferredLanguage=Language,
                Village=Village,
                # District=District,
                # State=State,
                Pincode=PinCode,
                confirmAddressLine1=confirmAddressLine1,
                confirmAddressLine2=confirmAddressLine2,
                confirmAddressLine3=confirmAddressLine3,
                confirmPincode=confirmPincode,
                confirmVillage=confirmVillage,
                # confirmState=confirmState,
                # confirmDistrict=confirmDistrict,
                HouseType=HouseType,
                LandInAcre=LandInAcre,
                NumberofAnimals=NoOfAnimals,
                PovertyLine=PovertyLine,
                BankName=BankName,
                BankAccountNo=BankAccountNo,
                ConfirmBankAccountNo=ConfirmbankAccountNo,
                BankIFSCCode=BankIFSCcode,
                ConfirmBankIFSCCode=ConfirmbankIFSCcode,
                BranchName=Branch,
                CenterId=CenterId,
                CategoryType=CategoryType,
                ProductCategory=ProductCategory,
                Product=Product,
                PurposeId=PurposeId,
                LoanAmount=LoanAmount,
                InterestRate=IntRate,
                RepayFrequency=RepayFreq,
                GroupName=GroupName,
                CoInsurerRelation=CoInsurerRelation,
                CoInsurerName=CoInsurerName,
                CoOccupation=CoOccupation,
                CoInsurerDOB=CoInsurerdob,
                CoInsurerAge=CoInsurerage,
                KYCIDType=CokycIdType,
                KYCID=KycId,
                RemarkComments=RemarkComments,
                NomineeRelation=NomineeRelation,
                NomineeName=NomineeName,
                NomineeDateOfBirth=NomineeDob,
                NomineeAge=NomineeAge,
            ).save()
        messages.success(request, "Your Form is Submitted Successfully ")
        # LoanAPPID = customerKYC.objects.filter(Aadhaar=AadhaarNumber)
        # for c in LoanAPPID:
        #     applicationNO = c.ApplicationNumber
        #     customerKYC(Application_No=applicationNO).save()
    else:
        fm = customerKYCform()
    return render(
        request,
        "AgentcustomerKYC.html",
        {
            "AppID": AppID,
            "LoanDetail": LoanDetail,
            "Branch": Branch,
            "CenterId": CenterId,
            "AgentDetails": AgentDetails,
            "loanDetails": LoanDetail,
            "form": fm,
        },
    )


def loanDetailsAmount(request):
    if request.method == "GET":
        product = request.GET.get("Product_name")
        loandata = LoanDetails.objects.get(Product=product)
        data = {
            "LoanAmount": loandata.LoanAmount,
            "InterestRate": loandata.InterestRate,
            "RepayFrequency": loandata.RepayFrequency,
        }
    return JsonResponse(data)


# class CustomerRegistrationView(View):
#      def get(self,request):
#           form = customerRegistraionForm()
#           return render(request,'../templates/signup.html',{'form':form});
#      def post(self,request):
#           form = customerRegistraionForm(request.POST)
#           if form.is_valid():
#                form.save()
#                messages.success(request,'congratulations your account has been created !!')
#           return render(request,'../templates/signup.html',{'form':form});
