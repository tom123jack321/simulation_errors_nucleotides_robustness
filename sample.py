# new DNA files are saved in "new_dna"

import os
from module_robustness import change_nucleotide

error_rates = [0.1, 0.2, 0.3]
error_types = ["substitution", "deletion", "insertion", "mix"]
original_files = ["dna_1", "dna_2"]

if __name__ == "__main__":
 for input_file in original_files :
   for error_rate in error_rates :
    for error_type in error_types :
      dna_new = "new_dna/" + input_file + "_new" +"_"+ str(error_rate) +"_"+ str(error_type)
      n_base, n_err_base = change_nucleotide(input_file, error_rate, error_type, dna_new)
