#!/usr/bin/env python
# coding: utf-8

# In[1]:


#the sum of first five integers
1+2+3+4+5


# In[2]:


#the average of sara(age23), mark(age19) and fatima age(32)
a=(23+19+32)/3
print("average age is :",a )


# In[3]:


#the number of times 73 goes into 403
403//73


# In[4]:


#2 to the power 10th
2**10


# In[5]:


#absolute value 
abs(54-57)


# In[7]:


#lowest price
a=(34.99,29.95,31.50)
min(a)


# In[10]:


#sum of 2 and 2 is less than 4
2+2<4


# In[14]:


#the value of 7 // 3 is equal to 1+1
7 // 3 == 1+1


# In[15]:


#the sum of the three square and four square is equal to 25
(3**2)+(4**2) == 25


# In[16]:


#the sum of 2,4 and 6 is greater than 12
2+4+6>12


# In[18]:


#the lowest price among $34.99, 29.95 and 31.40 is less than 30.00
a=min(34.99 ,29.95 ,31.40)
b = a < 30.00
print(b)


# In[20]:


#assign the value 3 to variable a
a = 3
#assign tha value 4 to variable b
b = 4
#assign the value of c to a*a + b*b
c = (a*a)+(b*b)
print(c)


# In[16]:


#start by executing the assignment statement
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1 + " " + s2 + " " + s3)
print(10 * (s1 + " "))
print(s1 , s2 ,s2 ,s3, s3 , s3, s3 )
print((s2+s2+s3) ,(s2+s2+s3), (s2+s2+s3), (s2+s2+s3), (s2+s2+s3))


# In[17]:


#start by executing the assignment 
s = '0123456789'
#now write the sngle experssion using stringle s and the index operator that evalute to 
print(s[0])
print(s[1])
print(s[6])
print(s[8])
print(s[9])


# In[18]:


#first excute the assignment
words = ['bat','ball','barn','basket','badminton']
print(min(words))
print(max(words))


# In[31]:


#given the list of student homework grade
grades = [9,7,7,10,3,9,6,6,2]
#an experssion that evalute to the number of 7 grades
print(grades.count(7))
#An statement that change the last to the 4
print(grades.append(4))
print(max(grades))
print(min(grades))
avg = (9+7+7+10+3+9+6+6+2)/9
print(avg)
print(sum(grades))
print(len(grades))
print((sum(grades))/(len(grades)))


# In[2]:


#(a)
a=((2+3)==4)or  (a>=5)
print(a)


# In[3]:


#(a)
a=False+False
b=type(a)
print(b)
#(b)
c=2*3**2.0
d=type(c)
print(d)
#(c)
e=(4//2)+(4%2)
f=type(e)
print(f)
#(d)
x=(2+3)==4 or 5>=5
y=type(x)
print(y)


# In[ ]:


#(a)
#using pythagoraus theorem
from math import sqrt
c=sqrt((a**2)+(b**2))


# In[ ]:


#(b)
c==5


# In[ ]:


#(c)
pi=3.142
area=pi*(a**2)#(d)
(x-a)**2 + (y-b)**2 < r**2


# In[ ]:


#(d)
(x-a)**2 + (y-b)**2 < r**2


# # 2.11

# In[1]:


#(a)
(-1)+(-2)+(-3)+(-4)+(-5)+(-6)+(-7)


# In[2]:


#(b)


# In[ ]:


#(c)
2**(-20)


# In[3]:


#(d)
4356//61


# In[4]:


#(e)
4356%61


# # 2.12

# In[ ]:


s1='-'
s2='+'
#(a)
s1+s2


# In[ ]:


#(b)
s1+s2+s1


# In[ ]:


#(c)
s2+s1+s1


# In[ ]:


#(e)
(s2+s1+s1)*10+s2


# In[ ]:


#(f)
(s2+s1+(s2*3)+(s1*2))*5


# # 2.13

# In[ ]:


s='abcdefghijklmnopqrstuvwxyz'
#(a)
s[0]


# In[ ]:


#(b)
s[2]


# In[ ]:


#(c)
s[-1]


# In[ ]:


#(d)
s[-2]


# In[ ]:


#(e)
s[16]


# # 2.14

# In[5]:


s='goodbye'
#(a)
s[0]=='g'


# In[6]:


#(b)
s[6]=='g'


# In[7]:


#(c)
s[0]+s[1]=='g'+'a'


# In[9]:


#(d)
s[-2]=='x'


# In[10]:


#(e)
s[3]=='d'


# In[11]:


#(f)
s[0]==s[-1]


# In[12]:


#(g)
s[-1]+s[-2]+s[-3]+s[-4]=='tion'


# # 2.14

# In[13]:


#(a)
a='anachronistically'
b='counterintuitive'
len(a)>len(b)


# In[14]:


#(b)
a=['misrepresentation','misinterpretation']
a.sort()
a


# In[15]:


#(c)
a='floccinaucinihilipilification'
'e' not in a


# In[16]:


#(d)
a=('counterrevolution')
b=('counter')
c=('resolution')
len(a)==len(b)+len(c)


# # 2.16

# In[18]:



#(a)
a=6
b=7
#(b)
c=a+b/2
#(c)
inventory=['paper','staples','pencils']
#(d)
first='John'
middle='Fitzegrald'
last='Kennedy'
#(e)
fullname=first+''+middle+''+last


# # 2.17

# In[19]:


#(a)
17+(-9)<10


# In[20]:


#(b)
len(inventory) > ((len(fullname))*4)


# In[21]:


#(c)
c != 24


# In[ ]:


#(e)
len(middle) > len(first), len(middle) < len(last)


# # 2.18

# In[ ]:


#(a)
flowers=['rose','bougainvillea','yucca','marigold','daylilly','lilly of the valley']
#(b)
'potato' in flowers


# In[ ]:


#(c)
thorny=[flowers[0],flowers[1],flowers[2]]
#(d)
poisnous=[flowers[-1]]
#(e)
dangerous=thorny+poisnous


# # 2.19

# In[ ]:


answers=['Y','N','N','Y','N','Y','Y','Y','N','N','N']
#(a)
numYes=answers.count('Y')
#(b)
numNo=answers.count('N')
#(c)
percentYes=(numYes*100)/len(answers)
#(d)
answers.sort()
#(e)
f=answers.index('Y')


# # 2.21

# In[ ]:


s='Abdul'
t='Wassay'
s[0]+t[0]


# # 2.23

# In[23]:


monthsL=['Jan','Feb','Mar','May']
monthsT=('Jan','Feb','Mar','May')
#(a)
monthsL.insert(3,'Apr')
monthsT.insert(3,'Apr')

#error found because  tupple is immutable.


# In[24]:


#(b)
monthsL.append('Jun')
monthsT.append('Jun')

#error found because  tupple is immutable.


# In[25]:


#(c)
monthsL.pop()
monthsT.pop()

#error found because  tupple is immutable.


# In[26]:


#(d)
monthsL.remove(monthsL[2])
monthsT.remove(monthsT[2])

#error found because  tupple is immutable.


# In[27]:


#(e)
monthsL.reverse()
monthsT.reverse()

#error found because  tupple is immutable.


# In[28]:


#(f)
monthsL.sort()
monthsT.sort()

#error found because  tupple is immutable.


# # 2.24

# In[1]:


grades=['A','C','E','A','B','D','D','F','B','E','A','C','B','F']
counts=grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('E'),grades.count('F')


# # 2,25

# In[32]:


grades=('A','C','E','A','B','D','D','F','B','E','A','C','B','F')
counts=grades.count('A'),grades.count('B'),grades.count('C'),grades.count('D'),grades.count('E'),grades.count('F')


# In[ ]:





# In[ ]:




