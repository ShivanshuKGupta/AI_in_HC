# %% [markdown]
# # Analysis

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Loading Dataset
meta_data = pd.read_csv("HAM10000_metadata.csv")

# Getting Labels
# all_labels = meta_data['dx']
labels = meta_data['dx'].isin(['bcc', 'mel', 'akiec'])
meta_attributes = meta_data[["dx", "dx_type", "age", "sex", "localization"]]

# missing value remove
imputer = SimpleImputer(strategy='most_frequent')
for col in meta_attributes.columns:
    # print(f"{col=}")
    meta_attributes[col] = imputer.fit_transform(meta_attributes[[col]]).ravel()

# %%
ages = meta_attributes['age']
n = len(meta_attributes)
samples_taken = ages.value_counts()
x = samples_taken.keys().sort_values()
y = []

for age in x:
    indices = meta_attributes['age']==age
    ratio = sum(meta_attributes[indices]['dx'].isin(['bcc', 'mel', 'akiec']))/samples_taken[age]
    # plt.text(x=age, y=ratio,s= "%.2f"%ratio, ha='center', va='bottom')
    y.append(ratio)

plt.plot(x, y)
plt.text(0, 0.5, "Here, we took the ratio instead of raw count\nso as to avoid biasness towards any age")
plt.ylabel("Ratio of count of cancer samples to total samples taken")
plt.xlabel("Age")
plt.xticks(ticks=range(0, 90, 5))
plt.title("Age vs Cancer Patients")
plt.show()
samples_taken

# %%
localizations = meta_attributes['localization']
# n = len(meta_attributes)
samples_taken = localizations.value_counts()
x = samples_taken.keys().sort_values()
y = []

for localization in x:
    indices = meta_attributes['localization']==localization
    y.append(sum(meta_attributes[indices]['dx'].isin(['bcc', 'mel', 'akiec']))/samples_taken[localization])

plt.plot(x, y)
plt.ylabel("Ratio of count of cancer samples to total samples taken")
plt.xlabel("Localization")
plt.title("Localization vs Cancer Patients")
plt.xticks(rotation='vertical')
plt.show()
samples_taken

# %%
dx_types = meta_attributes['dx_type']
# n = len(meta_attributes)
samples_taken = dx_types.value_counts()
x = samples_taken.keys().sort_values()
y = []

for dx_type in x:
    indices = meta_attributes['dx_type']==dx_type
    ratio = sum(meta_attributes[indices]['dx'].isin(['bcc', 'mel', 'akiec']))/samples_taken[dx_type]
    plt.text(x=dx_type, y=ratio,s= "%.2f"%ratio, ha='center', va='bottom')
    y.append(ratio)

plt.plot(x, y)
plt.ylabel("Ratio of count of cancer samples to total samples taken")
plt.xlabel("dx_type")
# plt.text(0, 0.5, "Here, we took the ratio instead of raw count\nso as to avoid biasness towards any age")
plt.title("dx_type vs Cancer Patients")
plt.xticks(rotation='vertical')
plt.show()
samples_taken

# %%
sexs = meta_attributes['sex']
samples_taken = sexs.value_counts()
x = samples_taken.keys().sort_values()
y = []

for sex in x:
    indices = meta_attributes['sex']==sex
    ratio = sum(meta_attributes[indices]['dx'].isin(['bcc', 'mel', 'akiec']))/samples_taken[sex]
    plt.text(x=sex, y=ratio,s= "%.2f"%ratio, ha='center', va='bottom')
    y.append(ratio)

plt.bar(x, y)
plt.ylabel("Ratio of count of cancer samples to total samples taken")
plt.xlabel("sex")
plt.title("sex vs Cancer Patients")
# plt.xticks(rotation='ho')
plt.show()
samples_taken


