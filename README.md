# Data-Cleaning






D206 DATA CLEANING  
Performance assessment
WGU- MSDA
Data cleaning assignment  using med_raw_data
Nefisa Hassen

Dr. Eric Straw
Assignment due 2/28/23






























Table of Contents
Part I: Research Question and Variables
A.Research Question and Variables.................................................................................................3
B. Required Variables and Examples...............................................................................................3
Part II: Data-Cleaning Plan (Detection)
C1. Data Cleaning Plan....................................................................................................................4
C2.  Reasoning for methods used....................................................................................................4
C3. Programming Language and Libraries.....................................................................................5
C4 codes used to detect duplicates, missing values, outliers .........................................................5
Part III: Data Cleaning (Treatment)
D1:cleaning findings.......................................................................................................................6
D2:justification of mitigation methods………………………………………………………….. 6
D3:summary of the outcomes…………………………………………………………..………..7
D4:mitigation code …………………………………………………………………………….7
D5:clean data……………………………………………………………………………………8
D6:limitations……………………………………………………………………………………9
D7:impact of limitations…………………………………………………………………………9
Part IV: PCA
E1. Principal Components List........................................................................................................9
E2:criteria used
E3:benefits……………………………………………………………………………………….10
F. Panopto Recording....................................................................................................................10
G. Web Source References.............................................................................................................10
H. Sources and References............................................................................................................10














Part I 
A.	Question
  What are the top 3 reasons ( medical conditions) that caused readmission?

B. The data set has 10,000 rows and 53 columns.  The data set has both categorical and numerical  responses. eg categorical  response such as ‘Yes’ or ‘No’  and numerical response for columns  such as income, population,  and age.
The data set includes the “ReAdmis” column  which shows patients who are readmitted to the hospital within a month of discharge.  The columns  such as high blood pressure, stroke, obesity, arthritis, diabetes, etc. show a patient's medical condition. patient information (service they received, days in hospital, type of initial admission, etc.) patient demographic information  such as gender, age, job, and  education. 8 columns  with survey responses from patients. 
The variable are names and data types are stated below
variables  and data types 	variables  and data types 
Unnamed: 0              int64
CaseOrder               int64
Customer_id            object
Interaction            object
UID                    object
City                   object
State                  object
County                 object
Zip                     int64
Lat                   float64
Lng                   float64
Population              int64
Area                   object
Timezone               object
Job                    object
Children              float64
Age                   float64
Education              object
Employment             object
Income                float64
Marital                object
Gender                 object
ReAdmis                object
VitD_levels           float64
Doc_visits              int64
Full_meals_eaten        int64
VitD_supp               int64
Soft_drink             object
Initial_admin          object
HighBlood              object
Stroke                 object
Complication_risk      object
Overweight            float64
Arthritis              object
	Diabetes               object
Hyperlipidemia         object
BackPain               object
Anxiety               float64
Allergic_rhinitis      object
Reflux_esophagitis     object
Asthma                 object
Services               object
Initial_days          float64
TotalCharge           float64
Additional_charges    float64
Item1                   int64
Item2                   int64
Item3                   int64
Item4                   int64
Item5                   int64
Item6                   int64
Item7                   int64
Item8                   int64



 C1:PLAN TO ASSESS QUALITY OF DATA

There are a few steps used to cleaning the Medical_raw_data.cvs file.  After importing the data in jupyter notebook, data was verified  via dtypes() function to show variables names and data types for each column. Next , unique values are displayed   by using the unique() function to clearly see unique values in a column.  
The plan to address  duplicate, missing values  and outlines are  as follows.
duplicate 
First the  unique() function was used to find unique values for the variables. In addition  For  ordinal categorical  data types, the value_counts() was used to display the count of each unique value in  a variable such as  education, complication_risk, Marital status, income, employment etc.  Each ordinal categorical  variable with yes/no  values was replaced by numerical values  0/1 to communicate to the algorithm that one the value is larger than the other  (Larose
& Larose, 2019 p.  36).  
Lastly to  detect duplicate  values the .duplicated() function was used.
data = med_data.loc[med_data.duplicated()] 
missing values
 The .isnull()  function was used to find variables with missing values. 
Outliers
  algorithm performs better when the data is standardized  (Larose
& Larose, 2019p. 39).  In order to identify outliers,  the first step is to  use  z scores to  standardize the data and identify outliers outside the range of  z scores >3  and <- 3.  The .std() function was used to  detect outliers  by looking at the standard deviation values for all the columns. 
C2.   The data contains missing values,  for multiple columns.  The treatment method is selected by  first plotting a graph  and explaining the distribution.  For columns whose graph has normal distribution, the missing values were replaced by the mean.  For columns with skewed  distribution  the median is used to replace the missing values.(Webinar 2: "Getting Started with Missing Values and Outliers" 
C3. 
 For this assignment I chose python. I find python easier to learn.  Python has simple syntax  which makes it easier to understand the codes. Python also has better visualization tools. 
Libraries and packages used
Pandas :used to import the data and 
Numpy: used for standard deviation
seaborn and matplotlib.pyplot: used to visualize data 
scipy import stats: the stats function used to find z score. 
 sklearn: to perform PCA

C4.   provide code
-Code to detect duplicates 
 data = med_data.loc[med_data.duplicated()]   
Code to detect missing value 
med_data.isnull().sum() 
-Code to detect outliers.
	To identity standard deviation  med_data.std() 
	 z variable created for each columns with outliers (population, income, TotalCharge,and adtionaly_charges)
   med_data ['Income_z']=stats.zscore(med_data['Income'])
med_data ['Population_z']=stats.zscore(med_data['Population'])
med_data ['TotalCharge_z']=stats.zscore(med_data['TotalCharge'])
med_data['Additional_charges_z']=stats.zscore(med_data['Additional_charges'])
	After creating the z variable, a new data set is created  containing only for outliers each  column below. 
med_data_outliers_income = med_data.query('Income_z > 3 | Income_z< -3')
med_data_outl_pop = med_data.query('Population_z > 3 | Population_z< -3')
med_data_outl_totalcharg = med_data.query('TotalCharge_z > 3 | TotalCharge_z< -3') # new dataset for containing outliers only 270 rows . can be fixed with median 
med_data_outliers_addCharg = med_data.query('Additional_charges_z > 3 |Additional_charges_z < -3') # new dataset created containing outliers only for the addtioncharge columns.  








Part III  data cleaning ( Treatment )
D1. 
Missing values were found on columns  such as children, age,income,soft drink,overweight, anxiety  and Initial days.  The number of missing values for each column with missing values are listed below.
Children              2588
Age                   2414
Soft_drink            2467
Overweight             982
Anxiety                984
Initial_days          1056
Identifying duplicates 
No duplicated columns were found. 
Identifying outliers
 By looking at the standard deviation  the columns  population, income, TotalCharge,and adtionaly_charges  have possible  outliers.  Z score is used to identify outliers for each column.  Income  has 180 outliers,
population 218
Total Charge 276
additional charge  0. 
Because the column addtionalCharge showed no outliers. Boxplot was to verify outliers. boxplot=seaborn.boxplot (x='Additional_charges', data =med_data)  by looking at the plotbox the outliers are seen clearly. The outliers are additional charges  above $27,000 
 


D2.   
There was no duplicate found, as a result  no treatment. 
 data = med_data.loc[med_data.duplicated()]   
Missing values are treated via imputation. By using the replace function, the missing values were replaced with the median values. 

By calculating the standard deviation, columns  such as  population, income, TotalCharge,and adtionaly_charges  showed possible outliers. To further investigate the data, z variable is created  and a new data set created containing only outliers for column population, income, TotalCharge. 
 The number of outliers per column is listed below. Considering the reach of  the column below it has a significant number of outliers. Imputation,  exclusion can affect the data. As a result  data retention is the best option. 
Income  has 180 outliers,
population 218
Total Charge 276
additional charge  0. The column  additional _charges showed no outliers with z score. To better analyze this, boxplot was used and outliers were identified. 
boxplot=seaborn.boxplot (x='Additional_charges', data =med_data). By looking at the graph. There are lots of outliers in the columns. 

D3.  and D4.
# remove unnamed columns
md = med_data.drop(med_data.columns[0], axis =1)
#replacing missing values with median or mean.  
med = med_data['Children'].fillna(med_data['Children'].median(), inplace = True) 
mean_val = med_data['Age'].fillna(med_data['Age'].mean(), inplace = True)
median_val = med_data['Income'].fillna(med_data['Income'].median(), inplace = True)
median_val = med_data['Overweight'].fillna(med_data['Overweight'].median(), inplace = True)
median_val = med_data['Anxiety'].fillna(med_data['Anxiety'].mean(), inplace = True)
median_val = med_data['Initial_days'].fillna(med_data['Initial_days'].median(), inplace = True)

# verifying there is no  missing data.  
med_data.isnull().sum() 
 
 No duplicated rows.
 
Outliers 

 -Creating  a  Z variable 
med_data ['Income_z']=stats.zscore(med_data['Income'])
med_data ['Population_z']=stats.zscore(med_data['Population'])
med_data ['TotalCharge_z']=stats.zscore(med_data['TotalCharge'])
med_data['Additional_charges_z'] = stats.zscore(med_data['Additional_charges'])

-Calculate z score to extract outlines outside 
med_data_outliers_income = med_data.query('Income_z > 3 | Income_z< -3')
med_data_outl_pop = med_data.query('Population_z > 3 | Population_z< -3')
med_data_outl_totalcharg = med_data.query('TotalCharge_z > 3 | TotalCharge_z< -3') 
med_data_outliers_addCharg = med_data.query('Additional_charges_z > 3 | Additional_charges_z < -3') 


Changing  categorical variables to numeric values. This code is used to all the categorical variables  to  change it to numerical value ( see the attached code)
med_data['ReAdmis_z']= med_data['ReAdmis']
ReAdmis_New ={" ReAdmis_New":{"yes":1,"No":0,"unknown":np.NAN}}

 See z variables with numeric values  for Income_z, Population_z, TotalCharge_z
  



D5. see clean data attached below. MSDA206_PA.CSV

D6.Univarial imputation method is used to treat missing values by replacing  median/ mean values. Although this method  does not reduce the sample size, it could distort the distribution of the data.
D7. One of the main issues a data analyst might encounter is not having a contact person from the organization that collected this data. It is important to have a way to ask questions and get a better understanding of the data. 
Part IV:PCA
 E1.variables used for PCA 
●	  Item1: Timely admission 
●	 Item2: Timely treatment 
●	 Item3: Timely visits 
●	 Item4: Reliability 
●	 Item5: Options 
●	Item6: Hours of treatment 
●	Item7: Courteous staff 
●	 Item8: Evidence of active listening from doctor


 
E2. based on the graph below PC values 0 and 1 should be kept as the variable shows strong connections E3. Benefits of PCA
 Performing PCA on the survey response with 8 questions helped to identify which survey question had more effect on  improving the patient's experience in the hospital. Looking at the result for the PCA   Item1(Timely admission )and   Item2( Timely treatment ) have stronger connections. The hospital can work to improve their admission process and resolve the wait time  for patients to receive  treatment. 


F.

G. No Third-Party Code Reference used. 

H.
EBSCO Discovery Service - Academic Libraries: EBSCO. EBSCO Information Services, Inc. | www.ebsco.com. (n.d.). Retrieved February 27, 2023, from https://www.ebsco.com/academic-libraries/products/ebsco-discovery-service 




