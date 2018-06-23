_name="hugo"
_lastName="hidalgo"
print('Hola mundo python ' + _name)
_old = 36

#concatenar cadenas + numeros
print("Hola " + _name + " tu edad: " + str(_old))

Fname = "Hugo"
Lname = "Hidalgo"
Age = "24"


print("{} {} is {} years old".format(Fname,Lname,Age))
print("{0} {1} is {2} years old".format(Fname,Lname,Age))
print("{Fname} {Lname} is {Age} years old".format(Fname='hugo',Lname='hidalgo',Age=23))
