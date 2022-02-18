#!/bin/bash
#SBATCH --nodes=1                      #Numero de Nós
#SBATCH --ntasks-per-node=12          #Numero de tarefas por Nó
#SBATCH --ntasks=1                     #Numero total de tarefas MPI
#SBATCH -p cpu_dev                       #Fila (partition) a ser utilizada
#SBATCH -J JOB			       #Nome job
#SBATCH --exclusive                    #Utilização exclusiva dos nós durante a execução do job

#Exibe os nós alocados para o Job
echo $SLURM_JOB_NODELIST
nodeset -e $SLURM_JOB_NODELIST

cd $SLURM_SUBMIT_DIR

#Configura os compiladores
#-------------------------#

## 1) Utilizando o OpenMPI com Intel PSXE (2016, 2017, 2018 ou 2019)
#source /scratch/app/modulos/intel-psxe-2016.sh
##########    ou    ##########
#source /scratch/app/modulos/intel-psxe-2017.sh
##########    ou    ##########
#source /scratch/app/modulos/intel-psxe-2018.sh
##########    ou    ##########
#source /scratch/app/modulos/intel-psxe-2019.sh
#source /scratch/app/modulos/intel-psxe-2020.sh
#module load openmpi/icc/2.0.4.2

##########    ou    ##########
## 2) Utilizando o OpenMPI com GNU
#module load openmpi/gnu/2.0.4.2

module load gcc/6.5        #10.2

#Configura o executavel
#EXEC=/scratch/CAMINHO/PARA/O/EXECUTAVEL
EXEC=testsd.sh
#exibe informações sobre o executável
/usr/bin/ldd $EXEC

srun -n $SLURM_NTASKS $EXEC
