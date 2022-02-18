import matplotlib.pyplot as plt
import numpy as np

labels = [128,256,512,1024,2048,4096,8192,16384]
matrix = []
#7 - 15 (para imprimir só alguns SIZEVEC, mudar o range abaixo)
for i in range(7,11):
    SIZEVEC = 2**i
    print("Tentando abrir "+"results2d/"+str(SIZEVEC)+"-128.txt")
    values128 = np.loadtxt("results2d/"+str(SIZEVEC)+"-128.txt")
    values256 = np.loadtxt("results2d/"+str(SIZEVEC)+"-256.txt")
    values512 = np.loadtxt("results2d/"+str(SIZEVEC)+"-512.txt")
    values1024 = np.loadtxt("results2d/"+str(SIZEVEC)+"-1024.txt")
    values2048 = np.loadtxt("results2d/"+str(SIZEVEC)+"-2048.txt")
    values4096 = np.loadtxt("results2d/"+str(SIZEVEC)+"-4096.txt")
    values8192 = np.loadtxt("results2d/"+str(SIZEVEC)+"-8192.txt")
    values16384 = np.loadtxt("results2d/"+str(SIZEVEC)+"-16384.txt")  
    vec1 = [np.mean(values128),np.mean(values256),np.mean(values512), np.mean(values1024), np.mean(values2048), np.mean(values4096), np.mean(values8192), np.mean(values16384)]
    plt.plot(vec1,label="SIZEVEC="+str(SIZEVEC))
    matrix.append(vec1)
plt.xticks([0,1,2,3,4,5,6,7],labels)
plt.xlabel('TILE')
plt.ylabel('Time')
plt.title('n = 16384')

values= np.loadtxt("results2d/naoOtimizado.txt")
plt.hlines(np.mean(values),0,7,label="Original")
plt.legend()
plt.show()


for i in range(11,15):
    SIZEVEC = 2**i
    print("Tentando abrir "+"results2d/"+str(SIZEVEC)+"-128.txt")
    values128 = np.loadtxt("results2d/"+str(SIZEVEC)+"-128.txt")
    values256 = np.loadtxt("results2d/"+str(SIZEVEC)+"-256.txt")
    values512 = np.loadtxt("results2d/"+str(SIZEVEC)+"-512.txt")
    values1024 = np.loadtxt("results2d/"+str(SIZEVEC)+"-1024.txt")
    values2048 = np.loadtxt("results2d/"+str(SIZEVEC)+"-2048.txt")
    values4096 = np.loadtxt("results2d/"+str(SIZEVEC)+"-4096.txt")
    values8192 = np.loadtxt("results2d/"+str(SIZEVEC)+"-8192.txt")
    values16384 = np.loadtxt("results2d/"+str(SIZEVEC)+"-16384.txt")  
    vec1 = [np.mean(values128),np.mean(values256),np.mean(values512), np.mean(values1024), np.mean(values2048), np.mean(values4096), np.mean(values8192), np.mean(values16384)]
    plt.plot(vec1,label="SIZEVEC="+str(SIZEVEC))
    matrix.append(vec1)

plt.xticks([0,1,2,3,4,5,6,7],labels)
plt.xlabel('TILE')
plt.ylabel('Time')
plt.title('n = 16384')

values= np.loadtxt("results2d/naoOtimizado.txt")
plt.hlines(np.mean(values),0,7,label="Original")
plt.legend()
plt.show()

#Colormap:
plt.imshow(matrix)
plt.colorbar()
plt.xticks([0,1,2,3,4,5,6,7],labels)
plt.yticks([0,1,2,3,4,5,6,7],labels)
plt.xlabel('TILE')
plt.ylabel('SIZEVEC')
plt.show()
