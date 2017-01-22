#!/usr/bin/python
# coding: utf8

import subprocess
import sys
import re # reguläre Ausdrücke

p=subprocess.Popen(["xrandr","--query"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
def Filter(Eingang):
    Ausdruck = re.search(r"[0-9]+x[0-9]+",Eingang) # Regulärer Ausdruck, um die Daten der Ausgabe von xrandr --query zu filtern
    Ausgang = Ausdruck.group()
    return Ausgang
Auswahl = []
while True:
    sys.stdout.flush()
    line = p.stdout.readline()
    if line != '':
    line_reg=line.rstrip()[0:3]
   # if re.search(r"[0-9]x[0-9]",line.rstrip()): # gefiltert als regulärer Ausdruck
   #if re.match(r"\s\s\s",line.rstrip()): # mit match schaut man, ob die ersten zeichen übereinstimmen --> \s bedeutet leerzeichen
   if line_reg == " ":
    Auswahl.append(Filter(line.rstrip()))
  else:
    break
Zaehler = 1
print "Menü:"
print "------------"
for x in Auswahl:
  print str(Zaehler) + ": "+x
  Zaehler += 1
print "------------"
Menuwahl = Auswahl[int(raw_input("Wähle eine Nummer: "))-1]
subprocess.Popen(["xrandr","-s",Menuwahl])
