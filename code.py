import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
data = pd.read_csv("/content/drive/MyDrive/datasets/exam.csv")
data.head()

# Define the new column names
new_column_names = [
    'Date_received', 'Product', 'Sub_product', 'Consumer_complaint_narrative',
    'Company_public_response', 'Company', 'State', 'ZIP_code', 'Submitted_via',
    'Company_response_to_consumer', 'Timely_response', 'Consumer_disputed'
]

# Rename the columns
data.columns = new_column_names

# Display the modified DataFrame
print(data.head())


# Get the sum of null values in each column
null_counts = data.isnull().sum()

# Get the total number of values in each column
total_counts = data.count()

# Calculate the non-null counts in each column
non_null_counts = total_counts - null_counts

# Combine the null, total, and non-null counts into a DataFrame
summary_df = pd.DataFrame({
    'Null_Counts': null_counts,
    'Total_Counts': total_counts,
    'Non_Null_Counts': non_null_counts
})

# Print the summary DataFrame
print(summary_df)


# Convert 'Date_received' column to datetime format
data['Date_received'] = pd.to_datetime(data['Date_received'])

# Extract year from the 'Date_received' column
data['Year'] = data['Date_received'].dt.year

# Group data by year and calculate the counts for each year
yearly_counts = data['Year'].value_counts().sort_index()

# Create a plot for each year
plt.figure(figsize=(10, 6))
plt.bar(yearly_counts.index, yearly_counts.values, color='blue')
plt.xlabel('Year')
plt.ylabel('Number of Complaints')
plt.title('Number of Complaints per Year')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Group data by 'Product' and calculate the counts for each product
product_counts = data['Product'].value_counts()

# Create a bar plot for each product
plt.figure(figsize=(12, 8))
product_counts.plot(kind='bar', color='blue')
plt.xlabel('Product')
plt.ylabel('Number of Complaints')
plt.title('Number of Complaints per Product')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



# Group data by 'Product' and 'Date_received', then calculate the counts for each group
product_time_counts = data.groupby(['Product', 'Date_received']).size().unstack()

# Create a plot for each product's complaints over time
plt.figure(figsize=(12, 8))
product_time_counts.plot(kind='line', marker='o', markersize=5)
plt.xlabel('Date Received')
plt.ylabel('Number of Complaints')
plt.title('Complaints Over Time for Each Product')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Adjust legend position
plt.subplots_adjust(right=0.85)  # Adjust subplot layout
plt.show()




# Extract year from the 'Date_received' column
data['Year'] = data['Date_received'].dt.year

# Group data by 'Product' and 'Year', then calculate the counts for each group
product_year_counts = data.groupby(['Product', 'Year']).size().unstack()

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(product_year_counts, cmap='YlGnBu', annot=True)
plt.xlabel('Year')
plt.ylabel('Product')
plt.title('Complaints Against Each Product Over the Years')
plt.tight_layout()
plt.show()




# Group data by 'Company_response_to_consumer' and calculate the counts for each group
response_counts = data['Company_response_to_consumer'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
response_counts.plot(kind='bar', color='purple')
plt.xlabel('Company Response to Consumer')
plt.ylabel('Number of Complaints')
plt.title('Number of Complaints for Each Company Response')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Count the occurrences of each value in 'Consumer_disputed'
dispute_counts = data['Consumer_disputed'].value_counts()

# Create a bar plot
plt.figure(figsize=(8, 6))
dispute_counts.plot(kind='bar', color='green')
plt.xlabel('Consumer Disputed')
plt.ylabel('Number of Complaints')
plt.title('Number of Complaints by Consumer Disputed Status')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


data = pd.read_csv("/content/drive/MyDrive/datasets/exam.csv")

# Plot top 10 products by complaint count
top_products = data['Product'].value_counts().head(10)
top_products.plot(kind='bar')
plt.xlabel('Product')
plt.ylabel('Number of Complaints')
plt.title('Top 10 Products by Complaint Count')
plt.xticks(rotation=45)
plt.show()
