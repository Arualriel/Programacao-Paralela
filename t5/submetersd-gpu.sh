#!/bin/bash
#SBATCH --nodes=1                      #Numero de Nós
#SBATCH --ntasks-per-node=1          #Numero de tarefas por Nó
#SBATCH --ntasks=1                     #Numero total de tarefas MPI
#SBATCH --cpus-per-task=12             ##24Numero de threads por tarefa MPI
#SBATCH -p cpu_dev                 #Fila (partition) a ser utilizada
#SBATCH -J JOB                 #Nome job


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


source /scratch/app/modulos/intel-psxe-2017.1.043.sh
module load gcc/6.5  ####10.2
export I_MPI_PMI_LIBRARY=/usr/lib64/libpmi.so
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

EXEC=testsd-gpu.sh           
 

srun -n $SLURM_NTASKS $EXEC 
