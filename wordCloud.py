#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

import os

from os import path
from wordcloud import WordCloud
from glob import glob

import matplotlib.pyplot as plt

os.system('clear')

ROOT = os.getcwd()
WORDS = {'word':0}
TOTAL_TEXT = ""

def readFolder(foldername):
	os.chdir(ROOT+'/'+foldername)
	# print glob(os.getcwd()+'/*')
	for file in glob(os.getcwd()+'/*'):
		readfile(file)
	pass

def readfile(filename):
	global TOTAL_TEXT
	# print 'readline: '+filename
	with open(filename) as fp:
		line = fp.readline()
		symbols_arr = [
		'Sao',
		'Paulo',
		'Campinas',
		'Indeed']
		while line:
			ln = line.split()
			for wd in ln:
				for sb in symbols_arr:
					wd = wd.replace(sb,'')
				if not wd in WORDS:
					WORDS.update({wd:1})
				else:
					WORDS[wd]+=1
				TOTAL_TEXT+=" "+str(wd)
			line = fp.readline()
		fp.close()
	pass

if __name__ == "__main__":
	print 'Welcome to Word cloud!'
	readFolder('./messages')

	t = TOTAL_TEXT

	wordcloud = WordCloud(max_words=50,height=1200,width=2000, min_font_size=10, background_color="white").generate(t)

	plt.axis("on")
	# plt.imshow(wordcloud, interpolation="bilinear")
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")

	os.chdir(ROOT)
	plt.savefig('wordcloud-output.png', dpi=200, facecolor='w', edgecolor='w', format='png')


	plt.show()