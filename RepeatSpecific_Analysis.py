# Repeat Specific analysis
#from matplotlib import pyplot
import pandas as pd
import seaborn as sns
import os
import scipy.stats
import numpy as np
#import collections
import matplotlib.pyplot as plt

out = open("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes/Repeats_covarage.tsv", 'w')

directory = "/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes/Archaea_Filtered_Files/" 


def all_files(infile): 
    Rc = 0
    with open(f'{directory}{infile}') as genome:
        for i in genome: 
            i = i.strip().split(" ")
        #    repeat_seq_len = i[3]
         #   filename = "infile"
            Repeats_cov = i[3]
            Rc += int(Repeats_cov)
        print(Rc, infile[10:31], file = out)
              
 
                    
files_dicrtry = "/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes/Archaea_Filtered_Files/"
extension = ('.tsv')
 
for file in os.listdir(files_dicrtry): # iterating the all files.
    if file.endswith(extension): # if files ends with .tsv extension.
       all_files(file) 

    
df = pd.read_csv("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes/Repeats_covarage.tsv", sep = " ")       
df1 = pd.read_csv("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_genomes/Genome_seq_len.tsv", sep = " ")

merge_genome_repCov = pd.concat([df, df1], axis = 1)

merge_genome_repCov.columns = ['rep_len','uniq','genome_len','uniq1']

#merge_genome_repCov.sort_values(by=['uniq'], inplace=True)

Rep_cov = merge_genome_repCov[['rep_len','uniq']]
genome_cov = merge_genome_repCov[['genome_len','uniq1']]
genome_cov.columns = ['genome_len', 'uniq']
#Rep_cov.sort_values(by=['uniq1'], inplace=True)

merged_Genome_Rep_cov = pd.merge(Rep_cov, genome_cov, on="uniq")

# We are normalizing the rep_cov values with genome size.
RepeatLen_cov = (merged_Genome_Rep_cov['rep_len'] / merged_Genome_Rep_cov['genome_len'])


# lets use kernel density to observe the distribution of data.

# Repeat_cov distribution, to just discribe how the covarage is, but in this we see there are 3 parts of peaks, lets see if there are relying on its genome size or not
sns.displot(RepeatLen_cov, kind="kde")

# Discriptive relation between Genome size and rep_cov.

test = merged_Genome_Rep_cov[['rep_len','genome_len']]
sns.displot(test, x=test['genome_len'], kde=True)
sns.displot(test, x=test['rep_len'], kde=True)

sns.displot(test, x="rep_len", y="genome_len")
sns.jointplot(data=test, x="rep_len", y="genome_len")




# pandas
test['Genome_log_value'] = np.log(test['genome_len'])
test['rep_log_value'] = np.log(test['rep_len'])

sns.displot(RepeatLen_cov, kde=True)
plt.xlabel("Repeat_Len_cov")


fig, ax = plt.subplots()
columns = [RepeatLen_cov]
ax.boxplot(columns, patch_artist=True, meanline=True, showmeans=True)
plt.xticks([1], ["Repeat seqn len's distribution overall Archeae genome"])
 

import pandas as pd

plt.show()





# let plot correlation 
corr_coeff = scipy.stats.pearsonr(merged_Genome_Rep_cov['rep_len'], merged_Genome_Rep_cov['genome_len'])

# scatter plot which shows relation between genome size and repeat len

#find line of best fit

plt.scatter(merged_Genome_Rep_cov['rep_len'],merged_Genome_Rep_cov['genome_len'])
plt.show()

print(df.sample(10))

# plot a correlation between genome size and repeat len.
#
#m = df1[df1['uniq1']== '_001719125.1_ASM17191']
#print(m)
#
#n = df[df['uniq']== '_000711905.1_ASM71190']
#print(n)
#
#
#print(pd.merge(Rep_cov,Genome_len, indicator=True, how='outer')
#         .query('_merge=="right_only"')
#         .drop('_merge', axis=1))




























# Datasets having two different lens cant be merged with help of "key", so we have concatinated them so both the files got same rows where other file got filled with NA's and split them and give them as "right and left" to merge where this NA's will also get filtered.

left = pd.DataFrame(

    {

        "key1": ["K3", "K2"],

        "A": ["A0", "A1"],

    }

)



right = pd.DataFrame(

    {

        "key": ["K1", "K3", "K2", "K4"],

        "C": ["C0", "C1", "C2", "C3"],

    }

)

merge_2_datasets = pd.concat([right, left], axis = 1)

split_genome_repeat_len = merge_2_datasets[['key1','A']]
split_genome_repeat_len.columns= ['key','A']
split_genome_repeat_len1 = merge_2_datasets[['key','C']]

result = pd.merge(split_genome_repeat_len, split_genome_repeat_len1, on="key")
print(result)




        
        
        