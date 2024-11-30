#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pylab
import statsmodels.api as sm
import statistics
from scipy import stats
from scipy.stats import chisquare
from scipy.stats import chi2_contingency


# In[39]:


df = pd.read_csv("medical_clean.csv")


# In[40]:


df.rename(columns = {'Item1':'TimelyAdmission', 
                    'Item2':'TimelyTreatment', 
                     'Item3':'TimelyVisits', 
                     'Item4':'Reliability', 
                     'Item5':'Options', 
                     'Item6':'HoursOfTreatment', 
                     'Item7':'CourteousStaff', 
                     'Item8':'EvidenceOfActiveListening'}, 
          inplace=True)


# In[41]:


contingency = pd.crosstab(df['ReAdmis'], df['Gender'])


# In[42]:


#B2. output
#stat, p, dof, expected = chi2_contingency(contingency )
c, p, dof, expected = chi2_contingency(contingency)

# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')


# # C1 Univarites statistics 
# two catagorical variable 
#      Readmis, gender
# two continuses variable 
#      timely admission, timely treatment 

# In[43]:


# Create histograms of contiuous & categorical variables
df[['TimelyAdmission','TimelyTreatment']].hist()
plt.savefig('medical_clean.jpg')
plt.tight_layout()


# In[44]:


df.describe()


# In[45]:


groupedGender = df.groupby(by= 'Gender').size()
groupedGender


# In[46]:


get_ipython().run_line_magic('matplotlib', 'inline')
groupedGender.plot.bar()


# In[47]:


groupedReAdmis = df.groupby(by= 'ReAdmis').size()
groupedReAdmis


# In[48]:


get_ipython().run_line_magic('matplotlib', 'inline')
groupedReAdmis.plot.bar()


# In[49]:


sns.boxplot('TimelyAdmission', data = df )
plt.show()


# In[50]:


sns.boxplot('TimelyTreatment', data = df)
plt.show()


# In[ ]:





# In[37]:


boxplt= df[['TimelyAdmission','TimelyTreatment']].plot(kind = 'box',title = 'TimelyAdmission vs TimelyTreatment')
plt.show()


# In[51]:


sns.histplot(binwidth=0.5, x= "Gender", hue="ReAdmis", data=df, stat="count", multiple="stack")


# In[ ]:





# In[ ]:





# In[ ]:




