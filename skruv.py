import math
stopp=0
while stopp==0:
	print("\n\nVälkommen till skruvlösaren v0.9\n\n")
	sokt=input("Vad söker du? (Fax, Måt, Mloss)  ")
	if sokt=="Fax":
		print("Löser för",sokt)
		Radieraknare=input("\n\nKänner du rm? (JA/NEJ)  ")
		if Radieraknare=='JA':
			params=input("\nAnge parametrar (\u03C6,d2,\u03B1,Måt,\u03BCg,\u03BCu,rm) separerade med mellanslag  ").split()
			rm=float(params[6])
		elif Radieraknare=='NEJ':
			params=input("\nAnge parametrar (\u03C6,d2,\u03B1,Måt,\u03BCg,\u03BCu,dw,dh) separerade med mellanslag  ").split()
			dw=float(params[6])
			dh=float(params[7])
			rm=(dw+dh)/4
		else:
			print("ERR")
			print(quit)	
		phi=float(params[0])
		phi=(phi/180)*3.14
		d2=float(params[1])
		alpha=float(params[2])
		alpha=(alpha/180)*3.14
		M=float(params[3])
		myg=float(params[4])
		myu=float(params[5])
		rho=math.atan(myg/math.cos(alpha))
		Fax=M/((d2/2)*math.tan(phi+rho)+(myu*rm))
		print("\nDen axialkraft som skruven utsätts för är: ", Fax, "N")

	elif sokt=="Måt":
		print("Löser för",sokt)
		Radieraknare=input("Känner du rm? (JA/NEJ)  ")
		if Radieraknare=='JA':
			params=input("\nAnge parametrar (\u03C6,d2,\u03B1,Fax,\u03BCg,\u03BCu,rm) separerade med mellanslag  ").split()
			rm=float(params[6])
		else:
			params=input("\nAnge parametrar (\u03C6,d2,\u03B1,Fax,\u03BCg,\u03BCu,dw,dh) separerade med mellanslag  ").split()
			dw=float(params[6])
			dh=float(params[7])
			rm=(dw+dh)/4
		phi=float(params[0])
		phi=(phi/180)*3.14
		d2=float(params[1])
		alpha=float(params[2])
		alpha=(alpha/180)*3.14
		Fax=float(params[3])
		myg=float(params[4])
		myu=float(params[5])
		rho=math.atan(myg/math.cos(alpha))
		M=Fax*((d2/2)*math.tan(phi+rho)+(myu*rm))
		print("\nDet åtdragningsmoment som krävs är: ",M,"Nm")

	elif sokt=="Mloss":
		print("Löser för",sokt)
		Radieraknare=input("Känner du rm? (JA/NEJ)  ")
		if Radieraknare=='JA':
			params=input("\nAnge parametrar (\u03C6,d2,\u03B1,Fax,\u03BCg,\u03BCu,rm) separerade med mellanslag  ").split()
			rm=float(params[6])
		else:
			params=input("\nAnge parametrar (\u03C6,d2,\u03B1,Fax,\u03BCg,\u03BCu,dw,dh) separerade med mellanslag  ").split()
			dw=float(params[6])
			dh=float(params[7])
			rm=(dw+dh)/4
		phi=float(params[0])
		phi=(phi/180)*3.14
		d2=float(params[1])
		alpha=float(params[2])
		alpha=(alpha/180)*3.14
		Fax=float(params[3])
		myg=float(params[4])
		myu=float(params[5])
		rho=math.atan(myg/math.cos(alpha))
		M=Fax*((d2/2)*math.tan(phi+rho)-(myu*rm))
		print("\nDet lossningsmoment som krävs är: ",M,"Nm")

	else:
		print("ERR")
		print(quit)

	stopp_svar=input("\nRäkna igen? (JA/NEJ)\n")
	if stopp_svar == "JA":
		print("KUL!\n\n")
	elif stopp_svar == "NEJ":
		print("\n\nTack för att du använde mig\n\n")
		print("""
			  ____       _  __    ____      _   _ __     __   
			 / __"| u   |"|/ / U |  _"\ uU |"|u| |\ \   /"/u  
			<\___ \/    | ' /   \| |_) |/ \| |\| | \ \ / //   
			 u___) |  U/| . \\u   |  _ <    | |_| | /\ V /_,-. 
			 |____/>>   |_|\_\   |_| \_\  <<\___/ U  \_/-(_/  
			  )(  (__),-,>> \\,-.//   \\_(__) )(    //        
			 (__)      \.)   (_/(__)  (__)   (__)  (__)       
			)""")
		stopp = 1

	else:
		print("\n\nERR")
		print(quit
)


# 2.47 14.701 30 300000 0.3 0.3 22 17