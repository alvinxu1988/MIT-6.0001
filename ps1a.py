#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:32:58 2021

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

monthly_salary = annual_salary/12

print(annual_salary, portion_saved, total_cost, monthly_salary)

while current_savings < total_cost*portion_down_payment:
    current_savings += monthly_salary*portion_saved+current_savings*r/12
    month += 1

print("Number of months:", month)