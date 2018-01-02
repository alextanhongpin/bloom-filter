from bitarray import bitarray

import mmh3
import math

class BloomFilter(set):
	def __init__(self, n = 10**6, p = 0.01):
		# super(BloomFilter, self).__init__()
		# m = size of bit array
		# n = expected number of items
		# p = probability percentage represented as decimal
		k, m = self.optimal_km(n, p)
		self.size = m
		self.bit_array = bitarray(m)
		self.bit_array.setall(0)
		self.hash_count = k
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		return iter(self.bit_array)
	
	def add(self, item):
		for i in range(self.hash_count):
			index = mmh3.hash(item, i) % self.size
			self.bit_array[index] = 1
		return self
	
	def optimal_km(self, n = 10**6, p = 0.01):
		'''Returns the optimal values for:
			k = number of hashes
			m = size of bit array
		given 
			n = size of the items 
			p = probability percentage represented as decimal
		'''
		ln2 = math.log(2)
		lnp = math.log(p)
		k = -lnp/ln2
		m = -n*lnp/((ln2)**2)
		return int(math.ceil(k)), int(math.ceil(m))
	
	def __contains__(self, item):
		out = True
		for i in range(self.hash_count):
			index = mmh3.hash(item, i) % self.size
			if self.bit_array[index] == 0:
				return False
		
		return out
	
def main():
	bloom = BloomFilter()
	animals = ['dog', 'cat', 'giraffe']
	for animal in animals:
		bloom.add(animal)
	
	for animal in animals:
		if animal in bloom:
			print('{} is in bloom filter as expected'.format(animal))
		else:
			print('False negative for {}'.format(animal))
		
	for other in ['paper', 'food']:
		if other in bloom:
			print('{} is in bloom, but false positive'.format(other))
		else:
			print('{} is not in bloom'.format(other))

	pass

if __name__ == '__main__':
	main()
