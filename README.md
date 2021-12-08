# Customer Personality Anaylsis using Python

:file_folder:Dataset: https://www.kaggle.com/imakash3011/customer-personality-analysis :file_folder:

In this project, unsupervised data clustering is performed on customers' records from a supermarket's database.

Customer segmentation is the practice of dividing customers into groups that reflect similarities among each other. Customers will be divided into segments to optimize the significance of each individual customer in the business, to modify products according to the distinct needs and behaviours of each customer, and also to help the business cater to the different concenrns of different types of customers.

## :mag:About the dataset:mag:
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

## :scissors:Data Cleaning:scissors:

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

## :wrench:Data Preprocessing:wrench:
The following steps are taken to preprocess the data:
1. Label encoding categorical features
2. Scaling features using a standard scaler
3. Generating a subset dataframe for reduction of dimensionality

### Dimensionality Reduction
Steps taken in this subsection:
- Dimensionality reduction with **Principal Component Analysis**
- Plotting of the reduced dataframe

## :family:Clustering:family:
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

## :bust_in_silhouette:Cluster Profiling:bust_in_silhouette:

### About Cluster Number 0:
- Definitely a parent
- Between 2 and 4 family members
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

### About Cluster Number 3:
- Definitely a parent
- Between 2 and 5 family members
- Majority have 1 teenager at home
- In the older age groups
- Low income group

## :page_with_curl:Conclusion:page_with_curl:
Throughout this project, unsupervised clustering has been performed. Dimensionality reduction was employed, followed by agglomerative clustering. Four clusters have been produced and used for customer profiling per cluster according to their household structures, income and spending. The information extracted can be used for planning future marketing strategies.

### Recommendation
The amount of spending exhibited by Groups 0, 1 and 2 appears to be proportional to their income, namely average income/spending, low income/spending and high income/spending, respectively.

However, Group 3 exhibits a disparity between spending and income amounts, namely low spending and high income. The ideal customer can be perceived as one which spends a proportional amount to their income, which is not the case for Group 3.

The recommendation is that the marketing team targets Group 3 with better-planned promotional campaigns, particularly those which provide more value per amount spent. This can be supported by evaluating the responsiveness of Group 3 towards sequential marketing campaigns. Group 3 is highly responsive to the first campaign, however, retention of interest towards promotions appears to drastically drop afterwards, whilst completely vanishing after the second campaign. There is strong indication that promotional campaigns conducted in the past have been largely unsatisfactory for the retailer's customer base, particularly for customers with sub-optimal income/spending proportions, such as those belonging to Group 3.

It must be noted that the nature of the promotional campaigns conducted in the past is not defined by this data set. For example, the data provided in this data set could be describing engagement towards campaigns for products with typically low purchase frequency, such as turkeys around Thanksgiving - whilst a promotional campaign for this product is likely to attract one large wave of purchases, the customers are very unlikely to re-purhcase a turkey after Thanksgiving, even when discounted.

Further analysis must be carried out to extract information to support the design of future promotional campaigns, such as:
- Average income of customers
- Average total spend of customers
- Average amount of time customers have been registered with the retailer for
- The most frequent education level amongst customers
