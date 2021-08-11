import ipaddress
interno1=ipaddress.ip_network('10.0.0.0/16')
interno2=ipaddress.ip_network('10.50.0.0/16')
rangeVpn=ipaddress.ip_network('192.168.0.0/16')
ipList=['241.223.148.36','26.66.77.16','60.142.8.92']



def verificaRange(ip):
    ip=ipaddress.ip_address(ip)
    if (ip in interno1) :
        return True
    if(ip in interno2):
        return True
    if(ip in rangeVpn):
        return True
    if(ip in ipList):
        return True
    return False

arquivoLog = input ("Qual o nome do arquivo de log?: ")
arquivo=open(arquivoLog,'r')
linhas=arquivo.readlines()
porta22=open("porta22.txt","a")
portaHttp=open("portaHttp.txt","a")
semIp=open("semIp.txt","a")
i=0
for linha in linhas:
    if i==0:
        i=1
        continue
    separado=linha.split()
    srcaddr = separado[0]
    dstaddr = separado[1]
    port = separado[2]
    action = separado[3]

    if(verificaRange(srcaddr) == False and verificaRange(dstaddr) == False):
        semIp.write(linha + "\n")
        continue
    if(port=='22'):
        porta22.write(linha + "\n" )
    if(port=='443' or port=='80'):
        portaHttp.write(linha + "\n")










