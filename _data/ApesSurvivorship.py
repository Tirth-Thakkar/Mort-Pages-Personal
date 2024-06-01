import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def prepare_data(csv_file):
    df = pd.read_csv(csv_file)

    if 'Type' not in df.columns:
        raise ValueError("Column 'Type' not found in the CSV file")
    
    # Split the 'Type' column into separate rows
    df_expanded = df.assign(Type=df['Type'].str.split(',')).explode('Type')

    # Strip any extra whitespace from the 'Type' entries
    df_expanded['Type'] = df_expanded['Type'].str.strip()
    
    # Get the current directory
    current_dir = os.getcwd()

    # Construct the path to the CSV_Output directory
    output_dir = os.path.join(current_dir, "_data", "CSV_Data", "CSV_Data_Processed")

    # Grouping the Data by the Type (Species, Breed, Gender, etc.)
    for type_name, group, in df_expanded.groupby('Type'):
        # Construct the path to the output file
        sanitized_type_name = type_name.replace('/', '_').replace('\\', '_')
        output_file = os.path.join(output_dir, f"{sanitized_type_name}.csv")
        
        # Save the grouped data to a new CSV file
        group.to_csv(output_file, index=False)
        
        print(f"Data saved to {output_file}")

def analyze_deaths(csv_file, stats_csv_file):
    # Function to calculate age range for a given age
    def calculate_age_range(age):
        return int(age // 5) * 5

    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Making sure that the Data 
    if 'Age of Death' not in df.columns:
        raise ValueError("Column 'Age of Death' not found in the CSV file")

    # Create a new column 'Age Range' to store the age range for each person
    df['Age Range'] = df['Age of Death'].apply(calculate_age_range)

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
        print(f"Age Range {age_range}-{age_range + 4.9} years:")
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

if __name__ == '__main__':
    # Get the current directory
    current_dir = os.getcwd()
    
    # Construct the path to the CSV_Data directory
    data_dir = os.path.join(current_dir, "_data", "CSV_Data")
    
    # Construct the path to the CSV_Output directory
    output_dir = os.path.join(current_dir, "_data", "CSV_Output")
    
    # # Define the file names
    # women_19th_cent_file = os.path.join(data_dir, "19th_Cent_NJ_Burials_Women.csv")
    # men_19th_cent_file = os.path.join(data_dir, "19th_Cent_NJ_Burials_Men.csv")
    # men_20th_cent_file = os.path.join(data_dir, "20th_Cent_SD_Burials_Men.csv")
    # women_20th_cent_file = os.path.join(data_dir, "20th_Cent_SD_Burials_Women.csv")
    
    # # Define the output file names
    # women_19th_cent_stats_file = os.path.join(output_dir, "age_range_statistics_women_19th_cent.csv")
    # men_19th_cent_stats_file = os.path.join(output_dir, "age_range_statistics_men_19th_cent.csv")
    # men_20th_cent_stats_file = os.path.join(output_dir, "age_range_statistics_men_20th_cent.csv")
    # women_20th_cent_stats_file = os.path.join(output_dir, "age_range_statistics_women_20th_cent.csv")
    
    # # Run the analyze_deaths function for each file
    # analyze_deaths(women_19th_cent_file, women_19th_cent_stats_file)
    # analyze_deaths(men_19th_cent_file, men_19th_cent_stats_file)
    # analyze_deaths(men_20th_cent_file, men_20th_cent_stats_file)
    # analyze_deaths(women_20th_cent_file, women_20th_cent_stats_file)

    dog_life_expectancy = os.path.join(data_dir, "dog_life_expectancy.csv")
    acturial_data_19thC = os.path.join(data_dir, "actuarial_Data_19th_cent_NJ_burials.csv")
    acturial_data_20thC = os.path.join(data_dir, "actuarial_Data_20th_cent_SD_burials.csv")

    prepare_data(dog_life_expectancy)
    prepare_data(acturial_data_19thC)
    prepare_data(acturial_data_20thC)
    