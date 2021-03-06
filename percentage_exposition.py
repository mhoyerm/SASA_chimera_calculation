import os
import sys

storage = sys.argv[0] 
files = os.listdir(storage)
fout_name = sys.argv[1] 
fout = open(os.path.join(storage, fout_name),'w')

def main():

	fout.write('Proteins'+','+'Polar'+','+'Apolar'+','+'Charged'+'\n')
	for file in files:
	    names = []
	    if file[:14] == 'partial_result':
	        raw_file = open(file,'r')
	        archive = raw_file.read()
	        lista1 = archive.split('\n')[:3]
	        names.append(file[15:19]) #Take the names        
	        for i in range(len(lista1)):  #Take the percentages
	            if i == 2:
	                values = lista1[i].split('\t')
	                values.remove(values[0])
	                output = names + values #Lines with name and percentages
	                line = str(output)
	                a = line.replace("]",'')
	                b = a.replace('[','')
	                c = b.replace("'",'')
	                fout.write(str(c)+'\n')
	    elif file == 'output_exposition_bonded.txt':
	    	pass

if __name__ == "__main__":
	main()