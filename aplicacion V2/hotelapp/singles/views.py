from django.shortcuts import render
from django.http import HttpResponse
from .forms import SingleModelForm
import numpy as np
import pandas as pd
import joblib
import pickle
import os
from joblib import *
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from random import *
from .multiply_columns_transformer import MultiplyColumns
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from .models import Single
def ingresar(request):
    coso = Single.objects.first()
    #Single.objects.all().delete()
    form = SingleModelForm()
    obj = Single.objects.get(activated=False)
    form = SingleModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pipelineTres.pkl')

        review = obj.texto

        df_recent = pd.DataFrame({"review_text": [review]})
        with open(path, 'rb') as f:
            pipeline = pickle.load(f)

        y_predicted =  pipeline.predict(df_recent)

        
        #Single.objects.all().delete()
        neg = y_predicted[0]
        print(neg)
        nega = False
        if neg==0:
            nega=True
        else:
            nega=False
        Single.objects.create(
            texto = review,
            negativo= nega
        )
            
            
        obj.activated=True
        obj.save()
        coso = Single.objects.first()
    return render(request, 'ingresar.html', {'comment': coso})

def result(request):
    comment = Single.objects.first()
    

    return render(request, 'result.html', {'comment': comment})

