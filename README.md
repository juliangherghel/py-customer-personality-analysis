# Customer Personality Anaylsis using Python

Dataset: https://www.kaggle.com/imakash3011/customer-personality-analysis

In this project, unsupervised data clustering is performed on customers' records from a supermarket's database.

Customer segmentation is the practice of dividing customers into groups that reflect similarities among each other. Customers will be divided into segments to optimize the significance of each individual customer in the business, to modify products according to the distinct needs and behaviours of each customer, and also to help the business cater to the different concenrns of different types of customers.

## :mag: About the dataset :mag::
The dataset consists of 2240 datapoints and 29 attributes. This can be re-organized into the following subsets:
### Customer's Information
- ID
- Year_Birth
- Education
- Marital_Status
- Income
- Kidhome
- Teenhome
- Dt_Customer
- Recency
- Complain

### Products
Amount spent on different products in the last 2 years
- MntWines
- MntFruits
- MntMeatProducts
- MntFishProducts
- MntSweetProducts
- MntGoldProds

### Place
- NumWebPurchases
- NumCatalogPurchases
- NumStorePurchases
- NumWebVisitsMonth

### Promotion
- NumDealsPurchases
- AcceptedCmp1
- AcceptedCmp2
- AcceptedCmp3
- AcceptedCmp4
- AcceptedCmp5
- Response

## Data Cleaning

An overview of the work carried out in this section encompasses the following:
1. Removal of missing values
2. Creation of a new feature (**"Customer_For"**) out of **"Dt_Customer"**
3. Engineering further new features
   - **"Age"** from **"Year_Birth"**
   - **"Spent"** indicating the total amount spent on products over the past two years
   - **"Living_With"** from **"Marital_Status"**
   - **"Children"** indicating the total amount of children in a household, including kids **and** teenagers
   - **"Family_Size"** indicating the total amount of people in a household
   - **"Is_Parent"** to indicate parenthood status
4. Divise three new categories in **"Education"** by simplifying existent value counts
5. Dropping redundant features

## Data Preprocessing
The following steps are taken to preprocess the data:
1. Label encoding categorical features
2. Scaling features using a standard scaler
3. Generating a subset dataframe for reduction of dimensionality

### Dimensionality Reduction
Steps taken in this subsection:
- Dimensionality reduction with **Principal Component Analysis**
- Plotting of the reduced dataframe

## Clustering
To apply clustering, the following steps have been taken:
1. **Elbow Method** to determine the required number of clusters
2. Clustering via **Agglomerative Clustering**
3. Evaluating the clusters formed via scatter plotting

### Income vs Spending
![Clusters' Profiles based on Income and Spending](/output/7.png)

The following patterns are identified:
- Group 0: average spending & average income
- Group 1: low spending & low income
- Group 2: high spending & high income
- Group 3: low spending & high income

## Cluster Profiling

### About Cluster Number 0:
- Definitely a parent
- Betweent 2 and 4 family members
- Most have a teenager at home
- In the older age groups

### About Cluster Number 1:
- Majority are parents
- Max 3 family members
- Majority have 1 kid (typically not teenagers)
- In the younger age groups

### About Cluster Number 2:
- Definitely not a parent
- Max 2 members in the family
- Slight majority of couples over single people
- Span all age groups
- High income group

### About Cluster Number 4:
- Definitely a parent
- Between 2 and 5 family members
- Majority have 1 teenager at home
- In the older age groups
- Low income group

## Conclusion
Throughout this project, unsupervised clustering has been performed. Dimensionality reducation was employed, followed by agglomerative clustering. Four clusters have been produced and used for customer profiling per cluster according to their household structures, income and spending. The information extracted can be used for planning future marketing strategies.
