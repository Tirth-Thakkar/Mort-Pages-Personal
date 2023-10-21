import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Stats_Data/UnbiasSurvey.csv')  # Replace 'your_data.csv' with the actual file path

# Assuming the CSV columns are named as 'Would you buy a new iPhone?' and 'Do you currently use an iPhone?'
# You can rename the columns for easier access
df.rename(columns={'Would you buy a new iPhone?': 'buy_new_iPhone',
                  'Do you currently use an iPhone?': 'current_iPhone_user'}, inplace=True)

# Calculate percentages for different categories
iphone_users = df[df['current_iPhone_user'] == 'Yes']
non_iphone_users = df[df['current_iPhone_user'] == 'No']

# Calculate the percentages of "Yes" and "No" for iPhone users and non-iPhone users
iphone_users_yes = len(iphone_users[iphone_users['buy_new_iPhone'] == 'Yes']) / len(iphone_users)
iphone_users_no = 1 - iphone_users_yes

non_iphone_users_yes = len(non_iphone_users[non_iphone_users['buy_new_iPhone'] == 'Yes']) / len(non_iphone_users)
non_iphone_users_no = 1 - non_iphone_users_yes

# Create data for the stacked bar graph
categories = ['Yes', 'No']
iphone_data = [iphone_users_yes, iphone_users_no]
non_iphone_data = [non_iphone_users_yes, non_iphone_users_no]

# Create the stacked bar graph
fig, ax = plt.subplots()
width = 0.35
x = range(len(categories))

plt.bar(x, iphone_data, width, label='iPhone Users')
plt.bar(x, non_iphone_data, width, label='Non-iPhone Users', bottom=iphone_data)

ax.set_xlabel('Response')
ax.set_ylabel('Relative Frequency')
ax.set_title('Stacked Relative Frequency Bar Graph')
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(categories)
ax.legend()

plt.show()
plt.savefig('stacked_bar_graph.png')  # Save the graph to a PNG file
