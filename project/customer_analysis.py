import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("sales_data.csv")
customers = pd.read_csv("customer_churn.csv")

print(sales.head())
print(customers.head())

print(sales.info())
print(customers.info())

print(sales.describe())

print(sales.isnull().sum())
print(customers.isnull().sum())

# Convert Date column to datetime
sales["Date"] = pd.to_datetime(sales["Date"])

print(sales.dtypes)

sales["Year"] = sales["Date"].dt.year
sales["Month"] = sales["Date"].dt.month_name()

print(sales.head())

print(sales.duplicated().sum())

sales.drop_duplicates(inplace=True)
print(sales.isnull().sum())

sales.to_csv("clean_sales_data.csv", index=False)


# Total Revenue
total_revenue = sales["Total_Sales"].sum()

print("Total Revenue:", total_revenue)

total_customers = sales["Customer_ID"].nunique()

print("Total Customers:", total_customers)

top_customers = sales.groupby("Customer_ID")["Total_Sales"].sum()

top_customers = top_customers.sort_values(ascending=False)

print(top_customers.head(10))

region_sales = sales.groupby("Region")["Total_Sales"].sum()

print(region_sales)

average_region_sales = sales.groupby("Region")["Total_Sales"].mean()

print(average_region_sales)

product_sales = sales.groupby("Product")["Total_Sales"].sum()

print(product_sales.sort_values(ascending=False))

product_quantity = sales.groupby("Product")["Quantity"].sum()

print(product_quantity)

highest_region = region_sales.idxmax()

print("Highest Revenue Region:", highest_region)

best_product = product_sales.idxmax()

print("Best Selling Product:", best_product)

# Monthly Sales
monthly_sales = sales.groupby("Month")["Total_Sales"].sum()

print(monthly_sales)
monthly_quantity = sales.groupby("Month")["Quantity"].sum()

print(monthly_quantity)

average_price = sales.groupby("Product")["Price"].mean()

print(average_price)
expensive_product = average_price.idxmax()

print("Most Expensive Product:", expensive_product)

pivot_table = pd.pivot_table(
    sales,
    values="Total_Sales",
    index="Region",
    columns="Product",
    aggfunc="sum"
)

print(pivot_table)

top_customers.head(10).plot(kind="bar", figsize=(10,5))

plt.title("Top 10 Customers")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")
plt.show()

region_sales.plot(kind="bar", figsize=(8,5))

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

product_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    figsize=(7,7)
)

plt.ylabel("")
plt.title("Product Sales Distribution")
plt.show()

product_quantity.plot(kind="barh", figsize=(8,5))

plt.title("Quantity Sold by Product")
plt.xlabel("Quantity")
plt.show()

sales["Total_Sales"].plot(kind="hist", bins=10)

plt.title("Sales Distribution")
plt.xlabel("Total Sales")
plt.show()

print("\nCUSTOMER SALES ANALYSIS REPORT")
print("-" * 40)

print("Total Revenue:", total_revenue)
print("Total Customers:", total_customers)
print("Highest Revenue Region:", highest_region)
print("Best Selling Product:", best_product)

print("\nTop Customer")
print(top_customers.head(1))
