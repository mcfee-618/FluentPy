#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import sys

print("Content-type:text/html\n\n")
print("<b>enviroment</b><br>")
for key in os.environ.keys():
    print(key+"   :    "+ os.getenv(key))
    print("<br>")
