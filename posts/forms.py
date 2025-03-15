from django import forms
from .models import Post, Comment


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
        self.fields['title'].help_text = "Title should be at least 5 characters long."
        self.fields['content'].help_text = "Content should be at least 20 characters long."

    def clean_title(self):
        """
        Validate that the title is at least 5 characters long.
        """
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("The title must be at least 5 characters long.")
        return title

    def clean_content(self):
        """
        Validate that the content is at least 20 characters long and does not contain forbidden words.
        """
        content = self.cleaned_data.get('content')
        if len(content) < 20:
            raise forms.ValidationError("The content must be at least 20 characters long.")
        # Example check: Disallow certain forbidden words
        forbidden_words = ['forbidden', 'banned']
        for word in forbidden_words:
            if word in content.lower():
                raise forms.ValidationError(f"The content contains a forbidden word: '{word}'.")
        return content
