from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description"]
        error_messages = {
            "title": {
                "required": "Bu alan boş birakilamaz.",  # Custom error message for required field
            },
            "description": {
                "required": "Bu alan boş birakilamaz.",
            },
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 4:
            raise forms.ValidationError("Title must be at least 4 characters long.")
        if len(title) > 12:
            raise forms.ValidationError("Title cannot exceed 12 characters.")
        return title

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if len(description) < 4:
            raise forms.ValidationError("Description must be at least 4 characters long.")
        if len(description) > 12:
            raise forms.ValidationError("Description cannot exceed 12 characters.")
        return description
