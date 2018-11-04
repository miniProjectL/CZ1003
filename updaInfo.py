import matplotlib.animation as animation
import matplotlib.pyplot as plt
from PIL import Image
from pylab import *
import pyautogui,sys,math
import matplotlib.image as mpimg
import operator
from tkinter import *


canteenName=["Ananda Kitchen","North Hill Food Court","North Indian Cuisine","Canteen 9","Canteen 2","Canteen 1","NTU NorthSpine Plaza","Peach Garden","NIE Canteen","Food Court 16","Food Court 13","Canteen 14"]
categoryCanteen=["chicken rice","ban mian","duck rice","seafood"]

canteeninfo = [["Food Court 1​","chicken rice",3.5,3],
               ["Food Court 1​","ban mian",3,4],
               ["Food Court 1​","seafood",3.5,15],
               ["Food Court 1​","xiaolongbao",4,10],
               ["Food Court 2","chicken rice",3.6,3.2],
               ["Food Court 2​","ban mian",2.6,3],
               ["Food Court 2","seafood",4,17],
               ["Food Court 2","xiaolongbao",4.3,14],
               ["Food Court 14","chicken rice",4,3.8],
               ["Food Court 14","ban mian",3,4.1],
               ["Food Court 14","seafood",3.9,10],
               ["Food Court 14","xiaolongbao",3.8,12],
               ["North Hill Food Court","chicken rice",3.5,4],
               ["North Hill Food Court","ban mian",3,3.5]]
canteeninfo=list(canteeninfo)
# canteen,category,rank,price
#
# def addInfo():
# #------------Select Canteen------------------------
#     for count, item in enumerate(canteenName):
#         print(count, item)
#
#     selection0=int(input("Please select which canteen "))
#     canteen=canteenName[selection0]
#
# #------------Select category------------------------
#     for count, item in enumerate(categoryCanteen):
#         print(count, item)
#     selection1=int(input("Please select which category "))
#
#     for inList in canteeninfo:
#         if inList[0]==canteen:
#             a=int(canteeninfo.index(inList))
#             if categoryCanteen[selection1]==canteeninfo[a][1]:
#                 selection1=int(input("Please again"))
#             else:
#                 pass
#     category=categoryCanteen[selection1]
# #------------Select rank and price------------------------
#     rank=input("which rank ? ")
#     price=input("which price would you like to do? ")
#     addList=[canteen,category,rank,price]
#
#     addList=list(addList)
#     canteeninfo.append(addList)
#
# # addInfo()
# # print(canteeninfo)
#
# def editInfo():
#     for count, item in enumerate(canteenName):
#         print(count, item)
#     selection0=int(input("Please select which canteen "))
#     canteen=canteenName[selection0]
#
#     for count, item in enumerate(categoryCanteen):
#         print(count, item)
#     selection1=int(input("Please select which category "))
#     category=categoryCanteen[selection1]
#
#     for inList in canteeninfo:
#         if inList[0]==canteen:
#             a=int(canteeninfo.index(inList))
#             if canteeninfo[a][1]==category:
#                 rank=input("which rank ? ")
#                 price=input("which price would you like to do? ")
#                 canteeninfo[a][2]=rank
#                 canteeninfo[a][3]=price
#             break

# editInfo()
# print(canteeninfo)

def deleteInfo():
    for count, item in enumerate(canteenName):
        print(count, item)
    selection0=int(input("Please select which canteen "))
    canteen=canteenName[selection0]

    for count, item in enumerate(categoryCanteen):
        print(count, item)
    selection1=int(input("Please select which category "))
    category=categoryCanteen[selection1]

    for inList in canteeninfo:
        if inList[0]==canteen:
            a=int(canteeninfo.index(inList))
            if canteeninfo[a][1]==categoryCanteen[selection1]:
                canteeninfo.pop(a)
            else:
                selection1=int(input("No such category,Please select again "))

# print(canteeninfo)
# deleteInfo()
# print(canteeninfo)




