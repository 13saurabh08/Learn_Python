# -*- coding: utf-8 -*-
"""Python Excersice .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FUm_Fcun1DO6RUWe5RcbApjSh58YIu9q

We are learning different datatypes in Python
"""

#comments -- comments are not part of the executable code, they are added only to increase the readability

"""Ways in which we can execute the code cell

1. shift+enter

2. ctrl+enter

3. play button
"""

a=155

print(a)

type(a)

b=-8.9

print(b)

type(b)

c=4-2j

print(c)

type(c)

d="Indian Ocean"

print(d)

type(d)

name="Aashutosh"

print(name)

type(name)

num="-4.895"

print(num)

type(num)

my_list=['Apple','Russia','Mango','India',45,52,-4.5,-3.8]

print(my_list)

type(my_list)

new_list=[12,9,4,5,2,8,7]

print(new_list)

type(new_list)

akash_list=['Mango',22,-2.9]

print(akash_list)

type(akash_list)

num=[1233,"Pratik"]

print(num)

type(num)

t=('Apple','Russia','Mango','India',45,52,-4.5,-3.0)

print(t)

type(t)

"""Operations in Lists and Strings

1. Concatination

2. Indexing

3. Slicing
"""

#Concatination in Strings
a='My'
b='Desktop'

print(a+b)

print(a+' '+b)

first_name='Aashutosh'
middle_name='Kumar'
last_name='Mishra'

print("Your full name is",first_name+' '+middle_name+' '+last_name)

#concatination in Lists
l1=[1,2,3,4,5]
l2=['Mango','Apple']

print(l1+l2)

print(l2+l1)

#Indexing in strings

word='Indian Ocean'

word[9]

word[-1]

word[2]

word[-5]

#Indexing in Lists

l_new=['AI','Data Science','Mango','PineApple','Python','PySpark',5,7,9,10]

#fetching 'a' from 'mango' ?
Aditya=l_new[2]

print(Aditya)

Aditya[1]

l_new[2]

l_new[-8]

l_new[5]

l_new[-5]

l_new[8]

l_new[-2]

l_new[-7]

l_new[3]

#concatination and indexing
f_name='Pratikshya'
m_name='Vishwas'
print(f_name+" "+m_name)

name=f_name+" "+m_name

name[11]

name[-7]

#Slicing in Strings
a='United Nations'

a[0:6]

a[7:]

a[-7:]

a[3:13]

a[-11:-1]

#Slicing in Lists
my_list=[1,2,3,'Russia','USA','Alaska','Israel',5,8,-4.9]

my_list[4:7]

my_list[-6:]
