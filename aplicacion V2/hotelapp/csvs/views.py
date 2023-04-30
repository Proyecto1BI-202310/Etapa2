from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csv
from comentarios.models import Comentario
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

# Create your views here.

def upload_file_view(request):
    Csv.objects.all().delete()
    Comentario.objects.all().delete()
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pipelineTres.pkl')


        # Proceso de prueba del cliente
        df_recent = pd.read_csv(obj.file_name.path) # Lectura de los datos recientes

        with open(path, 'rb') as f:
            pipeline = pickle.load(f)

        y_predicted =  pipeline.predict(df_recent)
        for index, row in df_recent.iterrows():
            if index==0:
                pass
            else:

                neg = y_predicted[index]
                nega = False
                if neg==0:
                    nega=True
                else:
                    nega=False
                Comentario.objects.create(
                    idd = index,
                    title = row[1],
                    rating = int(row[2]),
                    texto = row[3],
                    location = row[4],
                    hotel = row[5],
                    negativo= nega
                    
                )
            
        obj.activated=True
        obj.save()


    return render(request, 'csvs/upload.html', {'form': form})
