from Bio import Entrez, SeqIO
import pandas as pd
import time

Entrez.email = "A.N.Other@example.com"

species_df = pd.read_csv("species.csv")
genes_df = pd.read_csv("genes.csv")
output = "genes.fasta"

with open(output, "w") as out_fasta:
    for species in species_df["species"]:
        for gene in genes_df["gene"]:

            query = f'{gene}[Gene] AND {species}[Organism] AND mRNA'
            try:
                search = Entrez.esearch(db="nucleotide",term=query,retmax=1)
                search_results = Entrez.read(search)
                search.close()

                id_list = search_results["IdList"]

                if not id_list:
                    print(f"No result for {gene} in {species}")
                    continue

                seq_id = id_list[0]

                stream = Entrez.efetch(db="nucleotide", id=seq_id, rettype="fasta", retmode="text")

                sequence = stream.read()
                stream.close()

                out_fasta.write(sequence)

                print(f"Downloaded {gene} from {species}")
                time.sleep(0.5)
            
            except Exception as e:
                print(f"Error with {gene} {species}: {e}")


# In the terminal, in the correct folder:
# python -m venv venv
# pip install biopython pandas
# python scripts/downlaod_sequence.py
