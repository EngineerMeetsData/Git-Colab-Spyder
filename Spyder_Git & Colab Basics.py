# Spyder_Git & Colab Basics

print ("Git & Colab Basics")

import pandas as pd
df = pd.read_csv('DataSeerGrabPrizeData.csv')

df.describe()

df = df.dropna()

df.describe()

df.to_csv('Spyder_Grab Dataset NEW.csv', index=False)
