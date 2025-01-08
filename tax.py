ctc = int(input('Enter your anual CTC:'))

if ctc < 5000000:
    salary=ctc*.82
elif ctc<1000000:
    salary=ctc*.72
elif ctc<2000000:
    salary=ctc*.62
else:
    salary=ctc*.52

print("You in hand monthly salary will be-", round(salary/12,2))