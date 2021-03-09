names = '''

'''
nameset = names.split("\n")
accs = []
accname = nameset[3].split(",https://www.instagram.com/")
oldaccname = accname[1].split(",")
oldaccname = oldaccname[0]

for i in range(len(nameset)):
  accname = nameset[i].split(",https://www.instagram.com/")
  acc = nameset[i].split("https://www.instagram.com/")

  try:
    accname = accname[1].split(",")
    acc = nameset[i].split("https://www.instagram.com/")
    acc = acc[1].split(",")
    accs.append(acc[0])

  except IndexError:
  	accname = accname

  if accname[0] != oldaccname:
  	#print(accs)
  	txxt = oldaccname + ".txt"
  	with open(txxt, 'w') as filehandle:
  		
  		for i in accs:
  			if i != "" or " ":
  				filehandle.writelines('%s\n' % i)

  	accs = []
  filehandle.close()
  oldaccname = accname[0]
