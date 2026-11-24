import pandas as pd
sales = pd.DataFrame({    
	"month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],    
	"sales_k": [80, 85, 82, 95, 110, 130],
    "products_sold": [100, 120, 110, 140, 160, 200]
})
# Calculate average sales
average = sales["sales_k"].mean()
# Find the highest sales value
highest_sales = sales["sales_k"].max()
# Find the row index of the highest sales
highest_index = sales["sales_k"].idxmax()
# Find the corresponding month
highest_month = sales.loc[highest_index, "month"]
# Display results
print("Average sales ($k):", average)
print("Highest sales ($k):", highest_sales)
print("Highest-sales month:", highest_month)
# list number of sold products in each month
#sales["sold_products"] = [800, 850, 820, 950, 1100, 1300]   
#print('Sales Data:')
#print(sales)
print("Products sold each month:", sales["products_sold"].tolist())

#print month with least sales
least_sales = sales["sales_k"].min()
print("Least sales ($k):", least_sales)

#print the sum of sales for whole 6 months
total_sales = sales["sales_k"].sum()
print("Total sales for 6 months ($k):", total_sales)

#average sales price of the products sold in each month
sales["average_price"] = sales["sales_k"] * 1000 / sales["products_sold"]
print('Average Sales Price per Month:')
print(sales)
