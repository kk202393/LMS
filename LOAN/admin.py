from django.contrib import admin
from LOAN.models import *

# Register your models here.
@admin.register(haed_office)
class haed_officeModelAdmin(admin.ModelAdmin):
    list_display = ["id", "haed_office_name", "created_date", "created_by"]


@admin.register(circle)
class circleModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "haed_office_name",
        "circle_name",
        "created_date",
        "created_by",
    ]


@admin.register(zone)
class zoneModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "haed_office_name",
        "circle_name",
        "zone",
        "created_date",
        "created_by",
    ]


# @admin.register(region)
# class zoneModelAdmin(admin.ModelAdmin):
#     list_display = [
#         "id",
#         "haed_office_name",
#         "circle_name",
#         "zone",
#         "created_date",
#         "region",
#         "created_by",
#     ]


@admin.register(branch)
class branchModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "haed_office_name",
        "circle_name",
        "zone",
        "branch_Name",
        "created_date",
        "created_by",
    ]


@admin.register(center)
class centerModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "haed_office_name",
        "circle_name",
        "zone",
        "branch_Name",
        "center_name",
        "created_date",
        "created_by",
    ]


@admin.register(Center_ID)
class centerIdModelAdmin(admin.ModelAdmin):
    list_display = ["agents_Name", "branchName", "centerId"]


@admin.register(Agent)
class Agent_dataModelAdmin(admin.ModelAdmin):
    list_display = ["user_Id", "agents_Name", "branch_Name"]


@admin.register(commonfield)
class commonfieldModelAdmin(admin.ModelAdmin):
    list_display = [
        "ApplicationId",
        "Branch",
        "CenterId",
        "CustomerId",
        "Status",
        "Cycle",
        "Group",
    ]


@admin.register(customerKYC)
class customerKYCModelAdmin(admin.ModelAdmin):
    list_display = [
        "FirstName",
        "LastName",
        "Gender",
        "DateOfBirth",
        "MaritalStatus",
        "VoterCard",
        "FSType",
        "FSName",
        "FSDateOfBirth",
        "MothersName",
        "FSAdhaar",
        "AddressLine1",
        "AddressLine2",
        "AddressLine3",
        "Pincode",
        "District",
        "State",
        "Caste",
        "Religion",
        "PreferredLanguage",
        "Qualification",
        "Aadhaar",
        "OtherKYCIdtype",
        "OtherKYCId",
        "PhoneNumber",
    ]


@admin.register(ProductDetails)
class ProductDetailsModelAdmin(admin.ModelAdmin):
    list_display = [
        "CategoryType",
        "ProductCategory",
        "Product",
        "LoanAmount",
        "AppliedAmount",
        "InterestRate",
        "RepayFrequency",
        "ProductInvoiceNumber",
    ]


@admin.register(PurposeDetails)
class PurposeModelAdmin(admin.ModelAdmin):
    list_display = [
        "Purpose",
        "SubPurpose",
    ]


@admin.register(InsuranceDetails)
class InsuranceDetailsAdmin(admin.ModelAdmin):
    list_display = ["InsuranceId"]


@admin.register(FinancialDetails)
class FinancialDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "BankName",
        "BankAccountNo",
        "BankIFSCCode",
    ]


@admin.register(LoanDetails)
class LoanDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "loanName",
        "Product",
        "loanMode",
        "LoanAmount",
        "InterestRate",
        "RepayFrequency",
    ]


@admin.register(HouseholdDetails)
class HouseholdDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "MonthlyFamilyExpense",
        "MonthlyFamilyIncome",
        "ClientMonthlyEMIAmountCB",
        "CoClientMonthlyEMIAmountCB",
        "TotalFamilyMonthlyEMIAmount",
        "NumberofAnimals",
        "LandInAcre",
    ]


@admin.register(CreditBureauDetails)
class CreditBureauDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "OtherMFISHG",
        "InternalRating",
        "OtherLoanAmount",
        "OtherOSAmount",
        "EligibleMontlyEMI",
        "CBResponseDate",
        "GenericMFIScore",
    ]


@admin.register(NomineeDetails)
class NomineeDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "DateOfBirth",
    ]


@admin.register(CoInsurerDetails)
class CoInsurerDetailsAdmin(admin.ModelAdmin):
    list_display = [
        "CoInsurerName",
    ]


@admin.register(CustomerRegistered)
class CustomerRegisteredAdmin(admin.ModelAdmin):
    list_display = [
        "CustomerRegistered",
        "ApplicationApplied",
        "ExpectedDisbursementDate",
        "TopUp",
        "HouseVisit",
    ]


@admin.register(RejectionReasonComments)
class RejectionReasonCommentsAdmin(admin.ModelAdmin):
    list_display = [
        "RejectionReason",
        "Comments",
    ]


@admin.register(SharedServiceDetials)
class SharedServiceDetialsAdmin(admin.ModelAdmin):
    list_display = [
        "SharedServiceDetail",
        "SharedServiceRejectionCount",
        "BankValidationRemarks",
    ]
