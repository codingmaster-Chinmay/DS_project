import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

# Load the dataset
file_path = r"C:\Users\Chinmay\Desktop\Resume\INTERNSHIPS\plasmid internship data sceince\Data_science_internship\OnlineRetail.xlsx"
df = pd.read_excel(file_path, sheet_name="OnlineRetail")

# Data Cleaning
df.dropna(subset=['CustomerID'], inplace=True)
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

df['CustomerID'] = df['CustomerID'].astype(int)

# Create a user-item matrix
user_item_matrix = df.pivot_table(index='CustomerID', columns='StockCode', values='Quantity', aggfunc='sum', fill_value=0)

# Convert to sparse matrix
sparse_matrix = csr_matrix(user_item_matrix)

# Compute cosine similarity between customers
customer_similarity = cosine_similarity(sparse_matrix)
customer_similarity_df = pd.DataFrame(customer_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# Function to get product recommendations
def recommend_products(customer_id, num_recommendations=5):
    if customer_id not in customer_similarity_df.index:
        return "Customer ID not found."
    
    similar_customers = customer_similarity_df[customer_id].sort_values(ascending=False).index[1:6]
    similar_customers_purchases = df[df['CustomerID'].isin(similar_customers)]
    
    recommended_products = similar_customers_purchases['StockCode'].value_counts().index[:num_recommendations].tolist()
    
    return df[df['StockCode'].isin(recommended_products)][['StockCode', 'Description']].drop_duplicates()

# Example usage
customer_id = df['CustomerID'].iloc[0]  # Picking a sample customer
recommendations = recommend_products(customer_id)

print(recommendations)
