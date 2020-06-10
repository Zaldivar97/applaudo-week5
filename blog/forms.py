from django import forms

from .models import Post, Tag


class PostCreateForm(forms.ModelForm):
    TAG_CHOICES = [(tag.id, tag.name) for tag in Tag.objects.all()]
    title = forms.CharField(label='')
    content = forms.CharField(label='', widget=forms.Textarea())
    tags = forms.MultipleChoiceField(
        label='',
        widget=forms.CheckboxSelectMultiple,
        choices=TAG_CHOICES
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
