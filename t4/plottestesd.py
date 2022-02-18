import matplotlib.pyplot as plt
import numpy as np

labels = [1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
labelsn = [8,9,10,11,12,13,14,15,16,17]
cor=["blue","green","purple","magenta","orange","yellow","cyan","red","brown","gray","black"]

#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)
for k in range(1,7):
    vec2=np.zeros(10)
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
        
        valuesi1 = np.loadtxt("resultssd/results002/naoOtimizado8"+str(i)+".txt")
        valuesi2 = np.loadtxt("resultssd/results002/naoOtimizado9"+str(i)+".txt")
        valuesi3 = np.loadtxt("resultssd/results002/naoOtimizado10"+str(i)+".txt")
        valuesi4 = np.loadtxt("resultssd/results002/naoOtimizado11"+str(i)+".txt")
        valuesi5 = np.loadtxt("resultssd/results002/naoOtimizado12"+str(i)+".txt")
        valuesi6 = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi7 = np.loadtxt("resultssd/results002/naoOtimizado14"+str(i)+".txt")
        valuesi8 = np.loadtxt("resultssd/results002/naoOtimizado15"+str(i)+".txt")
        valuesi9 = np.loadtxt("resultssd/results002/naoOtimizado16"+str(i)+".txt")
        valuesi10 = np.loadtxt("resultssd/results002/naoOtimizado17"+str(i)+".txt")
        vec2 = [np.mean(valuesi1),np.mean(valuesi2),np.mean(valuesi3),np.mean(valuesi4),np.mean(valuesi5),np.mean(valuesi6),np.mean(valuesi7),np.mean(valuesi8),np.mean(valuesi9),np.mean(valuesi10)]
        vec1 = [np.mean(values6),np.mean(values7),np.mean(values8),np.mean(values9),np.mean(values10),np.mean(values11),np.mean(values12),np.mean(values13),np.mean(values14),np.mean(values15)]
        plt.plot(vec1,label="Thread="+str(i),color=cor[i-1])
        plt.plot(vec2,color=cor[i-1],ls='--')#original paralelo

    
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^4)')
    plt.ylabel('Time')
    plt.title('Desempenho código'+str(k))
    
    
    for j in range(8,18):
        values = np.loadtxt("resultssd/results001/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original',color=cor[10],ls='-.')#original sem paralelizar
        
    for j in range(8,18):
        values = np.loadtxt("resultssd/results0/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original SM',color=cor[10],ls=':')#original com strip mining

    plt.legend()
    plt.savefig('codigo'+str(k)+'sdsl1.png', format='png')
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
            
        valuesi1 = np.loadtxt("resultssd/results002/naoOtimizado8"+str(i)+".txt")
        valuesi2 = np.loadtxt("resultssd/results002/naoOtimizado9"+str(i)+".txt")
        valuesi3 = np.loadtxt("resultssd/results002/naoOtimizado10"+str(i)+".txt")
        valuesi4 = np.loadtxt("resultssd/results002/naoOtimizado11"+str(i)+".txt")
        valuesi5 = np.loadtxt("resultssd/results002/naoOtimizado12"+str(i)+".txt")
        valuesi6 = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi7 = np.loadtxt("resultssd/results002/naoOtimizado14"+str(i)+".txt")
        valuesi8 = np.loadtxt("resultssd/results002/naoOtimizado15"+str(i)+".txt")
        valuesi9 = np.loadtxt("resultssd/results002/naoOtimizado16"+str(i)+".txt")
        valuesi10 = np.loadtxt("resultssd/results002/naoOtimizado17"+str(i)+".txt")
        vec21 = [np.mean(valuesi1),np.mean(valuesi2),np.mean(valuesi3),np.mean(valuesi4),np.mean(valuesi5),np.mean(valuesi6),np.mean(valuesi7),np.mean(valuesi8),np.mean(valuesi9),np.mean(valuesi10)]
        vec11 = [np.mean(values6),np.mean(values7),np.mean(values8),np.mean(values9),np.mean(values10),np.mean(values11),np.mean(values12),np.mean(values13),np.mean(values14),np.mean(values15)]
        plt.plot(vec11,label="Thread="+str(i),color=cor[i-11])
        plt.plot(vec21,color=cor[i-11],ls='--')#original paralelo

    
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^4)')
    plt.ylabel('Time')
    plt.title('Desempenho código'+str(k))
    
    
    for j in range(8,18):
        values = np.loadtxt("resultssd/results001/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original',color=cor[10],ls='-.')#original sem paralelizar

    for j in range(8,18):
        values = np.loadtxt("resultssd/results0/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original SM',color=cor[10],ls=':')#original com strip mining

    plt.legend()
    plt.savefig('codigo'+str(k)+'sdsl2.png', format='png')
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
            
        valuesi1 = np.loadtxt("resultssd/results002/naoOtimizado8"+str(i)+".txt")
        valuesi2 = np.loadtxt("resultssd/results002/naoOtimizado9"+str(i)+".txt")
        valuesi3 = np.loadtxt("resultssd/results002/naoOtimizado10"+str(i)+".txt")
        valuesi4 = np.loadtxt("resultssd/results002/naoOtimizado11"+str(i)+".txt")
        valuesi5 = np.loadtxt("resultssd/results002/naoOtimizado12"+str(i)+".txt")
        valuesi6 = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi7 = np.loadtxt("resultssd/results002/naoOtimizado14"+str(i)+".txt")
        valuesi8 = np.loadtxt("resultssd/results002/naoOtimizado15"+str(i)+".txt")
        valuesi9 = np.loadtxt("resultssd/results002/naoOtimizado16"+str(i)+".txt")
        valuesi10 = np.loadtxt("resultssd/results002/naoOtimizado17"+str(i)+".txt")
        vec22 = [np.mean(valuesi1),np.mean(valuesi2),np.mean(valuesi3),np.mean(valuesi4),np.mean(valuesi5),np.mean(valuesi6),np.mean(valuesi7),np.mean(valuesi8),np.mean(valuesi9),np.mean(valuesi10)]
        vec12 = [np.mean(values6),np.mean(values7),np.mean(values8),np.mean(values9),np.mean(values10),np.mean(values11),np.mean(values12),np.mean(values13),np.mean(values14),np.mean(values15)]
        plt.plot(vec12,label="Thread="+str(i),color=cor[i-21])
        plt.plot(vec22,color=cor[i-21],ls='--')#original paralelo

    
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^4)')
    plt.ylabel('Time')
    plt.title('Desempenho código'+str(k))
    
    for j in range(8,18):
        values = np.loadtxt("resultssd/results001/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original',color=cor[10],ls='-.')#original sem paralelizar
   

    for j in range(8,18):
        values = np.loadtxt("resultssd/results0/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original SM',color=cor[10],ls=':')#original com strip mining


    plt.legend()
    plt.savefig('codigo'+str(k)+'sdsl3.png', format='png')
    plt.show()    

    #Colormap:
#    plt.imshow(matrix)
 #   plt.colorbar()
  #  plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
  #  plt.yticks([0,1,2,3,4,5,6,7,8,9],labels)
  #  plt.xlabel('N (x10^5)')
  #  plt.ylabel('STRIP')
  #  plt.savefig('colormap-codigo'+str(k)+'.png', format='png')
  #  plt.show()

