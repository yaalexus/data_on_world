# visualization of export, agriculture production, per capita income and population of 122 countries 
# import library Numeric python, Pandas and matplotlib
import numpy as np
# importing pandas, numpy and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Importing data from CSV file  
export_by_country = pd.read_csv("exports.csv")
income_per_capita = pd.read_csv("income_per_person.csv")
agriculture_production = pd.read_csv("agriculture_output.csv")
population_by_country = pd.read_csv("population.csv")

# generating numpy array
export = np.array(export_by_country)
exp = np.array(export[:,-1], dtype = float)
income = np.array(income_per_capita)
inc_pp = np.array(income[:,-1], dtype = float)
agriculture = np.array(agriculture_production)
agri = np.array(agriculture[:,-1], dtype = float)
population = np.array(population_by_country)
pop = np.array(population[:,-1], dtype = float)

# ploting data and customisation
plt.scatter(exp, agri , c=inc_pp ,s=pop/100000 , alpha = 0.5)
plt.xlabel('Exports of goods and services (% of GDP)')
plt.ylabel('Agriculture, value added (% of GDP)')
plt.title('(Size variation as per population and colour variation as per income per capita)')
plt.xlim(-10, 215)
plt.ylim(-5, 55)
plt.grid(True)
plt.text(190, -2, 'Singapore')
plt.text(171, 2, 'Luxembourg')
plt.text(34, 24, 'India 1.2 billion')
plt.text(48, 9, 'china 1.35 billion')
plt.text(19, 50, 'Sierra Leone')
plt.text(0, 0, 'USA')
plt.colorbar()
plt.show()
