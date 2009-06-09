from django.test import TestCase
from django import forms
from django.forms.forms import BoundField
from form_helpers.templatetags import form_helpers

class MockForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    middle_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100)

class TestFormTemplateTags(TestCase):
    
    def test_render_field(self):
        form = MockForm()
        field = BoundField(form, form.fields['first_name'], 'first_name')
        form_helpers.render_field(field)
        self.assertEqual(True, True)
