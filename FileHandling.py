f = open("abc.txt", "r")
# f.write(" - The Gurukul for Coders!")

# str = f.read()

# str = f.readline()
# str += f.readline(5)

# str = f.readlines()

f.seek(3, 0)
str = f.readline()
print(str)

#f.seek(3, 1)
#str = f.readline()
#print(str)


#f.seek(3, 1)
#str = f.readline()
#print(str)


#f.seek(3, 1)
#str = f.readline()
#print(str)


f.close()