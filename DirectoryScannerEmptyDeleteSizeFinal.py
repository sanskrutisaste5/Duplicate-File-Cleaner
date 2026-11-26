#####################################################
#
# Importing required libraries
#
####################################################

import os
import sys 
import time    
import schedule

#####################################################

#Function name   : DirectoryScanner
#Input           : DirectoryPath 
#Description     : Delete all empty files periodically
#Data            : 19/07/2026
#Author          : Sanskruti Sameer Saste

####################################################

def DirectoryScanner(DirectoryPath):
    Border = "-"*40
    
    timestamp = time.ctime()
    LogFileName = "Marvellous%s.log"%(timestamp) 
    LogFileName = LogFileName.replace(" ","_")  
    LogFileName = LogFileName.replace(":","_")   

    Ret = False

    Ret = os.path.exists(DirectoryPath)  

    if(Ret == False):
        print("Marvellous Automation Error : There is no such directory with name",DirectoryPath)  
        return
    
    Ret = os.path.isdir(DirectoryPath)   

    if(Ret == False):
        print("Marvellous Automation Error : It is not a directory with name",DirectoryPath)
        return      

    print("Log file gets created with name:",LogFileName)
    
    fobj = open(LogFileName,"w") 
    fobj.write(Border+"\n")
    fobj.write("Marvellous Automation Script \n") 
    fobj.write(Border+"\n\n")

    fobj.write(" Files from the directory are :\n\n")
    fobj.write(Border+"\n")

    TotalFiles = 0
    EmptyFiles = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
        for fname in FileName:
            TotalFiles = TotalFiles + 1

            fname = os.path.join(FolderName,fname)
            fobj.write(f"{fname} :{os.path.getsize(fname)} \n") 

            if(os.path.getsize(fname) == 0):  
                EmptyFiles = EmptyFiles + 1  
                os.remove(fname)

    fobj.write(Border+"\n")
    fobj.write(f"Total files scanned : {TotalFiles}\n")
    fobj.write(f"Total Emptyfiles found and deleted : {EmptyFiles}\n")

    fobj.write(Border+"\n")

    fobj.write("Log file gets created at :"+timestamp)
    fobj.write("\n"+Border+"\n")

    fobj.close()

#####################################################

#Function name   : main
#Input           : command line arguments 
#Description     : It controls the script
#Data            : 19/07/2026
#Author          : Sanskruti Sameer Saste

####################################################

def main():
    Border = "-"*40      
    print(Border)
    print("Marvellous Automation Script")
    print(Border)

    if(len(sys.argv)==2):

        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("for better usuage please check --u flag")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")

        else:
          
          schedule.every(1).minute.do(DirectoryScanner,sys.argv[1])

          while True:
            schedule.run_pending()
            time.sleep(1)
            
    else:
        print("invalid parameter")
        print("please use --h or --u for more info")

    print(Border)
    print("Thankyou for using Marvellous Automation Script")
    print(Border)
    
#####################################################
#
# Starter of the automation script
#
####################################################

if __name__ =="__main__":
    main()

