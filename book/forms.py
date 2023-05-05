from django import forms
from .models import book



class book_form(forms.ModelForm):
    class Meta:
        model=book
        fields=['title','author','publisher','publish_date','category']
        labels={'title':'Title','author':'Author','publisher':'Publisher','publish_date':'Publish_Date','category':'Category'}
        Choice=(
            ('Select','select'),
            ('Programming','Programming'),
            ('Ethics','Ethics'),
            ('Calculus','Calculus'),
            ('Social','Social'),
            ('Business','Business'),
            ('English literature','English Literature'),
            ('Hindi literature','Hindi Literature'),
            # ('Select'),
            # ('Programming'),
            # ('Ethics'),
            # ('Calculus'),
            # ('Social'),
            # ('Business'),
            # ('English literature'),
            # ('Hindi literature'),
        )
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control title','placeholder':'Title'}),
            'author':forms.TextInput(attrs={'class':'form-control author','placeholder':'author'}),
            'publisher':forms.TextInput(attrs={'class':'form-control publisher','placeholder':'publisher'}),
            'publish_date':forms.DateInput(attrs={'class':'form-control publish_date ','placeholder':'dd/mm/yyyy'}),
            'category':forms.Select(choices=Choice, attrs={'class':'form-control category','placeholder':'category'}),
        }