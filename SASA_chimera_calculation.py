import sys
import os
import numpy as np

def main():

	var = sys.argv[0] 

	files = os.listdir(var)

	ptn_list = []
	for name in files:
	    ptn = name[5:]
	    ptn_list.append(ptn)
	    
	ptn_list2 = []
	for name2 in files:
	    ptn2 = name2[:4]
	    ptn_list2.append(ptn2)

	aminoacids = ['ALA','ILE','LEU','MET','VAL','PHE','TRP','TYR','ASN','CYS',
	              'GLN','SER','THR','ASP','GLU','ARG','HIS','LYS','GLY','PRO']

	for code in ptn_list:
	    print(f'\n\ncode = {code}')
	    SASA = "SASA_"+str(code)
	    SESA = "SESA_"+str(code)
	    if SASA in files:
	        
	        #SASA
	        SASA_file = var + '/' + SASA
	        with open(SASA_file, 'r') as filehandle1:
	            filecontent1 = filehandle1.read()
	            lista = filecontent1.split('\t')[1:]
	            
	            values1 = []
	            for i in range(len(lista)):
	                if i%2 != 0:
	                    lista[i].replace('\n','')
	                    values1.append(float(lista[i]))
	            array1 = np.array(values1)
	        
	        #SESA
	        SESA_file = var + '/' + SESA
	        with open(SESA_file, 'r') as filehandle2:
	            filecontent2 = filehandle2.read()
	            lista2 = filecontent2.split('\t')[1:]

	            values2 = []
	            for e in range(len(lista2)):
	                if e%2 != 0:
	                    lista2[e].replace('\n','')
	                    values2.append(float(lista2[e]))
	            array2 = np.array(values2)
	                    
	        print(f'array1 = {array1}')
	        print(f'array2 = {array2}')
	        realSASA = (array1/(array1 + array2))*100

	        #PDB
	        PDB_file = var + '/' + code.lower() + '.pdb.txt'
	        with open(PDB_file, 'r') as filePDBhandle:
	            filePDB = filePDBhandle.read()
	            lista3 = filePDB.split('<td><pre>')[4:]
	            
	            code_list = []
	            for element in lista3:
	                code2 = element[1:4]
	                if code2 in aminoacids:
	                    code_list.append(code2)
	            
	        with open(str(code)+'_chimera_SASA.txt', 'w') as fout:
	            fout.write('Residue' + '\t' + 'Ratio(%)' + '\n')

	            for i in range(len(code_list)):
	                if code == '6URP':
	                    print(f'realSASA = {realSASA}')
	                fout.write(code_list[i] + '\t' + str(realSASA[i]) + '\n')


if __name__ == "__main__":
	main()