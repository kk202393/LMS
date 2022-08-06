from django.db import models
from django.contrib.auth.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class haed_office(models.Model):
    haed_office_name = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return str(self.haed_office_name)

    class Meta:
        verbose_name_plural = "1. haed_office"


class circle(models.Model):
    haed_office_name = models.ForeignKey(
        haed_office, on_delete=models.CASCADE, null=True
    )
    circle_name = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "2. circle"

    def __str__(self):
        return str(self.circle_name)


class zone(models.Model):
    haed_office_name = models.ForeignKey(
        haed_office, on_delete=models.CASCADE, null=True
    )
    circle_name = models.ForeignKey(circle, on_delete=models.CASCADE, null=True)
    zone = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "3. Zone"

    def __str__(self):
        return str(self.zone)


class region(models.Model):
    haed_office_name = models.ForeignKey(
        haed_office, on_delete=models.CASCADE, null=True
    )
    circle_name = models.ForeignKey(circle, on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey(zone, on_delete=models.CASCADE, null=True)
    region = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "4. region"

    def __str__(self):
        return str(self.region)


class branch(models.Model):
    haed_office_name = models.ForeignKey(haed_office, on_delete=models.CASCADE)
    circle_name = models.ForeignKey(circle, on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    region = models.ForeignKey(region, on_delete=models.CASCADE)
    branch_Name = models.CharField(max_length=100, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "5. branch"

    def __str__(self):
        return str(self.branch_Name)


class center(models.Model):
    haed_office_name = models.ForeignKey(
        haed_office, on_delete=models.CASCADE, null=True
    )
    circle_name = models.ForeignKey(circle, on_delete=models.CASCADE, null=True)
    zone = models.ForeignKey(zone, on_delete=models.CASCADE)
    region = models.ForeignKey(region, on_delete=models.CASCADE)
    branch_Name = models.ForeignKey(branch, on_delete=models.CASCADE, null=True)
    center_name = models.CharField(max_length=100, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "6. center"

    def __str__(self):
        return str(self.branch_Name)


CategoryType = (
    ("SNT", "SNT"),
    ("IGL", "IGL"),
)


class Center_ID(models.Model):
    agents_Name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    branchName = models.ForeignKey(branch, null=True, on_delete=models.CASCADE)
    centerId = models.CharField(null=True, max_length=50)


class Agent(models.Model):
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    agents_Name = models.CharField(null=True, max_length=50)
    branch_Name = models.ForeignKey(branch, null=True, on_delete=models.CASCADE)


LOANGROUP = (("kailash", "kailash"),)


class commonfield(models.Model):
    ApplicationId = models.CharField(null=True, max_length=50)
    Branch = models.CharField(null=True, max_length=50)
    CenterId = models.CharField(null=True, max_length=50)
    CustomerId = models.CharField(null=True, max_length=50)
    Status = models.CharField(null=True, max_length=50)
    Cycle = models.CharField(null=True, max_length=50)
    Group = models.CharField(choices=LOANGROUP, null=True, max_length=50)


OTHERKYCTYPE = (
    ("Ration card", "Ration card"),
    ("Pen card", "Pen card"),
    ("Driving license", "Driving license"),
)
KYCIDType = (
    ("Aadhar card", "Aadhar card"),
    ("Ration card", "Ration card"),
    ("Voter card", "Voter card"),
    ("Driving license", "Driving license"),
)
GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Others", "Others"),
)

MaritalStatus = (
    ("Married", "Married"),
    ("UnMarried", "UnMarried"),
    ("Widow", "Widow"),
    ("Separated", "Separated"),
    ("Widower", "Widower"),
    ("Divorced", "Divorced"),
)
FSType = (
    ("Father", "Father"),
    ("Spouse", "Spouse"),
)
CAST = (
    ("General", "General"),
    ("OBC", "OBC"),
    ("Scheduled Tribes", "Scheduled Tribes"),
    ("Schedules Castes", "Schedules Castes"),
    ("Minority", "Minority"),
)
Religion = (
    ("Hindu", "Hindu"),
    ("Muslim", "Muslim"),
    ("Other", "Other"),
)
Qualification = (
    ("Primary", "Primary"),
    ("Metric", "Metric"),
    ("Intermediate", "Intermediate"),
    ("Graduate", "Graduate"),
    ("Post Graduate", "Post Graduate"),
)
PreferredLanguage = (
    ("Hindi", "Hindi"),
    ("English", "English"),
)
STATE_CHOICES = (
    ("Andhra Pradesh", "Andhra Pradesh"),
    ("Andaman and Nicobar Islands", "Andaman and Nicobar Islands"),
    ("Arunachal Pradesh", "Arunachal Pradesh"),
    ("Assam", "Assam"),
    ("Bihar", "Bihar"),
    ("Chandigarh", "Chandigarh"),
    ("Chhattisgarh", "Chhattisgarh"),
    (
        "Dadar and Nagar Haveli",
        "Dadar and Nagar Haveli",
    ),
    ("Daman and Diu", "Daman and Diu"),
    ("Delhi", "Delhi"),
    ("Goa", "Goa"),
    ("Gujarat", "Gujarat"),
    ("Haryana", "Haryana"),
    ("Himachal Pradesh", "Himachal Pradesh"),
    ("Jharkhand", "Jharkhand"),
    ("Jammu and Kashmir", "Jammu and Kashmir"),
    ("Karnataka", "Karnataka"),
    ("Kerala", "Kerala"),
    ("Lakshadweep", "Lakshadweep"),
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Maharashtra", "Maharashtra"),
    ("Manipur", "Manipur"),
    ("Meghalaya", "Meghalaya"),
    ("Mizoram", "Mizoram"),
    ("Nagaland", "Nagaland"),
    ("Odisha", "Odisha"),
    ("Punjab", "Punjab "),
    ("Puducherry", "Puducherry"),
    ("Rajasthan", "Rajasthan"),
    ("Sikkim", "Sikkim"),
    ("Tamil Nadu", "Tamil Nadu"),
    ("Telangana", "Telangana"),
    ("Tripura", "Tripura"),
    ("Uttar Pradesh", "Uttar Pradesh"),
    ("Uttarakhand", "Uttarakhand"),
    ("West Bengal", "West Bengal"),
)
District_CHOICES = ()
HouseType = (
    ("Pakka", "Pakka"),
    ("Kachha", "Kachha"),
    ("Rental", "Rental"),
)
PovertyLine = (
    ("Above Poverty Line", "Above Poverty Line"),
    ("Below Poverty Line", "Below Poverty Line"),
)
PurposeId = (
    ("Transportation", "Transportation"),
    ("Agriculture", "Agriculture"),
    ("Tranding", "Tranding"),
    ("Production", "Production"),
)
categoryType = (
    ("SNT", "SNT"),
    ("IGL", "IGL"),
)

PreferredLanguage = (
    ("Hindi", "Hindi"),
    ("English", "English"),
)
GroupName = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
)
BankName = (
    ("Bank of Baroda", "Bank of Baroda"),
    ("Bank of India", "Bank of India"),
    ("Bank of Maharashtra", "Bank of Maharashtra"),
    ("Canara Bank", "Canara Bank"),
    ("Central Bank of India", "Central Bank of India"),
    ("Indian Bank", "Indian Bank"),
    ("Indian Overseas Bank", "Indian Overseas Bank"),
    ("Punjab & Sind Bank", "Punjab & Sind Bank"),
    ("Punjab National Bank", "Punjab National Bank"),
    ("State Bank of India", "State Bank of India"),
    ("UCO Bank", "UCO Bank"),
    ("Union Bank of India", "Union Bank of India"),
    ("Axis Bank", "Axis Bank"),
    ("Bandhan Bank", "Bandhan Bank"),
    ("CSB Bank", "CSB Bank"),
    ("City Union Bank", "City Union Bank"),
    ("DCB Bank", "DCB Bank"),
    ("Dhanlaxmi Bank", "Dhanlaxmi Bank"),
    ("Federal Bank", "Federal Bank"),
    ("HDFC Bank", "HDFC Bank"),
    ("ICICI Bank", "ICICI Bank"),
    ("Induslnd Bank", "Induslnd Bank"),
    ("IDFC First Bank", "IDFC First Bank"),
    ("Jammu & Kashmir Bank", "Jammu & Kashmir Bank"),
    ("Karnataka Bank", "Karnataka Bank"),
    ("Karur Vysya Bank", "Karur Vysya Bank"),
    ("Kotak Mahindra Bank", "Kotak Mahindra Bank"),
    ("Lakshmi Vilas Bank", "Lakshmi Vilas Bank"),
    ("Nainital Bank", "Nainital Bank"),
    ("RBL Bank", "RBL Bank"),
    ("South Indian Bank", "South Indian Bank"),
    ("Tamilnad Mercantile Bank", "Tamilnad Mercantile Bank"),
    ("YES Bank", "YES Bank"),
    ("IDBI Bank", "IDBI Bank"),
)


class customerKYC(models.Model):
    id = models.AutoField(primary_key=True)
    Application_No = models.IntegerField(unique=True, null=True)
    Aadhaar = models.BigIntegerField(unique=True)
    VoterCard = models.CharField(unique=True, max_length=50)
    OtherKYCIdtype = models.CharField(null=True, max_length=50, choices=OTHERKYCTYPE)
    OtherKYCId = models.CharField(null=True, max_length=50)
    Custimage = models.ImageField(upload_to="img", null=True)
    Aadharimage = models.ImageField(upload_to="img", null=True)
    VoterIDimage = models.ImageField(upload_to="img", null=True)
    Doc1image = models.ImageField(upload_to="img", null=True)
    Doc2image = models.ImageField(upload_to="img", null=True)
    FirstName = models.CharField(null=True, max_length=50)
    LastName = models.CharField(null=True, max_length=50)
    Gender = models.CharField(null=True, max_length=50, choices=GENDER)
    DateOfBirth = models.DateField(
        null=True,
    )
    Age = models.IntegerField()
    MaritalStatus = models.CharField(null=True, max_length=50, choices=MaritalStatus)
    FSName = models.CharField(null=True, max_length=50)
    FSType = models.CharField(null=True, max_length=50, choices=FSType)
    FSDateOfBirth = models.DateField(null=True)
    FSAdhaar = models.BigIntegerField(unique=True)
    MothersName = models.CharField(null=True, max_length=50)
    Caste = models.CharField(null=True, max_length=50, choices=CAST)
    Religion = models.CharField(null=True, max_length=50, choices=Religion)
    Qualification = models.CharField(null=True, max_length=50, choices=Qualification)
    Occupation = models.CharField(null=True, max_length=50)
    PhoneNumber = models.BigIntegerField()
    AddressLine1 = models.CharField(max_length=50)
    AddressLine2 = models.CharField(max_length=50)
    AddressLine3 = models.CharField(max_length=50)
    PreferredLanguage = models.CharField(
        choices=PreferredLanguage, null=True, max_length=50
    )
    Pincode = models.IntegerField()
    Village = models.CharField(null=True, max_length=100)
    State = models.CharField(null=True, max_length=50, choices=STATE_CHOICES)
    District = models.CharField(null=True, max_length=100, choices=District_CHOICES)
    confirmAddressLine1 = models.CharField(max_length=50)
    confirmAddressLine2 = models.CharField(max_length=50)
    confirmAddressLine3 = models.CharField(max_length=50)
    confirmPincode = models.IntegerField(
        null=True,
    )
    confirmVillage = models.CharField(null=True, max_length=100)
    confirmState = models.CharField(null=True, max_length=50, choices=STATE_CHOICES)
    confirmDistrict = models.CharField(
        null=True, max_length=100, choices=District_CHOICES
    )
    # FinancialDetails for customer
    HouseType = models.CharField(null=True, max_length=50, choices=HouseType)
    LandInAcre = models.FloatField()
    NumberofAnimals = models.IntegerField()
    PovertyLine = models.CharField(null=True, max_length=50, choices=PovertyLine)
    BankName = models.CharField(choices=BankName, null=True, max_length=50)
    BankAccountNo = models.BigIntegerField(null=True)
    ConfirmBankAccountNo = models.BigIntegerField(null=True)
    BankIFSCCode = models.CharField(null=True, max_length=50)
    ConfirmBankIFSCCode = models.CharField(null=True, max_length=50)
    # LoanDetails for customerKYC
    BranchName = models.CharField(null=True, max_length=50)
    CenterId = models.CharField(null=True, max_length=50)
    ProductCategory = models.CharField(null=True, max_length=50)
    CategoryType = models.CharField(null=True, max_length=50, choices=categoryType)
    Product = models.CharField(null=True, max_length=50)
    PurposeId = models.CharField(null=True, max_length=50, choices=PurposeId)
    LoanAmount = models.IntegerField()
    InterestRate = models.FloatField()
    RepayFrequency = models.FloatField()
    GroupName = models.CharField(null=True, max_length=50, choices=GroupName)
    # CoInsurerDetails for cutomerKYC
    CoInsurerRelation = models.CharField(null=True, max_length=50)
    CoInsurerName = models.CharField(null=True, max_length=50)
    CoInsurerDOB = models.DateField(null=True)
    CoInsurerAge = models.IntegerField()
    KYCIDType = models.CharField(choices=KYCIDType, null=True, max_length=50)
    KYCID = models.CharField(null=True, max_length=50)
    CoOccupation = models.CharField(null=True, max_length=50)
    RemarkComments = models.CharField(max_length=500)
    # NomineeDetails for customerKYC
    NomineeRelation = models.CharField(null=True, max_length=50)
    NomineeName = models.CharField(null=True, max_length=50)
    NomineeDateOfBirth = models.DateField(null=True)
    NomineeAge = models.IntegerField()

    @property
    def ApplicationNumber(self):
        Branch = self.BankName[:4]
        Aadhar = self.Aadhaar[:4]
        year = self.id
        return Branch + Aadhar + year


class ProductDetails(models.Model):
    CategoryType = models.CharField(null=True, max_length=50)
    ProductCategory = models.CharField(null=True, max_length=50)
    Product = models.CharField(null=True, max_length=50)
    LoanAmount = models.IntegerField()
    AppliedAmount = models.IntegerField()
    InterestRate = models.FloatField()
    RepayFrequency = models.FloatField()
    ProductInvoiceNumber = models.FloatField()
    SanctionStatus = models.CharField(null=True, max_length=50)


LOAN_MODE = (("WEEKLY", "WEEKLY "), ("BIWEEKLY", "BIWEEKLY"), ("MONTHLY", "MONTHLY"))


class LoanDetails(models.Model):
    loanName = models.CharField(null=True, max_length=50)
    Product = models.CharField(null=True, max_length=50)
    loanMode = models.CharField(choices=LOAN_MODE, null=True, max_length=50)
    LoanAmount = models.IntegerField()
    InterestRate = models.FloatField()
    RepayFrequency = models.IntegerField()

    def __str__(self):
        return str(self.Product)


class PurposeDetails(models.Model):
    Purpose = models.CharField(null=True, max_length=50)
    SubPurpose = models.CharField(null=True, max_length=50)


class InsuranceDetails(models.Model):
    InsuranceId = models.CharField(null=True, max_length=50)


class FinancialDetails(models.Model):
    ClientMonthlyEMIAmountCB = models.IntegerField()
    MonthlyFamilyIncome = models.IntegerField()
    MonthlyFamilyExpense = models.IntegerField()
    ClientMonthlyEMIAmount = models.IntegerField()
    FamilyMonthlyEMIAmount = models.IntegerField()
    HouseType = models.CharField(null=True, max_length=50)
    LandInAcre = models.FloatField()
    NumberofAnimals = models.IntegerField()
    PovertyLine = models.CharField(null=True, max_length=50)
    BankName = models.CharField(null=True, max_length=50)
    BankAccountNo = models.CharField(null=True, max_length=50)
    ConfirmBankAccountNo = models.CharField(null=True, max_length=50)
    BankIFSCCode = models.CharField(null=True, max_length=50)
    ConfirmBankIFSCCode = models.CharField(null=True, max_length=50)


class HouseholdDetails(models.Model):
    MonthlyFamilyExpense = models.IntegerField()
    MonthlyFamilyIncome = models.IntegerField()
    ClientMonthlyEMIAmountCB = models.IntegerField()
    CoClientMonthlyEMIAmountCB = models.IntegerField()
    TotalFamilyMonthlyEMIAmount = models.IntegerField()
    NumberofAnimals = models.IntegerField()
    LandInAcre = models.IntegerField()


class CreditBureauDetails(models.Model):
    OtherMFISHG = models.CharField(null=True, max_length=50)
    InternalRating = models.FloatField()
    OtherLoanAmount = models.IntegerField()
    OtherOSAmount = models.CharField(null=True, max_length=50)
    EligibleMontlyEMI = models.FloatField()
    CBResponseDate = models.DateField(null=True)
    GenericMFIScore = models.FloatField()


class NomineeDetails(models.Model):
    NomineeRelation = models.CharField(null=True, max_length=50)
    NomineeName = models.CharField(null=True, max_length=50)
    DateOfBirth = models.DateField(null=True)
    Age = models.IntegerField()


class CoInsurerDetails(models.Model):
    CoInsurerRelation = models.CharField(null=True, max_length=50)
    CoInsurerName = models.IntegerField()
    CoOccupation = models.CharField(null=True, max_length=50)
    CoInsurerDOB = models.DateField(null=True)
    CoInsurerAge = models.IntegerField()
    KYCIDType = models.CharField(null=True, max_length=50)
    KYCID = models.CharField(null=True, max_length=50)
    RemarkComments = models.TextField()


class CustomerRegistered(models.Model):
    CustomerRegistered = models.DateField(null=True)
    ApplicationApplied = models.DateField(null=True)
    ExpectedDisbursementDate = models.DateField(null=True)
    TopUp = models.BooleanField()
    HouseVisit = models.BooleanField()


class RejectionReasonComments(models.Model):
    RejectionReason = models.TextField()
    Comments = models.TextField()


class SharedServiceDetials(models.Model):
    SharedServiceDetail = models.CharField(null=True, max_length=50)
    SharedServiceRejectionCount = models.CharField(null=True, max_length=50)
    BankValidationRemarks = models.CharField(null=True, max_length=50)


CALCULATION_TYPE = (("FLAT", "FLAT "), ("REDUCING", "REDUCING"))
LOAN_MODE = (("WEEKLY", "WEEKLY "), ("BIWEEKLY", "BIWEEKLY"), ("MONTHLY", "MONTHLY"))


class calculator(models.Model):
    calculation_type = models.CharField(choices=CALCULATION_TYPE, max_length=100)
    loanMode = models.CharField(choices=LOAN_MODE, max_length=100)
    rateOfIntrest = models.IntegerField()
    loan_amount = models.IntegerField()
    terms = models.IntegerField()
