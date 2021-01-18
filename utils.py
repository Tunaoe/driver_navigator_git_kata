import pandas as pd


def get_female_passengers():
    titanic = pd.read_csv('data/titanic_train.csv')
    titanic_f = titanic[titanic['Sex']=='male']
    return titanic_f