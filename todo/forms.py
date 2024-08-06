from django import forms
from .models import ToDoItem

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description']  # フォームに含めるモデルのフィールドを指定

        # カスタマイズしたい場合は、ウィジェットを定義
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter the description'}),
        }
