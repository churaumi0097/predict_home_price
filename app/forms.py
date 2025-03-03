from . import models
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ["area", "floor_num", "all_floor_num", "floor_plan", "room_size","structure","const_year",
        "station", "sun", "bath","toilet","bath_toilet" ,"add_bt", "kitchen", "conro", "conro_num",
        "storage","air_conditioning","barrier_free","comfort","building","outdoor",
        "energy","garbage","water_supply"]
  
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        required_fields = ["area", "floor_plan", "structure", "room_size", "const_year", "station"]
        for field in required_fields:
            self.fields[field].required = True
            self.fields[field].widget.attrs.update({
                "placeholder": "必須項目です",
                "class": "form-control"
            })

    # バリデーションのカスタムエラーメッセージ
    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            value = cleaned_data.get(field)
            if self.fields[field].required and not value:
                self.add_error(field, f"{self.fields[field].label}を入力してください。")
        return cleaned_data