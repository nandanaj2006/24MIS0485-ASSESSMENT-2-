
farms = [
    ["Green Valley", "Wheat", 100, 45],
    ["Sunny Acres", "Corn", 150, 80],
    ["Highland", "Wheat", 80, 55],
    ["Riverbed", "Rice", 120, 60],
]


farm_data = []
for farm in farms:
  name, crop, area, yield_val = farm
  yield_per_acre = yield_val / area
  farm_data.append(
      {"name": name, "crop": crop, "area": area, "yield": yield_val, "productivity": yield_per_acre}
  )


highest_farm = max(farm_data, key=lambda x: x["productivity"])


total_productivity = sum(f["productivity"] for f in farm_data)
average_productivity = total_productivity / len(farm_data)


high_yield_farms = [f for f in farm_data if f["yield"] > 50]


sorted_farms = sorted(farm_data, key=lambda x: x["productivity"], reverse=True)


print("--- Farm Productivity Details ---")
for f in farm_data:
  print(f"{f['name']}: {f['productivity']:.2f} tons/acre")

print(f"\nHighest Productivity Farm: {highest_farm['name']} ({highest_farm['productivity']:.2f} tons/acre)")
print(f"Average Yield per Acre: {average_productivity:.2f} tons/acre")

print("\nFarms Producing More Than 50 Tons:")
for f in high_yield_farms:
  print(f"- {f['name']} ({f['yield']} tons)")

print("\nFarms Sorted by Productivity (High to Low):")
for f in sorted_farms:
  print(f"{f['name']}: {f['productivity']:.2f} tons/acre")
