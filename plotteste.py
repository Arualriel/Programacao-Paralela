import matplotlib.pyplot as plt
import numpy as np

labels = [1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
labelsn = [6,7,8,9,10,11,12,13,14,15]

#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)
for k in range(5,9):
    m=np.zeros(10)
    ind=np.zeros(10)
    matrix = []
    matrix2 = np.zeros((8,10))
    vec2=np.zeros(10)
    for i in range(10,20):
        STRIP = 2**i
        #print("Tentando abrir "+"results/results"+str(k)+"/"+str(STRIP)+"-600000.txt")
        values6 = np.loadtxt("results/results"+str(k)+"/600000-"+str(STRIP)+".txt")
        values7 = np.loadtxt("results/results"+str(k)+"/700000-"+str(STRIP)+".txt")
        values8 = np.loadtxt("results/results"+str(k)+"/800000-"+str(STRIP)+".txt")
        values9 = np.loadtxt("results/results"+str(k)+"/900000-"+str(STRIP)+".txt")
        values10 = np.loadtxt("results/results"+str(k)+"/1000000-"+str(STRIP)+".txt")        
        values11 = np.loadtxt("results/results"+str(k)+"/1100000-"+str(STRIP)+".txt")
        values12 = np.loadtxt("results/results"+str(k)+"/1200000-"+str(STRIP)+".txt")
        values13 = np.loadtxt("results/results"+str(k)+"/1300000-"+str(STRIP)+".txt")
        values14 = np.loadtxt("results/results"+str(k)+"/1400000-"+str(STRIP)+".txt")
        values15 = np.loadtxt("results/results"+str(k)+"/1500000-"+str(STRIP)+".txt")
            
        vec1 = [np.mean(values6),np.mean(values7),np.mean(values8),np.mean(values9),np.mean(values10),np.mean(values11),np.mean(values12),np.mean(values13),np.mean(values14),np.mean(values15)]
        plt.plot(vec1,label="STRIP="+str(STRIP))
        matrix.append(vec1)
    
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.xlabel('N (x10^5)')
    plt.ylabel('Time')
    plt.title('Desempenho código'+str(k))

    plt.legend()
    plt.savefig('codigo'+str(k)+'1.png', format='png')
    plt.show()

    for j in range(10):
    	for i in range(10):
            if m[j]<=matrix[i][j]:
                m[j]=matrix[i][j]
                ind[j]=i
                
    print("iteração k=",k,"menores 1=",m,"índices=",ind)

    m=np.zeros(10)
    ind=np.zeros(10)
    #print("matriz 2",matrix2)
    for j in range(10):
    	for i in range(8):
            if m[j]<=matrix2[i,j]:
                m[j]=matrix2[i,j]
                ind[j]=i
                
    print("iteração k=",k,"menores 2=",m,"índices=",ind)

    #Colormap:
    plt.imshow(matrix)
    plt.colorbar()
    plt.xticks([0,1,2,3,4,5,6,7,8,9],labelsn)
    plt.yticks([0,1,2,3,4,5,6,7,8,9],labels)
    plt.xlabel('N (x10^5)')
    plt.ylabel('STRIP')
    plt.savefig('colormap-codigo'+str(k)+'.png', format='png')
    plt.show()

