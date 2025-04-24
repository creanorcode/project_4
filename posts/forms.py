from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email adress", required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First name", required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name  = forms.CharField(label="Last name", required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    """
    Form for creating and editing a Post.
    This form includes custom validation and dynamic widget customization.
    """
    class Meta:
        model = Post
        # Define which fields to include in the form
        fields = ['title', 'content', 'category']
        # Define widget with Bootstrap classes and placeholders for better UX
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title here'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter the post content here'
            }),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Optional adjust field attributes dynamically.
        Here we add help texts to guide the user.
        """
        super().__init__(*args, **kwargs)
        self.fields['title'].help_text = "Title should be at \
        least 5 characters long."
        self.fields['content'].help_text = "Content should be \
        at least 20 characters long."

    def clean_title(self):
        """
        Validate that the title is at least 5 characters long.
        """
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("The title must \
            be at least 5 characters long.")
        return title

    def clean_content(self):
        """
        Validate that the content is at least 20
        characters long and does not contain forbidden words.
        """
        content = self.cleaned_data.get('content')
        if len(content) < 20:
            raise forms.ValidationError("The content \
            must be at least 20 characters long.")
        # Example check: Disallow certain forbidden words
        forbidden_words = ['forbidden', 'banned']
        for word in forbidden_words:
            if word in content.lower():
                raise forms.ValidationError(f"The content \
                contains a forbidden word: '{word}'.")
        return content


class CommentForm(forms.ModelForm):
    """
    Form for creating a Comment on a Post.
    This form includes basic validation and Bootstrap widget styling.
    """
    class Meta:
        model = Comment
        fields = ['content']
        # Use Bootstrap classes with a placeholder for the comment field
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write your comment here'
            }),
        }

    def __init__(self, *args, **kwargs):
        """
        Add help text to the comment field.
        """
        super().__init__(*args, **kwargs)
        self.fields['content'].help_text = "Please ensure your \
        comment is meaningful and at least 5 characters long."

    def clean_content(self):
        """
        Validate that the comment is at least 5 characters long.
        """
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError("The comment \
            must be at least 5 characters long.")
        return content
