from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('content', 'image')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': "What's on your mind?"}),
        }
    def clean_content(self):
        content = self.cleaned_data.get('content')
        prohibited_words = ['shit', 'fuck', 'bobo']
        if any(word in content.lower() for word in prohibited_words):
            raise forms.ValidationError("Your tweet contains a prohibited word.")
        return content



