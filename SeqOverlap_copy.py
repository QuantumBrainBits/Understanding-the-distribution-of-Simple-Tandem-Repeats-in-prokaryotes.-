infile = "/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaearepeats/GCA_020344955_imperfM5_CollapseData.tsv"

#out = open("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaearepeats/GCA_020344955_imperfM6_SeqOverlaps.tsv", 'w')            

# Where there is no overlap between 2 sequences, we wont get any info other than (chrm, start, end, len = start-end)


#iteration = 0


with open(infile) as fh: # We are using 'infile' for reading the file, as it will read the file line by line taking the each line as an item in list.
    for l, line in enumerate(fh): # enumerate() function allows you to loop over an iterable object and keep track of how many iterations have occurred, in this line, object l is storing tracking the itterations.
        line = line.strip().split('\t') # As file is not in form of table each line we have to 'strip' to remove the unneccesary gaps and split to delimit the values.
        EndC = (line[4])
        StartC = (line[3])
        lens = (line[5])
        motifs = line[6]
        seqs = int(line[1])
        seqe = int(line[2])
        mutation_allowed = line[7]
        imperfseq = line[8]
        overlapped_seq_len = seqe - seqs 
        chrom = line[0]
        if "," in StartC: 
            StartC = StartC.split(',')
            LenC = [int(l) for l in lens.split(',')]
            EndC = EndC.split(',')       
            outer_i = 0
            motifs = motifs.split(',')
            imperfseq = imperfseq.split(',')
            t1 = ""                
            mutation_allowed = mutation_allowed.split(',')
#            print(len(LenC))
            val = ""
            novrlp = ""
            test1 = ""
            ss = ""
            ss1 = ""
            for endc in EndC:
                #novrlp = ""
                inner_i = outer_i + 1
                for jstartc in StartC[outer_i + 1:]:
                    #test = StartC[1]
                    #print(test) 
 #                   print(outer_i, inner_i)
                    outer = 0 
                    overlap = int(endc) - int(jstartc)
                    if overlap > 0:
                        i_fraction = round(abs(overlap)/LenC[outer_i], 2)
                        j_fraction = round(abs(overlap)/LenC[inner_i], 2)
                        if i_fraction > 1: i_fraction = 1
                        if j_fraction > 1: j_fraction = 1
                        motif = motifs[outer_i]
                        motif1 = motifs[inner_i]
                        seqlen = LenC[outer_i]
                        seqlen1 = LenC[inner_i]
                        mut_alwd = mutation_allowed[outer_i] 
                        mut_alwd1 = mutation_allowed[inner_i] 
                        ss = imperfseq[inner_i]
                        novrlp = ss[overlap:] 
                        ss1 = imperfseq[0]
                        val += (f'({motif}:{seqlen}:{mut_alwd}-{overlap})-')#{novrlp}-)') # - ({motif1} : {seqlen1} : {mut_alwd1} - {overlap}) - {mseq}')
 #                        print(LenC[outer_i], i_fraction, overlap, motifs[outer_i]) 
 #                       print(LenC[inner_i], j_fraction, overlap, motifs[inner_i])
                        outer += 1   
                        if outer == 1:
                            break
                    else:
                        break
                    inner_i += 1
                    
                test1 = ss1+novrlp    
        #print(chrom, seqs, seqe, overlapped_seq_len, val)
                outer_i += 1
            print(chrom, seqs, seqe, overlapped_seq_len, val, test1, ss1,novrlp) #, file = out)
            
#out.close()