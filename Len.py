import os

out = open("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes/lens_occurance.tsv", 'w')

directory = "/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes/" 



def all_files(infile):
    with open(f'{directory}{infile}') as genome1:
      data = genome1.read()
      Genome_len = int(len(data))
    with open(f'{directory}{infile}') as genome:
        lens_dict = {} 
        for i in genome: 
          i = i.strip().split("\t")
          if i[3] not in lens_dict:
            z = i[3]
            lens_dict[z] = 1
          else:
            lens_dict[z] += 1
        for j in lens_dict:
          updt =  lens_dict[j] / Genome_len 
          print(j, updt)
                
            
 
                    
files_dicrtry = "/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes"
extension = ('erf.tsv')

for file in os.listdir(files_dicrtry): # iterating the all files.
    if file.endswith(extension): # if files ends with .tsv extension.
      all_files(file) 

