# -*- coding: utf-8 -*-

class Preprocess:
	@staticmethod
	def cleanFile(csvFile):
		with open(csvFile) as infile, open(csvFile + '.cleaned', 'w') as outfile:
			for line in infile:
				new_line = ''
				for attribute in line.split(','):
					if (attribute == ''):
						attribute = '0'
					new_line += str(attribute + ',')
				if (new_line[len(new_line) - 1] == ','):
					new_line = new_line[:-1]
				outfile.write(new_line)
			infile.close()
			outfile.close()
