monthly_inc = float(input("Enter your monthly income: "))
monthly_exp = float(input("Enter your monthly expenses: "))
monthly_sav = monthly_inc - monthly_exp
print("Your monthly savings are","$",monthly_sav)
projected_sav = monthly_sav * 12 + (monthly_sav * 12 * 0.05)
print("Projected savings after one year, with interest, is:","$",projected_sav)