
f=open('dat.txt','rb')
dat=f.read()
f.close()

rows = dat.split(b'\n')

nums=[]

for row in rows:
	tmp = row[40:48]
	tmp=list(tmp)
	tmp.reverse()
	tmp=bytes(tmp)
	type(tmp)
	try:
		nums.append(int(tmp,16))
	except ValueError as ve:
		print("Opps")
		print(ve)
'''
for i in range(len(nums)):
	print(type(nums[i]))
	print(nums[i])
	'''

for i in range(len(nums)-2):
	print("sub = %d " % ((nums[i+1]- nums[i] ) / 1024) )
	