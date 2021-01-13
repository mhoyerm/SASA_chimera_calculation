# SASA_chimera_calculation.py
Python software which takes AreaSAS and AreaSES for amino acid residues TXT files, obtained by Chimera 1.14, and calculates a percentage solvent accessibility value for each residue in a protein. The output file was later used as input in percentage_proportion.py and percentage_exposition.py

The algorithm reads all files in a given folder, so input files must all be located in the same folder. 

TXT file of AreaSAS must be named as: "SASA_" + PDB ID code

TXT file of AreaSES must be named as: "SESA_" + PDB ID code

Usage:

<code>
python sasa_chimera_calculation.py "C:\path\"
</code>

# percentage_proportion.py
Algorithm which receives output files from SASA_chimera_calculation.py or GETAREA.pl (available on curie.utmb.edu/getarea.html), and calculates the percentage proportion of apolar, polar and charged amino acid residues in a protein.

Usage:

<code>
  python percentage_proportion.py "C:\path\" <output.txt>
  </code>

# percentage_exposition.py
Algorithm which receives output files from SASA_chimera_calculation.py or GETAREA.pl (available on curie.utmb.edu/getarea.html), and calculates the arithmetic mean of percentage exposition values of amino acid residues classified as apolar, polar and charged in a protein.

Usage:

<code>
  python percentage_exposition.py "C:\path\" <output.txt>
  </code>
  
# aminoacid_proportion.py
Algorithm which receives output files from SASA_chimera_calculation.py or GETAREA.pl (available on curie.utmb.edu/getarea.html), and calculates the percentage proportion of amino acid residues classified as short, long or neutro chain in a protein.

Usage:

<code>
  python percentage_proportion.py "C:\path\" <output.txt>
  </code>

# aminoacid_exposition.py
Algorithm which receives output files from SASA_chimera_calculation.py or GETAREA.pl (available on curie.utmb.edu/getarea.html), and calculates the arithmetic mean of percentage exposition values of amino acid residues classified as short, long or neutro chain in a protein.

Usage:

<code>
  python aminoacid_exposition.py "C:\path\" <output.txt>
  </code>

