#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 13:27:45 2021

@author: AlvinXu
"""

#Initializing state variables
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost*portion_down_payment
current_savings = 0.0
r = 0.04
semi_annual_raise = 0.07
portion_saved = 0.0
total_month = 36


annual_salary = float(input("Enter the starting annual salary: "))

monthly_salary = annual_salary/12

#Saying rate without investment reture as upper bound
portion_saved = (down_payment/total_month)/monthly_salary

num_guesses = 0
low = 0
high = portion_saved*10000
guess = (high + low)//2

while abs(current_savings - down_payment) >= 100:
    month = 0
    monthly_salary = annual_salary/12
    current_savings = 0.0
    
    while month < total_month:
        current_savings += monthly_salary*guess/10000+current_savings*r/12
        month += 1
        if month%6 == 0:
            monthly_salary = monthly_salary*(1+semi_annual_raise)

        
    
    if current_savings < down_payment:
        low = guess
    else:
        high = guess
        
    guess = (high + low)//2
    num_guesses += 1


if guess >10000:
    print("It is not possible to pay the down payment in three years")
else:
    print("Best savings rate:", guess/10000)
    print("Steps in bisection search:", num_guesses)





