# Import the pandas library
import pandas as pd

# Load the CSV data into a pandas DataFrame
data = pd.read_csv("job_data.csv")

# Define the job titles for which you want to compute the average salary
job_titles = ["Data Architect", "Senior Business Analyst", "Data Scientist", "Machine Learning Engineer"]

# Initialize a dictionary to store the average salaries for each job title
average_salaries = {}

# Compute the average salary for each job title
for title in job_titles:
    # Filter the data for the current job title
    filtered_data = data[data["job_title"] == title]
    
    # Calculate the average salary for the filtered data
    average_salary = filtered_data["num_of_salaries"].mean()
    
    # Store the result in the dictionary
    average_salaries[title] = average_salary

# Print the average salaries
for title, average_salary in average_salaries.items():
    print(f"Average Salary for {title}: {average_salary:.2f}")
