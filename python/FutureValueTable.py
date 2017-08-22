

def main():

	#program to calculate the value of an investment
	print("Future Value with interest compounded annually")
	print("---------------------------------------------")
	print("Year Amount(5%)  Amount(6%)  Amount(7%)  Amount(8%)  Amount(9%)  Amount(10%)")
	print("---- ----------	----------	----------	----------	----------	-----------")

	future_value = 0
	principal = 1000


	for k in range(1,11):
		message = ''
		for q in range (5,11):
			#future_value = principal * (1 + (i * j))
			message += ("	  " +format(principal * ((1 + (q/100))**k), '.2f'))
		print (k,message)

	print(" ")
	print(" ")
	print("Future value with simple annual interest")
	print("---------------------------------------------")
	print("Year Amount(5%)  Amount(6%)  Amount(7%)  Amount(8%)  Amount(9%)  Amount(10%)")
	print("---- ----------	----------	----------	----------	----------	-----------")

	for i in range(1,11):
		message = ''
		for j in range (5,11):
			#future_value = principal * (1 + (i * j))
			message += ( "	  " + format(principal * (1 + (i * (j/100))), '.2f'))
		print( i,message)

main()