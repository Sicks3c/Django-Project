from django.http import HttpResponse
from django.shortcuts import render
import re

def home(request):
	return render (request, 'home.html')

def translate(request):
	translation = ''
	original = request.GET['originaltext'].lower()
	for word in original.split():
		if re.match(r'[aeiou]', word[0]):
			# Vowel
			translation += word + 'yay '

		else:
			#"cheers" = "heerscay"
			# heers
			translation += word[1:]
			# C
			translation += word[0]
			# Ay
			translation += 'ay '
			# constant

	return render (request, 'translate.html',{'original': original, 'translation': translation})

def about(request):
	return render (request, 'about.html')





