'''
Bussiness Problem:
    
Number of pallets should be stored  in inventory for shipping to different customers is very volatile leading to understocking or overstocking  understocking leading to not honoring client requirements and overstocking is leading to inventory cost .
 
Bussiness Objective:
    Minimize the volatile in inventory Stock.
    
Bussiness Constrain:
    Reduce the human invention
    
Sucess Criteria :
    
 Bussiness Sucess Criteria:
    Reduce the Volatlity by atleasst 90%
    
Machine Learning Sucess Criteria :
    Achive an accuracy by atleast 96%
    
Economics Sucess Criteria:
Achive a cost saving of at least $Im

''''
 Load the Data
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt  
 
from feature_engine.outliers import Winsorizer
from sklearn.preprocessing import OneHotEncoder
from sqlalchemy import create_engine 

import pymysql

# MySQL database connection details
db_host = 'your_host'
db_user = 'your_username'
db_password = 'your_password'
db_name = 'your_database'

# Excel file path
excel_file = 'C:C:/Users/Lenovo/Downloads/Data Set (2)/pallet_Masked_fulldata.xlsx'

# Create a database connection

from pymysql import connect
import pandas as pd
data_base = connect(host = 'localhost',
                    user = 'root',
                    password = 'Aaksshay03$')
connection = pymysql.connect(
   
   user = 'root'  # user name,
   pw = 'Aaksshay03$'  # password,
   db =  'pallet_masked_fulldata'  # database name,
   engine = create_engine(f"mysql+pymysql://{user}:{pw}@localhost/{db}")
)

try:
    # Read data from the Excel file into a DataFrame
    df = pd.read_excel(excel_file, engine='openpyxl')

    # Insert the data into the MySQL table
    df.to_sql('Pallets_data', con=connection, if_exists='replace', index=False)

finally:
    # Close the database connection
    connection.close()
# to_sql() - function to push the dataframe onto a SQL table.
pallet_data.to_sql('univ_tbl', con = engine, if_exists = 'replace', chunksize = 1000, index = False)

sql = 'select * from pallet_data_tbl;'
df = pd.read_sql_query(sql, engine)







df = pd.read_excel(r"C:/Users/Lenovo/Downloads/Data Set (2)/pallet_Masked_fulldata.xlsx")
df.describe()
df.info()
df.isna().sum()
df.duplicated().sum()
# Create dummy variables
df_new = pd.get_dummies(df)
df.mean()
df.median()
df.mode()

df.std()
df.var()
df.max()
df.min()


df.isnull().sum()
df.tail()


###   AUTO EDA VISUALIZATIONS 



import matplotlib.pyplot as plt

plt.bar(x=range(80962), height=df.CustName)
plt.bar(x=range(80962),height=df.QTY)
plt.bar(x=range(80962), height=df.WHName)

plt.hist(df.CustName)
plt.hist(df.QTY)
plt.hist(df.WHName)

plt.boxplot(df.CustName, vert=0)
plt.boxplot(df.QTY, vert=0)
plt.boxplot(df.WHName, vert=0)


import seaborn as sns

sns.displot(df.CustName) #Deprecated histogram function from seaborn ,Distrubution plot

sns.displot(df.QTY) # Histogram from seaborn

sns.displot(df.WHName)


# Density Plot

sns.kdeplot(df.CustName, bw =1, fill = True)

sns.kdeplot(df.QTY ,bw = 1, fill = True)

sns.kdeplot(df.WHName, bw  = 1, fill = True)

# Duplicates in rows 
duplicate = df.duplicated()  # Returns Boolean Seriers denoting duplicate rows.
duplicate

sum(duplicate)
# We  can correlation coeffient values to identify coloumns which have duplicate infomation.
df.corr()

df.isnull().sum()

# Auto EDA 


import sweetviz as sv

s = sv.analyze(df)
s.show_html()






df.CustName = df.CustName.astype('str')
df.dtypes

df.WHName = df.WHName.astype('str')
df.dtypes


plt.boxplot(df.QTY)
#Creating duplicate of data frame before treating outliers 
df1 = df.copy()
#Deleting negative values
df = df.drop(df.index[df['QTY']< 0])

plt.boxplot(df.QTY, vert=0)

############################# OUTLIERS TREATMENT #########################
# Let's find outliers in QTY
sns.boxplot(df.QTY)

# Detection of outliers  (find limits  for QTY based on IQR)
IQR = df['QTY'].quantile(0.75)  - df['QTY'].quantile(0.25)

lower_limit = df['QTY'].quantile(0.25)-(IQR * 1.5)
upper_limit = df['QTY'].quantile(0.75)+(IQR * 1.5)   


############################# 1. Remove (let's trim the dataset) ######################
# Trimming Technique
# Let's flag the outliers in the dataset 
outliers_df = np.where(df.QTY> upper_limit,True,False)
df_trimmed = df.loc[~(outliers_df), ] 
df.shape, df_trimmed.shape
df['df_replaced'] = np.where(df['QTY'] > upper_limit, upper_limit, df['QTY'])
sns.boxplot(df.df_replaced) 

# Define the model with IQR method
winsor_iqr = Winsorizer(capping_method = 'iqr',
                        # choose IQR rule boundariers or gaussian for mean and std
                          tail = 'right', # cap left ,right or both tails 
                          fold = 1.5,
                          variables = (['QTY'])
df_s = winsor_iqr.fit_transform(df[['QTY']])
winsor_iqr = 42  # Define winsor_iqr as a variable with a value of 42

# Inspect the minimum caps and maximum caps 
# winsor.left_tail_caps _,  winsor.right_tail_caps_
# Let's see boxplot 
sns.boxplot(df_s.QTY)

# Define the model with Gaussian method
winsor_gaussian  = Winsorization(capping_method = 'gaussian',
                                 #choose IQR rule boundariers or gaussian for mean and std
                                tail = 'right',# cap left ,right or both tails
                                fold = 3 ,
                                variables =  ['QTY'])
df_t = winsor_gaussian.fit_transform(df[['QTY']])
sns.boxplot(df_t.QTY)
# Define the model with percentiles:
# Default values
# Right tail : 95th percentile
# Left tail : 5th percentile
   feature engine           transformation
   = transformation.YeoJohnsonTransformer(variables = 'QTY')
   u_tf = tf.fit_transform(df)
   
   ob = stats.probplot(edu_tf.QTY,dist = stats.norm,plot = pylab)

#####################################################################################################################
################################# Standardization and Normalisation ###########
# Standardization 
from sklearn.preprocessing import StandardScaler



# Create a StandardScaler object
scaler = StandardScaler()

# Fit the scaler to your data and transform the data
scaled_data = scaler.fit_transform(df[['QTY']])
Convert the array back to a dataframe
df = pd.DataFrame(df)
Modified df = dataset.describe()

# Normalization 
load dataset 
# Normalization function - Custom Function 
Range converts to  : 0 to 1
from norm_func(i):
    x = (i-i.min())/(i.max()-i.min())
    return(x)



import pandas as pd
# Define your normalization function (replace this with your actual normalization function)
def norm_func(x):
    # Your normalization logic here
    # For example, you can use Min-Max normalization:
    return (x - x.min()) / (x.max() - x.min())

# Create a DataFrame (replace 'data' with your actual data)
data = {'QTY': [50, 125,125,125,150]}
df = pd.DataFrame(data)

# Apply the normalization function to the 'QTY' column
df['QTY_normalized'] = norm_func(df['QTY'])

# Describe the DataFrame with the normalized column
df_norm = df.describe()

# Display the resulting DataFrame
print(df_norm)

Random_imputer = RandomSampleImputer(['QTY'])
["QTY_new"] = pd.DataFrame(random_imputer.fit_transform(df[["QTY_new"]]))
["QTY_new"].isna().sum()
.isna().sum()

########################
Normal Quantile-Quantile Plot

Checking whether data is normally distrubuted
sats.probplot(df.QTY,dist = "norm",plot = pylab)
Yeo- Johnson Transform


'''We can apply it to our dataset without scaling the data.
We supports zero values and negative values.It does not require the value for 
which input variable to be strictly postive.'''

pob = stats.probplot(df.QTY,dist = stats.norm,plot = pylab)
norm feature_engine import transformation 
Set up the variable transformer

