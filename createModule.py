#Simple python script to create directories and files for a new module in the brs-scanner angular2 project

import os, sys

currentDir = os.getcwd();

dir = input("Module Name: ")

os.chdir("client/modules")

os.mkdir( dir );

os.chdir(dir);

open(dir + ".component.ts", 'w');
open(dir + ".component.css", 'w');
open(dir + ".component.html", 'w');

open(dir + ".module.ts", 'w');
open(dir + ".routing.ts", 'w');

os.chdir("../../test");
os.mkdir( dir );

os.chdir(dir);
open(dir + "-component.spec.ts", 'w');



print ("Module has been created");