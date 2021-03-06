#!/usr/bin/env python3
# coding: utf8

import subprocess
import sys
import re # reguläre Ausdrücke

def Filter(Eingang):
	Ausgang = re.findall(r"[0-9]+x[0-9]+",Eingang) # Regulärer Ausdruck, um die Daten der Ausgabe von xrandr --query zu filtern
	return Ausgang

p=subprocess.Popen(["xrandr","--query"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
Auswahl = Filter(str(p.stdout.read()))
Zaehler = 1
print("Menü:")
print("------------")
Zaehler = 1
for key in Auswahl[1:len(Auswahl)]: # Erster Eintrag ist doppelt, deswegen ohne Index 0
	print(str(Zaehler) + ": "+str(key))
	Zaehler += 1
print("------------")
auswahl = Auswahl[int(input("Wähle eine Nummer: "))-1]
subprocess.Popen(["xrandr","-s",auswahl])
