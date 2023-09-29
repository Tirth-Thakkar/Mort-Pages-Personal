import pandas as pd

def analyze_deaths(csv_file, stats_csv_file):
    # Function to calculate age range for a given age
    def calculate_age_range(age):
        return int(age // 5) * 5

    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

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
    # Run Program here Path will change per system
    analyze_deaths('/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Data/19th_Cent_NJ_Burials_Women.csv', '/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Output/age_range_statistics_women_19th_cent.csv')
    analyze_deaths('/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Data/19th_Cent_NJ_Burials_Men.csv', '/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Output/age_range_statistics_men_19th_cent.csv')
    analyze_deaths('/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Data/20th_Cent_SD_Burials_Men.csv', '/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Output/age_range_statistics_men_20th_cent.csv')
    analyze_deaths('/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Data/20th_Cent_SD_Burials_Women.csv', '/home/tirth/vscode/Mort-Pages-Personal/_data/CSV_Output/age_range_statistics_women_th_cent.csv')