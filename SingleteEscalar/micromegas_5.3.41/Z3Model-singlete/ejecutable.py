import subprocess 

print("Ejecutando modeloz3")
subprocess.getoutput("python modeloz3.py")
print("Ejecutando csection")
subprocess.getoutput("python csection.py")
for i in range(0,100,1): 
	print("El computador se apagara en: " + str(100-i))

subprocess.getoutput("shutdown -h")
