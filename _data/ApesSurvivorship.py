import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from lifelines import KaplanMeierFitter
from lifelines.utils import median_survival_times 
from lifelines.statistics import logrank_test

def prepare_data(csv_file):
    df = pd.read_csv(csv_file)
    
    # Getting base file name without the extension to construct output csv to account for multiple types across files with same name 
    file_base_name = os.path.splitext(os.path.basename(csv_file))[0]

    if 'Type' not in df.columns:
        raise ValueError("Column 'Type' not found in the CSV file")
    
    # Split the 'Type' column into separate rows
    df_expanded = df.assign(Type=df['Type'].str.split(',')).explode('Type')

    # Strip any extra whitespace from the 'Type' entries
    df_expanded['Type'] = df_expanded['Type'].str.strip()
    
    # Get the current directory
    current_dir = os.getcwd()

    # Construct the path to the CSV_Data_Processed directory
    output_dir = os.path.join(current_dir, "_data", "CSV_Data", "CSV_Data_Processed")

    path_output_array = []
    # Grouping the Data by the Type (Species, Breed, Gender, etc.)
    for type_name, group, in df_expanded.groupby('Type'):
        # Construct the path to the output file
        sanitized_type_name = type_name.replace('/', '_').replace('\\', '_')
        output_file = os.path.join(output_dir, f"{file_base_name}_{sanitized_type_name}.csv")
        path_output_array.append(output_file)
        # Save the grouped data to a new CSV file
        group.to_csv(output_file, index=False)
        
        print(f"Data saved to {output_file}")
    return path_output_array


def analyze_deaths(csv_file, stats_csv_file, age_band):
    # Function to calculate age range for a given age range of 5 years (e.g., 0-4, 5-9, etc.)
    def calculate_age_range(age, age_band):
        return int(age // age_band) * age_band

    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Making sure that the Data 
    if 'Age of Death' not in df.columns:
        raise ValueError("Column 'Age of Death' not found in the CSV file")

    # Create a new column 'Age Range' to store the age range for each person
    df['Age Range'] = df['Age of Death'].apply(calculate_age_range, args=(age_band,))

    # Initialize variables to store statistics
    age_range_stats = {}
    total_people = len(df)
    
    # Initialize variables to store cumulative deaths and surviving members
    cumulative_deaths = 0
    
    # Iterate through each unique age range
    for age_range in sorted(df['Age Range'].unique()):
        # Filter the DataFrame for the current age range
        age_range_df = df[df['Age Range'] == age_range]
        
        # Calculate the number of deaths in the current age range
        deaths_in_range = len(age_range_df)
        
        # Update cumulative deaths
        cumulative_deaths += deaths_in_range
        
        # Calculate the number of surviving members in the current age range
        surviving_members = total_people - cumulative_deaths
        
        # Calculate the mortality rate
        mortality_rate = cumulative_deaths / total_people
        
        # Store the statistics in a dictionary
        age_range_stats[age_range] = {
            'Deaths in Range': deaths_in_range,
            'Surviving Members': surviving_members,
            'Mortality Rate': mortality_rate
        }

    # Print the statistics
    for age_range, stats in age_range_stats.items():
        print(f"Age Range {age_range}-{age_range + age_band-0.1} years:")
        print(f"  Number of Deaths: {stats['Deaths in Range']}")
        print(f"  Surviving Members: {stats['Surviving Members']}")
        print(f"  Mortality Rate: {stats['Mortality Rate']:.2%}")
        print()

    # Create a DataFrame for the statistics
    stats_df = pd.DataFrame.from_dict(age_range_stats, orient='index')
    stats_df.index.name = 'Age Range'
    stats_df.reset_index(inplace=True)

    # Save the statistics to a new CSV file
    stats_df.to_csv(stats_csv_file, index=False)

    print(f"Statistics saved to {stats_csv_file}")

def perform_analysis(csv_file, age_range, separate_types):
    # Get the current directory
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "CSV_Output", "CSV_Output_Processed")
    output_file_arr = []
    
    if separate_types:
        data = prepare_data(csv_file)
        for path in data:    
            
            # Get the base file name without extension will be different due to Type Separation
            path_base_name = os.path.splitext(os.path.basename(path))[0]
            output_file = os.path.join(output_dir, f"{path_base_name}_statistics.csv")
            
            # Construct the path to the CSV_Output_Processed directory
            analyze_deaths(path, output_file, age_range)
            output_file_arr.append(output_file)
    else: 
        
        # Getting base file name
        path_base_name = os.path.splitext(os.path.basename(csv_file))[0]
        output_file = os.path.join(output_dir, f"{path_base_name}_statistics.csv")
        
        # Output to the CSV_Output Directory
        analyze_deaths(csv_file, output_file, age_range)
        output_file_arr.append(output_file)

    return output_file_arr

def plot_curve(csv_file, title):
    df = pd.read_csv(csv_file)

    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "CSV_Output", "CSV_Output_Processed")
    
    
    # Getting the file name of the CSV File Passed in 
    file_base_name = os.path.splitext(os.path.basename(csv_file))[0]
    output_path = os.path.join(output_dir, f"{file_base_name}_Survivorship_Curve.png")
    
    if "Age Range" not in df.columns:
        raise ValueError("Column 'Age Range' not found in the CSV file")
    
    age_range = df['Age Range']
    surviving_members = df['Surviving Members']
    plt.figure()
    plt.xlabel('Age Range')
    plt.ylabel('Surviving Members')
    plt.title(f'Survivorship Curve {title}')
    plt.plot(age_range, surviving_members, marker='.')
    
    # If You Want to Show the Plot  
    # plt.show()
    
    plt.savefig(output_path)  
    plt.close()



# If we wanted to expand beyond what you would see in APES and would be more realistic towards the actual
# world we would use the elements that are covered in the fields of Survival Analysis 
# There may be some calculus involved to determine function types either Type 1, 2, or 3 Survivorship Curves  
# Learn more https://en.wikipedia.org/wiki/Survivorship_curve 

def survival_analysis(csv_file):
    kaplan_meier_estimator = KaplanMeierFitter()
    df = pd.read_csv(csv_file)
    
    if "Surviving Members" not in df.columns:
        raise ValueError("Column 'Surviving Members' not found in the CSV file")
    
    # Creating a new DataFrame for duration or the life that each individual lived for 
    # Based on the amount of deaths in the age range adds the Age Range they died in to the DataFrame 
    duration = df['Age Range'].repeat(df['Deaths in Range'])

    # Using the fit function from the Lifelines library to the fit the Kaplan Meier Estimator Model to the Dataset
    # This is similar to what you may have seen scikit-learn's fit or prediction functionality
    kaplan_meier_estimator.fit(duration)
    
    # Getting the file name of the CSV File Passed in
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "_data", "CSV_Output", "CSV_Output_Processed")
    file_base_name = os.path.splitext(os.path.basename(csv_file))[0]
    output_path = os.path.join(output_dir, f"{file_base_name}_KMF_Survival_Function.png")
    
    # Plotting and saving the surivival function
    kaplan_meier_estimator.survival_function_.plot()
    plt.xlabel('Age Range')
    plt.ylabel('Survivorship Probability') 
    plt.savefig(output_path)


if __name__ == '__main__':
    # Get the current directory
    current_dir = os.getcwd()
    
    # Construct the path to the CSV_Data directory
    data_dir = os.path.join(current_dir, "_data", "CSV_Data")
    
    # Construct the path to the CSV_Output directory
    output_dir = os.path.join(current_dir, "_data", "CSV_Output")

    actuarial_data_19thC = os.path.join(data_dir, "actuarial_data_19th_cent_NJ_burials.csv")
    actuarial_data_20thC = os.path.join(data_dir, "actuarial_data_20th_cent_SD_burials.csv")

    # Data Source for Dog Data https://rvc-repository.worktribe.com/output/1558210 
    actuarial_data_dogs= os.path.join(data_dir, "dog_life_expectancy.csv")

    # A narrower age range allows for more detailed analysis, a wider one for a smoother less accurate curve 
    cent_19th_output_arr = perform_analysis(csv_file = actuarial_data_19thC, age_range = 5, separate_types = True)
    cent_20th_output_arr = perform_analysis(csv_file = actuarial_data_20thC, age_range = 5, separate_types = True)
    
    # Recommended to not separate_types for dogs due to many different breeds in the dataset creating too many files 
    # Unless you like 200+ files in your directory =)
    dog_path_output_arr = perform_analysis(csv_file = actuarial_data_dogs, age_range = 1, separate_types = False)
    
    for path in dog_path_output_arr:
        survival_analysis(path)
        plot_curve(path, "Dog Life Expectancy")

    for path in cent_19th_output_arr:
        survival_analysis(path)
        plot_curve(path, "19th Century Actuarial Data")

    for path in cent_20th_output_arr:
        plot_curve(path, "20th Century Actuarial Data")
        