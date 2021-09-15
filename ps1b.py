#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 23:56:05 2021

@author: AlvinXu
"""

#Initializing state variables
total_cost = 0.0
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
annual_salary = 0.0
portion_saved = 0.0
month = 0


#Retrieve user inputs
annual_salary = float(input("The starting annual salary: "))
portion_saved = float(input("The portion of salary to be saved: "))
total_cost = float(input("The cost of your dream home: "))
semi_annual_raise = float(input("The semi-annual salary raise: "))

monthly_salary = annual_salary/12

print(annual_salary, portion_saved, total_cost, monthly_salary)

while current_savings < total_cost*portion_down_payment:
    current_savings += monthly_salary*portion_saved+current_savings*r/12
    month += 1
    if month%6 == 0:
        monthly_salary *= 1+semi_annual_raise

print("Number of months:", month)