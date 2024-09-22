import os
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import chi2_contingency
import numpy as np


def split_profession(csv_file_path):
    # Load the data
    df = pd.read_csv(csv_file_path)
    file_base_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    
    if 'job_title' not in df.columns:
        raise ValueError("Column 'job_title' not found in the CSV file")

    # Split the 'job_title' column into separate rows
    df_expanded = df.assign(job_title=df['job_title'].str.split(',')).explode('job_title')

    # Strip any extra whitespace from the 'job_title' entries
    df_expanded['job_title'] = df_expanded['job_title'].str.strip()
    
    # Get the current directory
    current_dir = os.getcwd()

    # Construct the path to the CSV_Data_Processed directory
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed", "Job_Title")

    path_output_array = []
    # Grouping the Data by the job_title (Species, Breed, Gender, etc.)
    for type_name, group, in df_expanded.groupby('job_title'):
        # Construct the path to the output file
        sanitized_type_name = type_name.replace('/', '_').replace('\\', '_')
        output_file = os.path.join(output_dir, f"{file_base_name}_{sanitized_type_name}.csv")
        path_output_array.append(output_file)
        # Save the grouped data to a new CSV file
        group.to_csv(output_file, index=False)
        
        print(f"Data saved to {output_file}")
    return path_output_array

def plot_average_salary_job(path_output_array):
    # Creating a bar graph with profession type and average salary into one image
    job_salaries = []
    for file_path in path_output_array:
        df = pd.read_csv(file_path)
        # Calculate the average salary for each job title
        avg_salary = df['salary_in_usd'].mean()
        job_title = df['job_title'].unique()[0]
        job_salaries.append((job_title, avg_salary))
    
    # Sort the job salaries in descending order based on average salary
    job_salaries.sort(key=lambda x: x[1], reverse=True)

    # Applying some processing shortening common job titles
    # Data Science --> DS
    # Engineer --> Eng
    # Machine Learning --> ML

    for i in range(len(job_salaries)):
        job_salaries[i] = (job_salaries[i][0].replace("Data Science", "DS").replace("Engineer", "Eng").replace("Machine Learning", "ML"), job_salaries[i][1])
    
    
    job_titles = [job[0] for job in job_salaries]
    average_salary_arr = [job[1] for job in job_salaries]
    
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.bar(job_titles, average_salary_arr)
    ax.set_xlabel('Job Titles')
    ax.set_ylabel('Average Salaries ($USD)')
    ax.set_title(f'Average Salary for Data Scientists by Job Title')
    ax.set_xticklabels(job_titles, rotation=90)  # Set the tick labels and rotate them
    plt.tight_layout()
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed",'average_salary_job.png')
    plt.savefig(output_dir, dpi=300)
    plt.show()
    
def split_exp(csv_file_path):
    # Load the data
    # Load the data
    df = pd.read_csv(csv_file_path)
    file_base_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    
    if 'experience_level' not in df.columns:
        raise ValueError("Column 'experience_level' not found in the CSV file")

    # Split the 'experience_level' column into separate rows
    df_expanded = df.assign(job_title=df['experience_level'].apply(lambda x: ','.join(x) if isinstance(x, list) else x)).explode('experience_level')

    # Strip any extra whitespace from the 'experience_level' entries
    df_expanded['experience_level'] = df_expanded['experience_level'].str.strip()
    
    # Get the current directory
    current_dir = os.getcwd()

    # Construct the path to the CSV_Data_Processed directory
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed","Exp")

    path_output_array = []
    # Grouping the Data by the job_title 
    for type_name, group, in df_expanded.groupby('experience_level'):
        # Construct the path to the output file
        sanitized_type_name = type_name.replace('/', '_').replace('\\', '_')
        output_file = os.path.join(output_dir, f"{file_base_name}_{sanitized_type_name}.csv")
        path_output_array.append(output_file)
        # Save the grouped data to a new CSV file
        group.to_csv(output_file, index=False)
        
        print(f"Data saved to {output_file}")
    return path_output_array
    
def plot_sal_vs_exp(path_output_array):
    # Creating a bar graph with exp level and average salary into one image
    job_salaries = []
    for file_path in path_output_array:
        df = pd.read_csv(file_path)
        # Calculate the average salary for each exp level
        avg_salary = df['salary_in_usd'].mean()
        exp = df['experience_level'].unique()[0]
        job_salaries.append((exp, avg_salary))
    
    # Sort the exp level salaries in descending order based on average salary
    job_salaries.sort(key=lambda x: x[1], reverse=True)

    
    exp_levels = [job[0] for job in job_salaries]
    average_salary_arr = [job[1] for job in job_salaries]
    
    fig, ax = plt.subplots()
    ax.bar(exp_levels, average_salary_arr)
    ax.set_xlabel('Experience Levels')
    ax.set_ylabel('Average Salaries ($USD)')
    ax.set_title('Average Salary for Data Scientists by Experience Level')
    ax.set_xticklabels(exp_levels, rotation=90)
    plt.tight_layout()
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed",'average_salary_exp.png')
    plt.savefig(output_dir, dpi=300)
    plt.show()

def split_company_size(csv_file_path):
    # Load the data
    df = pd.read_csv(csv_file_path)
    file_base_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    
    if 'company_size' not in df.columns:
        raise ValueError("Column 'company_size' not found in the CSV file")

    # Split the 'company_size' column into separate rows
    df_expanded = df.assign(job_title=df['company_size'].str.split(',')).explode('company_size')

    # Strip any extra whitespace from the 'company_size' entries
    df_expanded['company_size'] = df_expanded['company_size'].str.strip()
    
    # Get the current directory
    current_dir = os.getcwd()

    # Construct the path to the CSV_Data_Processed directory
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed", "Job_Title")

    path_output_array = []
    # Grouping the Data by the company_size 
    for type_name, group, in df_expanded.groupby('company_size'):
        # Construct the path to the output file
        sanitized_type_name = type_name.replace('/', '_').replace('\\', '_')
        output_file = os.path.join(output_dir, f"{file_base_name}_{sanitized_type_name}.csv")
        path_output_array.append(output_file)
        # Save the grouped data to a new CSV file
        group.to_csv(output_file, index=False)
        
        print(f"Data saved to {output_file}")
    return path_output_array

def plot_salary_vs_company_size(path_output_array):
    job_salaries = []
    for file_path in path_output_array:
        df = pd.read_csv(file_path)
        # Calculate the average salary for each company size
        avg_salary = df['salary_in_usd'].mean()
        company_size = df['company_size'].unique()[0]
        job_salaries.append((company_size, avg_salary))
    
    # Sort the company sizes in descending order based on average salary
    job_salaries.sort(key=lambda x: x[1], reverse=True)

    company_size = [job[0] for job in job_salaries]
    average_salary_arr = [job[1] for job in job_salaries]
    
    fig, ax = plt.subplots()
    ax.bar(company_size, average_salary_arr)
    ax.set_xlabel('Company Size')
    ax.set_ylabel('Average Salaries ($USD)')
    ax.set_title('Average Salary for Data Scientists by Company Size')
    ax.set_xticklabels(company_size, rotation=90)
    plt.tight_layout()
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed",'average_salary_company_size.png')
    plt.savefig(output_dir, dpi=300)
    plt.show()
    
def split_remote_rate(csv_file_path):
    # Load the data
    df = pd.read_csv(csv_file_path)
    file_base_name = os.path.splitext(os.path.basename(csv_file_path))[0]

    if "remote_ratio" not in df.columns:
        raise ValueError("Column 'remote_ratio' not found in the CSV file")
    
    # Categorize 'remote_rate' column into remote category, if remote rate is 100 or greater the role is remote, else it is not remote
    df['remote_status'] = df['remote_ratio'].apply(lambda x: 'Remote' if x >= 100 else 'In-Office')

    # Split the 'remote_status' column into separate rows
    df_expanded = df.assign(job_title=df['remote_status'].str.split(',')).explode('remote_status')

    # Strip any extra whitespace from the 'remote_status' entries
    df_expanded['remote_status'] = df_expanded['remote_status'].str.strip()

    # Get the current directory
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed", "Remote_Status")

    path_output_array = []
    # Grouping the Data by the remote_status
    for type_name, group, in df_expanded.groupby('remote_status'):
        # Construct the path to the output file
        sanitized_type_name = type_name.replace('/', '_').replace('\\', '_')
        output_file = os.path.join(output_dir, f"{file_base_name}_{sanitized_type_name}.csv")
        path_output_array.append(output_file)
        # Save the grouped data to a new CSV file
        group.to_csv(output_file, index=False)
        
        print(f"Data saved to {output_file}")

    return path_output_array

def plot_salary_vs_remote_status(path_output_array):
    job_salaries = []
    for file_path in path_output_array:
        df = pd.read_csv(file_path)
        # Calculate the average salary for each work type
        avg_salary = df['salary_in_usd'].mean()
        remote_status = df['remote_status'].unique()[0]
        job_salaries.append((remote_status, avg_salary))
    
    # Sort the job salaries in descending order based on average salary
    job_salaries.sort(key=lambda x: x[1], reverse=True)

    remote_status = [job[0] for job in job_salaries]
    average_salary_arr = [job[1] for job in job_salaries]
    
    fig, ax = plt.subplots()
    ax.bar(remote_status, average_salary_arr) 
    ax.set_xlabel('Remote Status')
    ax.set_ylabel('Average Salaries ($USD)')
    ax.set_title('Average Salary for Data Scientists by Remote Status')
    ax.set_xticklabels(remote_status, rotation=90)
    plt.tight_layout()
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed",'average_salary_remote.png')
    plt.savefig(output_dir, dpi=300)
    plt.show()


def create_company_size_experience_table(path_output_array):
    # Create an empty dictionary to store the counts
    count_dict = {}
        
    # Iterate over each file path in the path output array
    for file_path in path_output_array:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Get the company size and experience level
            company_size = row['company_size']
            experience_level = row['experience_level']
            
            # Check if the company size is already in the count dictionary
            if company_size in count_dict:
                # Check if the experience level is already in the nested dictionary
                if experience_level in count_dict[company_size]:
                    # Increment the count for the combination of company size and experience level
                    count_dict[company_size][experience_level] += 1
                else:
                    # Initialize the count for the experience level
                    count_dict[company_size][experience_level] = 1
            else:
                # Initialize the count for the company size and experience level
                count_dict[company_size] = {experience_level: 1}
    print(count_dict)
        
    # Create a DataFrame from the count dictionary
    df_count = pd.DataFrame(count_dict)
    # Fill missing values with 0
    df_count.fillna(0, inplace=True)
        
    # Plot the table using matplotlib
    fig, ax = plt.subplots()
    ax.axis('off')
    table = ax.table(cellText=df_count.values, colLabels=df_count.columns, rowLabels=df_count.index, loc='center', cellLoc='center', colWidths=[0.5]*len(df_count.columns))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    plt.title('Company Size vs Experience Level')
    plt.tight_layout()
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed",'company_size_experience_table.png')
    plt.savefig(output_dir, dpi=300)
    plt.show()            
    
    return df_count

def chi_squared_test_of_independence_company_size_vs_work_experience(df_count):
    # Perform the chi-squared test of independence
    chi2, p, dof, expected = chi2_contingency(df_count)
    print(f"Chi-squared: {chi2}")
    print(f"p-value: {p}")
    print(f"Degrees of freedom: {dof}") 
    print("Expected:")
    print(expected)
    if p < 0.05:
        print("Reject the null hypothesis: Company size and work experience are dependent")
    else:
        print("Fail to reject the null hypothesis: Company size and work experience are independent")
    
    # Create a table of expected values
    fig, ax = plt.subplots()
    ax.axis('off')
    table = ax.table(cellText=np.round(expected, 4), colLabels=df_count.columns, rowLabels=df_count.index, loc='center', cellLoc='center', colWidths=[0.5]*len(df_count.columns))
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    plt.title('Expected Values')
    plt.tight_layout()
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed",'expected_values.png')
    plt.savefig(output_dir, dpi=300)
    plt.show()
    
    # Find the value with the greatest contribution to the chi-squared statistic
    max_contribution = np.max((df_count.values - expected)**2 / expected)
    max_contribution_index = np.argmax((df_count.values - expected)**2 / expected)
    max_contribution_row = max_contribution_index // len(df_count.columns)
    max_contribution_col = max_contribution_index % len(df_count.columns)
    max_contribution_value = df_count.index[max_contribution_row], df_count.columns[max_contribution_col]
    print(f"The value with the greatest contribution to the chi-squared statistic is {max_contribution_value} with a contribution of {max_contribution}")
    
    # Create a plot of the chi-squared distribution
    x = np.linspace(0, 400, 100000)
    y = stats.chi2.pdf(x, dof)
    
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.fill_between(x, y, where=(x >= chi2), color='red', alpha=0.5)
    ax.axvline(x=chi2, color='black', linestyle='--')
    ax.annotate(f"  X^2: {np.round(chi2,4)}", xy=(chi2, 0.02), xytext=(chi2, 0.1), arrowprops=dict(facecolor='black', arrowstyle='->'))
    ax.set_xlabel('Chi-squared Statistic')
    ax.set_ylabel('Probability Density')
    ax.set_title('Chi-squared Distribution')
    plt.tight_layout()
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "DS_SAL_Data", "DS_SAL_Data_Processed",'chi_squared_distribution.png')
    plt.savefig(output_dir, dpi=300)
    plt.show()
    

if __name__ == '__main__':
    # Load the data
    csv_file_path = os.path.join("_data", "DS_SAL_Data", "ds_salaries.csv")
    
    # Analysis by Experience Level
    path_arr_exp = split_exp(csv_file_path)
    plot_sal_vs_exp(path_arr_exp)

    # Analysis by Type of Job
    path_arr_job = split_profession(csv_file_path)
    plot_average_salary_job(path_arr_job)

    # Analysis by Company Size
    path_arr_comp = split_company_size(csv_file_path)
    plot_salary_vs_company_size(path_arr_comp)

    # Analysis by Remote Status
    path_arr_remote = split_remote_rate(csv_file_path)
    plot_salary_vs_remote_status(path_arr_remote)

    # Create the company size and experience level table
    df_count = create_company_size_experience_table(path_arr_comp)
    chi_squared_test_of_independence_company_size_vs_work_experience(df_count)




