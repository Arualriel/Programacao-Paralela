import matplotlib.pyplot as plt
import numpy as np

labels = [1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
labelsn = [8,9,10,11,12,13,14,15,16,17]
cor=["blue","red","green","orange","purple","magenta","yellow","cyan","brown","gray","black","pink","wine","navy"]

#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)
#### reultados com a gpu
for k in range(2):
    values6 = np.loadtxt("results-gpu/results"+str(k)+"/8.txt")
    values7 = np.loadtxt("results-gpu/results"+str(k)+"/9.txt")
    values8 = np.loadtxt("results-gpu/results"+str(k)+"/10.txt")
    values9 = np.loadtxt("results-gpu/results"+str(k)+"/11.txt")
    values10 = np.loadtxt("results-gpu/results"+str(k)+"/12.txt")        
    values11 = np.loadtxt("results-gpu/results"+str(k)+"/13.txt")
    values12 = np.loadtxt("results-gpu/results"+str(k)+"/14.txt")
    values13 = np.loadtxt("results-gpu/results"+str(k)+"/15.txt")
    values14 = np.loadtxt("results-gpu/results"+str(k)+"/16.txt")
    values15 = np.loadtxt("results-gpu/results"+str(k)+"/17.txt")
    
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
    
    values6o = np.loadtxt("results-ori/results"+str(k)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k)+"/17.txt")
    vec1 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]

    if (k==0):
        plt.plot(vec1,label="GPU sem SM",color=cor[k+2],ls=':')
    else:
        plt.plot(vec1,label="GPU com SM",color=cor[k+2],ls=':')


#### resultados com o cod otimizado

for k in range(1,7):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
    values6 = np.loadtxt("results-oti/results4/8-"+str(k)+".txt")
    values7 = np.loadtxt("results-oti/results4/9-"+str(k)+".txt")
    values8 = np.loadtxt("results-oti/results4/10-"+str(k)+".txt")
    values9 = np.loadtxt("results-oti/results4/11-"+str(k)+".txt")
    values10 = np.loadtxt("results-oti/results4/12-"+str(k)+".txt")        
    values11 = np.loadtxt("results-oti/results4/13-"+str(k)+".txt")
    values12 = np.loadtxt("results-oti/results4/14-"+str(k)+".txt")
    values13 = np.loadtxt("results-oti/results4/15-"+str(k)+".txt")
    values14 = np.loadtxt("results-oti/results4/16-"+str(k)+".txt")
    values15 = np.loadtxt("results-oti/results4/17-"+str(k)+".txt")
 
 
    values6o = np.loadtxt("results-ori/results"+str(k%2)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k%2)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k%2)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k%2)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k%2)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k%2)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k%2)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k%2)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k%2)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k%2)+"/17.txt")
    vec2 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]
    plt.plot(vec2,label="Otimizado t="+str(k),color=cor[k-1])


plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
plt.xlabel('N (x10^4)')
plt.ylabel('Speedup')
plt.title('Speedup')
plt.legend()
plt.savefig('speedup1.png', format='png')
plt.show()
 

#### reultados com a gpu
for k in range(2):
    values6 = np.loadtxt("results-gpu/results"+str(k)+"/8.txt")
    values7 = np.loadtxt("results-gpu/results"+str(k)+"/9.txt")
    values8 = np.loadtxt("results-gpu/results"+str(k)+"/10.txt")
    values9 = np.loadtxt("results-gpu/results"+str(k)+"/11.txt")
    values10 = np.loadtxt("results-gpu/results"+str(k)+"/12.txt")        
    values11 = np.loadtxt("results-gpu/results"+str(k)+"/13.txt")
    values12 = np.loadtxt("results-gpu/results"+str(k)+"/14.txt")
    values13 = np.loadtxt("results-gpu/results"+str(k)+"/15.txt")
    values14 = np.loadtxt("results-gpu/results"+str(k)+"/16.txt")
    values15 = np.loadtxt("results-gpu/results"+str(k)+"/17.txt")
    
    
    values6o = np.loadtxt("results-ori/results"+str(k)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k)+"/17.txt")
    vec3 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]
    if (k==0):
        plt.plot(vec3,label="GPU sem SM",color=cor[k],ls='--')
    else:
        plt.plot(vec3,label="GPU com SM",color=cor[k],ls='--')
 
#### resultados com o cod original

for k in range(2):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
    values6 = np.loadtxt("results-ori/results"+str(k)+"/8.txt")
    values7 = np.loadtxt("results-ori/results"+str(k)+"/9.txt")
    values8 = np.loadtxt("results-ori/results"+str(k)+"/10.txt")
    values9 = np.loadtxt("results-ori/results"+str(k)+"/11.txt")
    values10 = np.loadtxt("results-ori/results"+str(k)+"/12.txt")        
    values11 = np.loadtxt("results-ori/results"+str(k)+"/13.txt")
    values12 = np.loadtxt("results-ori/results"+str(k)+"/14.txt")
    values13 = np.loadtxt("results-ori/results"+str(k)+"/15.txt")
    values14 = np.loadtxt("results-ori/results"+str(k)+"/16.txt")
    values15 = np.loadtxt("results-ori/results"+str(k)+"/17.txt")
    
    values6o = np.loadtxt("results-ori/results"+str(k)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k)+"/17.txt")
    vec4 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]

    if (k==0):
        plt.plot(vec4,label="Original sem SM",color=cor[k+2],ls=':')
    else:
        plt.plot(vec4,label="Original com SM",color=cor[k+2],ls=':') 
 
#### resultado com o codigo otimizado    
for k in range(6,13):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
    values6 = np.loadtxt("results-oti/results4/8-"+str(k)+".txt")
    values7 = np.loadtxt("results-oti/results4/9-"+str(k)+".txt")
    values8 = np.loadtxt("results-oti/results4/10-"+str(k)+".txt")
    values9 = np.loadtxt("results-oti/results4/11-"+str(k)+".txt")
    values10 = np.loadtxt("results-oti/results4/12-"+str(k)+".txt")        
    values11 = np.loadtxt("results-oti/results4/13-"+str(k)+".txt")
    values12 = np.loadtxt("results-oti/results4/14-"+str(k)+".txt")
    values13 = np.loadtxt("results-oti/results4/15-"+str(k)+".txt")
    values14 = np.loadtxt("results-oti/results4/16-"+str(k)+".txt")
    values15 = np.loadtxt("results-oti/results4/17-"+str(k)+".txt")
    
    values6o = np.loadtxt("results-ori/results"+str(k%2)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k%2)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k%2)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k%2)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k%2)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k%2)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k%2)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k%2)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k%2)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k%2)+"/17.txt")
    vec5 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]

    plt.plot(vec5,label="Otimizado t="+str(k),color=cor[k-6])

#########k=24###########
k=24
values6 = np.loadtxt("results-oti/results4/8-"+str(k)+".txt")
values7 = np.loadtxt("results-oti/results4/9-"+str(k)+".txt")
values8 = np.loadtxt("results-oti/results4/10-"+str(k)+".txt")
values9 = np.loadtxt("results-oti/results4/11-"+str(k)+".txt")
values10 = np.loadtxt("results-oti/results4/12-"+str(k)+".txt")        
values11 = np.loadtxt("results-oti/results4/13-"+str(k)+".txt")
values12 = np.loadtxt("results-oti/results4/14-"+str(k)+".txt")
values13 = np.loadtxt("results-oti/results4/15-"+str(k)+".txt")
values14 = np.loadtxt("results-oti/results4/16-"+str(k)+".txt")
values15 = np.loadtxt("results-oti/results4/17-"+str(k)+".txt")

values6o = np.loadtxt("results-ori/results"+str(k%2)+"/8.txt")
values7o = np.loadtxt("results-ori/results"+str(k%2)+"/9.txt")
values8o = np.loadtxt("results-ori/results"+str(k%2)+"/10.txt")
values9o = np.loadtxt("results-ori/results"+str(k%2)+"/11.txt")
values10o = np.loadtxt("results-ori/results"+str(k%2)+"/12.txt")        
values11o = np.loadtxt("results-ori/results"+str(k%2)+"/13.txt")
values12o = np.loadtxt("results-ori/results"+str(k%2)+"/14.txt")
values13o = np.loadtxt("results-ori/results"+str(k%2)+"/15.txt")
values14o = np.loadtxt("results-ori/results"+str(k%2)+"/16.txt")
values15o = np.loadtxt("results-ori/results"+str(k%2)+"/17.txt")
vec6 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]

plt.plot(vec6,label="Otimizado t="+str(k),color=cor[13])
k=0
########################
plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
plt.xlabel('N (x10^4)')
plt.ylabel('Speedup')
plt.title('Speedup')
plt.legend()
plt.savefig('speedup2.png', format='png')
plt.show()


#### reultados com a gpu
for k in range(2):
    values6 = np.loadtxt("results-gpu/results"+str(k)+"/8.txt")
    values7 = np.loadtxt("results-gpu/results"+str(k)+"/9.txt")
    values8 = np.loadtxt("results-gpu/results"+str(k)+"/10.txt")
    values9 = np.loadtxt("results-gpu/results"+str(k)+"/11.txt")
    values10 = np.loadtxt("results-gpu/results"+str(k)+"/12.txt")        
    values11 = np.loadtxt("results-gpu/results"+str(k)+"/13.txt")
    values12 = np.loadtxt("results-gpu/results"+str(k)+"/14.txt")
    values13 = np.loadtxt("results-gpu/results"+str(k)+"/15.txt")
    values14 = np.loadtxt("results-gpu/results"+str(k)+"/16.txt")
    values15 = np.loadtxt("results-gpu/results"+str(k)+"/17.txt")


    values6o = np.loadtxt("results-ori/results"+str(k)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k)+"/17.txt")
    vec7 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]

    if (k==0):
        plt.plot(vec7,label="GPU sem SM",color=cor[k],ls='--')
    else:
        plt.plot(vec7,label="GPU com SM",color=cor[k],ls='--')
 
#### resultados com o cod original

for k in range(2):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
    values6 = np.loadtxt("results-ori/results"+str(k)+"/8.txt")
    values7 = np.loadtxt("results-ori/results"+str(k)+"/9.txt")
    values8 = np.loadtxt("results-ori/results"+str(k)+"/10.txt")
    values9 = np.loadtxt("results-ori/results"+str(k)+"/11.txt")
    values10 = np.loadtxt("results-ori/results"+str(k)+"/12.txt")        
    values11 = np.loadtxt("results-ori/results"+str(k)+"/13.txt")
    values12 = np.loadtxt("results-ori/results"+str(k)+"/14.txt")
    values13 = np.loadtxt("results-ori/results"+str(k)+"/15.txt")
    values14 = np.loadtxt("results-ori/results"+str(k)+"/16.txt")
    values15 = np.loadtxt("results-ori/results"+str(k)+"/17.txt")
    
    values6o = np.loadtxt("results-ori/results"+str(k)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k)+"/17.txt")
    vec8 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]

    if (k==0):
        plt.plot(vec8,label="Original sem SM",color=cor[k+2],ls=':')
    else:
        plt.plot(vec8,label="Original com SM",color=cor[k+2],ls=':') 


#### resultado com o codigo otimizado  

for k in range(1,13):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
    values6 = np.loadtxt("results-oti/results4/8-"+str(k)+".txt")
    values7 = np.loadtxt("results-oti/results4/9-"+str(k)+".txt")
    values8 = np.loadtxt("results-oti/results4/10-"+str(k)+".txt")
    values9 = np.loadtxt("results-oti/results4/11-"+str(k)+".txt")
    values10 = np.loadtxt("results-oti/results4/12-"+str(k)+".txt")        
    values11 = np.loadtxt("results-oti/results4/13-"+str(k)+".txt")
    values12 = np.loadtxt("results-oti/results4/14-"+str(k)+".txt")
    values13 = np.loadtxt("results-oti/results4/15-"+str(k)+".txt")
    values14 = np.loadtxt("results-oti/results4/16-"+str(k)+".txt")
    values15 = np.loadtxt("results-oti/results4/17-"+str(k)+".txt")
    
    values6o = np.loadtxt("results-ori/results"+str(k%2)+"/8.txt")
    values7o = np.loadtxt("results-ori/results"+str(k%2)+"/9.txt")
    values8o = np.loadtxt("results-ori/results"+str(k%2)+"/10.txt")
    values9o = np.loadtxt("results-ori/results"+str(k%2)+"/11.txt")
    values10o = np.loadtxt("results-ori/results"+str(k%2)+"/12.txt")        
    values11o = np.loadtxt("results-ori/results"+str(k%2)+"/13.txt")
    values12o = np.loadtxt("results-ori/results"+str(k%2)+"/14.txt")
    values13o = np.loadtxt("results-ori/results"+str(k%2)+"/15.txt")
    values14o = np.loadtxt("results-ori/results"+str(k%2)+"/16.txt")
    values15o = np.loadtxt("results-ori/results"+str(k%2)+"/17.txt")
    vec9 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]
    plt.plot(vec9,label="Otimizado t="+str(k),color=cor[k-1])


#########k=24###########
k=24
values6 = np.loadtxt("results-oti/results4/8-"+str(k)+".txt")
values7 = np.loadtxt("results-oti/results4/9-"+str(k)+".txt")
values8 = np.loadtxt("results-oti/results4/10-"+str(k)+".txt")
values9 = np.loadtxt("results-oti/results4/11-"+str(k)+".txt")
values10 = np.loadtxt("results-oti/results4/12-"+str(k)+".txt")        
values11 = np.loadtxt("results-oti/results4/13-"+str(k)+".txt")
values12 = np.loadtxt("results-oti/results4/14-"+str(k)+".txt")
values13 = np.loadtxt("results-oti/results4/15-"+str(k)+".txt")
values14 = np.loadtxt("results-oti/results4/16-"+str(k)+".txt")
values15 = np.loadtxt("results-oti/results4/17-"+str(k)+".txt")
values6o = np.loadtxt("results-ori/results"+str(k%2)+"/8.txt")
values7o = np.loadtxt("results-ori/results"+str(k%2)+"/9.txt")
values8o = np.loadtxt("results-ori/results"+str(k%2)+"/10.txt")
values9o = np.loadtxt("results-ori/results"+str(k%2)+"/11.txt")
values10o = np.loadtxt("results-ori/results"+str(k%2)+"/12.txt")        
values11o = np.loadtxt("results-ori/results"+str(k%2)+"/13.txt")
values12o = np.loadtxt("results-ori/results"+str(k%2)+"/14.txt")
values13o = np.loadtxt("results-ori/results"+str(k%2)+"/15.txt")
values14o = np.loadtxt("results-ori/results"+str(k%2)+"/16.txt")
values15o = np.loadtxt("results-ori/results"+str(k%2)+"/17.txt")
vec10 = [np.mean(values6o)/np.mean(values6),np.mean(values7o)/np.mean(values7),np.mean(values8o)/np.mean(values8),np.mean(values9o)/np.mean(values9),np.mean(values10o)/np.mean(values10),np.mean(values11o)/np.mean(values11),np.mean(values12o)/np.mean(values12),np.mean(values13o)/np.mean(values13),np.mean(values14o)/np.mean(values14),np.mean(values15o)/np.mean(values15)]
plt.plot(vec10,label="Otimizado t="+str(k),color=cor[13])
k=0
########################
    
plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
plt.xlabel('N (x10^4)')
plt.ylabel('Speedup')
plt.title('Speedup')
plt.legend()
plt.savefig('speedup3.png', format='png')
plt.show()


