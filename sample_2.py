import os
from module_robustness import change_nucleotide

error_rates = [0.1, 0.2, 0.3]
error_types = ["substitution", "deletion", "insertion", "mix"]
original_files = ["dna_1", "dna_2"]
# the number of tests for each file at every error rate every error type
number_tests = 100
robustness_log = "robustness.txt"

fh_rob = open(robustness_log, "wt")
s_dict = {}
s_dict["substitution"] = "substituted"
s_dict["deletion"] = "deleted"
s_dict["insertion"] = "inserted"
s_dict["mix"] = "substituted, deleted or inserted"
if __name__ == "__main__":
 for input_file in original_files :
   dna_new = "new_dna/" + input_file + "_new"
   for error_rate in error_rates :
    for error_type in error_types :
      n_test = 0
      n_success = 0
      while( n_test < number_tests ) :
        if(os.path.isfile(dna_new)) : os.remove(dna_new)
        n_base, n_err_base = change_nucleotide(input_file, error_rate, error_type, dna_new)
        # ===============================================================
        # Put some test codes here
        # ===============================================================
        n_test += 1
        ###################### end while #################################
      success_rate = n_success/number_tests
      fh_rob.write("Error rate: "+str(error_rate) +"\n")
      fh_rob.write("Error type: "+str(error_type) +"\n")
      fh_rob.write("The number of tests: "+str(number_tests) +"\n")
      fh_rob.write("The number of successful recoveries: "+str(n_success) +"\n")
      fh_rob.write("Success rate: "+str(success_rate) +"\n")
      fh_rob.write("Tested file: "+str(input_file) +"\n")
      fh_rob.write("The number of nucleotides in each test: " + str(n_base) +"\n")
      fh_rob.write("The number of nucleotides " + s_dict[error_type] + " in each test: " + str(n_err_base) +"\n")
      fh_rob.write("\n")
