# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 11:27:03 2022

@author: Shaik Sohail

"""

import sys

try:
    # Inputs from the user
    
    marital_status = input("Enter M for married and S for single: ")
    monthly_hours_worked = float(input("Enter number of hours worked in the month: "))
    wage_rate = float(input("Enter the wage rate: "))
    bonus = float(input("Enter the bonus received: "))
    gross_income = (monthly_hours_worked * wage_rate) + bonus
    
    
    # This function computes the "FED TAXABLE GROSS" by taking gross_income
    # as an arugument
    def before_tax_deductions(gross_income):
        adjustments = 0 # default value
        var_401k = 0.187 * gross_income
        if var_401k > 20000:
            print("The 401k is capped to $20,000 by federal law")
            var_401k = 20000
        dental_plus = 0 # default value
        flex_med = 0 # default value
        var_403b = 0.05 * gross_income # It is 5% of gross income
        if var_403b > 7000:
            print("The 403b is capped to $7,000 by federal law")
            var_403b = 7000
        fed_taxable_gross = gross_income - (adjustments + var_401k + dental_plus\
                                            + flex_med + var_403b)
        return fed_taxable_gross
    
    # This function calculates taxable slabs based on gross income
    income = {'gross_income': gross_income}
    def tax_slabs(fed_taxable_gross,income_dict=income):
        for key , income in income_dict.items():
            yearly_income = income  * 12
            if yearly_income <= 10275: #tax slab 10%
                tax = 0.10 * fed_taxable_gross
            elif yearly_income >= 10275 and yearly_income < 41775:
                tax = 0.12 * fed_taxable_gross #tax slab 12%
            elif yearly_income >= 41775 and yearly_income < 89075:
                tax = 0.22 * fed_taxable_gross #tax slab 22%
            elif yearly_income >= 89075 and yearly_income < 170050:
                tax = 0.24 * fed_taxable_gross # tax slabs 24%
            else:
                tax = 0.3 * fed_taxable_gross #tax slab 30%

        return tax
    
    # This function computes medical and oasdi using tax deduction code of each filer 
    def fed_medical_and_oasdi(fed_taxable_gross):
        
        fed_med_ee = 0.0145 * fed_taxable_gross # 1.45% default value
        fed_oasdi_ee = 0.062 * fed_taxable_gross # 6.2% default value
        if (gross_income > 200000): # according to the tax deduction code table
            additional_med_tax = 0.009 * (gross_income - 200000)
        else:
            additional_med_tax = 0
        fed_medical_and_oasdi_deductions = fed_med_ee + fed_oasdi_ee +\
        additional_med_tax
        
        return fed_medical_and_oasdi_deductions
            
        
    # This function computes total taxes using tax slabs of each filer 
    # based on marital status and gross income
    def total_taxes(fed_taxable_gross):
        w4_exemptions = 0 #(Default value)
        fed_witholding = tax_slabs(fed_taxable_gross)
        fed_medical_and_oasdi_deductions = fed_medical_and_oasdi(fed_taxable_gross)
        
        after_tax_income = fed_taxable_gross - (w4_exemptions + fed_witholding + \
                                                fed_medical_and_oasdi_deductions)
            
        return after_tax_income
    
    # This function deals with after tax deductions after your tax income
    def after_tax_deductions(after_tax_income):
        group_life_insurance = 0 # Default value
        Supplemental_life_3x_salary = 0 # Default value
        long_term_disability = 60 #Default value
        
        after_tax_deductions = group_life_insurance + Supplemental_life_3x_salary+\
                                 long_term_disability
        
        return (after_tax_income - after_tax_deductions)
    
    # This function calls the three taxable functions which is required 
    # to calculate the net income
    def main(gross_income):
        
        fed_taxable_gross = before_tax_deductions(gross_income)
        after_tax_income = total_taxes(fed_taxable_gross)
        net_income = after_tax_deductions(after_tax_income)
        
        return net_income
    
    # main function calling
    net_income = main(gross_income)
    print("The net income for the given gross income is",net_income)
        
        
except ValueError:
    print("please enter valid formats, marital status should be a string.  Monthly hours, wage rate and bonus should be numbers")

except Exception :
    exc_type, fname, exc_tb = sys.exc_info()
    print(exc_type, "Line number: "+ str(exc_tb.tb_lineno))



