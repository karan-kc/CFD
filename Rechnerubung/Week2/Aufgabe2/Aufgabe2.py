#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import shutil
import matplotlib.pyplot as mpl

#Duplicate Directory
shutil.copytree('/home/ensm_student/Documents/CFD/Rechnerubung/Week2/Aufgabe1/RANS', './RANS')

#Change Reynolds Number from 186 to 950
with open('RANS/config','r+') as fout:
    text = fout.read()
    text = re.sub(r'186','950',text)
    fout.seek(0)
    fout.write(text)
    fout.truncate()

import subprocess as sub
my_wd = "./RANS/"
filename = "./Allrun"
sub.Popen(filename, cwd=my_wd, shell=True).wait()


class simData(object):
    pass


def readRANSresults(foldername):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    rans_data = simData()
    rans_data.y_plus = []
    rans_data.U = []
    rans_data.k = []
    rans_data.uv = []

    # Geschwindigkeit einlesen
    with open(foldername + 'RANS/postProcessing/sample/815/wallNormal_U.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            # Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variablen abspeichern (1. und 2. Spalte)
            rans_data.y_plus.append(float(split_line[0]))
            rans_data.U.append(float(split_line[1]))
    # TKE einlesen
    with open(foldername + 'RANS/postProcessing/sample/815/wallNormal_k.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            # Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (2. Spalte)
            rans_data.k.append(float(split_line[1]))
    # Reynolds-Spannungen einlesen
    with open(foldername + 'RANS/postProcessing/sample/815/wallNormal_R.xy') as fin:
        # Zeilen einlesen
        data_lines = fin.readlines()

        # Zeile für Zeile verarbeiten
        for line in data_lines:
            # Splitten:
            split_line = line.split('\t')
            # die benötigten Daten in die Variable abspeichern (3. Spalte)
            rans_data.uv.append(float(split_line[2]))
    # Datenobjekt zurückgeben
    return rans_data


def readDNSresults(foldername):
    """
    This function reads the output file of a simulation
    """
    # Datenobjekt definieren
    dns_data = simData()
    dns_data.y_plus = []
    dns_data.U = []
    dns_data.k = []
    dns_data.uv = []

    # Geschwindigkeit einlesen
    with open(foldername + 'Re950.prof') as fin:
        # Read lines
        data_lines = fin.readlines()

        # Process line by line
        for line in data_lines:
            # If statement to only perform loop on lines not starting with '%'
            if line.startswith('%') == False:
                # Split:
                split_line = line.split()
                # Save the required data in the variables
                dns_data.y_plus.append(float(split_line[1]))
                dns_data.U.append(float(split_line[2]))
                dns_data.k.append(
                    (float(split_line[3]) ** 2 + (float(split_line[4])) ** 2 + (float(split_line[5])) ** 2) / 3)
                dns_data.uv.append(float(split_line[10]))
    # Datenobjekt zurückgeben
    return dns_data


def plotData(rans_data, dns_data, foldertosave):
    """
    This function plots the data given data object
    """
    # Geschwindigkeit plotten
    mpl.figure(1)
    mpl.plot(rans_data.y_plus, rans_data.U, 'r-', label='RANS')
    mpl.plot(dns_data.y_plus, dns_data.U, 'r--', label='DNS')
    # Achsenbeschriftung
    mpl.xlabel('$y^+$')
    mpl.ylabel(
        r'$\bar{U}^+$')  # 'r' vor dem Text inkludiert backslash, sonst wird die Zeile falsch interpretiert, siehe https://docs.python.org/2/reference/lexical_analysis.html#string-literals
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.savefig(foldertosave + '/U.png', format="png")

    # TKE und uv
    mpl.figure(2)
    mpl.plot(rans_data.y_plus, rans_data.k, 'r-', label='RANS $k^+$')
    mpl.plot(rans_data.y_plus, rans_data.uv, 'b-', label=r'RANS $\overline{u^\prime v^\prime}^+$')
    mpl.plot(dns_data.y_plus, dns_data.k, 'r--', label='DNS $k^+$')
    mpl.plot(dns_data.y_plus, dns_data.uv, 'b--', label=r'DNS $\overline{u^\prime v^\prime}^+$')
    # Achsenbeschriftung
    mpl.xlabel('$y^+$')
    mpl.ylabel('$k^+$, $\overline{u^\prime v^\prime}^+$')
    # Legende aktivieren
    mpl.legend()
    # Abspeichern als PNG
    mpl.savefig(foldertosave + '/k_uv.png', format="png")


def main():
    """
    this is the function used to call all functions necessary for the task
    """

    # Ordner mit den Datensätzen
    data_path = './'

    # Datensatz einlesen
    rans = readRANSresults(data_path)
    dns = readDNSresults(data_path)
    # Datensatz plotten und abspeichern
    plotData(rans, dns, './')


###############################################################################
### Führt die main-Funktion aus nachdem Einlesen aller Funktionen und Definitionen
###############################################################################
if __name__ == "__main__":
    main()