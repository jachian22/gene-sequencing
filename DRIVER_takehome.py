class GeneReader(object):

	def __init__(self):
		self.fragIDs = None
		self.fileName = None
		self.fragList = []
		self.chromosome = None

	def fastaReader(self, fileName):
		'''
		Reads in fasta-formatted files.

		INPUT: fileName (str)
		'''
		try:
			with open(fileName, 'r') as f:
				fragments = map(lambda x: x.strip('\r\n'), f.read().split('>')[1:])
			self.fragIDs = map(lambda x: x.split('\r\n', 1)[0], fragments)
			fragmentList = map(lambda x: x.split('\r\n', 1)[1], fragments)
			self.fragList = map(lambda x: ''.join(x.split('\r\n')), fragmentList)
		except:
			raise Exception('Wrong file type. You dun goofed!')

	def combineFrags(self, fragA, fragB):
		'''
		Takes two DNA sequence fragments and combines them by their overlapping
		sequences. NOTE: Will only combine if more than half the sequence matches.

		INPUT: fragA (str), fragB (str)
		OUTPUT: combinedFragment (str) or None
		'''
		larger = max(fragA, fragB)
		smaller = min(fragA, fragB)
		lenL = len(larger)
		lenS = len(smaller)

		streak1 = 0
		streak2 = 0
		for i, val in enumerate(smaller):
			if smaller[:i+1] == larger[-i-1:]:
				streak1 = max(streak1, i+1)
			if larger[:i+1] == smaller[-i-1:]:
				streak2 = max(streak2, i+1)

		if streak1 > lenS / 2:
			return larger + smaller[streak1:]
		elif streak2 > lenS / 2:
			return smaller + larger[streak2:]

	def setCombinedFrag(self, fragmentList):
		'''
		Takes a list of sequence fragments and finds the chromosome associated
		with the list of fragments in the file.

		INPUT: fragmentList (list)
		'''
		combinations = []
		usedFragments = set()
		currentFragment = None

		for i in xrange(len(fragmentList)):
			if currentFragment == None:
				usedFragments.add(i)
				currentFragment = fragmentList[i]
			if i in usedFragments: continue
			for j in xrange(i+1, len(fragmentList)):
				if j in usedFragments: continue
				joined = self.combineFrags(currentFragment, fragmentList[j])
				if joined != None:
					currentFragment = joined
					usedFragments.add(j)
			combinations.append(currentFragment)
			currentFragment = None

		if len(combinations) == 0:
			raise Exception('Fragments did not join correctly!')
		elif len(combinations) == 1:
			self.chromosome = combinations[0]
		else:
			self.setCombinedFrag(combinations)

	def setSequence(self, fileName):
		'''
		Takes a fasta-formatted file and finds the chromosome associated with
		the list of fragments in the file.

		INPUT: fileName (str)
		'''
		self.fastaReader(fileName)
		self.setCombinedFrag(self.fragList)

	def getSequence(self):
		'''
		Returns back the combined chromosome from the file.
		'''
		return self.chromosome

	def getFragIDs(self):
		'''
		Returns back the fragment IDs associated with the combined chromosome.
		'''
		return 'Sequence from: \n' + '\n'.join(self.fragIDs)

if __name__ == '__main__':
	genes = GeneReader()
	genes.setSequence('coding_challenge_data_set.txt')
	# print genes.getFragIDs()
	print genes.getSequence()