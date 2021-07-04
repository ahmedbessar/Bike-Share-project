# Basic Data Exploration with pandas on Bikeshare Data
Bikeshare data exploration using pandas library in Python for basic Udacity project.

## Overview
In this project, I will make use of Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I will write code to import the data and answer interesting questions about it by computing descriptive statistics. I will also write a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

## Running the program:
You can input 'python bikeshare.py' on your terminal to run this program. I use Anaconda's command prompt on a Windows 10 machine.

## Program details:
The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:

> - Most popular month
.Most popular day
.Most popular hour
.Most popular start station
.Most popular end station
.Most popular combination of start and end stations
.Total trip duration
.Average trip duration
Types of users by number
Types of users by gender (if available)
The oldest user (if available)
The youngest user (if available)
The most common birth year amongst users (if available)

