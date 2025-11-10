# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# 1. Create Sample Excel File
# ----------------------------
data = {
    'Repository': [
        'openshift/okd', 'openshift/okd', 'openshift/okd',
        'aws/containers-roadmap', 'aws/containers-roadmap', 'aws/containers-roadmap',
        'kubernetes/kubernetes', 'kubernetes/kubernetes', 'kubernetes/kubernetes'
    ],
    'Month': ['Jun', 'Jul', 'Aug', 'Jun', 'Jul', 'Aug', 'Jun', 'Jul', 'Aug'],
    'Pull_Requests': [50, 60, 75, 40, 50, 55, 60, 70, 80],
    'Forks': [30, 35, 40, 25, 28, 30, 35, 38, 42],
    'Issues': [20, 18, 25, 15, 18, 20, 22, 25, 28],
    'Active_Contributors': [10, 12, 15, 8, 10, 11, 12, 14, 16],
    'Automation_Feature_PRs': [20, 25, 35, 10, 15, 18, 20, 25, 30]
}

df = pd.DataFrame(data)

# Save as Excel
excel_file = 'github_metrics.xlsx'
df.to_excel(excel_file, index=False)
print(f"Sample Excel file saved as {excel_file}")

# ----------------------------
# 2. Read Data from Excel
# ----------------------------
df = pd.read_excel(excel_file)
print("Data loaded from Excel:")
print(df.head())

# ----------------------------
# 3. Set Visualization Style
# ----------------------------
sns.set(style='whitegrid')

# ----------------------------
# 4. Line Chart: Pull Requests Over Time by Repository
# ----------------------------
plt.figure(figsize=(10,6))
for repo in df['Repository'].unique():
    repo_data = df[df['Repository'] == repo]
    plt.plot(repo_data['Month'], repo_data['Pull_Requests'], marker='o', label=repo)

plt.title('Pull Requests Trend by Repository')
plt.xlabel('Month')
plt.ylabel('Number of Pull Requests')
plt.legend()
plt.tight_layout()
plt.savefig('Pull_Requests_Trend.png')
plt.show()

# ----------------------------
# 5. Bar Chart: Forks Per Repository (Latest Month)
# ----------------------------
latest_month = df['Month'].max()
latest_data = df[df['Month'] == latest_month]

plt.figure(figsize=(8,5))
sns.barplot(x='Repository', y='Forks', data=latest_data, palette='Greens_d')
plt.title(f'Forks Per Repository - {latest_month}')
plt.xlabel('Repository')
plt.ylabel('Number of Forks')
plt.tight_layout()
plt.savefig('Forks_Latest.png')
plt.show()

# ----------------------------
# 6. Bar Chart: Issues Per Repository (Latest Month)
# ----------------------------
plt.figure(figsize=(8,5))
sns.barplot(x='Repository', y='Issues', data=latest_data, palette='Reds_d')
plt.title(f'Issues Per Repository - {latest_month}')
plt.xlabel('Repository')
plt.ylabel('Number of Issues')
plt.tight_layout()
plt.savefig('Issues_Latest.png')
plt.show()

# ----------------------------
# 7. Bar Chart: Active Contributors (Latest Month)
# ----------------------------
plt.figure(figsize=(8,5))
sns.barplot(x='Repository', y='Active_Contributors', data=latest_data, palette='Purples_d')
plt.title(f'Active Contributors - {latest_month}')
plt.xlabel('Repository')
plt.ylabel('Number of Contributors')
plt.tight_layout()
plt.savefig('Active_Contributors_Latest.png')
plt.show()
