import matplotlib.pyplot as plt
import numpy as np

labels = [1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
labelst1 = [1,2,3,4]
labelst2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
####minha maquina 10o - 13p
#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)
for k in range(1,7):
    
    vec2=np.zeros(4)
    
    vec4=np.zeros(4)
    for i in range(1,5):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
        
        #values13s = np.loadtxt("resultssd/results"+str(k)+"/13-"+str(i)+".txt")
        values15 = np.loadtxt("resultssd/results"+str(k)+"/13-"+str(i)+".txt")
        
        #valuesi8s = np.loadtxt("resultssd/results0/naoOtimizado13.txt")
        valuesi10 = np.loadtxt("resultssd/results0/naoOtimizado13.txt")
        #valuesi80s = np.loadtxt("resultssd/results001/naoOtimizado10.txt")
        valuesi100 = np.loadtxt("resultssd/results001/naoOtimizado10.txt")
        #valuesi08s = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi010 = np.loadtxt("resultssd/results002/naoOtimizado10"+str(i)+".txt")
        
        #vec1s[i-1] = np.mean(valuesi8s)/np.mean(values13s)
        vec2[i-1] = np.mean(valuesi10)/np.mean(values15)
        #vec3s[i-1] = np.mean(valuesi08s)/np.mean(valuesi80s)
        vec4[i-1] = np.mean(valuesi010)/np.mean(valuesi100)
    #plt.plot(vec1s,label="Strip Mined N=13 x10^4")
    plt.plot(vec2,label="Strip Mined N=13 x10^4")
    #plt.plot(vec3s,label="Original N=13 x10^4",ls='-.')
    plt.plot(vec4,label="Original N=10 x10^4",ls='-.')

    plt.xticks([0,1,2,3],labelst1)
    plt.xlabel('Threads')
    plt.ylabel('Speedup')
    plt.title('Speedup do código'+str(k))
    plt.legend()
    plt.savefig('speedup-10-13-'+str(k)+'.png', format='png')
    plt.show()
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
    
    vec2s=np.zeros(30)
    
    vec4s=np.zeros(30)
    for i in range(1,31):
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
        ###SDUMONT 15 p -- 11 o
        #values13s = np.loadtxt("resultssd/results"+str(k)+"/13-"+str(i)+".txt")
        values15s = np.loadtxt("resultssd/results"+str(k)+"/15-"+str(i)+".txt")
        
        #valuesi8s = np.loadtxt("resultssd/results0/naoOtimizado13.txt")
        valuesi10s = np.loadtxt("resultssd/results0/naoOtimizado15.txt")
        #valuesi80s = np.loadtxt("resultssd/results001/naoOtimizado10.txt")
        valuesi100s = np.loadtxt("resultssd/results001/naoOtimizado11.txt")
        #valuesi08s = np.loadtxt("resultssd/results002/naoOtimizado13"+str(i)+".txt")
        valuesi010s = np.loadtxt("resultssd/results002/naoOtimizado11"+str(i)+".txt")
        
        #vec1s[i-1] = np.mean(valuesi8s)/np.mean(values13s)
        vec2s[i-1] = np.mean(valuesi10s)/np.mean(values15s)
        #vec3s[i-1] = np.mean(valuesi08s)/np.mean(valuesi80s)
        vec4s[i-1] = np.mean(valuesi010s)/np.mean(valuesi100s)
    #plt.plot(vec1s,label="Strip Mined N=13 x10^4")
    plt.plot(vec2s,label="Strip Mined N=15 x10^4")
    #plt.plot(vec3s,label="Original N=13 x10^4",ls='-.')
    plt.plot(vec4s,label="Original N=11 x10^4",ls='-.')

    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29],labelst2)
    plt.xlabel('Threads')
    plt.ylabel('Speedup')
    plt.title('Speedup do código SD'+str(k))
    plt.legend()
    plt.savefig('speedupsd-11-15-'+str(k)+'.png', format='png')
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

