# -*- coding: utf-8 -*-

import os
from random import randrange, random
from math import floor

def noFailIntInput(str):
	try:
		value = int(input(str))
		return value
	except: #on bloque toutes les exceptions. ajouter ValueError pour les ValueErrors seulement
		return None

class Casino():
	"""La classe du casino"""
	"""Elle vous guide dans les jeux et gère l'argent"""
	def __init__(self, argent):
		self.argent = argent
		self.activities = ["Roulette", "Découvrir"]
		print("Bienvenue au Casino !")
		print("Vous disposez actuellement de {} euro".format(self.argent) + ('s' if self.argent > 1 else ''), end="")
		input()
		
	def __foutreLeClientDehors(self, reason):
		print(reason)
		print("*Les employés vous jettent à la rue sans beaucoup de délicatesse.*")
		exit(0)
		
	def jouer(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		if self.argent == 0: self.__foutreLeClientDehors("T'es ruiné !")
		print("Choisissez une activité parmi les suivantes : ")
		for i, act in enumerate(self.activities):
			print("{}. {}".format(i+1, act))
		choix = noFailIntInput("Alors ? ")
		if choix == 1:
			self.jouerALaRoulette()
		else:
			self.jouer()
	
	def jouerALaRoulette(self):
		laRoulette = Roulette()
		while self.argent > 0:
			laRoulette.miser(self.argent)
			laRoulette.parier()
			self.argent += laRoulette.lancerLaBille()
			print("Il vous reste {} euro".format(self.argent) + ('s' if self.argent > 1 else ''))
			if input()=="Q": break
		self.jouer()
		

class Roulette():
	def __init__(self):
		print("Bienvenue sur cette table de jeu ! Jouons à la roulette")
	
	def miser(self, maximum):
		mise = noFailIntInput("Entrez une mise : ")
		if mise in range(1, maximum+1):
			self.mise = mise
		else:
			print("Entrée incorrecte. Veuillez réessayer")
			self.miser(maximum)
			
	def parier(self):
			num = noFailIntInput("Entrez un numéro : ")
			if num in range(0, 37):
				self.numero = num
			else:
				print("Entrée incorrecte. Veuillez réessayer")
				self.parier()
	
	def lancerLaBille(self):
		print("Rien ne va plus, les jeux sont faits !\nC'est parti !\nCa tourne...")
		resultat = randrange(0, 37) #floor(random() * 36)
		print("Et c'est le {} qui sort !".format(resultat))
		if resultat == self.numero:
			print("Bravo !!! Vous récupérez 36 fois votre mise !")
			return 35*self.mise
		else:
			if resultat%2 == self.numero%2:
				print("Vous avez au moins la bonne couleur (le {}) !".format(("noir" if self.numero%2 else "rouge")))
				print("Vous récupérez donc 2 fois votre mise.")
				return self.mise
			else:
				print("Pas de chance, vous n'avez même pas la bonne couleur !\nVous perdez donc votre mise.")
				return -self.mise
		
leCasino = Casino(1000)
leCasino.jouer()