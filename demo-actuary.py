"""
Created on Mon May 14 12:32:41 2018

This is non-pandas demo version 
@author: Andrew Acosta
"""

import actuary

bal  = 120000. # initial balance
rate = 3.99/100. # annual interest rate
term = 36 # 36 month loan
loan = dict()

# This will make a dictory in this format
# {Month: Interest, Principal, Payment, Bal (Pro), Bal (Retro)}

for m in range(1, term+1):
    interest = actuary.InterestPaid(term, m, rate)*bal/actuary.AnnuityImmediateA(term, rate)
    
    remaining_principal = actuary.PrincipalPaid(term, m, rate)*bal/actuary.AnnuityImmediateA(term, rate)
    
    payment = bal/actuary.AnnuityImmediateA(term, rate)
    
    balance_pro = actuary.BalanceRemaining(term, m, rate) *  bal/actuary.AnnuityImmediateA(term,rate)
    
    balance_retro = actuary.BalanceRemainingR(term,m, rate) * bal/actuary.AnnuityImmediateA(term, rate)
    
    loan[m] = (interest, remaining_principal, payment,	balance_pro, balance_retro)