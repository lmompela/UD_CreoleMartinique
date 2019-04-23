# USAGE: python3 not-to-release/automate-tagging.py gcf_dep-ud-test.conllu < gcf_dep-ud-test.conllu 

import sys, re

dico = {}
freq = {}

if len(sys.argv) < 1: 
	print('USAGE: python3 not-to-release/automate-tagging.py gcf_dep-ud-test.conllu < gcf_dep-ud-test.conllu')
	sys.exit(-1)

for line in open(sys.argv[1]).readlines():
	if line.strip() == '':
		continue
	if line[0] == '#': 
		continue
	row = line.split('\t')
	form = row[1]
	tag = row[4]

	if tag == '_':
		continue
	
	if form not in dico:
		dico[form] = {}
	if tag not in dico[form]:
		dico[form][tag] = 0	
		freq[form] = (0, 'X')

	dico[form][tag] += 1

	if dico[form][tag] >= freq[form][0]:
		freq[form] = (dico[form][tag], tag)

for line in sys.stdin.readlines():
	line = line.strip('\n')
	if line == '':
		print()
		continue
	if line[0] == '#':
		print(line)
		continue

	row = line.split('\t')
	form = row[1]
	if form in freq and row[3] == '_':
		row[9] = 'GuessedTag=' + freq[form][1] + ',' + str(freq[form][0])

	print('\t'.join(row))

