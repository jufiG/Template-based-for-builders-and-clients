class Fruits():
	x=5
	n=10
	def _init_(self,n):
		self.n=n
	def hai(self):
		print("this is fruit")
	def hello(self,colour):
		print("this is color",colour)
	def view(self,colour,number):
		print("this is number",number,colour)
p=Fruits()
print(p.n)
p.hai()
p.hello("red")
p.view("red",6)
print(p.x)
p.x=p.x+1
print(p.n)
q=Fruits()
print(q.x)
p.init()