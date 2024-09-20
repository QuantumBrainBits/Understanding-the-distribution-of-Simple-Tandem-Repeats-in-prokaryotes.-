infile = "/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaearepeats/GCA_020344955_imperfM5_CollapseData.tsv"

#out = open("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaearepeats/GCA_020344955_imperfM4_CollapseData_result.tsv", 'w')            


#iteration = 0

with open(infile) as fh: # We are using 'infile' for reading the file, as it will read the file line by line taking the each line as an item in list.
    for l, line in enumerate(fh): # enumerate() function allows you to loop over an iterable object and keep track of how many iterations have occurred, in this line, object l is storing tracking the itterations.
        line = line.strip().split('\t') # As file is not in form of table each line we have to 'strip' to remove the unneccesary gaps and split to delimit the values.
        EndC = (line[4])
        StartC = (line[3])
        lens = (line[5])
        motifs = line[6]
        if "," in StartC: 
            StartC = StartC.split(',')
            LenC = [int(l) for l in lens.split(',')]
            EndC = EndC.split(',')       
            outer_i = 0
            motifs = motifs.split(',')
            print(len(LenC))
            for endc in EndC:
                inner_i = outer_i + 1
                for jstartc in StartC[outer_i + 1:]:
                    #test = StartC[1]
                    #print(test)
                    print(outer_i, inner_i)
                    overlap = int(endc) - int(jstartc)
                    if overlap > 0:
                        i_fraction = round(abs(overlap)/LenC[outer_i], 2)
                        j_fraction = round(abs(overlap)/LenC[inner_i], 2)
                        if i_fraction > 1: i_fraction = 1
                        if j_fraction > 1: j_fraction = 1
                        print(LenC[outer_i], i_fraction, overlap, motifs[outer_i], line) 
                        print(LenC[inner_i], j_fraction, overlap, motifs[inner_i])
                    else:
                        break
                    inner_i += 1
                outer_i += 1
