import sys
import statistics

classifica = {'GLY':'Neutro','ALA':'Neutro','VAL':'Neutro','CYS':'Short','PRO':'Neutro',
		'LEU':'Neutro','ILE':'Neutro','MET':'Neutro','TRP':'Neutro','PHE':'Neutro',
		'SER':'Short','THR':'Long','TYR':'Long','ASN':'Short','GLN':'Long',
		'LYS':'Long','ARG':'Long','HIS':'Long','ASP':'Short','GLU':'Long'}

def classification(lista):
	short = 0
	longo = 0
	neutro = 0
	for name in lista:
		if name[0] in classifica:
			if dict.get(classifica,name[0]) == 'Short':
				short += 1
			elif dict.get(classifica,name[0]) == 'Long':
				longo += 1
			elif dict.get(classifica,name[0]) == 'Neutro':
				neutro += 1
	total = short + longo + neutro
	percent_short = (short/total)*100
	percent_long = (longo/total)*100
	percent_neutro = (neutro/total)*100
	return 'percent' + '\t' + str(percent_short) + '\t' + str(percent_long) + '\n'

def media(lista):
	short_values = []
	long_values = []
	neutro_values = []
	for name in lista:
		if name[0] in classifica:
			if dict.get(classifica,name[0]) == 'Short':
				short_values.append(float(name[6]))
			elif dict.get(classifica,name[0]) == 'Long':
				long_values.append(float(name[6]))
			elif dict.get(classifica,name[0]) == 'Neutro':
				neutro_values.append(float(name[6]))
	
	media_short = statistics.mean(short_values)
	media_long = statistics.mean(long_values)
	media_neutro = statistics.mean(neutro_values)  
	return 'media in/out' + '\t' + str(media_short) + '\t' + str(media_long) + '\n'

#main function
def main():

	filein = sys.argv[1] #input file name
	fileout = sys.argv[2] #output root file name

	#read the file's contents
	fin = open(filein, 'r')
	contents = fin.read()
	text = contents.split('</pre></td>\n<td><pre>')[2:]

	#open output file
	fout = open(fileout, 'w')

	lines = []
	for element in text:
		line = element.split(' ')
		lines.append(line)
		
	full = []
	for lista in lines:
		n = []
		for i in range(len(lista)):
			if lista[i] != '':
				n.append(lista[i])
		full.append(n)

	fout.write('Classification'+'\t'+'Short chain'+'\t'+'Long chain'+'\n')
	fout.write(classification(full))
	fout.write(media(full))

if __name__ == "__main__":
	main()