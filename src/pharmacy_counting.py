from collections import defaultdict
import sys

soc_list = []
status_list = []
state_list = []
inputs = None

def main():

	#initialize path
	if len(sys.argv) < 3:
  		sys.exit(1) 
	input_file = sys.argv[1]
	output_file = sys.argv[2]
	# input_file = '../input/itcont.txt'
	# output_file = '../output/top_cost_drug.txt'
	
	# Initialize container to store drug and prescriber info.
	drug_total_dict = defaultdict(list)
	prescriber_memo = defaultdict(set)

	# read file to inputs
	with open(input_file,'r') as f:
		label = f.readline().strip('\n').split(';')
		inputs = f.readlines()

	# process data and save into dict
	for i in inputs:
		content = i.strip('\n').split(',')
		name = (content[1]+content[2]).lower()
		drug_name = content[3]
		drug_cost = int(content[4])
		if len(drug_total_dict[drug_name]) != 0 :
			drug_total_dict[drug_name][0] += drug_cost
			if name not in prescriber_memo[drug_name]:
				prescriber_memo[drug_name].add(name)
				drug_total_dict[drug_name][1] += 1
		else:
			drug_total_dict[drug_name] = [drug_cost,1]
			prescriber_memo[drug_name].add(name)
	f.close()

	# write into file
	file = open(output_file,'w')
	file.write("drug_name,num_prescriber,total_cost\n")
	for key,value in sorted(drug_total_dict.items(),key = lambda x:(x[1][0]*(-1),x[0])):
		line = ','.join([key, str(value[1]), str(value[0])])
		file.write(line+'\n')

	file.close()
		
if __name__=='__main__':
	main()
