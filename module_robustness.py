# python3 

def change_nucleotide(dna_file, error_rate, error_type, dna_file_new) :
  # # input parameters
  # dna_file = "dna_sequences"
  # error_rate = 0.0001
  # error_rate = 0.003
  # # substitution, deletion, insertion, mix
  # error_type = "substitution"
  # error_type = "deletion"
  # error_type = "insertion"
  # error_type = "mix"

  # # output parameters
  # dna_file_new = "dna_sequences_new"

  import math
  import random

  n_base=0
  n_line=0
  lines = []
  m = []
  with open(dna_file, "r") as fp :
      lines = fp.read().splitlines()
  for l in lines :
      n_base += len(l)
      m.append(list(l))
  n_line = len(lines)
  n_b_line = len(lines[0])
  lines = []

  subs = {}
  subs["A"] = "TCG"
  subs["T"] = "ACG"
  subs["C"] = "ATG"
  subs["G"] = "ATC"
  s_ATCG = "ATCG"
  n_err_base = math.floor(n_base*error_rate)
  p_err_base = random.sample(range(1, n_base), n_err_base)
  p_err_base.sort(reverse=True)

  for p in p_err_base :
      p_line, p_base = divmod(p, n_b_line)
      if(error_type.lower() == "substitution") :
          b_original = m[p_line][p_base-1]
          b_new = subs[b_original.upper() ][ random.randint(0, 2)]
          m[p_line][p_base-1] = b_new
      elif(error_type.lower() == "deletion" ) :
          del m[p_line][p_base-1]
      elif(error_type.lower() == "insertion" ) :
          # random choice to insert before or after
          ins_c = random.randint(0, 1)
          m[p_line].insert( p_base-1+ins_c, s_ATCG[ random.randint(0, 3) ] )
      elif(error_type.lower() == "mix" ) :
          # random choice to substitution, deletion, insertion
          type_c = random.randint(0, 2)
          # substitution
          if(type_c==0) :
              b_original = m[p_line][p_base-1]
              b_new = subs[b_original.upper() ][ random.randint(0, 2)]
              m[p_line][p_base-1] = b_new
          # deletion
          elif(type_c==1) :
              del m[p_line][p_base-1]
          # insertion
          elif(type_c==2) :
              # random choice to insert before or after
              ins_c = random.randint(0, 1)
              m[p_line].insert( p_base-1+ins_c, s_ATCG[ random.randint(0, 3) ] )

  for l in m :
      lines.append( ''.join(l) )
  with open(dna_file_new, 'wt') as f2 :
      f2.write( '\n'.join(lines) )

  return [n_base, n_err_base]
