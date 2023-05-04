"""
Libraries used are: 

"""
from ast import Pass
from logging import exception
from tkinter.font import BOLD
from tkinter.tix import Tree
from turtle import end_fill
from typing import final
import pandas as pd
import colorama
from colorama import init
from colorama import Fore, Back, Style
import termcolor
from termcolor import cprint,colored
import pip
import matplotlib
from matplotlib import pyplot as plt

"""
=========================> Coloring Functions <====================

"""

# def Red():
#     return Fore.RED + Style.BRIGHT

# def Blue():
#     return Fore.BLUE + Style.BRIGHT

# def Green():
#     return Fore.GREEN + Style.BRIGHT

# def Yellow():
#     return Fore.YELLOW + Style.BRIGHT

# def Cyan():
#     return Fore.CYAN + Style.BRIGHT


# def resetColor():
#     return Fore.RESET + Style.RESET_ALL



# ----------------------------> End <--------------------------------- 



"""
--------------------> Data Class <--------------------

"""
class Data():


    def __init__(self, path='', xlsxData='',csvData='',summary='',dataframe=''):
        self.path = path
        self.xlsxData = xlsxData
        self.csvData = csvData
        self.summary = summary
        self.dataframe = dataframe



    class Visualization():

        def __init__(self, xaxis, yaxis, plottype):
            self.xaxis = xaxis
            self.yaxix = yaxis
            self.plottype = plottype


        def VisualMenu():

            print("""\n\n
            ..................................................

                {}\t1. Bar Plot
                \t2. Scatter Plot
                \t3. Box Plot
                \t4. Histogram
                \t5. Pie Chart
                \t6. Line Chart
                {}\t7. Exit{}
            
            ..................................................
            \n\n""".format(Fore.CYAN, Fore.RED, Fore.RESET))


        def VisualChoice():
            while True:

                Data.Visualization.VisualMenu()

                plottype = str(input("Please Enter Plot Type : " ))


                if plottype == '1':
                    print("\n\tPlotting Bar Plot.")
                    Data.Visualization.barplot()

                elif plottype == '2':
                    print("\n\tPlotting Scatter Plot.")
                    Data.Visualization.scatterplot()

                elif plottype == '3':
                    print("\n\tPlotting Box Plot.")
                    Data.Visualization.boxplot()

                elif plottype == '4':
                    print("\n\tPlotting Histogram Chart.")
                    Data.Visualization.histogram()

                elif plottype == '5':
                    print("\n\tPlotting Pie Chart")
                    Data.Visualization.piechart()

                elif plottype == '6':
                    print("\n\tPlotting Line Chart")
                    Data.Visualization.linechart()

                elif plottype == '7' or 'exit' or 'EXIT' or 'Exit':
                    print("\n\tExiting Visualization...")
                    break

                else :
                    print("\n\tPlease Enter Correct Choice...")



        

        def barplot():
            xaxis = str(input("First Axis Name  : "))
            yaxis = str(input("Second Axis Name : "))

            plt.bar(dataframe[xaxis], dataframe[yaxis])
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)
            plt.show()
            


        def scatterplot():

            try:

                def TwoPoints():
                    xaxis = str(input("Enter xaxis Name : "))
                    yaxis = str(input("Enter yaxis Name : "))
                    a = dataframe[xaxis]
                    plt.scatter(a, dataframe[xaxis],color='blue')
                    plt.scatter(a, dataframe[yaxis],color='red')
                    plt.ylabel(yaxis)
                    plt.xlabel(xaxis)
                    plt.show()

                TwoPoints()

            except Exception as e:
                print(e)



        def boxplot():
            try:
                xaxis = str( input("Enter xaxis Name : "))

                plt.boxplot(dataframe[xaxis])
                plt.show()

            except Exception as e:
                print(e)

        def histogram():
            try:
                axis = str(input("Enter Axis Name : "))

                plt.hist(dataframe[axis])
                plt.show()


            except Exception as e:
                print(e)

        def piechart():
            try:
                axis = str(input("Enter Axis Name : "))
                
                plt.pie(dataframe[axis])
                plt.show()

            except Exception as e :
                print(e)


        def linechart():
            try:
                xaxis = str(input("Enter xaxis name : "))
                yaxis = str(input("Enter yaxis Name : "))

                plt.plot(dataframe[xaxis], 'g')
                plt.plot(dataframe[yaxis], 'r')
                plt.xlabel(xaxis)
                plt.ylabel(yaxis)
                plt.show()

            except Exception as e:
                print(e)



    def Get_Path(self):
        print(end="\n\n")
        path = input("Please Enter your data path :  ")
        print("\n")

        Splitter = path.split(".")


        # """
        # =====================> Choice Menu Fuction Starts From Here <=====================
        # """
        def choiceMenu():


            while True:
                DataProcessing.ProcessingMenu()
                print(end="\n\n")
                choice = input("\nPlease Enter Your Choice : ")

                if choice == '1':
                    print(end="\n\n\n")
                    head()


                elif choice == '2':
                    print(end="\n\n\n")
                    tail()

                elif choice == '3':
                    print(end="\n\n\n")
                    nullValues()

                elif choice == '4':
                    print(end="\n\n\n")
                    describe()


                elif choice == '5':
                    print(end="\n\n\n")
                    Data.Visualization.VisualChoice()

                elif choice == '6' or 'Exit' or 'EXIT' or 'exit':
                    print(end="\n\n\n")
                    print("choice is 6. Breaking the loop.")
                    break

                else:
                    print("Please enter correct choice....")

        # """
        # ******************************************************************************************************************************
        # """




        # """
        # =====================> Processing Fuction Starts From Here <=====================
        # """

        def head():
            print("\n\tPrinting First 5 Rows",end="\n\n")
            print(dataframe.head())

        
        def tail():
            print("\n\tPrinting Last 5 Rows",end="\n\n")
            print(dataframe.tail())



        def nullValues():

            try: 
                print("\n\tPrinting Null Values Data")

                isnull = dataframe.isnull()
                print("\n\n" , isnull , end="\n")


                print("\n\nTotal Null Values: ",end="\n")
                isnullSum = isnull.sum()
                print("\n")
                print(isnullSum)

            except Exception as e:
                print(e)



        def describe():
            desc = dataframe.describe()
            print(desc)


            print("\n\nColumns Present are : \n\n")
            cprint(dataframe.columns,'yellow',attrs=['bold'])
            print(end="\n\n")


        # """
        # ******************************************************************************************************************************
        # """

        try:
            if 'xlsx' in Splitter:
                global dataframe
                dataframe = pd.read_excel(path)   
                choiceMenu()


            elif 'csv' in Splitter:
                dataframe = pd.read_csv(path)              
                choiceMenu()

            else:
                cprint("\n\n\tPlease Enter Correct File. \n\tOr Check extensions.")
                cprint("\n\tUse only ", end="")
                cprint(".CSV", 'red', attrs=[BOLD],end='')
                cprint(" and ", end='')
                cprint(".XLSX", 'red', attrs=[BOLD],)
                print(end="\n\n")
        
        except Exception as e:

            print("\n\tFile " + Fore.RED + Style.BRIGHT + "\"{}\"".format(path) + Fore.RESET + Style.RESET_ALL + " is not present.")
            print(end="\n\n")
        



#--------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------



class DataProcessing(Data):

    
    
    #--------------------------------------------------------------------------------------------------------------
    def ProcessingMenu():
        print(Style.BRIGHT + """\n\n
        =============================================={}

            1. Show First Lines (head)
            2. Show Last Lines (tail)
            3. Show Null Values 
            4. Show Information
            5. Graps and Visualization{}
            6. Exit{}

        ==============================================
        """.format(Fore.GREEN,Fore.RED,Fore.RESET))


    #-------------------------------------------------------------------------------------------------------------- 

    def xlsxDataFrame():
        pass

        
        
def installPkgs():
    try:
        packageName = ['install', 'pandas', 'numpy', 'termcolor', 'colorama']

        if hasattr(pip,'main'):
            pip.main(packageName)
        else:
            pip._internal.main(packageName)

    except Exception as e:
        print(e)
        


#--------------------------------------------------------------------------------------------------------------





"""  Main Function """

if __name__ == '__main__':
    installPkgs()
    obj = Data()
    obj.Get_Path()
