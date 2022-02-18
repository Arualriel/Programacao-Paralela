import matplotlib.pyplot as plt
import numpy as np

labels = [1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
labelsn = [8,9,10,11,12,13,14,15,16,17]
cor=["blue","green","purple","magenta","orange","yellow","cyan","red","brown","gray"]

#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)

#    matrix = []
#    vec2=np.zeros(10)

for k in range(1,7):
    for i in range(1,11):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
        values6 = np.loadtxt("resultssd/results"+str(k)+"/8-"+str(i)+".txt")
        values7 = np.loadtxt("resultssd/results"+str(k)+"/9-"+str(i)+".txt")
        values8 = np.loadtxt("resultssd/results"+str(k)+"/10-"+str(i)+".txt")
        values9 = np.loadtxt("resultssd/results"+str(k)+"/11-"+str(i)+".txt")
        values10 = np.loadtxt("resultssd/results"+str(k)+"/12-"+str(i)+".txt")
        values11 = np.loadtxt("resultssd/results"+str(k)+"/13-"+str(i)+".txt")
        values12 = np.loadtxt("resultssd/results"+str(k)+"/14-"+str(i)+".txt")
        values13 = np.loadtxt("resultssd/results"+str(k)+"/15-"+str(i)+".txt")
        values14 = np.loadtxt("resultssd/results"+str(k)+"/16-"+str(i)+".txt")
        values15 = np.loadtxt("resultssd/results"+str(k)+"/17-"+str(i)+".txt")
        
        valuesi1 = np.loadtxt("resultssd/results0/naoOtimizado8.txt")
        valuesi2 = np.loadtxt("resultssd/results0/naoOtimizado9.txt")
        valuesi3 = np.loadtxt("resultssd/results0/naoOtimizado10.txt")
        valuesi4 = np.loadtxt("resultssd/results0/naoOtimizado11.txt")
        valuesi5 = np.loadtxt("resultssd/results0/naoOtimizado12.txt")
        valuesi6 = np.loadtxt("resultssd/results0/naoOtimizado13.txt")
        valuesi7 = np.loadtxt("resultssd/results0/naoOtimizado14.txt")
        valuesi8 = np.loadtxt("resultssd/results0/naoOtimizado15.txt")
        valuesi9 = np.loadtxt("resultssd/results0/naoOtimizado16.txt")
        valuesi10 = np.loadtxt("resultssd/results0/naoOtimizado17.txt")
        
        valuesi01o = np.loadtxt("resultssd/results001/naoOtimizado8.txt")
        valuesi02o = np.loadtxt("resultssd/results001/naoOtimizado9.txt")
        valuesi03o = np.loadtxt("resultssd/results001/naoOtimizado10.txt")
        valuesi04o = np.loadtxt("resultssd/results001/naoOtimizado11.txt")
        valuesi05o = np.loadtxt("resultssd/results001/naoOtimizado12.txt")
        valuesi06o = np.loadtxt("resultssd/results001/naoOtimizado13.txt")
        valuesi07o = np.loadtxt("resultssd/results001/naoOtimizado14.txt")
        valuesi08o = np.loadtxt("resultssd/results001/naoOtimizado15.txt")
        valuesi09o = np.loadtxt("resultssd/results001/naoOtimizado16.txt")
        valuesi010o = np.loadtxt("resultssd/results001/naoOtimizado17.txt")
        
        valuesi01 = np.loadtxt("resultssd/results002/naoOtimizado8"+str(i)+".txt")
        valuesi02 = np.loadtxt("resultssd/results002/naoOtimizado9"+str(i)+".txt")
        valuesi03 = np.loadtxt("resultssd/results002/naoOtimizado10"+str(i)+".txt")
        valuesi04 = np.loadtxt("resultssd/results002/naoOtimizado11"+str(i)+".txt")
        valuesi05 = np.loadtxt("resultssd/results002/naoOtimizado12"+str(i)+".txt")
        valuesi06 = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi07 = np.loadtxt("resultssd/results002/naoOtimizado14"+str(i)+".txt")
        valuesi08 = np.loadtxt("resultssd/results002/naoOtimizado15"+str(i)+".txt")
        valuesi09 = np.loadtxt("resultssd/results002/naoOtimizado16"+str(i)+".txt")
        valuesi010 = np.loadtxt("resultssd/results002/naoOtimizado17"+str(i)+".txt")
            
        vec1 = [np.mean(valuesi1)/np.mean(values6),np.mean(valuesi2)/np.mean(values7),np.mean(valuesi3)/np.mean(values8),np.mean(valuesi4)/np.mean(values9),np.mean(valuesi5)/np.mean(values10),np.mean(valuesi6)/np.mean(values11),np.mean(valuesi7)/np.mean(values12),np.mean(valuesi8)/np.mean(values13),np.mean(valuesi9)/np.mean(values14),np.mean(valuesi10)/np.mean(values15)]
        
        vec2 = [np.mean(valuesi01o)/np.mean(valuesi01),np.mean(valuesi02o)/np.mean(valuesi02),np.mean(valuesi03o)/np.mean(valuesi03),np.mean(valuesi04o)/np.mean(valuesi04),np.mean(valuesi05o)/np.mean(valuesi05),np.mean(valuesi06o)/np.mean(valuesi06),np.mean(valuesi07o)/np.mean(valuesi07),np.mean(valuesi08o)/np.mean(valuesi08),np.mean(valuesi09o)/np.mean(valuesi09),np.mean(valuesi010o)/np.mean(valuesi010)]
        plt.plot(vec1,label="Thread="+str(i),color=cor[i-1])
        plt.plot(vec2,color=cor[i-1],ls='-.')
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^4)')
    plt.ylabel('Speedup')
    plt.title('Speedup código'+str(k))
    plt.legend()
    plt.savefig('speedup-cod'+str(k)+'sd1.png', format='png')
    plt.show()
    for i in range(11,21):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
        values6 = np.loadtxt("resultssd/results"+str(k)+"/8-"+str(i)+".txt")
        values7 = np.loadtxt("resultssd/results"+str(k)+"/9-"+str(i)+".txt")
        values8 = np.loadtxt("resultssd/results"+str(k)+"/10-"+str(i)+".txt")
        values9 = np.loadtxt("resultssd/results"+str(k)+"/11-"+str(i)+".txt")
        values10 = np.loadtxt("resultssd/results"+str(k)+"/12-"+str(i)+".txt")        
        values11 = np.loadtxt("resultssd/results"+str(k)+"/13-"+str(i)+".txt")
        values12 = np.loadtxt("resultssd/results"+str(k)+"/14-"+str(i)+".txt")
        values13 = np.loadtxt("resultssd/results"+str(k)+"/15-"+str(i)+".txt")
        values14 = np.loadtxt("resultssd/results"+str(k)+"/16-"+str(i)+".txt")
        values15 = np.loadtxt("resultssd/results"+str(k)+"/17-"+str(i)+".txt")
        
        valuesi1 = np.loadtxt("resultssd/results0/naoOtimizado8.txt")
        valuesi2 = np.loadtxt("resultssd/results0/naoOtimizado9.txt")
        valuesi3 = np.loadtxt("resultssd/results0/naoOtimizado10.txt")
        valuesi4 = np.loadtxt("resultssd/results0/naoOtimizado11.txt")
        valuesi5 = np.loadtxt("resultssd/results0/naoOtimizado12.txt")
        valuesi6 = np.loadtxt("resultssd/results0/naoOtimizado13.txt")
        valuesi7 = np.loadtxt("resultssd/results0/naoOtimizado14.txt")
        valuesi8 = np.loadtxt("resultssd/results0/naoOtimizado15.txt")
        valuesi9 = np.loadtxt("resultssd/results0/naoOtimizado16.txt")
        valuesi10 = np.loadtxt("resultssd/results0/naoOtimizado17.txt")
        
        valuesi01o = np.loadtxt("resultssd/results001/naoOtimizado8.txt")
        valuesi02o = np.loadtxt("resultssd/results001/naoOtimizado9.txt")
        valuesi03o = np.loadtxt("resultssd/results001/naoOtimizado10.txt")
        valuesi04o = np.loadtxt("resultssd/results001/naoOtimizado11.txt")
        valuesi05o = np.loadtxt("resultssd/results001/naoOtimizado12.txt")
        valuesi06o = np.loadtxt("resultssd/results001/naoOtimizado13.txt")
        valuesi07o = np.loadtxt("resultssd/results001/naoOtimizado14.txt")
        valuesi08o = np.loadtxt("resultssd/results001/naoOtimizado15.txt")
        valuesi09o = np.loadtxt("resultssd/results001/naoOtimizado16.txt")
        valuesi010o = np.loadtxt("resultssd/results001/naoOtimizado17.txt")
        
        valuesi01 = np.loadtxt("resultssd/results002/naoOtimizado8"+str(i)+".txt")
        valuesi02 = np.loadtxt("resultssd/results002/naoOtimizado9"+str(i)+".txt")
        valuesi03 = np.loadtxt("resultssd/results002/naoOtimizado10"+str(i)+".txt")
        valuesi04 = np.loadtxt("resultssd/results002/naoOtimizado11"+str(i)+".txt")
        valuesi05 = np.loadtxt("resultssd/results002/naoOtimizado12"+str(i)+".txt")
        valuesi06 = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi07 = np.loadtxt("resultssd/results002/naoOtimizado14"+str(i)+".txt")
        valuesi08 = np.loadtxt("resultssd/results002/naoOtimizado15"+str(i)+".txt")
        valuesi09 = np.loadtxt("resultssd/results002/naoOtimizado16"+str(i)+".txt")
        valuesi010 = np.loadtxt("resultssd/results002/naoOtimizado17"+str(i)+".txt")
            
        vec12 = [np.mean(valuesi1)/np.mean(values6),np.mean(valuesi2)/np.mean(values7),np.mean(valuesi3)/np.mean(values8),np.mean(valuesi4)/np.mean(values9),np.mean(valuesi5)/np.mean(values10),np.mean(valuesi6)/np.mean(values11),np.mean(valuesi7)/np.mean(values12),np.mean(valuesi8)/np.mean(values13),np.mean(valuesi9)/np.mean(values14),np.mean(valuesi10)/np.mean(values15)]
        
        vec22 = [np.mean(valuesi01o)/np.mean(valuesi01),np.mean(valuesi02o)/np.mean(valuesi02),np.mean(valuesi03o)/np.mean(valuesi03),np.mean(valuesi04o)/np.mean(valuesi04),np.mean(valuesi05o)/np.mean(valuesi05),np.mean(valuesi06o)/np.mean(valuesi06),np.mean(valuesi07o)/np.mean(valuesi07),np.mean(valuesi08o)/np.mean(valuesi08),np.mean(valuesi09o)/np.mean(valuesi09),np.mean(valuesi010o)/np.mean(valuesi010)]
        plt.plot(vec12,label="Thread="+str(i),color=cor[i-11],)
        plt.plot(vec22,color=cor[i-11],ls='-.')
    
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^4)')
    plt.ylabel('Speedup')
    plt.title('Speedup código'+str(k))
    plt.legend()
    plt.savefig('speedup-cod'+str(k)+'sd2.png', format='png')
    plt.show()
    for i in range(21,31):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
        values6 = np.loadtxt("resultssd/results"+str(k)+"/8-"+str(i)+".txt")
        values7 = np.loadtxt("resultssd/results"+str(k)+"/9-"+str(i)+".txt")
        values8 = np.loadtxt("resultssd/results"+str(k)+"/10-"+str(i)+".txt")
        values9 = np.loadtxt("resultssd/results"+str(k)+"/11-"+str(i)+".txt")
        values10 = np.loadtxt("resultssd/results"+str(k)+"/12-"+str(i)+".txt")        
        values11 = np.loadtxt("resultssd/results"+str(k)+"/13-"+str(i)+".txt")
        values12 = np.loadtxt("resultssd/results"+str(k)+"/14-"+str(i)+".txt")
        values13 = np.loadtxt("resultssd/results"+str(k)+"/15-"+str(i)+".txt")
        values14 = np.loadtxt("resultssd/results"+str(k)+"/16-"+str(i)+".txt")
        values15 = np.loadtxt("resultssd/results"+str(k)+"/17-"+str(i)+".txt")
        
        valuesi1 = np.loadtxt("resultssd/results0/naoOtimizado8.txt")
        valuesi2 = np.loadtxt("resultssd/results0/naoOtimizado9.txt")
        valuesi3 = np.loadtxt("resultssd/results0/naoOtimizado10.txt")
        valuesi4 = np.loadtxt("resultssd/results0/naoOtimizado11.txt")
        valuesi5 = np.loadtxt("resultssd/results0/naoOtimizado12.txt")
        valuesi6 = np.loadtxt("resultssd/results0/naoOtimizado13.txt")
        valuesi7 = np.loadtxt("resultssd/results0/naoOtimizado14.txt")
        valuesi8 = np.loadtxt("resultssd/results0/naoOtimizado15.txt")
        valuesi9 = np.loadtxt("resultssd/results0/naoOtimizado16.txt")
        valuesi10 = np.loadtxt("resultssd/results0/naoOtimizado17.txt")
        
        valuesi01o = np.loadtxt("resultssd/results001/naoOtimizado8.txt")
        valuesi02o = np.loadtxt("resultssd/results001/naoOtimizado9.txt")
        valuesi03o = np.loadtxt("resultssd/results001/naoOtimizado10.txt")
        valuesi04o = np.loadtxt("resultssd/results001/naoOtimizado11.txt")
        valuesi05o = np.loadtxt("resultssd/results001/naoOtimizado12.txt")
        valuesi06o = np.loadtxt("resultssd/results001/naoOtimizado13.txt")
        valuesi07o = np.loadtxt("resultssd/results001/naoOtimizado14.txt")
        valuesi08o = np.loadtxt("resultssd/results001/naoOtimizado15.txt")
        valuesi09o = np.loadtxt("resultssd/results001/naoOtimizado16.txt")
        valuesi010o = np.loadtxt("resultssd/results001/naoOtimizado17.txt")
        
        
        valuesi01 = np.loadtxt("resultssd/results002/naoOtimizado8"+str(i)+".txt")
        valuesi02 = np.loadtxt("resultssd/results002/naoOtimizado9"+str(i)+".txt")
        valuesi03 = np.loadtxt("resultssd/results002/naoOtimizado10"+str(i)+".txt")
        valuesi04 = np.loadtxt("resultssd/results002/naoOtimizado11"+str(i)+".txt")
        valuesi05 = np.loadtxt("resultssd/results002/naoOtimizado12"+str(i)+".txt")
        valuesi06 = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi07 = np.loadtxt("resultssd/results002/naoOtimizado14"+str(i)+".txt")
        valuesi08 = np.loadtxt("resultssd/results002/naoOtimizado15"+str(i)+".txt")
        valuesi09 = np.loadtxt("resultssd/results002/naoOtimizado16"+str(i)+".txt")
        valuesi010 = np.loadtxt("resultssd/results002/naoOtimizado17"+str(i)+".txt")
            
        vec13 = [np.mean(valuesi1)/np.mean(values6),np.mean(valuesi2)/np.mean(values7),np.mean(valuesi3)/np.mean(values8),np.mean(valuesi4)/np.mean(values9),np.mean(valuesi5)/np.mean(values10),np.mean(valuesi6)/np.mean(values11),np.mean(valuesi7)/np.mean(values12),np.mean(valuesi8)/np.mean(values13),np.mean(valuesi9)/np.mean(values14),np.mean(valuesi10)/np.mean(values15)]
        
        vec23 = [np.mean(valuesi01o)/np.mean(valuesi01),np.mean(valuesi02o)/np.mean(valuesi02),np.mean(valuesi03o)/np.mean(valuesi03),np.mean(valuesi04o)/np.mean(valuesi04),np.mean(valuesi05o)/np.mean(valuesi05),np.mean(valuesi06o)/np.mean(valuesi06),np.mean(valuesi07o)/np.mean(valuesi07),np.mean(valuesi08o)/np.mean(valuesi08),np.mean(valuesi09o)/np.mean(valuesi09),np.mean(valuesi010o)/np.mean(valuesi010)]
        plt.plot(vec13,label="Thread="+str(i),color=cor[i-21],)
        plt.plot(vec23,color=cor[i-21],ls='-.')
    

    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^4)')
    plt.ylabel('Speedup')
    plt.title('Speedup código'+str(k))
    plt.legend()
    plt.savefig('speedup-cod'+str(k)+'sd3.png', format='png')
    plt.show()




#    matrix.append(vec1)
    
#    for i in range(8,18):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
#        values6 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values7 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values8 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values9 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values10 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")        
#        values11 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values12 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values13 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values14 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
#        values15 = np.loadtxt("results/results0/naoOtimizado"+str(i)+".txt")
            
#        vec1 = [np.mean(values6),np.mean(values7),np.mean(values8),np.mean(values9),np.mean(values10),np.mean(values11),np.mean(values12),np.mean(values13),np.mean(values14),np.mean(values15)]
#        plt.plot(vec1,label="Thread="+str(i))
#        matrix.append(vec1)
    
    

    #Colormap:
#    plt.imshow(matrix)
 #   plt.colorbar()
  #  plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
  #  plt.yticks([0,1,2,3,4,5,6,7,8,9],labels)
  #  plt.xlabel('N (x10^5)')
  #  plt.ylabel('STRIP')
  #  plt.savefig('colormap-codigo'+str(k)+'.png', format='png')
  #  plt.show()

