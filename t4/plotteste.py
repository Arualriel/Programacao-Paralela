import matplotlib.pyplot as plt
import numpy as np

labels = [1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
labelsn = [8,9,10,11,12,13,14,15,16,17]
cor=["blue","green","orange","red","purple"]

#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)
for k in range(1,7):
    matrix = []
    vec2=np.zeros(10)
    for i in range(1,5):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
        values6 = np.loadtxt("results/results"+str(k)+"/8-"+str(i)+".txt")
        values7 = np.loadtxt("results/results"+str(k)+"/9-"+str(i)+".txt")
        values8 = np.loadtxt("results/results"+str(k)+"/10-"+str(i)+".txt")
        values9 = np.loadtxt("results/results"+str(k)+"/11-"+str(i)+".txt")
        values10 = np.loadtxt("results/results"+str(k)+"/12-"+str(i)+".txt")        
        values11 = np.loadtxt("results/results"+str(k)+"/13-"+str(i)+".txt")
        values12 = np.loadtxt("results/results"+str(k)+"/14-"+str(i)+".txt")
        values13 = np.loadtxt("results/results"+str(k)+"/15-"+str(i)+".txt")
        values14 = np.loadtxt("results/results"+str(k)+"/16-"+str(i)+".txt")
        values15 = np.loadtxt("results/results"+str(k)+"/17-"+str(i)+".txt")
        
            
        vec1 = [np.mean(values6),np.mean(values7),np.mean(values8),np.mean(values9),np.mean(values10),np.mean(values11),np.mean(values12),np.mean(values13),np.mean(values14),np.mean(values15)]
        plt.plot(vec1,label="Thread="+str(i),color=cor[i-1])
        matrix.append(vec1)
    
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
    
    
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^4)')
    plt.ylabel('Time')
    plt.title('Desempenho código'+str(k))
   
    
    for j in range(8,18):
        values = np.loadtxt("results/results001/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original',color=cor[4],ls='-.')
   
    for i in range(1,5):
        for j in range(8,18):
            values = np.loadtxt("results/results002/naoOtimizado"+str(j)+str(i)+".txt")
            vec2[j-8] = np.mean(values)
        plt.plot(vec2,color=cor[i-1],ls='--')
        
    for j in range(8,18):
        values = np.loadtxt("results/results0/naoOtimizado"+str(j)+".txt")
        vec2[j-8] = np.mean(values)
    plt.plot(vec2,label='Original SM',color=cor[4],ls=':')

    plt.legend()
    plt.savefig('codigo'+str(k)+'.png', format='png')
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

