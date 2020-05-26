f = open("input.txt","r") #尮e fila vi skal telle vokaler med lesetilgang

f_out = open("output.txt","w")
file_content = f.read()

count = 0

for i in file_content:
    if (i == 'a') or (i == 'A'):
        count = count + 1

print(count)

f_out.write("A or a:")
f_out.write(str(count))

f.close() #alltid lukk fula etter bruk
f_out.close()


#test_str = f.read()

#print(test_str[1])

#count = 0

#for i in test_str:
#if i =='o':

#count = count + 1