import time
import sys
from url import urlinfo
from pdfanalysis import pdfinfo
from imagerecon import recon
from iplocator import iplocate
from TraceIP import read_multiple_ip
from webscrap import Links
from NameInfo import Nameinfo
from number import number
R = '\033[1;31;40m' 
G = '\033[1;32;40m'
C = '\033[1;36;40m'
Y = '\033[1;33;40m' 
def reconinput():
    inp=(input("Info>> "))
    if(inp == '4'):
        recon()
    elif (inp=='5'):
        iplocate()
    elif(inp=='6'):
        read_multiple_ip()
    elif(inp =='1'):
        urlinfo()
    elif (inp=='2'):
        pdfinfo()
    elif(inp=='3'):
        Links()
    elif (inp=='7'):
        Nameinfo()
    elif (inp=='8'):
        number()
    elif(inp=='exit'):
        exit()
    elif(inp=='tools'):
        print(G+"""Tools available 
    
            1.URL redirection checker
            2.PDF meta data analysis
            3.URL lookup in webpages

            usage : type exit to stop
            """)
    else:
        print(R+"Enter an valid option")
    while True:
        reconinput()    
        
if __name__=="__main__":
   reconinput()
     
    
