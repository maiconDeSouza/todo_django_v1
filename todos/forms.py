from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title',)

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 3:
            self.add_error(
                'title', 'A tarefa deve ter três ou mais letras')
        return title
