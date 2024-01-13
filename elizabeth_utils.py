''' This module provides a reusable byline for the author's services. '''

import math
import statistics
company_name: str = "EA Consulting Services"
count_number_of_employees: int = 15
has_international_presence: bool = True
average_customer_rating: float = 4.9
services_offered: list = ["Power Bi to Tableau Migration", "Data modelling", "Data Visualization", "Expert Placement and Recruiting"]
customer_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#using formatted strings
number_of_employees_string: str = f"Active Employees: {count_number_of_employees}"
international_presence_string: str = f"International Presence: {has_international_presence}"
customer_rating_string: str = f"Average Customer Rating: {average_customer_rating}"

import statistics
smallest= min(customer_satisfaction_scores)
largest= max(customer_satisfaction_scores)
total= sum(customer_satisfaction_scores)
count= len(customer_satisfaction_scores)
mean= statistics.mean(customer_satisfaction_scores)
mode= statistics.mode(customer_satisfaction_scores)
median= statistics.median(customer_satisfaction_scores)
standard_deviation=statistics.stdev(customer_satisfaction_scores)

#Defining Main Function
def main():
    ''' Display all output'''
 print(company_name)
 print(number_of_employees_string)
 print(international_presence_string)
 print(customer_rating_string)
 print(services_offered)
   
