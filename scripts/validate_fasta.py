from Bio import SeqIO

fasta_file = "genes.fasta"
valid_bases = set("ATGCN")
total_sequences = 0

print("Validating FASTA file...")

for record in SeqIO.parse(fasta_file, "fasta"):
    total_sequences += 1
    sequence = str(record.seq).upper()
    invalid = set(sequence) - valid_bases

    print(f"ID: {record.id}")
    print(f"length: {len(sequence)}")

    if len(sequence) == 0:
        print("Sequence is empty.")

    if invalid:
        print(f"Invalid sequence: {invalid}")

print(f"\n Total sequences: {total_sequences}")
print(f"\n Validation completed.")
