"""
EA Marketing Services

This module provides a reusable byline for transportation services.

"""

import math
import statistics

# Company information
company_name = "EA Marketing Services"
count_active_projects = 5
has_international_presence = False
average_client_satisfaction = 4.7
services_offered = ["Rebranding", "Logo Design", "Proposal Writeups"]
satisfaction_scores = [4.8, 4.6, 4.9, 5.0, 4.7, 8.3, 0.7, .27,.32]

# Statistics calculations
smallest = min(satisfaction_scores)
largest = max(satisfaction_scores)
total = sum(satisfaction_scores)
count = len(satisfaction_scores)
mean = statistics.mean(satisfaction_scores)
mode = statistics.mode(satisfaction_scores)
median = statistics.median(satisfaction_scores)
standard_deviation = statistics.stdev(satisfaction_scores)

# Descriptive statistics string
stats_string = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

def main():
    ''' Display company information and statistics '''
    print("Company Information:")
    print(f"Company Name: {company_name}")
    print(f"Active Projects: {count_active_projects}")
    print(f"International Presence: {has_international_presence}")
    print(f"Average Client Satisfaction: {average_client_satisfaction}")

    print("\nServices Offered:")
    for service in services_offered:
        print(f"- {service}")

    print("\nDescriptive Statistics:")
    print(stats_string)

if __name__ == "__main__":
    main()

    print(byline)



   
