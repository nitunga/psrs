# f = open("psrs1.txt", "w")

# f = open("psrs.txt","w")
# f.write("Hello World")
# f.close()

# f = open("psrs.txt", "r")
# print(f.read())


f = open('psrs.txt', 'r+')
# f.write("\n elisha nyagwaru \n")
# f.close()
f.truncate(0)
f.close()

f = open("psrs.txt", "r")
print(f.read())
