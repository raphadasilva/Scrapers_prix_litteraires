#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import urllib.parse
import re
from bs4 import BeautifulSoup
import csv

depart ="https://fr.wikipedia.org/wiki/Prix_"
prix = ["Goncourt", "Renaudot", "Femina", "Medicis"]
ficsv = open('laureats_prix_litteraires_france.csv','w+')

try:
	majcsv = csv.writer(ficsv)
	majcsv.writerow(('Concours','Sacre','Ouvrage', 'Editeur', 'Lauréat','Naissance','Age','Source'))
	for pri in prix:
		concours = pri
		url_prix = depart+pri 
		url = requests.get(url_prix) 
		print("Lien : "+url_prix)
		soupe = BeautifulSoup(url.text)
		tableau = soupe.find("table", {"class":"wikitable sortable"})
		lignes = tableau.findAll("tr") 
		for ligne in lignes:
			cellules = ligne.findAll("td")
			if cellules:
				sacre = cellules[0].get_text()
				if sacre:
					sacre = int(sacre)
				vainqueur = cellules[2].find("a")
				if vainqueur:
					auteur = vainqueur.get('title')
					bio = vainqueur.get('href')
					url_bio = urllib.parse.urljoin(depart, bio)
					destination = requests.get(url_bio)
					soupe_bio = BeautifulSoup(destination.text)
					print("Page de l'auteur(e) "+auteur)
					date = soupe_bio.find("time")
					if date:
						dnaissance = date.get('datetime')
						if dnaissance:
							naissance = int(dnaissance.split("-")[0])
					else:
						print("Pas de date de naissance pour "+auteur)
				else:
					auteur = cellules[2].get_text()
				if naissance and sacre:
					age = sacre - naissance
				else:
					age = 0
				ouvrage = cellules[3].get_text()
				editeurs = cellules[4].find("a")
				if editeurs:
					editeur = editeurs.get('title')
				else:
					editeur = ""
				print(concours, sacre, ouvrage, editeur, auteur, naissance, age, url_bio)
				majcsv.writerow((concours, sacre, ouvrage, editeur, auteur, naissance, age, url_bio))
finally:
	ficsv.close()