plot_examples = [
{
"User request": "Plot a graph of total Apple vs Samsung sales in 2024.",
"code": """
import matplotlib.pyplot as plt
import numpy as np
import calendar

fig, ax = plt.subplots(figsize=(8,6))

def add_labels(x, y):
  if isinstance(y, pd.Series):
    y = y.to_frame()

  for i in range(len(x)):
    if y.shape[1] == 1:
      val = y.iloc[i, 0]
      plt.text(i, (val / 2), val, ha='center', va='center', rotation='vertical')
    else:
      for j, col in enumerate(y.columns):
        val = y.iloc[i, j]
        plt.text(i + j * 0.4, val / 2, val, ha='center', va='center', rotation='vertical')

if "month" in df:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

numeric_columns = df.select_dtypes(include=[np.number]).columns
categorical_columns = df.select_dtypes(exclude=[np.number]).columns

if len(categorical_columns) == 0:
  df.plot(kind="bar", ax=ax)
  ax.set_xticks([])
  ax.set_xlabel("")
  ax.set_title("Distribution of Numeric Columns")
  plt.tight_layout()

else:
  if len(numeric_columns) == 1 and len(categorical_columns) == 1:
    ax.bar(df[categorical_columns[0]], df[numeric_columns[0]])
    ax.set_xlabel(df[categorical_columns[0]].name)
    add_labels(df[categorical_columns[0]], df[numeric_columns[0]])

  elif len(numeric_columns) > 1 and len(categorical_columns) == 1:
    x = np.arange(len(df))
    width = 0.8 / len(numeric_columns)
    for i, column in enumerate(numeric_columns):
      ax.bar(x + i*width, df[column], width=width, label=column)
    add_labels(x, df[numeric_columns])
    ax.set_xlabel(df[categorical_columns[0]].name)
    ax.set_xticks(x + width*(len(numeric_columns)-1)/2)
    ax.set_xticklabels(df[categorical_columns[0]], rotation=90, ha='right')

  else:
    x = np.arange(len(df))
    width = 0.8 / max(1, len(numeric_columns))
    for i, column in enumerate(numeric_columns):
      ax.bar(x + i*width, df[column], width=width, label=column)
    add_labels(x, df[numeric_columns])
    ax.set_xlabel(df[categorical_columns[0]].name)
    ax.set_xticks(x + width*(len(numeric_columns)-1)/2)
    ax.set_xticklabels(df[categorical_columns[0]], rotation=90, ha='right')

  ax.set_title("Your Chart Title")
  ax.set_ylabel(df[numeric_columns[0]].name)

  if len(numeric_columns) > 1:
    ax.legend(loc='upper center', ncol=len(numeric_columns))

  plt.tight_layout()
"""
},
{
"User request": "Plot a bar chart of sales by month.",
"code": """
import matplotlib.pyplot as plt
import numpy as np
import calendar

fig, ax = plt.subplots(figsize=(8,6))

if "month" in df:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

numeric_columns = df.select_dtypes(include=[np.number]).columns
categorical_columns = df.select_dtypes(exclude=[np.number]).columns

if len(categorical_columns) > 0:
  x = np.arange(len(df))
  width = 0.8 / len(numeric_columns)
  for i, col in enumerate(numeric_columns):
    ax.bar(x + i*width, df[col], width=width, label=col)
  ax.set_xticks(x + width*(len(numeric_columns)-1)/2)
  ax.set_xticklabels(df[categorical_columns[0]], rotation=45, ha='right')
  ax.set_title("Monthly Sales Comparison")
  ax.set_ylabel("Sales")
  ax.legend()
else:
  df.plot(kind="bar", ax=ax)
  ax.set_title("Bar Chart of Numeric Columns")

plt.tight_layout()
"""
},
{
"User request": "Plot a line chart showing monthly revenue trend.",
"code": """
import matplotlib.pyplot as plt
import calendar

fig, ax = plt.subplots(figsize=(8,6))

if "month" in df:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

numeric_columns = df.select_dtypes(include=[np.number]).columns

df.plot(x="month", y=numeric_columns, kind="line", marker="o", ax=ax)
ax.set_title("Monthly Revenue Trend")
ax.set_ylabel("Revenue")
ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
"""
},
{
"User request": "Plot a pie chart showing the percentage share of total Apple vs Samsung sales.",
"code": """
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6,6))

numeric_columns = df.select_dtypes(include=[float, int]).columns
values = df[numeric_columns].iloc[0] if len(df) == 1 else df[numeric_columns].sum()
labels = numeric_columns

ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
ax.set_title("Percentage Share of Sales")
ax.axis('equal')
"""
},
{
"User request": "Plot a scatter plot between total sales and profit.",
"code": """
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,6))
numeric_columns = df.select_dtypes(include=[float, int]).columns

if len(numeric_columns) >= 2:
  ax.scatter(df[numeric_columns[0]], df[numeric_columns[1]], color='blue', alpha=0.6)
  ax.set_xlabel(numeric_columns[0])
  ax.set_ylabel(numeric_columns[1])
  ax.set_title(f"Scatter Plot: {numeric_columns[0]} vs {numeric_columns[1]}")
else:
  df.plot(kind="bar", ax=ax)
  ax.set_title("Bar Chart (Fallback)")

plt.tight_layout()
"""
},
{
"User request": "Plot a pie chart of month-wise Apple's sales in 2024.",
"code": """
import matplotlib.pyplot as plt
import calendar

fig, ax = plt.subplots(figsize=(7,7))

# Convert month numbers to abbreviations if column exists
if "month" in df.columns:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

# Identify numeric and categorical columns
numeric_columns = df.select_dtypes(include=["number"]).columns
categorical_columns = df.select_dtypes(exclude=["number"]).columns

# Auto-detect columns (e.g., 'month' and 'apple_sales')
if "month" in df.columns:
  label_col = "month"
else:
  label_col = categorical_columns[0] if len(categorical_columns) > 0 else df.columns[0]

if "apple_sales" in df.columns:
  value_col = "apple_sales"
else:
  value_col = numeric_columns[0] if len(numeric_columns) > 0 else df.columns[0]

# Plot pie chart
ax.pie(df[value_col], labels=df[label_col], autopct='%1.1f%%', startangle=90)
ax.set_title("Month-wise Apple Sales in 2024")

plt.tight_layout()
"""
},
{
"User request": "Plot a line chart of month-wise Apple vs Samsung sales in 2024.",
"code": """
import matplotlib.pyplot as plt
import numpy as np
import calendar

fig, ax = plt.subplots(figsize=(8,6))

# Convert month numbers to abbreviations if present
if "month" in df.columns:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

# Identify numeric and categorical columns
numeric_columns = df.select_dtypes(include=["number"]).columns
categorical_columns = df.select_dtypes(exclude=["number"]).columns

# Auto-detect label and value columns
if "month" in df.columns:
  label_col = "month"
else:
  label_col = categorical_columns[0] if len(categorical_columns) > 0 else df.columns[0]

# Detect Apple and Samsung sales columns
apple_col = None
samsung_col = None
for col in df.columns:
  if "apple" in col.lower():
    apple_col = col
  elif "samsung" in col.lower():
    samsung_col = col

# Fallback to numeric columns if not found
if not apple_col or not samsung_col:
  if len(numeric_columns) >= 2:
    apple_col, samsung_col = numeric_columns[:2]
  else:
    apple_col = numeric_columns[0]

# Plot line(s)
if apple_col and samsung_col:
  ax.plot(df[label_col], df[apple_col], marker='o', label="Apple Sales")
  ax.plot(df[label_col], df[samsung_col], marker='o', label="Samsung Sales")
else:
  ax.plot(df[label_col], df[apple_col], marker='o', label=apple_col)

# Labels and formatting
ax.set_title("Month-wise Apple vs Samsung Sales in 2024")
ax.set_xlabel(label_col.capitalize())
ax.set_ylabel("Sales")
ax.legend(loc='upper left')
plt.grid(True)
plt.tight_layout()
"""
},
{
"User request": "Plot a histogram of total sales distribution.",
"code": """
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,6))
numeric_columns = df.select_dtypes(include=[float, int]).columns

if len(numeric_columns) > 0:
  ax.hist(df[numeric_columns[0]], bins=10, color='skyblue', edgecolor='black')
  ax.set_xlabel(numeric_columns[0])
  ax.set_ylabel("Frequency")
  ax.set_title(f"Histogram of {numeric_columns[0]}")
else:
  st.warning("No numeric columns available for histogram.")

plt.tight_layout()
"""
},
{
"User request": "Plot a horizontal bar chart comparing Apple and Samsung sales for 2024.",
"code": """
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7,5))
numeric_columns = df.select_dtypes(include=[float, int]).columns

if len(df) == 1:
  values = df[numeric_columns].iloc[0]
  ax.barh(numeric_columns, values, color=['#4e79a7', '#f28e2b'])
  for i, v in enumerate(values):
    ax.text(v, i, f" {v}", va='center')
  ax.set_title("Sales Comparison for 2024")
  ax.set_xlabel("Sales")
else:
  df.plot(kind="barh", ax=ax)
  ax.set_title("Horizontal Bar Chart")

plt.tight_layout()
"""
},
{
"User request": "Plot a multi-line chart of Apple and Samsung monthly sales.",
"code": """
import matplotlib.pyplot as plt
import calendar

fig, ax = plt.subplots(figsize=(8,6))

if "month" in df:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

numeric_columns = df.select_dtypes(include=[float, int]).columns
df.plot(x="month", y=numeric_columns, ax=ax, marker='o')

ax.set_title("Apple vs Samsung Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
"""
},
{
"User request": "Plot a stacked bar chart of Apple and Samsung sales per month.",
"code": """
import matplotlib.pyplot as plt
import calendar

fig, ax = plt.subplots(figsize=(8,6))

if "month" in df:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

numeric_columns = df.select_dtypes(include=[float, int]).columns
df.plot(x="month", y=numeric_columns, kind="bar", stacked=True, ax=ax)

ax.set_title("Stacked Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.legend()
plt.tight_layout()
"""
},
{
"User request": "Plot a box plot showing sales data spread.",
"code": """
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,6))
numeric_columns = df.select_dtypes(include=[float, int]).columns

df.boxplot(column=numeric_columns, ax=ax)
ax.set_title("Box Plot of Sales Data")
ax.set_ylabel("Values")
plt.tight_layout()
"""
},
{
"User request": "Plot an area chart showing cumulative monthly sales.",
"code": """
import matplotlib.pyplot as plt
import calendar

fig, ax = plt.subplots(figsize=(8,6))

if "month" in df:
  df["month"] = df["month"].astype(int).apply(lambda x: calendar.month_abbr[x])

numeric_columns = df.select_dtypes(include=[float, int]).columns
df.plot(x="month", y=numeric_columns, kind="area", stacked=False, alpha=0.6, ax=ax)

ax.set_title("Cumulative Monthly Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.tight_layout()
"""
}
]
