import pandas as pd
import numpy as np

sales_data = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "revenue": [80000, 85000, 82000, 95000, 110000, 130000],
    "products_sold": [400, 420, 410, 450, 500, 550]
})

# =========================
# Part A: Data Analysis
# =========================

#1.	Calculate the total sales revenue for the six months.
print(f"Total sales revenue:{np.sum(sales_data['revenue']):,}") #with number formatting
# another way to calculate total sales revenue
#print(f"Total sales revenue:{sum(sales_data['revenue']):,}") # with number formatting

#2.	Calculate the average monthly revenue.
total = sum(sales_data['revenue'])
count = len(sales_data)
average = total / count
print(f"Average sales revenue: {average:,}")

#3.	Identify the month with the highest sales revenue.
highest_month = sales_data.loc[sales_data['revenue'].idxmax(), 'month']
highest_revenue = sales_data['revenue'].max()

print(f"Highest sales revenue: {highest_revenue:,}")
print(f"Month: {highest_month}")

#4.	Identify the month with the lowest sales revenue.
lowest_month = sales_data.loc[sales_data['revenue'].idxmin(), 'month']
lowest_revenue = sales_data['revenue'].min()

print(f"Lowest sales revenue: {lowest_revenue:,}")
print(f"Month: {lowest_month}")

#5. Calculate the total number of products sold.
print(f"Total products sold: {np.sum(sales_data['products_sold']):,}")

#6.	Calculate the average revenue per product for each month.
sales_data["avg_revenue_per_product"] = (
    sales_data["revenue"] / sales_data["products_sold"]
)
print("Average revenue per product sold each month:")
print(sales_data[["month", "avg_revenue_per_product"]]) 


print(f"Average revenue per product: {np.mean(sales_data['avg_revenue_per_product']):,.2f}")
#7.	Calculate the percentage increase in revenue from January to June.
june = 130000
jan = 80000
increase = june - jan
percentage_increase = ((june - jan) / jan) * 100
print(f"Percentage increase in revenue from January to June: {percentage_increase:.2f}%")


# ===========================
# Part B: Identifying Trends
# ===========================

#1. Did revenue increase consistently every month? 
if sales_data["revenue"].diff().dropna().gt(0).all():
    print("Yes, revenue increased consistently every month.")
else:
    print("No, revenue did not increase consistently every month.")

#2. Which month experienced a decline in revenue compared with the previous month?
decline_months = sales_data.loc[
    sales_data["revenue"].diff().lt(0),
    "month"
]
print("Months with a decline in revenue compared with the previous month:")
print(decline_months.tolist())


#3.	How much did revenue change between February and March, in dollars and as a percentage?
february_revenue = sales_data.loc[sales_data["month"] == "Feb", "revenue"].iloc[0]
march_revenue = sales_data.loc[sales_data["month"] == "Mar", "revenue"].iloc[0]
percentage_change = ((march_revenue - february_revenue) / february_revenue) * 100
print(f"Revenue change from February to March: ${march_revenue - february_revenue:,} ({percentage_change:.2f}%)")

#4. Did the number of products sold increase between January and June?
january_products = sales_data.loc[sales_data["month"] == "Jan", "products_sold"].iloc[0]
june_products = sales_data.loc[sales_data["month"] == "Jun", "products_sold"].iloc[0]

if june_products > january_products:
    print("Yes, the number of products sold increased between January and June.")
else:
    print("No, the number of products sold did not increase between January and June.")

 #5. Did average revenue per product increase between January and June?  

january_avg_revenue = sales_data.loc[sales_data["month"] == "Jan", "avg_revenue_per_product"].iloc[0] 
june_avg_revenue = sales_data.loc[sales_data["month"] == "Jun", "avg_revenue_per_product"].iloc[0]

if june_avg_revenue > january_avg_revenue:
    print("Yes, the average revenue per product increased between January and June.")
else:
    print("No, the average revenue per product did not increase between January and June.")

# =================================
# Part C: Business Interpretation
# =================================
#1. Identify three key findings about the company's sales performance.
#* on april onword the sales revenue increased significantly, which could be due to seasonal demand or successful marketing campaigns. 
#* March the sales revenue decreased compared to February, indicating a potential issue that needs to be addressed.
#* June sale revenue was peak.

#2. Explain whether revenue growth appears to be associated with increasing sales volume, increasing average revenue per product, or both.
sales_data["avg_revenue_per_product"] = (
    sales_data["revenue"] / sales_data["products_sold"]
)

print(sales_data[["month", "revenue", "products_sold", "avg_revenue_per_product"]])
#Increasing sales volume: Products sold generally increased from 400 in January to 550 in June.
#Increasing average revenue per product: Revenue per product increased from about $200 to $236.36.

#3. Recommend two actions the company could take to improve its sales performance.
#* Implement targeted marketing campaigns to address the decline in sales during March.
#* Analyze the factors contributing to the revenue increase in April and replicate those strategies in other months.