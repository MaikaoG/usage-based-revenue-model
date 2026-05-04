import pandas as pd

# Sample customer usage data
data = pd.DataFrame({
    "customer_segment": ["Light", "Medium", "Heavy", "Enterprise"],
    "customers": [100, 50, 20, 5],
    "usage_units_per_customer": [1_000, 10_000, 50_000, 250_000]
})

# Pricing assumptions
price_per_usage_unit = 0.00025  # $0.25 per 1,000 usage units
cost_per_usage_unit = 0.00002   # estimated infrastructure / AI cost per unit

# Model calculations
data["total_usage_units"] = data["customers"] * data["usage_units_per_customer"]
data["revenue"] = data["total_usage_units"] * price_per_usage_unit
data["cost"] = data["total_usage_units"] * cost_per_usage_unit
data["gross_margin"] = data["revenue"] - data["cost"]
data["gross_margin_percent"] = data["gross_margin"] / data["revenue"]

print(data)

print("\nSummary:")
print(f"Total revenue: ${data['revenue'].sum():,.2f}")
print(f"Total cost: ${data['cost'].sum():,.2f}")
print(f"Total gross margin: ${data['gross_margin'].sum():,.2f}")
print(f"Gross margin %: {data['gross_margin'].sum() / data['revenue'].sum():.1%}")
