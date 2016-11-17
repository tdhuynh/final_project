from haystack import indexes
from sherlock.models import Profile, About

class ProfileIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr="user")
    first_name = indexes.CharField(model_attr="first_name")
    middle_name = indexes.CharField(model_attr="middle_name")
    last_name = indexes.CharField(model_attr="last_name")
    gender = indexes.CharField(model_attr="gender")
    joined = indexes.CharField(model_attr="joined")

    def get_model(self):
        return Profile

class AboutIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr="user")
    biography = indexes.CharField(model_attr="biography")
    birthdate = indexes.CharField(model_attr="birthdate")
    city_of_birth = indexes.CharField(model_attr="city_of_birth")
    state_of_birth = indexes.CharField(model_attr="state_of_birth")
    country_of_birth = indexes.CharField(model_attr="country_of_birth")
    sex_at_birth = indexes.CharField(model_attr="sex_at_birth")
    eye_color = indexes.CharField(model_attr="eye_color")
    mother_first_name = indexes.CharField(model_attr="mother_first_name")
    mother_maiden_name = indexes.CharField(model_attr="mother_maiden_name")
    mother_last_name = indexes.CharField(model_attr="mother_last_name")
    father_first_name = indexes.CharField(model_attr="father_first_name")
    father_last_name = indexes.CharField(model_attr="father_last_name")
    birth_hospital = indexes.CharField(model_attr="birth_hospital")
    searching_for = indexes.CharField(model_attr="searching_for")

    def get_model(self):
        return About