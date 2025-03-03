from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Post
from .forms import PostForm
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib 
import os
import lightgbm
from django.shortcuts import get_object_or_404



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "static", "le_pkl", "model.joblib")
load_model = joblib.load(model_path)


def make_dataframe(post,BASE_DIR):
    df = pd.DataFrame([post])
    df.columns = ["city", "ground_num", "const_floor_num", "間取り", "area", "建物構造", "const_year",
                  "ns_time", "sun", "kind_bath", "kind_toilet", "sep_bath_toilet", "add_bt",
                  "kind_kitchen", "kind_conro", "num_conro",
                  'storage', 'air_conditioning', 'barrier_free', 'comfort', 'building_features',
                  'outdoor_space', 'energy', 'garbage', 'water_facilities']
    df = df.replace({None:"nan", '':"nan"})
    return df



cols = ["add_bt","kind_kitchen","kind_conro",'storage','air_conditioning', 'barrier_free', 'comfort', 'building_features','outdoor_space', 'energy', 'garbage', 'water_facilities']

def pretreatment(df, cols):
    for col in cols:
        df[col] = df[col].apply(lambda x: list(x) if isinstance(x, (list, tuple)) else x)
        df[col] = df[col].apply(lambda x: [item for item in x if item != ''] if isinstance(x, list) else x)
        df[col] = df[col].apply(
            lambda x: " ".join(x) if isinstance(x, list) and len(x) >= 2 else 
            (x[0] if isinstance(x, list) and len(x) == 1 else x)
        )
        df[col] = df[col].apply(lambda x: " ".join(x) if isinstance(x, list) else x)
    
    return df


le_cols = ["city","間取り","建物構造","kind_bath","kind_toilet","add_bt","kind_kitchen","kind_conro",'storage','air_conditioning', 'barrier_free', 'comfort', 'building_features','outdoor_space', 'energy', 'garbage', 'water_facilities']

def le(df, le_cols, BASE_DIR):
    for col in le_cols:
        df[col] = df[col].replace("", "nan")
        le_load = joblib.load(os.path.join(BASE_DIR, "static", "le_pkl", f"{col}.pkl"))
        known_classes = set(le_load.classes_)  
        unknown_values = set(df[col]) - known_classes  
        if unknown_values:
            raise ValueError(f"Column '{col}' contains unseen labels: {unknown_values}")
        df[col] = le_load.transform(df[col])  
    return df

    
def predict(df,load_model):
    ypred = load_model.predict(df)
    df["predict"] = ypred
    return df



class Home(TemplateView):
    template_name = "home.html"

class Predict(CreateView):
    model = Post
    form_class = PostForm
    template_name = "predict.html"

    def form_valid(self, form):
        form_data = form.cleaned_data
        df = make_dataframe(form_data,BASE_DIR) 
        pre_df = pretreatment(df,cols)
        le_df = le(pre_df,le_cols,BASE_DIR)
        price_df = predict(le_df,load_model)
        price = int(price_df["predict"].iloc[0])

        post_instance = form.save(commit=False) 
        post_instance.predict_price = price  
        post_instance.save() 

        self.object = post_instance
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("result", kwargs={"pk": self.object.pk})


class Result(TemplateView):
    template_name = "result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        context["post"] = post
        return context