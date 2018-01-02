from bitarray import bitarray

import mmh3

class BloomFilter(set):
	def __init__(self, size, hash_count):
		# super(BloomFilter, self).__init__()
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
		self.size = size
		self.hash_count = hash_count
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		return iter(self.bit_array)
	
	def add(self, item):
		for i in range(self.hash_count):
			index = mmh3.hash(item, i) % self.size
			self.bit_array[index] = 1
		return self
	
	def __contains__(self, item):
		out = True
		for i in range(self.hash_count):
			index = mmh3.hash(item, i) % self.size
			if self.bit_array[index] == 0:
				return False
		
		return out
	
def main():
	bloom = BloomFilter(100, 10)
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
