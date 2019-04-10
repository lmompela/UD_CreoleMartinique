import sys, re 

dico = {
'févriyé':'NOUN'
}

sent_idx = 1

def guess_tag(idx, s, dico):
	tag = '_'

	if s in "!\"'()+,./:?«»–—‘“”•…":
		return 'PUNCT'
	elif idx != 1 and s[0].isupper():
		return 'PROPN'
	elif re.match('^[0-9]+$', s):
		return 'NUM'
	elif s in dico:
		return dico[s]

	return tag

for line in sys.stdin.readlines():
# !"'()+,./:?«»–—‘“”•…  0123456789
	orig_line = line.strip('\n')
	for c in "!\"'()+,./:?«»–—‘“”•…":
		line = line.replace(c, ' ' + c + ' ')
		line = re.sub('  *', ' ', line)

	line = line.strip()

	print('# sent_id = %d' % sent_idx)
	print('# text = %s' % orig_line)
	idx = 0
	for tok in line.split(' '):
		idx += 1
		tag = guess_tag(idx, tok, dico)
		lemma = tok
		#       1    2    3    4    5   6     7    8    9    10
		row = (idx, tok, lemma, tag, tag, '_', '_', '_', '_', '_')
		print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % row)

	print('')
	sent_idx = sent_idx + 1
