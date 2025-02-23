#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
***************************************************************************************************************************************************
*   Nom: QRCodeGen.py
*   Date: 17-11-24
*   Version: 1.1
*   Changelog: V1.0@16-10-18: Version minimale, pour créer un QRCode pour un manuel
*              V1.1@17-11-24: Mise à jour, refonte globale, besoin d'un QRCode pour mon CV.
*   Auteur: BYGBee
*   Objectif: Générer un QRCode minimal et le sauvegarder.
"""

#LIBRAIRIES
import pyqrcode

#CONSTANTS
	#NONE

def main():
	print("Debut de la generation d'un QRCode maison")
	
	payload="https://github.com/BYGBee"
	
	print("Payload OK, début de la création du code")
	
	try:
		#QR = pyqrcode.create(payload, error='H')#No need for high error coding in this case
		QR = pyqrcode.create(payload, error='L')
		print("QR est créée")
	
		print("Trying to save image")
		QR.png('bygbee.png', scale=5, module_color=[0x00, 0x00, 0x00, 0xff], background=[0xff, 0xff, 0xff, 0xff], quiet_zone=5)
	
	except Exception as e:
		print (e)
	print("That's all folks!")
	print("Hit any key to quit...")
	input()
	
	
	
#LAUNCHER
if __name__ == "__main__":
	main()
	
