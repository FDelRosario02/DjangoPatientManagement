from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django import forms
from .models import Record
from .models import Patient

class SignUpFrom(UserCreationForm):
    """
    A custom form for user sign up.
    """

    # Define the first name field
    first_name = forms.CharField(
        label="",  # No label for the field
        max_length="100",  # Maximum length of the input
        widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': "form-control"})  # Attributes for the input field
    )

    # Define the last name field
    last_name = forms.CharField(
        label="",  # No label for the field
        max_length="100",  # Maximum length of the input
        widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': "form-control"})  # Attributes for the input field
    )

    class Meta:
        """
        Meta class for the form.
        """
        model = User  # The model for which the form is created
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')  # The fields of the form

    def __init__(self, *args, **kwargs):
        """
        Initialization method for the form.
        """
        super(SignUpFrom, self).__init__(*args, **kwargs)  # Call the parent class's initialization method

        # Modify the attributes of the username field
        self.fields['username'].widget.attrs['class'] = 'form-control'  # Add the 'form-control' class to the field
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'  # Add a placeholder to the field
        self.fields['username'].label = ''  # Remove the label from the field
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'  # Add help text to the field

        # Modify the attributes of the password1 field
        self.fields['password1'].widget.attrs['class'] = 'form-control'  # Add the 'form-control' class to the field
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'  # Add a placeholder to the field
        self.fields['password1'].label = ''  # Remove the label from the field
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'  # Add help text to the field

        # Modify the attributes of the password2 field
        self.fields['password2'].widget.attrs['class'] = 'form-control'  # Add the 'form-control' class to the field
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'  # Add a placeholder to the field
        self.fields['password2'].label = ''  # Remove the label from the field
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'  # Add help text to the field


        #Create Add Recird Form
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class":"form-control"}), label="")
    address =forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Adderss ", "class":"form-control"}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "City Name", "class":"form-control"}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "State Name", "class":"form-control"}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Zipcode ", "class":"form-control"}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Email", "class":"form-control"}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class":"form-control"}), label="")

    class Meta:
        model =Record
        exclude = ("user", )

class AddPatientForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}),
        label=""
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
        label=""
    )
    date_of_birth = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(attrs={"placeholder": "Date of Birth", "class": "form-control", "type": "date"}),
        label=""
    )
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        widget=forms.widgets.Select(attrs={"class": "form-control"}),
        label=""
    )
    address = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
        label=""
    )
    phone = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
        label=""
    )
    email = forms.EmailField(
        required=False,
        widget=forms.widgets.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}),
        label=""
    )
    blood_type = forms.ChoiceField(
        required=True,
        choices=[('A+','A+'), ('A-','A-'), ('B-','B-'), ('B+','B+'), ('AB-','AB-'), ('AB+','AB+'), ('O-','O-'), ('O+','O+')],
        widget=forms.widgets.Select(attrs={"placeholder": "Blood Type", "class": "form-control"}),
        label=""
    )
    allergies = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(attrs={"placeholder": "Allergies", "class": "form-control", "rows": 3}),
        label=""
    )
    current_medications = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(attrs={"placeholder": "Current Medications", "class": "form-control", "rows": 3}),
        label=""
    )

    class Meta:
        model = Patient
        exclude = ("user", )
    def __init__(self, *args, **kwargs):
        super(AddPatientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.label = ""