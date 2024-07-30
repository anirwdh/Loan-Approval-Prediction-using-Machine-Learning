import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv("LoanApprovalPrediction.csv") 
data.head(5)
obj = (data.dtypes == 'object') 
print("Categorical variables:",len(list(obj[obj].index)))

# Dropping Loan_ID column 
data.drop(['Loan_ID'],axis=1,inplace=True)

obj = (data.dtypes == 'object') 
object_cols = list(obj[obj].index) 
plt.figure(figsize=(18,36)) 
index = 1

for col in object_cols: 
y = data[col].value_counts() 
plt.subplot(11,4,index) 
plt.xticks(rotation=90) 
sns.barplot(x=list(y.index), y=y) 
index +=1
# Import label encoder 
from sklearn import preprocessing 
	
# label_encoder object knows how 
# to understand word labels. 
label_encoder = preprocessing.LabelEncoder() 
obj = (data.dtypes == 'object') 
for col in list(obj[obj].index): 
data[col] = label_encoder.fit_transform(data[col])

# To find the number of columns with 
# datatype==object 
obj = (data.dtypes == 'object') 
print("Categorical variables:",len(list(obj[obj].index)))

plt.figure(figsize=(12,6)) 

sns.heatmap(data.corr(),cmap='BrBG',fmt='.2f', 
			linewidths=2,annot=True)
sns.catplot(x="Gender", y="Married", 
			hue="Loan_Status", 
			kind="bar", 
			data=data)
