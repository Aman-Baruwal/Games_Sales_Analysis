import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('vgsales.csv')

df.head()

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.info())

df.describe().T

for col in df.columns[:5]:
    print(f'{col} : {df[col].unique()}')
    print('-'*50)

plt.figure(figsize=(8,6))
sns.countplot(data = df , x = 'Platform', order=df['Platform'].value_counts().index, palette='magma')
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()