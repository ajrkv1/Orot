import json

FILENAME = "orot.json"

OUTFILE = "orot_ready.jsonl"

fp = open(FILENAME,"r")
jfile = json.load(fp)
fp.close
jout = list()

fp = open(OUTFILE,"w")
fp.write("")
fp.close()

fp = open(OUTFILE,"a")
for i in jfile["text"].values():
	for j in i.values():
		for par in j:
			
			while type(par) != type(str()):
				par = par[0]
			print(type(par))
			try:
				json.dump({'prompt':'',"completion":par},fp,ensure_ascii=False)
				fp.write("\n")
			except:
				print("THE PROBLEM IS:\n\n\n" + str(par))
			finally:
				pass

fp.close()
