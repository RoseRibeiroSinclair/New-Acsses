# --- Simple Data Analysis Example ---

# 1. We create a list of data (programming languages used in Data Engineering)
skills = ["Python", "SQL", "Cloud", "Python", "Spark", "SQL", "Python"]

# 2. We count how many times "Python" appears in our data
python_count = skills.count("Python")

# 3. We display the results on the screen
print("=== DATA ENGINEERING MARKET ANALYSIS ===")
print("Total skills analyzed:", len(skills))
print("How many times Python was found:", python_count)

# 4. A simple business logic condition
if python_count > 2:
    print("Market Trend: Python is highly demanded!")
else:
    print("Market Trend: Keep studying.")
