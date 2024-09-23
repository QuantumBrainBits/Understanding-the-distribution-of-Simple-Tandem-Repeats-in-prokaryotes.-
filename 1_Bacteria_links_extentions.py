out = open("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/Arceae_refseq_ftp_links_extensions.txt", 'w')

with open("/home/ccmb/Desktop/KIRAN_GUEST WORKER/Bacteria_classes_evolutionary_analysis/archaea_refseq_ftp_links.txt") as links:
    for link in links:
        l = link.replace("\n", "")
        link = link.strip().split("/")
        #if "na" in link:
         #   print(link)
#       print(l, link)
        ext0 = "/"            
        ext1 = link[9]
#        if  "1_NA" in ext1:
#            print(ext1)
        ext2 = "_genomic.fna.gz"
        cont = ext0+ext1+ext2
        #print('variable/ {}/_genomic_fna.gz.'.format('iterative of line[9]'))
        print(l+cont, file=out)        

out.close()



