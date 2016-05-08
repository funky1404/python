# -*- coding:utf-8 -*-
# IP WHOIS SEARCH BY JINI(2014.7.23) yj1004. chang@samsung.com
# IPWhois module install Before
# python ./ipwhois.py > 파일명.txt

import socket
import os
from ipwhois import IPWhois
from pprint import pprint

data = open('ip-data.txt' )
data.seek(0)

for each1 in data:
    each2 = each1.replace( "\n","" )
    try:
        obj = IPWhois(each2)
        results = obj.lookup()  #obj.lookup_rdap(depth=0)
        print(each2,":::" ,results['nets'][ 0][ 'country'],":::" ,results['nets'][ 0][ 'city'],":::" ,results['nets'][ 0][ 'name'],":::" ,results['nets'][ 0][ 'tech_emails'])
    except:
        print(each2,"error" )

data.close()