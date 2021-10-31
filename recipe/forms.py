from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    """
    Form for recipe review
    """
    class Meta:
        """
        Form has field of body from Review model
        """
        model = Review
        fields = ('body',)
