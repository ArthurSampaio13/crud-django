from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Book

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                "placeholder": "E-mail"
            }
        )
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "Primeiro nome"
            }
        )
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                "placeholder": "Último nome"
            }
        )
    )
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '''
            <span class="form-text text-muted">
                <small>Obrigatório. 150 caracteres ou menos.</small>
            </span>
        '''
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '''
            <ul class="form-text text-muted small">
                <li>Deve ser única.</li>
                <li>Deve conter pelo menos 8 caracteres.</li>
                <li>Não deve ser toda numérica.</li>
            </ul>
        '''
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '''
            <span class="form-text text-muted">
                <small>Digite a mesma senha que acima.</small>
            </span>
        '''

class AddBookForm(forms.ModelForm):
    title = forms.CharField(required=True, 
                            widget=forms.widgets.TextInput(
                            attrs={"placeholder" : "Título do livro", "class" : "form-control"}
                            ))
    description = forms.CharField(required=True, 
                            widget=forms.widgets.Textarea(
                            attrs={"placeholder" : "Descrição do livro", "class" : "form-control"}
                            ))
    year = forms.IntegerField(required=True, 
                            widget=forms.widgets.NumberInput(
                            attrs={"placeholder" : "Ano do livro", "class" : "form-control"}
                            ))
    genre = forms.CharField(required=True, 
                            widget=forms.widgets.TextInput(
                            attrs={"placeholder" : "Gênero do livro", "class" : "form-control"}
                            ))
    value = forms.IntegerField(required=True, 
                            widget=forms.widgets.NumberInput(
                            attrs={"placeholder" : "Ano do livro", "class" : "form-control"}
                            ))
    
    class Meta():
        model = Book
        fields = ('title', 'description', 'year', 'genre', 'value')