from cProfile import label
import django
from django.contrib.auth.models import *
from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import *
from requests import request
from LOAN.models import *
from django.core import validators


class customerKYCform(forms.ModelForm):
    class Meta:
        model = customerKYC
        # fields = "__all__"
        fields = [
            "Aadhaar",
            "VoterCard",
            "OtherKYCIdtype",
            "OtherKYCId",
            # "Custimage",
            # "Aadharimage",
            # "VoterIDimage",
            "FirstName",
            "LastName",
            "Gender",
            "DateOfBirth",
            "Age",
            "MaritalStatus",
            "FSName",
            "FSType",
            "FSDateOfBirth",
            "FSAdhaar",
            "MothersName",
            "Caste",
            "Religion",
            "Qualification",
            "Occupation",
            "PhoneNumber",
            "AddressLine1",
            "AddressLine2",
            "AddressLine3",
            "PreferredLanguage",
            "Pincode",
            "Village",
            "State",
            # "District",
            "confirmAddressLine1",
            "confirmAddressLine2",
            "confirmAddressLine3",
            "confirmPincode",
            "confirmVillage",
            "confirmState",
            # "confirmDistrict",
            "HouseType",
            "LandInAcre",
            "NumberofAnimals",
            "PovertyLine",
            "BankName",
            "BankAccountNo",
            "ConfirmBankAccountNo",
            "BankIFSCCode",
            "ConfirmBankIFSCCode",
            # "BranchName",
            # "CenterId",
            "GroupName",
            # "ProductCategory",
            "CategoryType",
            # "Product",
            "PurposeId",
            "LoanAmount",
            "InterestRate",
            "RepayFrequency",
            "CoInsurerRelation",
            "CoInsurerName",
            "CoInsurerDOB",
            "CoInsurerAge",
            "KYCIDType",
            "KYCID",
            "CoOccupation",
            "RemarkComments",
            "NomineeRelation",
            "NomineeName",
            "NomineeDateOfBirth",
            "NomineeAge",
        ]
        labels = {
            "Aadhaar": "Aadhar Number",
            "VoterCard": "Voter Card",
            "OtherKYCIdtype": "Other KYC Id Type",
            "DateOfBirth": "Date Of Birth",
            "MaritalStatus": "Marital Status",
            "FSDateOfBirth": "FS Date Of Birth",
            "FirstName": "First Name",
            "LastName": "Last Name",
            "FSAdhaar": "FS Adhaar",
            "FSName": "FS Name",
            "MothersName": "Mothers Name",
            "PreferredLanguage": "Preferred Language",
            "HouseType": "House Type",
            "LandInAcre": "Land In Acre",
            "NumberofAnimals": "Number of Animals",
            "PovertyLine": "Poverty Line",
            "BankName": "Bank Name",
            "BankAccountNo": "Bank Account Number",
            "ConfirmBankAccountNo": "Confirm Bank Account Number",
            "BankIFSCCode": "Bank IFSC Code",
            "ConfirmBankIFSCCode": "Confirm Bank IFSC Code",
            "GroupName": "Group Name",
            "CategoryType": "Category Type",
            "PurposeId": "Purpose Id",
            "LoanAmount": "Loan Amount",
            "InterestRate": "Interest Rate",
            "RepayFrequency": "Repay Frequency",
            "CoInsurerRelation": "Co Insurer Relation",
            "CoInsurerName": "Co Insurer Name",
            "CoInsurerDOB": "Co Insurer DOB",
            "CoInsurerAge": "Co Insurer Age",
            "KYCIDType": "KYC ID Type",
            "KYCID": "KYC ID",
            "CoOccupation": "Co Occupation",
            "RemarkComments": "Remark Comments",
            "NomineeRelation": "Nominee Relation",
            "NomineeName": "Nominee Name",
            "NomineeDateOfBirth": "Nominee Date Of Birth",
            "NomineeAge": "Nominee Age",
            "PhoneNumber": "Phone Number",
        }
        help_text = {
            "Aadhaar": "Enter Your Aadhar Number",
            "VoterCard": "Enter Your VoterID Number",
        }
        error_messages = {
            "Aadhaar": {
                "required": "Please Enter Your Aadhar Number",
            },
            "VoterCard": {
                "required": "Please Enter Your Voter Card Number",
            },
        }
        widgets = {
            "DateOfBirth": forms.DateInput(
                attrs={
                    "type": "date",
                    "id": "txtDOB",
                    "name": "dob",
                    "onchange": "fnCalculateAge();",
                }
            ),
            "Age": forms.NumberInput(attrs={"id": "age", "name": "age", "value": ""}),
            "FSDateOfBirth": forms.DateInput(
                attrs={
                    "type": "date",
                    "id": "fsDOB",
                    "name": "fsDOB",
                }
            ),
            "CoInsurerDOB": forms.DateInput(
                attrs={
                    "type": "date",
                    "id": "coInsurerdob",
                    "name": "coInsurerdob",
                    "onchange": "fnCalculateAge2();",
                }
            ),
            "CoInsurerAge": forms.NumberInput(
                attrs={"id": "co-Insurerage", "name": "coInsurerage", "value": ""}
            ),
            "NomineeDateOfBirth": forms.DateInput(
                attrs={
                    "type": "date",
                    "id": "NomineeDob",
                    "name": "NomineeDob",
                    "onchange": "fnCalculateAge3();",
                }
            ),
            "NomineeAge": forms.NumberInput(
                attrs={"id": "NomineeAge", "name": "NomineeAge", "value": ""}
            ),
            "ConfirmBankAccountNo": forms.PasswordInput(),
            "ConfirmBankIFSCCode": forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        group = customerKYC.objects.get(GroupName="A" or "B" or "C" or "D" or "E")
        Account = self.cleaned_data["BankAccountNo"]
        confirmAccount = self.cleaned_data["ConfirmBankAccountNo"]
        BankIFSCCode = self.cleaned_data["BankIFSCCode"]
        ConfirmBankIFSCCode = self.cleaned_data["ConfirmBankIFSCCode"]
        Age = self.cleaned_data["Age"]
        CoInsurerAge = self.cleaned_data["CoInsurerAge"]
        NomineeAge = self.cleaned_data["NomineeAge"]
        Pincode = self.cleaned_data["Pincode"]
        confirmPincode = self.cleaned_data["confirmPincode"]
        PhoneNumber = self.cleaned_data["PhoneNumber"]

        if Account != confirmAccount:
            raise forms.ValidationError(
                "Bank Account Number and Confirm Bank Account Number Must be Same"
            )
        elif BankIFSCCode != ConfirmBankIFSCCode:
            raise forms.ValidationError(
                "Bank IFCS Code and Confirm IFCS Code Must be Same"
            )
        elif 18 <= Age <= 58:
            raise forms.ValidationError(
                "Age Must be Same Less than 58 and greater than 18"
            )
        elif 18 <= CoInsurerAge <= 58:
            raise forms.ValidationError(
                "Age Must be Same Less than 58 and greater than 18"
            )
        elif 18 <= NomineeAge <= 58:
            raise forms.ValidationError(
                "Age Must be Same Less than 58 and greater than 18"
            )
        elif len(group) == 4:
            raise forms.ValidationError(
                "You can not create member in this group try other group"
            )
        elif 6 < len(Pincode) < 6:
            raise forms.ValidationError("Pin Code Must have 6 digits")
        elif 6 < len(confirmPincode) < 6:
            raise forms.ValidationError("confirm Pincode Must have 6 digits")
        elif 10 < len(PhoneNumber) < 10:
            raise forms.ValidationError("Moble Number Must have 10 digits")
        # return self.cleaned_data


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    Remember_me = forms.CharField(widget=forms.CheckboxInput)


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=("Old Password:"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "autocomplete": "current-password",
                "autofocus": True,
            }
        ),
    )
    new_password1 = forms.CharField(
        label=("New Password:"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "autocomplete": "new-password"}
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("Confirm New Password:"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "autocomplete": "new-password"}
        ),
    )


class MypasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "autocomplete": "email"}
        )
    )


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=("New Password:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("Confirm New Password:"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )


class haed_officeform(forms.Form):
    haed_office_name = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    created_by = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"})
    )
    Remember_me = forms.CharField(widget=forms.CheckboxInput)


class circleform(forms.ModelForm):
    class Meta:
        model = circle
        fields = ["haed_office_name", "circle_name", "created_by"]
        widgets = {
            "haed_office_name": forms.Select(attrs={"class": "form-control"}),
            "circle_name": forms.TextInput(attrs={"class": "form-control"}),
            "created_by": forms.TextInput(attrs={"class": "form-control"}),
        }


class zoneform(forms.ModelForm):
    class Meta:
        model = zone
        fields = ["haed_office_name", "circle_name", "zone", "created_by"]
        widgets = {
            "haed_office_name": forms.Select(attrs={"class": "form-control"}),
            "circle_name": forms.Select(attrs={"class": "form-control"}),
            "zone": forms.TextInput(attrs={"class": "form-control"}),
            "created_by": forms.TextInput(attrs={"class": "form-control"}),
        }


class agentform(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ["user_Id", "agents_Name", "branch_Name"]
        widgets = {
            "user_Id": forms.Select(attrs={"class": "form-control"}),
            "agents_Name": forms.TextInput(attrs={"class": "form-control"}),
            "branch_Name": forms.Select(attrs={"class": "form-control"}),
        }


class branchform(forms.ModelForm):
    class Meta:
        model = branch
        fields = [
            "haed_office_name",
            "circle_name",
            "zone",
            "region",
            "branch_Name",
            "created_by",
        ]
        widgets = {
            "haed_office_name": forms.Select(attrs={"class": "form-control"}),
            "circle_name": forms.Select(attrs={"class": "form-control"}),
            "zone": forms.Select(attrs={"class": "form-control"}),
            "region": forms.TextInput(attrs={"class": "form-control"}),
            "branch_Name": forms.TextInput(attrs={"class": "form-control"}),
            "created_by": forms.TextInput(attrs={"class": "form-control"}),
        }


class centerform(forms.ModelForm):
    class Meta:
        model = center
        fields = [
            "haed_office_name",
            "circle_name",
            "zone",
            "region",
            "branch_Name",
            "center_name",
            "created_by",
        ]
        widgets = {
            "haed_office_name": forms.Select(attrs={"class": "form-control"}),
            "circle_name": forms.Select(attrs={"class": "form-control"}),
            "zone": forms.Select(attrs={"class": "form-control"}),
            "region": forms.TextInput(attrs={"class": "form-control"}),
            "branch_Name": forms.TextInput(attrs={"class": "form-control"}),
            "center_name": forms.TextInput(attrs={"class": "form-control"}),
            "created_by": forms.TextInput(attrs={"class": "form-control"}),
        }


class centerIdform(forms.ModelForm):
    class Meta:
        model = Center_ID
        fields = ["agents_Name", "branchName", "centerId"]

        Widgets = {
            "agents_Name": forms.Select(attrs={"class": "form-control"}),
            "branchName": forms.Select(attrs={"class": "form-control"}),
            "centerId": forms.TextInput(attrs={"class": "form-control"}),
        }


class calculatorForm(forms.ModelForm):
    class Meta:
        model = calculator
        fields = [
            "calculation_type",
            "loanMode",
            "rateOfIntrest",
            "loan_amount",
            "terms",
        ]
        widgets = {
            "calculation_type": forms.Select(attrs={"class": "form-control"}),
            "loanMode": forms.Select(attrs={"class": "form-control"}),
        }


class customerRegistraionForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password(again)",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    email = forms.CharField(
        required=True, widget=forms.EmailInput(attrs={"class": "form-control"})
    )


class meta:
    model = User
    fields = ["username", "email", "password1", "password2"]
    labels = {"email": "Email"}
    Widget = {"username": forms.TextInput(attrs={"class": "form-control"})}


class customerRegistraionForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="Confirm Password(again)",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
