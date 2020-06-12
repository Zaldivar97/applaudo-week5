from django import forms

from .models import Post, Tag


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='',
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Title of the post'}
                            )
                            )
    content = forms.CharField(label='', widget=forms.Textarea(), required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects,
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
