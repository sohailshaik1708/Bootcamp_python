# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 11:00:42 2022

@author: Shaik Sohail
"""
import sys

try:
    # Inputs from the user
    # number of elements
    number_elements = int(input("Enter number of employees you want to calculate for: "))
    # Below line read inputs from user using map() function 
    monthly_hours_worked_list = list(map(float,input("\nEnter the hours they have worked: ").strip().split()))[:number_elements]
    wage_rate_list = list(map(float,input("\nEnter the wages they are paid: ").strip().split()))[:number_elements]
    bonus_list = list(map(float,input("\nEnter the bonuses they got: ").strip().split()))[:number_elements]

    gross_income_list = []
    for hours,wage,bonus in zip(monthly_hours_worked_list,wage_rate_list,bonus_list):
        gross_income = (hours * wage) + bonus
        gross_income_list.append(gross_income)
        
    
    # This function computes the "FED TAXABLE GROSS" by taking gross_income
    # as an arugument
    def before_tax_deductions(gross_income_list):
        fed_taxable_gross_list = []
        fed_taxable_gross_deductions_list = []
        for gross_income in gross_income_list:
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
                
            fed_taxable_gross_deductions = (adjustments + var_401k + dental_plus\
                                                + flex_med + var_403b)
            fed_taxable_gross = gross_income - fed_taxable_gross_deductions
            
            fed_taxable_gross_deductions_list.append(fed_taxable_gross_deductions)
            
            fed_taxable_gross_list.append(fed_taxable_gross)
            
        return fed_taxable_gross_list, fed_taxable_gross_deductions_list
    
    # This function calculates taxable slabs based on gross income
    def tax_slabs(fed_taxable_gross_list,gross_income_list):
        tax_list = []
        for taxable_gross , gross_income in zip(fed_taxable_gross_list,gross_income_list):
            yearly_income = gross_income  * 12
            if yearly_income <= 10275: #tax slab 10%
                tax = 0.10 * taxable_gross
            elif yearly_income >= 10275 and yearly_income < 41775:
                tax = 0.12 * taxable_gross #tax slab 12%
            elif yearly_income >= 41775 and yearly_income < 89075:
                tax = 0.22 * taxable_gross #tax slab 22%
            elif yearly_income >= 89075 and yearly_income < 170050:
                tax = 0.24 * taxable_gross # tax slabs 24%
            else:
                tax = 0.3 * taxable_gross #tax slab 30%
                
            tax_list.append(tax)

        return tax_list
    
    # This function computes medical and oasdi using tax deduction code of each filer 
    def fed_medical_and_oasdi(fed_taxable_gross_list):
        fed_medical_and_oasdi_deductions_list = []
        for taxable_gross, gross_income in zip(fed_taxable_gross_list,gross_income_list):
            fed_med_ee = 0.0145 * taxable_gross # 1.45% default value
            fed_oasdi_ee = 0.062 * taxable_gross # 6.2% default value
            if (gross_income > 200000): # according to the tax deduction code table 
                additional_med_tax = 0.009 * (gross_income - 200000)
            else:
                additional_med_tax = 0
                
            fed_medical_and_oasdi_deductions = fed_med_ee + fed_oasdi_ee +\
            additional_med_tax
            
            fed_medical_and_oasdi_deductions_list.append(fed_medical_and_oasdi_deductions)
            
        return fed_medical_and_oasdi_deductions_list
    
    # This function computes total taxes using tax slabs of each filer 
    # based on marital status and gross income
    def total_taxes(fed_taxable_gross_list):
        w4_exemptions = 0 #(Default value)
        fed_witholding_list = tax_slabs(fed_taxable_gross_list,gross_income_list)
        fed_medical_and_oasdi_deductions_list = fed_medical_and_oasdi(fed_taxable_gross_list)
        
        after_tax_income_list = []
        for fed_taxable_gross,fed_witholding,fed_medical_and_oasdi_deductions in \
            zip(fed_taxable_gross_list,fed_witholding_list,fed_medical_and_oasdi_deductions_list):
                
                after_tax_income = fed_taxable_gross - (w4_exemptions + fed_witholding + \
                                                fed_medical_and_oasdi_deductions)
                
                after_tax_income_list.append(after_tax_income) 
            
        return after_tax_income_list,fed_witholding_list,fed_medical_and_oasdi_deductions_list
    
    # This function deals with after tax deductions after your tax income
    def after_tax_deductions(after_tax_income_list):
        group_life_insurance = 0 # Default value
        Supplemental_life_3x_salary = 0 # Default value
        long_term_disability = 60 #Default value
        
        after_tax_deductions_var = group_life_insurance + Supplemental_life_3x_salary+\
                                 long_term_disability
        
        net_income_list = []
        for after_tax_income in after_tax_income_list:
            net_income = after_tax_income - after_tax_deductions_var
            net_income_list.append(net_income)
        
        
        return net_income_list,after_tax_deductions_var
    
    
    # This function calls the three taxable functions which is required 
    # to calculate the net income
    def main(gross_income_list):
        
        fed_taxable_gross_list, fed_taxable_gross_deductions_list = before_tax_deductions(gross_income_list)
        after_tax_income_list,fed_witholding_list,fed_medical_and_oasdi_deductions_list = total_taxes(fed_taxable_gross_list)
        net_income_list, after_tax_deductions_var = after_tax_deductions(after_tax_income_list)
        
        return fed_taxable_gross_list,fed_taxable_gross_deductions_list, after_tax_income_list,fed_witholding_list,fed_medical_and_oasdi_deductions_list,net_income_list,after_tax_deductions_var
    
    # main function calling
    fed_taxable_gross_list,fed_taxable_gross_deductions_list,after_tax_income_list,fed_witholding_list,fed_medical_and_oasdi_deductions_list,net_income_list,after_tax_deductions_var = main(gross_income_list)
    
    # In the payroll_dictionary I am storing each record of employee in the dictionary, so that it will be further useful
    # for storing it in databases or converting it into dataframe and do further computations or visualizations.

    ''' Sample Output for this dictoinary
        {0: {'gross_income': 4200.0, 
             'fed_taxable_gross_deductions': 995.4, 
             'total taxes': {'fed_witholding': 705.012, 'fed_medical_and_oasdi_deductions': 245.15189999999998}, 
             'after_tax_income': 2254.4361, 
             'after_tax_income_deductions': 60, 
             'net_income': 2194.4361},
         1: {'gross_income': 6000.0, 
             'fed_taxable_gross_deductions': 1422.0,
             'total taxes': {'fed_witholding': 1007.16, 'fed_medical_and_oasdi_deductions': 350.217}, 
             'after_tax_income': 3220.623, 
             'after_tax_income_deductions': 60, 
             'net_income': 3160.623}
         ...
         .
         .
    '''
    payroll_dictionary = {}
        
    for idx, (gross_income,fed_taxable_gross_deductions,after_tax_income,fed_witholding,fed_medical_and_oasdi_deductions,net_income) in enumerate(zip(gross_income_list, fed_taxable_gross_deductions_list, after_tax_income_list,fed_witholding_list,fed_medical_and_oasdi_deductions_list,net_income_list)):
        payroll_dictionary[idx] = {}
        payroll_dictionary[idx]['gross_income'] = gross_income
        payroll_dictionary[idx]['fed_taxable_gross_deductions'] = fed_taxable_gross_deductions
        payroll_dictionary[idx]['total taxes'] = {}
        payroll_dictionary[idx]['total taxes']['fed_witholding'] = fed_witholding
        payroll_dictionary[idx]['total taxes']['fed_medical_and_oasdi_deductions'] = fed_medical_and_oasdi_deductions
        payroll_dictionary[idx]['after_tax_income'] = after_tax_income
        payroll_dictionary[idx]['after_tax_income_deductions'] = after_tax_deductions_var
        payroll_dictionary[idx]['net_income'] = net_income
        
    print(payroll_dictionary)
    
        
except ValueError as e:
    print("please enter valid formats: ", e)

except Exception :
    exc_type, fname, exc_tb = sys.exc_info()
    print(exc_type, "Line number: "+ str(exc_tb.tb_lineno))
