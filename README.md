![divvy](https://user-images.githubusercontent.com/10078499/124369903-41e6ec00-dc71-11eb-966d-b5a686dd260e.jpg)
# Data Exploration with pandas on Bikeshare Data
Bikeshare data exploration using pandas library in Python for basic Udacity project.

## Overview
In this project, I will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I will write code to import the data and answer interesting questions about it by computing descriptive statistics. I will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

## How to Run:
- Clone the project
- Prerequisite
     - You must have installed python and libraries like numpy and pandas.
- Run the project
     - Open the terminal
     - And run python Bikeshare.py

## The Datasets:
- Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
   - Start Time (e.g., 2017-01-01 00:07:57)
   - End Time (e.g., 2017-01-01 00:20:53)
   - Trip Duration (in seconds - e.g., 776)
   - Start Station (e.g., Broadway & Barry Ave)
   - End Station (e.g., Sedgwick St & North Ave)
   - User Type (Subscriber or Customer)
- The Chicago and New York City files also have the following two columns:
   - Gender
   - Birth Year

## Program Details:
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:

> - Most popular month
> - Most popular day
> - Most popular hour
> - Most popular start station
> - Most popular end station
> - Most popular combination of start and end stations
> - Total trip duration
> - Average trip duration
> - Types of users by number
> - Types of users by gender (if available)
> - The oldest user (if available)
> - The youngest user (if available)
> - The most common birth year amongst users (if available)

Finally, the user is prompted with the choice of restarting the program or not.

## Requirements:
* [Python 3.6.6](https://www.python.org/) - The language used to develop this.
* [pandas](https://pandas.pydata.org/) - One of the libraries used for this.
* [numpy](https://numpy.org/) - One of the libraries used for this.
* [time](https://docs.python.org/3/library/time.html) - One of the libraries used for this.
