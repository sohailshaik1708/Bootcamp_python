# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 13:31:17 2022

@author: Sohail Shaik
"""

import sys                # import statement for sys to use functions like exit, quit etc
import numpy as np        # numpy to compute math operations

try:
    tvm_list = []   #empty list to store time value money problem variables
    # present value is entered by the user, it is stripped left and right for any spaces and ',' is replaced with empty string 
    # if the value is not entered then it is defaulted with '0'
    present_value = float(input('Please enter the present value: ').strip().replace(',','') or 0)
    
    # the values are appended to a list for further computations
    tvm_list.append(present_value)
    
    # future value is entered by the user, it is stripped left and right for any spaces and ',' is replaced with empty string 
    # if the value is not entered then it is defaulted with '0'
    future_value = float(input('Please enter the future value: ').strip().replace(',','') or 0)
    # the values are appended to a list for further computations
    tvm_list.append(future_value)
    # discount rate is entered by the user, it is stripped left and right for any spaces and '%' is replaced with empty string 
    # if the value is not entered then it is defaulted with '0'
    discount_rate = float(input('please enter the discounting rate in percentage: ').strip().replace('%','') or 0)
    # the values are appended to a list for further computations
    tvm_list.append(discount_rate)
    # compounding rate is entered by the user, it is stripped left and right for any spaces and ',' is replaced with empty string 
    # if the value is not entered then it is defaulted with '0'
    compounding = float(input('Please enter the compounding rate example: Enter 1 for yearly, 2 for half yearly 4 for quarterly and so on..: ').strip().replace(',','') or 0)
    # the values are appended to a list for further computations
    tvm_list.append(compounding)
    # time period is entered by the user, it is stripped left and right for any spaces and ',' is replaced with empty string 
    # if the value is not entered then it is defaulted with '0'
    time_period = float(input('please enter the time period to compute: ').strip().replace(',','') or 0)
    # the values are appended to a list for further computations
    tvm_list.append(time_period)
    
    #This is a lambda function which counts the number of unknows in the output, if there are more than
    # one missing inputs then the program will exit and tell the user to enter the input from the begining
    null_counts = lambda x : x.count(0)
    count = null_counts(tvm_list)
    #if 2 or more missing values then exit
    if count >= 2:
        print('Please enter atleast four non zero integer/float values in the input, PROGRAM EXIT!!!')
        sys.exit()
        
    # In this if condition loop we are calculating present value, given all other parameters
    if present_value == 0.0:
        # Formula for present value 
        # PV = Future value/(1+ discounting rate/compounding)** (compounding * time period)
        discounting_factor = (1 + ((discount_rate * 0.01)/compounding)) # multiplying discount rate with  0.01 to convert % in decimals      
        present_value = future_value/(discounting_factor ** (compounding * time_period))
        print("The present value is: ", round(present_value,2)) #rounding the present value to 2 decimals
     # In this if condition loop we are calculating present value, given all other parameters
    elif future_value == 0.0:
        # Formula for future value 
        # FV = present value * (1 + discounting rate/compounding) ** (compounding * time)
        # ** represents exponent in python.
        discounting_factor = (1 + ((discount_rate * 0.01)/compounding)) # multiplying discount rate with  0.01 to convert % in decimals      
        future_value = present_value * (discounting_factor) ** (compounding * time_period)
        print("The future value is: ", round(present_value,2))
    elif discount_rate == 0.0:
        # Formula for discount rate 
        # r (discount_rate) = (compounding * (((future_value/present_value) ** 1/(compounding * time_period)) - 1))
        var_time_factor = 1/(compounding * time_period) # stored this in another variable so that equation looks aesthetic
        discount_rate = (compounding * (((future_value/present_value) ** var_time_factor) - 1))
        print(f"The discount rate is: {round(discount_rate * 100,2)}%" ) # multiplied by 100 because to convert it into % from decimals and then round it by 2
        # Used python f strings to show the value and % symbol
    elif time_period == 0.0:
        # Formula for time period
        # t (time period) =  log(future_value/present_value)/ compounding * (log(1 + (discount_rate * 0.01)/compounding))
        var_numerator = np.log(future_value/present_value) # using numpy package for logarithm
        var_denomenator = compounding * (np.log(1 + (discount_rate * 0.01)/compounding))
        time_period = var_numerator/var_denomenator # divided both the equations
        print("The time period is: ", round(time_period,2)) #rouding the time period to 2 decimal places
    else:
        print('It is very difficult to calculate compounding period') # finding out the equation for compounding frequency is difficult, 
        # as it requires substituting 'm' values until both sides of the equations are approximately equal inshort the answer works on approximations.
except ValueError as e:
    print('please enter valid number data types in the input ', e)
except Exception :
    exc_type, fname, exc_tb = sys.exc_info()
    print(exc_type, "Line number: "+ str(exc_tb.tb_lineno))

