menu = input("""
Hi select an option
1. cms to ft
2. km to miles
3. USD to INR
4. Exit
""")

if menu == '1':
  cm = float(input('enter the cm value'))
  print('ft value is',0.032*cm)
elif menu == '2':
  km = float(input('enter the km value'))
  print('miles value is',km*0.62)
elif menu == '3':
  usd = float(input('enter usd'))
  print('inr',usd*80)
else:
  exit()