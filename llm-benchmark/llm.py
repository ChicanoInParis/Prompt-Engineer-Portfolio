import pandas as pd

# Load the CSV file to examine its contents
file_path = '/Users/simplesolutions.technology/Desktop/Learning/Data Science & Machine Learning/LLMs Benchmarks/LLM-zero-one-shot.csv'
df = pd.read_csv(file_path)

# Show basic information and the first few rows
df.info(), df.head()

import matplotlib.pyplot as plt

# Step 1: Clean the data
df_clean = df.dropna(subset=['Model Name', 'Accuracy (0 - 5)'])

# Step 2: Group by Model Name and calculate average accuracy
model_avg = df_clean.groupby('Model Name')['Accuracy (0 - 5)'].mean().sort_values(ascending=False)

# Step 3: Identify the top model(s)
top_score = model_avg.max()
top_models = model_avg[model_avg == top_score]

# Step 4: Plot the model comparison
plt.figure(figsize=(12, 8))
model_avg.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Average Accuracy Score (0-5) per LLM')
plt.xlabel('Model Name')
plt.ylabel('Average Accuracy')
plt.xticks(rotation=90)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display results
model_avg.head(), top_models, plt.show()