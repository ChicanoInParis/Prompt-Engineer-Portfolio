---
layout: default
title: "My First Dive Into Testing Local LLMS (and Accidentally Learning Data Science)"
date: 2025-06-19
---
# 🧪 My First Dive into Testing Local LLMs (and Accidentally Learning Data Science)

Hi. Let me start by saying I am not a data scientist. I’m just a guy who is naturally curious and a bit intrepid. So when I read somewhere that I could host LLMs *locally*—without giving my data away every time I used ChatGPT or another AI—I decided to try it.

Of course, I had absolutely no idea what I was doing. So I downloaded LM Studio, then went nuts and downloaded **half a terabyte** worth of different LLMs just to test drive them. Then I thought, “Well, there has to be some sort of way to **quantify just how good they are for what I need**, right?”

---

## ⚙️ Creating My First Evaluation Framework

I lined up **31 LLMs of various sizes**—having no idea what “parameter size” actually meant—and started small. I created a simple scoring rubric and some structured test prompts. At first, it was overwhelming. I realized I was the proverbial dog that had caught the car… except the car was an 18-wheel semi full of data and tools I didn’t know how to use.

So I pivoted.

I simplified my approach: just a handful of **zero-shot** and **one-shot** questions to give me a sense of each LLM’s general usefulness. I wanted to test:

- Math  
- Coding  
- Creativity  
- Niche knowledge (I used medical terminology)  
- Logic  
- Ambiguity  
- Error handling  

Each category got a pair of questions:

- A **zero-shot** question (no context)  
- And a **one-shot or few-shot** version that gave an example to guide the LLM  

**Example for coding:**

> (Zero-shot) “Write a Python function to reverse a string.”  
>  
> (One/multi-shot) “Example: `reverse('hello') → 'olleh'`. Now write the function.”

Then I rated the model’s answer on a **0–5 scale** based on how close it got to the ideal answer. That gave me some structure—and a way to track how each model performed over time.

---

## 🐍 Enter Python, Pandas, and a Jupyter Notebook

Once I had scores, I needed a way to **analyze them**. I’d heard of tools like pandas and Jupyter notebooks but had never really used them.

So I taught myself just enough Python to:

- Load the CSV of my results into pandas  
- Clean up the data  
- Group it by model name  
- Calculate an average score for each one  

Then I used **matplotlib** to visualize the results in a simple bar chart.

Here’s what the core of my notebook looks like:

<pre>
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('LLM-zero-one-shot.csv')

# Clean the data
df_clean = df.dropna(subset=['Model Name', 'Accuracy (0 - 5)'])

# Group and calculate average score per model
model_avg = df_clean.groupby('Model Name')['Accuracy (0 - 5)'].mean().sort_values(ascending=False)

# Plot the results
plt.figure(figsize=(12, 8))
model_avg.plot(kind='bar', color='skyblue')
plt.title('Average Accuracy Score (0–5) per LLM')
plt.xlabel('Model Name')
plt.ylabel('Average Score')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
```
</pre>
It’s simple, but it works. With this, I can easily see which models did best overall, and begin comparing them based on my own needs—not just benchmark scores designed for research labs.

⸻

🧠 What I Learned (and What Comes Next)

My goal is simple: I want to discover which LLM—or which combo—is the most practical for my usage habits.

But in doing this, I stumbled into something bigger: I want to dive deep into LLMs. I want to learn what I can do with them, how to use them in my personal and professional life, and I want to get really f***ing good at it.

This is just the first step. I’ve pared this project down to the most basic data points: model name, parameter count, and average score. It starts to answer my first question—“Which model works best for me?”—and opens the door to the next.

There will be more tests soon. I’m currently enrolled in bootcamps for both Python and Data Science—because of this project. Because doing this made me want to do it again. And again. Bigger. Better. Faster.

⸻

💬 Got Thoughts?

If you’ve got ideas, suggestions, or critiques—send them my way. I’m learning. But I’m also building. And this is just the beginning.

You can find it here: <p><h3><a href="https://github.com/ChicanoInParis/LLM-Prompt-Evauation-Lab">LLM Prompt Evaluation Lab</a></h3></p>

R
<p><a href="{{ site.baseurl }}">← Back to Home</a></p>
