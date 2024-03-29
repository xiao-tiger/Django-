from django import forms
from apps.forms import FormMixin
from apps.news.models import News
from apps.news.models import Banners
from apps.course.models import Course


class EditNewsCategory(forms.Form, FormMixin):
    pk = forms.IntegerField()
    name = forms.CharField(max_length=200)


class NewsForm(forms.ModelForm, FormMixin):
    category = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['pub_time', 'category', 'author']


class EditNewsForm(forms.ModelForm, FormMixin):
    pk = forms.IntegerField()
    category = forms.IntegerField()

    class Meta:
        model = News
        exclude = ['pub_time', 'category', 'author']


class BannerForm(forms.ModelForm, FormMixin):

    class Meta:
        model = Banners
        fields = ['priority', 'image_url', 'link_to']


class EditBannerForm(forms.ModelForm, FormMixin):
    pk = forms.IntegerField()

    class Meta:
        model = Banners
        fields = ['priority', 'image_url', 'link_to']


class CourseForm(forms.ModelForm, FormMixin):
    category = forms.IntegerField()
    teacher = forms.IntegerField()

    class Meta:
        model = Course
        exclude = ['category', 'teacher', 'pub_time']



