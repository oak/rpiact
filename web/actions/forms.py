# -*- coding: utf-8 -*-
__author__ = 'adcarvalho'
from django import forms
from web.models import Action


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action