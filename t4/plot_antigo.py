import matplotlib.pyplot as plt
import numpy as np

labels = [128,256,512,1024,2048,4096,8192,16384,32768,65536]
labelsn = [8,9,10,11,12,13,14,15,16,17]

#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)

m=np.zeros(10)
ind=np.zeros(10)
matrix = []
vec2=np.zeros(10)
for i in range(7,17):
    STRIP = 2**i
    #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
    values8 = np.loadtxt("results8/8-"+str(STRIP)+".txt")
    values9 = np.loadtxt("results8/9-"+str(STRIP)+".txt")
    values10 = np.loadtxt("results8/10-"+str(STRIP)+".txt")
    values11 = np.loadtxt("results8/11-"+str(STRIP)+".txt")
    values12 = np.loadtxt("results8/12-"+str(STRIP)+".txt")        
    values13 = np.loadtxt("results8/13-"+str(STRIP)+".txt")
    values14 = np.loadtxt("results8/14-"+str(STRIP)+".txt")
    values15 = np.loadtxt("results8/15-"+str(STRIP)+".txt")
    values16 = np.loadtxt("results8/16-"+str(STRIP)+".txt")
    values17 = np.loadtxt("results8/17-"+str(STRIP)+".txt")
           
    vec1 = [np.mean(values8),np.mean(values9),np.mean(values10),np.mean(values11),np.mean(values12),np.mean(values13),np.mean(values14),np.mean(values15),np.mean(values16),np.mean(values17)]
    plt.plot(vec1,label="STRIP="+str(STRIP))
    matrix.append(vec1)
    
plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
plt.xlabel('N (x10^4)')
plt.ylabel('Time')
plt.title('Desempenho código 8')
    
plt.legend()
plt.savefig('codigo81.png', format='png')
plt.show()

    #plt.imshow(matrix2)
    #plt.colorbar()
    #plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    #plt.yticks([0,1,2,3,4,5,6,7,8,9],labels)
    #plt.xlabel('N (x10^5)')
    #plt.ylabel('cod')
    #plt.savefig('colormap-codigo'+str(k)+'.png', format='png')
    #plt.show()
    #Colormap:
plt.imshow(matrix)
plt.colorbar()
plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
plt.yticks([0,1,2,3,4,5,6,7,8,9],labels)
plt.xlabel('N (x10^4)')
plt.ylabel('STRIP')
plt.savefig('colormap-codigo8.png', format='png')
plt.show()

