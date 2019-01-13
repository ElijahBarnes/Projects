#Get the three points to make the circle. Remember x_2,y_2 
#is the vertex that this circle is for.
print "Please input the coordinates of the 3 points"
print "x_1 is"
x_1 = input()
print "y_1 is"
y_1 = input()
print "x_2 is"
x_2 = input()
print "y_2 is"
y_2 = input()
print "x_3 is"
x_3 = input()
print "y_3 is"
y_3 = input()

a=((x_3**2 + y_3**2 - x_2**2 - y_2**2)/(2*(x_3-x_2))-((y_3-y_2)/(x_3-x_2)*(x_3**2 + y_3**2 - x_1**2 - y_1**2)/(y_3-y_1)))/(1-2*(x_3-x_1)*(y_3-y_2)/(x_3-x_2)*(y_3-y_1))

b=(x_3**2 + y_3**2 - x_1**2 - y_1**2-2*a*(x_3-x_1))/(2*(y_3-y_1))

r=((x_2-a)**2 + (y_2-b)**2 )**0.5
print "The center of the circle is (%s,%s)" %(a,b)
print "The radius of the circle is %s" %r