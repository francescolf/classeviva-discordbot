print("Caricamento in corso...")
import discord
import os
import sys
import asyncio
import aiohttp
import requests
from opzioni import *
from os import path
from discord.ext import commands
import json
import re
import datetime
from itertools import islice

versione = "0.1.1"

print("Controllo aggiornamenti...")
ver = requests.get('http://francescolf.altervista.org/ver.json')
ver = ver.json()
ver = ver["versione"]

if str(ver) != versione:
	print("\nE' disponibile un aggiornamento! Desideri scaricarlo?")
	print("**ATTENZIONE** Perderai le impostazioni del bot!")
	a = input("Aggiornare? [si/no]: ")
	if a == "si":
		os.system("git reset --hard")
		os.system("git pull origin")
		os.system("sudo chmod +x start-linux.sh")
		print("\n\nRiavviare il bot\n\n")
		sys.exit()
	else:
		print("\nAggiornamento annullato\n")


client = discord.Client()
botcompiti = commands.Bot(description="ClasseViva Discord Bot", command_prefix=Prefisso)


@botcompiti.event
async def on_ready():
	login()

	url2 = "https://web.spaggiari.eu/rest/v1/students/" + stid + "/card"	

	headers = {"Content-Type": "application/json", "Z-Dev-ApiKey": "+zorro+", "User-Agent": "zorro/1.0", "Z-Auth-Token": sttk}
	ri = requests.get(url2, headers=headers) 
	infoscuola = ri.json()
	indscuola = infoscuola["card"]["schName"]
	nomescuola = infoscuola["card"]["schDedication"]
	cittscuola = infoscuola["card"]["schCity"]
	provscuola = infoscuola["card"]["schProv"]
	print("")
	print("Connesso come: {}".format(botcompiti.user.name))
	print("")
	indscuola = indscuola.title()
	nomescuola = nomescuola.title()
	cittscuola = cittscuola.title()
	print("Scuola: " + indscuola + " " + nomescuola + " (" + cittscuola + ", " + provscuola + ")")
	print("")
	print("Versione discord.py: " + discord.__version__)
	print("")
	print("")



@asyncio.coroutine
@botcompiti.command(pass_context=True)
async def oggi(ctx):
	login()

	url2 = "https://web.spaggiari.eu/rest/v1/students/" + stid + "/lessons/today"

	headers = {"Content-Type": "application/json", "Z-Dev-ApiKey": "+zorro+", "User-Agent": "zorro/1.0", "Z-Auth-Token": sttk}
	ri = requests.get(url2, headers=headers) 
	lezoggi = ri.json()



	with open('data/lezioni.txt', 'a') as filel:
		filel.truncate(0)
		filel.write(":clock1: **1 ORA**\n**Nessuna** - Nessuno\n\n\n:clock1: **2 ORA**\n**Nessuna** - Nessuno\n\n\n:clock1: **3 ORA**\n**Nessuna** - Nessuno\n\n\n:clock1: **4 ORA**\n**Nessuna** - Nessuno\n\n\n:clock1: **5 ORA**\n**Nessuna** - Nessuno\n\n\n")
		filel.write(":clock1: **6 ORA**\n**Nessuna** - Nessuno\n\n\n:clock1: **7 ORA**\n**Nessuna** - Nessuno\n\n\n:clock1: **8 ORA**\n**Nessuna** - Nessuno\n\n")
		filel.close()
		#os.system("pkill -f bot.py")
	noggetti = len(lezoggi['lessons'])
	coggetti = 0
	while coggetti < noggetti:
		if lezoggi["lessons"][coggetti]["lessonType"] != "Compresenza":
			ora_prof = lezoggi["lessons"][coggetti]["authorName"]
			ora_arg = lezoggi["lessons"][coggetti]["lessonArg"]
			ora_mat = lezoggi["lessons"][coggetti]["subjectDesc"]
			ora_ora = lezoggi["lessons"][coggetti]["evtHPos"]
			ora_prof = ora_prof.title()
			if ora_ora == 1:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[1] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[2] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			elif ora_ora == 2:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[5] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[6] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			elif ora_ora == 3:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[9] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[10] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			elif ora_ora == 4:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[13] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[14] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			elif ora_ora == 5:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[17] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[18] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			elif ora_ora == 6:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[21] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[22] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			elif ora_ora == 7:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[25] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[26] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			elif ora_ora == 8:
				with open('data/lezioni.txt', 'r+') as filel:
					ora_arg = ora_arg.replace('\n', ' ').replace('\r', '')
					file = filel.readlines()
					file[29] = "**" + ora_mat + "** - " + ora_prof + "\n"
					file[30] = ora_arg + "\n"
					filel.seek(0)
					filel.truncate()
					filel.writelines(file)
			coggetti = coggetti + 1
		else:
			coggetti = coggetti + 1

	gs = datetime.datetime.today().weekday()
	co = 0
	nr = 0
	with open("data/lezf.txt", "w") as filef:
		filef.truncate(0)

	if gs == 0:
		while co < oreLun:
			nr = nr + 4
			co = co + 1
		lezioni = []
		with open("data/lezioni.txt", "r") as filel:
   			ll = list(islice(filel, nr))

		with open("data/lezf.txt", "w") as filef:
  			for lez in ll:
        			filef.write(lez)
		with open("data/lezf.txt", "r") as filef:
			lezioni = filef.read()
	if gs == 1:
		while co < oreMar:
			nr = nr + 4
			co = co + 1
		lezioni = []
		with open("data/lezioni.txt", "r") as filel:
   			ll = list(islice(filel, nr))

		with open("data/lezf.txt", "w") as filef:
  			for lez in ll:
        			filef.write(lez)
		with open("data/lezf.txt", "r") as filef:
			lezioni = filef.read()
	if gs == 2:
		while co < oreMer:
			nr = nr + 4
			co = co + 1
		lezioni = []
		with open("data/lezioni.txt", "r") as filel:
   			ll = list(islice(filel, nr))

		with open("data/lezf.txt", "w") as filef:
  			for lez in ll:
        			filef.write(lez)
		with open("data/lezf.txt", "r") as filef:
			lezioni = filef.read()
	if gs == 3:
		while co < oreGio:
			nr = nr + 4
			co = co + 1
		lezioni = []
		with open("data/lezioni.txt", "r") as filel:
   			ll = list(islice(filel, nr))

		with open("data/lezf.txt", "w") as filef:
  			for lez in ll:
        			filef.write(lez)
		with open("data/lezf.txt", "r") as filef:
			lezioni = filef.read()
	if gs == 4:
		while co < oreVen:
			nr = nr + 4
			co = co + 1
		lezioni = []
		with open("data/lezioni.txt", "r") as filel:
   			ll = list(islice(filel, nr))

		with open("data/lezf.txt", "w") as filef:
  			for lez in ll:
        			filef.write(lez)
		with open("data/lezf.txt", "r") as filef:
			lezioni = filef.read()
	if gs == 5:
		while co < oreSab:
			nr = nr + 4
			co = co + 1
		lezioni = []
		with open("data/lezioni.txt", "r") as filel:
   			ll = list(islice(filel, nr))

		with open("data/lezf.txt", "w") as filef:
  			for lez in ll:
        			filef.write(lez)
		with open("data/lezf.txt", "r") as filef:
			lezioni = filef.read()

	if noggetti == 0:
		await botcompiti.send_message(ctx.message.channel, ":tada: Nessuna lezione oggi")
	else:			
		await botcompiti.send_message(ctx.message.channel, lezioni)


@asyncio.coroutine
@botcompiti.command(pass_context=True)
async def compiti(ctx):
	login()

	datainizio = datetime.datetime.today()
	datainiziosett = datetime.datetime.today().weekday()

	if sabato == "no":
		if datainiziosett == 4:
			datainizio = datainizio + datetime.timedelta(days=3)
			datafine = datainizio + datetime.timedelta(days=1)
			datainizio = datainizio.strftime('%Y%m%d')
			datafine = datafine.strftime('%Y%m%d')
		elif datainiziosett == 5:
			datainizio = datainizio + datetime.timedelta(days=2)
			datafine = datainizio + datetime.timedelta(days=1)
			datainizio = datainizio.strftime('%Y%m%d')
			datafine = datafine.strftime('%Y%m%d')
		else:
			datainizio = datainizio + datetime.timedelta(days=1)
			datafine = datainizio + datetime.timedelta(days=1)
			datainizio = datainizio.strftime('%Y%m%d')
			datafine = datafine.strftime('%Y%m%d')
	else:
		if datainiziosett == 5:
			datainizio = datainizio + datetime.timedelta(days=2)
			datafine = datainizio + datetime.timedelta(days=1)
			datainizio = datainizio.strftime('%Y%m%d')
			datafine = datafine.strftime('%Y%m%d')
		else:
			datainizio = datainizio + datetime.timedelta(days=1)
			datafine = datainizio + datetime.timedelta(days=1)
			datainizio = datainizio.strftime('%Y%m%d')
			datafine = datafine.strftime('%Y%m%d')
		

	url2 = "https://web.spaggiari.eu/rest/v1/students/" + stid + "/agenda/all/" + datainizio + "/" + datafine

	headers = {"Content-Type": "application/json", "Z-Dev-ApiKey": "+zorro+", "User-Agent": "zorro/1.0", "Z-Auth-Token": sttk}
	ri = requests.get(url2, headers=headers) 
	compiti = ri.json()

	noggetti = len(compiti['agenda'])
	coggetti = 0

	with open('data/compiti.txt', 'r+') as filec:
		filec.truncate(0)

	while coggetti < noggetti:
		try:
			if compiti["agenda"][coggetti]["evtCode"] == "AGHW":
				compito_prof = compiti["agenda"][coggetti]["authorName"]
				compito_desc = compiti["agenda"][coggetti]["notes"]
				compito_mat = compiti["agenda"][coggetti]["subjectDesc"]

				compito_prof = compito_prof.title()

				with open('data/compiti.txt', 'a') as filec:
					filec.write(':closed_book: **' + compito_mat + '** (' + compito_prof + ')\n' + compito_desc + '\n\n')
					coggetti = coggetti+1

			elif compiti["agenda"][coggetti]["evtCode"] == "AGNT":
				compito_prof = compiti["agenda"][coggetti]["authorName"]
				compito_desc = compiti["agenda"][coggetti]["notes"]

				compito_prof = compito_prof.title()

				with open('data/compiti.txt', 'a') as filec:
					filec.write(':page_facing_up: **Nota di ' + compito_prof + '**:' + '\n' + compito_desc + '\n\n')
					coggetti = coggetti+1
		except IndexError:
			break

	lf = os.path.getsize("data/compiti.txt")
	if lf > 3:
		with open('data/compiti.txt', 'r+') as filec:
			compitistr = filec.read()
			await botcompiti.send_message(ctx.message.channel, compitistr)
	else:
		await botcompiti.send_message(ctx.message.channel, ":tada: Nessun compito per domani")





@asyncio.coroutine
@botcompiti.command(pass_context=True)
async def verifiche(ctx):
	login()

	datainizio = datetime.datetime.today()
	if datetime.datetime.today().weekday() == 5 and sabato == "si" or datetime.datetime.today().weekday() == 4 and sabato == "no":
		datainizio = datetime.datetime.today()
		datainizio = datainizio + datetime.timedelta(days=1)

	oggi = datainizio
	datainizio = datainizio.strftime('%Y%m%d')
	if sabato == "si":
		dataven = oggi + datetime.timedelta( (5-oggi.weekday())%7+1 )
	else:
		dataven = oggi + datetime.timedelta( (4-oggi.weekday())%7+1 )
	datafine = dataven.strftime('%Y%m%d')

	url2 = "https://web.spaggiari.eu/rest/v1/students/" + stid + "/agenda/all/" + datainizio + "/" + datafine

	headers = {"Content-Type": "application/json", "Z-Dev-ApiKey": "+zorro+", "User-Agent": "zorro/1.0", "Z-Auth-Token": sttk}
	ri = requests.get(url2, headers=headers) 
	compiti = ri.json()


	noggetti = len(compiti['agenda'])
	coggetti = 0
	nver = 0

	with open('data/verifiche.txt', 'r+') as filev:
		filev.truncate(0)

	while coggetti < noggetti:
		try:
			if "Verifica" in compiti["agenda"][coggetti]["notes"] or "Compito in classe" in compiti["agenda"][coggetti]["notes"] or "Prova" in compiti["agenda"][coggetti]["notes"] or "verifica" in compiti["agenda"][coggetti]["notes"]:
				compito_prof = compiti["agenda"][coggetti]["authorName"]
				compito_desc = compiti["agenda"][coggetti]["notes"]
				compito_data = compiti["agenda"][coggetti]["evtDatetimeBegin"]
				compito_mat = compiti["agenda"][coggetti]["subjectDesc"]

				compito_data = str(compito_data[:10])
				compito_data = datetime.datetime.strptime(compito_data, '%Y-%m-%d')
				compito_sett = compito_data.weekday()

				if compito_sett == 0:
					compito_data = "Lunedi"
				if compito_sett == 1:
					compito_data = "Martedi"
				if compito_sett == 2:
					compito_data = "Mercoledi"
				if compito_sett == 3:
					compito_data = "Giovedi"
				if compito_sett == 4:
					compito_data = "Venerdi"
				if compito_sett == 5:
					compito_data = "Sabato"

				try:
					compito_mat = compito_mat.title()
				except AttributeError:
					compito_mat = compito_prof.title()


				with open('data/verifiche.txt', 'a') as filev:
					filev.write(':small_red_triangle_down: ' + compito_mat + ' - ' + compito_desc + ' (' + compito_data + ')' + '\n\n')
					coggetti = coggetti+1
					nver = nver + 1

			else:
				coggetti = coggetti+1

		except IndexError:
			await botcompiti.send_message(ctx.message.channel, "uhm... questo non doveva succedere.")


	if nver == 0:
		await botcompiti.send_message(ctx.message.channel, ":tada: Nessuna verifica questa settimana")

	elif nver == 1:
		with open('data/verifiche.txt', 'r+') as filev:
			compitistr = filev.read()
			await botcompiti.send_message(ctx.message.channel, ":information_source: Questa settimana hai " + str(nver) + " verifica:\n\n" + compitistr)

	else:
		with open('data/verifiche.txt', 'r+') as filev:
			compitistr = filev.read()
			await botcompiti.send_message(ctx.message.channel, ":information_source: Questa settimana hai " + str(nver) + " verifiche:\n\n" + compitistr)


def log(ora, utente, comando):
	print("[" + ora + "] " + utente + ": " + comando)

def login():
	urlbase = "https://web.spaggiari.eu/rest/v1"
	url = urlbase + "/auth/login/"
	headers = {"User-Agent": "zorro/1.0", "Z-Dev-Apikey": "+zorro+", "Content-Type": "application/json"}
	data = {"uid": username, "pass": password}
	r = requests.post(url, data=json.dumps(data), headers=headers) 
	rlogin = r.json()

	global sttk
	sttk = rlogin['token']
	global stid
	stid = re.sub(r"\D", "", rlogin['ident'])
	
	
try:
	botcompiti.run(TokenDiscord)
except discord.errors.LoginFailure as e:
	print("\n\nERRORE: Token Discord non valido (" + str(e) + ")\n\n")
	sys.exit()
