class	Counter:
	count=0

	def __init__(self,uname,upass):
	self.username=uname
	self.password=upass
	Counter.count=Counter.count+1
c1=Counter("ju","123")
c2=Counter("ja","456")
print("object count=",Counter.count)
	
	