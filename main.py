import os
import random

# global variables so they can be accessed by both methods
east_species_list = []
west_species_list = []

# open a new similarity file which will hold all the similarity percentages for all the species compared. This is so that we don't have to check each species-combo percentage and is for ease of viewing to compare results.
similarity_file = open("C:\\Users\\maddy\\OneDrive\\UW Classes\\Sophmore Year\\Quarter 3\\CSS 383\\Project 1 Update\\similarity_results.csv", "w")

def species_comparison(first_species, second_species):
  # have the global variable so that it runs on windows/linux
  os.putenv("BLASTDB_LMDB_MAP_SIZE", "1000000")

  # invoke the makeblastdb so that you can run commands through the .exe using BLAST
  firstCommand = "makeblastdb -in {subject_fasta_file} -input_type fasta -dbtype nucl"

  # specify the file name to use in the command statement using .format
  firstCommand = firstCommand.format(subject_fasta_file = first_species)

  # sends the first command, to invoke BLAST and to use its features, to the system
  os.system(firstCommand)

  # command that will be sent to the system to get output results for
  output = "blastn -query {query_fasta_file} -subject {subject_fasta_file} -task blastn -max_hsps 2 -outfmt 6 >> {species_one}_{species_two}_results.txt"

  # made an array to store all elements of the file name, so i can use part of it for the output file name, to make it easier to keep track when we do analysis of different comparisons.
  species_name_array = first_species.split("_")
  species_one_name = ""

  # if/else statement for including the genuine cases where 2 species breed and there one species x another species, then the size of array is always 7, so checks for that and includes those case, else prints the regular name of the species, removing .fa.
  if(len(species_name_array) == 7):
    species_one_name += (species_name_array[3].rstrip('.fa') + "_" + species_name_array[4].upper() + "_" + species_name_array[6].rstrip('.fa'))
  elif(len(species_name_array) == 4):
    species_one_name += (species_name_array[3].rstrip('.fa'))

  # if/else statement for including the genuine cases where 2 species breed and there one species x another species, then the size of array is always 7, so checks for that and includes those case, else prints the regular name of the species, removing .fa.
  species_two_array = second_species.split("_")
  species_two_name = ""
  if(len(species_two_array) == 7):
    species_two_name += (species_two_array[3].rstrip('.fa') + "_" + species_two_array[4].upper() + "_" + species_two_array[6].rstrip('.fa'))
  elif(len(species_two_array) == 4):
    species_two_name += (species_two_array[3].rstrip('.fa'))

  # put the appropriate values of the 
  output = output.format(query_fasta_file = first_species, subject_fasta_file = second_species, species_one = species_one_name, species_two = species_two_name)

  # prints the output just to make sure the correct files are being compared and the correct syntax is sent to the system for results
#  print(output)

  # execute the statement above to get the actual results
  os.system(output)

  results_file = "{species_one}_{species_two}_results.txt"
  results_file = results_file.format(species_one = species_one_name, species_two = species_two_name)  

  similarity = 0.0

  # open the txt file, send the content to an array so that we can save the percentage and then write it to the txt file so that we can save the percentages only for ease of viewing results.
  file_to_parse = open(results_file, "r+") 
  line = file_to_parse.readline().split("\t")
#  print(line)
  similarity = line[2]
  # sends the similarity percentage to a .txt file so that we can only see the percentage similarities for all the different types of species combinations compared.
  similarity_file.write(results_file + " , " + similarity + "\n")


def main():
  #this path represents the location where all the FASTA files
  #are located. Then, we list all the files in the directory
  #using the listdir function. 
  path = 'C:\\Users\\maddy\\OneDrive\\UW Classes\\Sophmore Year\\Quarter 3\\CSS 383\\Project 1 Update\\FASTA Files\\'
  allFiles = os.listdir(path)

  # runs through all the 17 files and organizes them according eastern or western species
  for each in allFiles:
    if ("brevirostrum" in each or "mediro" in each or "oxyri" in each or "trans" in each):
      west_species_list.append(each)
    else:
      east_species_list.append(each)

  # make sure both the hemispheres species are stored into the correct arrays
  print(east_species_list)
  print(west_species_list)
          
  print()

  # changed the directory to make sure we are putting the output files in the correct place. May be required based on particular systems the code in run on.
  os.chdir("C:\\Users\\maddy\\OneDrive\\UW Classes\\Sophmore Year\\Quarter 3\\CSS 383\\Project 1 Update")

  # within western species comparison
  similarity_file.write("Western species comparison results: \n\n")
  # do 100 tests to include all the unique possible combinations of species
  for i in range(100):
    species_one = random.choice(west_species_list)
    species_two = random.choice(west_species_list)

    # specify the first and second species that will be compared
    if (species_one == species_two):
      while(species_one == species_two):
        species_one = random.choice(west_species_list)
        species_two = random.choice(west_species_list)

    # call the method to find similarity results between the 2 species
    species_comparison(species_one, species_two)

  # within eastern species comparison
  # similarity_file.write("Eastern species comparison results: \n\n")
  # # do 600 tests to include all the unique possible combinations of species
  # for j in range(600):
  #   species_one = random.choice(east_species_list)
  #   species_two = random.choice(east_species_list)

  #   # specify the first and second species that will be compared
  #   if (species_one == species_two):
  #     while(species_one == species_two):
  #       species_one = random.choice(east_species_list)
  #       species_two = random.choice(east_species_list)

  #   species_comparison(species_one, species_two)

  # between both hemispheres comparison
  # similarity_file.write("Between Hemispheres species comparison results: \n\n")
  # do 600 tests to include all the unique possible combinations of species
  # for k in range(600):
  #   species_one = random.choice(east_species_list)
  #   species_two = random.choice(west_species_list)

  #   # specify the first and second species that will be compared
  #   if (species_one == species_two):
  #     while(species_one == species_two):
  #       species_one = random.choice(west_species_list)
  #       species_two = random.choice(west_species_list)

  #   species_comparison(species_one, species_two)

main()