script= 'spirits of ice bless this domain with your aura'
# ward rohan used as an example
mantra='humana'
#the word of power used to represent the mana source for the word
scriptLen=len(script)
mantraLen=len(mantra)
# takes the length of the both the script and the mantra
iteration= int(scriptLen/mantraLen)+1
# i couldnt get the round up function to work so i converted it to an int to always round down and added +1 to allow for a round up
mantra1= mantra*iteration
# this repeats the mantra over so theres enough space to work with the length of the script

# this finds where in the matrix the spaces are and puts the location into a new matrix
spaceIndex=[]
for i in range(0,scriptLen):
  if script[i]==' ':
    spaceIndex.append(i)

# finds the total number of spaces in the string so it can be substracted from the mantraiteration
numSpaces=script.count(' ')

# truncates the mantra interation to that it is the same size length as the script without spaces
mantra2=mantra1[0:len(script)-numSpaces]
mantra2List=list(mantra2)

# puts spaces into the mantr iteration so that it has the same spaces as the original script
for i in range (0,len(spaceIndex)):
    mantra2List.insert(spaceIndex[i],' ')


#####################################################################################################################3#

# spaces are converted into '{' because im converting the values into ascii
script2Num=[]
script123= script.replace(' ','{')

#loop that turns all of the letters into ascii code and subtracts 97 so that a=0,z=25 and space('{')= 26
for i in range(0,scriptLen):
    script2Num.append(ord(script123[i])-97)###the int is either 96 97 based off index

mantraJoined=''.join(mantra2List)
# this can also be done for mantra but python's strcmp function isnt stupid so this code is unused
#mantra123=mantraJoined.replace(' ','{')
#mantra2Num=[]
#for i in range(0,len(mantra123)):
#   mantra2Num.append(ord(mantra123[i])-97)###the int is either 96 97 based off index
#print(mantra2Num)


# this is the matrix for all the cypher where the mantra is the y axis 'a=,b=,c=' and the script is the x axis 'list('abc..)'

a=list('abcdefghijklmnopqrstuvwxyz ')
b=list('bcdefghijklmnopqrstuvwxyza ')
c=list('cdefghijklmnopqrstuvwxyzab ')
d=list('defghijklmnopqrstuvwxyzabc ')
e=list('efghijklmnopqrstuvwxyzabcd ')
f=list('fghijklmnopqrstuvwxyzabcde ')
g=list('ghijklmnopqrstuvwxyzabcdef ')
h=list('hijklmnopqrstuvwxyzabcdefg ')
i=list('ijklmnopqrstuvwxyzabcdefgh ')
j=list('jklmnopqrstuvwxyzabcdefghi ')
k=list('klmnopqrstuvwxyzabcdefghij ')
l=list('lmnopqrstuvwxyzabcdefghijk ')
m=list('mnopqrstuvwxyzabcdefghijkl ')
n=list('nopqrstuvwxyzabcdefghijklm ')
o=list('opqrstuvwxyzabcdefghijklmn ')
p=list('pqrstuvwxyzabcdefghijklmno ')
q=list('qrstuvwxyzabcdefghijklmnop ')
r=list('rstuvwxyzabcdefghijklmnopq ')
s=list('stuvwxyzabcdefghijklmnopqr ')
t=list('tuvwxyzabcdefghijklmnopqrs ')
u=list('uvwxyzabcdefghijklmnopqrst ')
v=list('vwxyzabcdefghijklmnopqrstu ')
w=list('wxyzabcdefghijklmnopqrstuv ')
x=list('xyzabcdefghijklmnopqrstuvw ')
y=list('yzabcdefghijklmnopqrstuvwx ')
z=list('zabcdefghijklmnopqrstuvwxy ')

# opens up a blank array for the final encryption
encryption=[]

# this nasty slew of if else if statements goes though the cypher to pic the correct letter of the encyption based off the mantra and the scripts letters
for ii in range(0,scriptLen):
    if mantraJoined[ii]==' ':
        encryption.append(' ')

    elif mantraJoined[ii]=='a':
        encryption.append(a[script2Num[ii]])

    elif mantraJoined[ii]=='b':
        encryption.append(b[script2Num[ii]])

    elif mantraJoined[ii]=='c':
        encryption.append(c[script2Num[ii]])

    elif mantraJoined[ii]=='d':
        encryption.append(d[script2Num[ii]])

    elif mantraJoined[ii]=='e':
        encryption.append(e[script2Num[ii]])

    elif mantraJoined[ii]=='f':
        encryption.append(f[script2Num[ii]])

    elif mantraJoined[ii]=='g':
        encryption.append(g[script2Num[ii]])

    elif mantraJoined[ii]=='h':
        encryption.append(h[script2Num[ii]])

    elif mantraJoined[ii]=='i':
        encryption.append(i[script2Num[ii]])

    elif mantraJoined[ii]=='j':
        encryption.append(j[script2Num[ii]])

    elif mantraJoined[ii]=='k':
        encryption.append(k[script2Num[ii]])

    elif mantraJoined[ii]=='l':
        encryption.append(l[script2Num[ii]])

    elif mantraJoined[ii]=='m':
        encryption.append(m[script2Num[ii]])

    elif mantraJoined[ii]=='n':
        encryption.append(n[script2Num[ii]])

    elif mantraJoined[ii]=='o':
        encryption.append(o[script2Num[ii]])

    elif mantraJoined[ii]=='p':
        encryption.append(p[script2Num[ii]])

    elif mantraJoined[ii]=='q':
        encryption.append(q[script2Num[ii]])

    elif mantraJoined[ii]=='r':
        encryption.append(r[script2Num[ii]])

    elif mantraJoined[ii]=='s':
        encryption.append(s[script2Num[ii]])

    elif mantraJoined[ii]=='t':
        encryption.append(t[script2Num[ii]])

    elif mantraJoined[ii]=='u':
        encryption.append(u[script2Num[ii]])

    elif mantraJoined[ii]=='v':
        encryption.append(v[script2Num[ii]])

    elif mantraJoined[ii]=='w':
        encryption.append(w[script2Num[ii]])

    elif mantraJoined[ii]=='x':
        encryption.append(x[script2Num[ii]])

    elif mantraJoined[ii]=='y':
        encryption.append(y[script2Num[ii]])

    elif mantraJoined[ii]=='z':
        encryption.append(z[script2Num[ii]])



# prints everything for the user to read
print('SCRIPT:     '+script)
print('MANTRA:     '+mantra)
print('CONVERTED:  '+mantraJoined)

print('ENCRYPTION: '+ ''.join(encryption))


































