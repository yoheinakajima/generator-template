from PIL import Image
import csv

pixelbeasts = []


while j < 10000:


	# generate random integer values
	pixelbeast=[]
	import random
	from random import choice

	# prepare a sequence, this example uses same rarity for every attribute, but you can change this up here
	beasts = [i for i in range(41)]
	beast = choice(beasts)

	shirts = [i for i in range(31)]
	shirt = choice(shirts)

	hats = [i for i in range(29)]
	hat = choice(hats)

	eyes = [i for i in range(10)]
	eye = choice(eyes)

	necklaces = [i for i in range(2)]
	neck = choice(necklaces)

	#you can put rules in here, such as "if cardinal, remove eyepatch" (because the combo didn't look good)
	if eyes == 2:
		if beast == 3:
			eyes = 0


	#combination defines the new pixelbeast
	pixelbeast = [beast,shirt,necklace,hat,eyes]
	

	# check if pixelbeast is unique
	exists = pixelbeast in pixelbeasts
	
	if exists:
		#if not unique, skip creating beast. skip adding +1 to j, add +1 to k instead.
		print("DUPLICATE!")
		print(exists)
		k+=1
	else:
		print(pixelbeast)
		pixelbeasts.append(pixelbeast)


		#attributes are saved in a img folder using the schema [attribute]#.png
		layer1 = Image.open("img/beast"+str(beast)+".png")
		layer2 = Image.open("img/eye"+str(eyes)+".png")
		layer3 = Image.open("img/shirt"+str(shirt)+".png")
		layer4 = Image.open("img/necklace"+str(necklace)+".png")
		layer5 = Image.open("img/hat"+str(hat)+".png")
		layer6 = Image.open("img/background1.png")


		#set up new image
		final = Image.new("RGBA", layer1.size)
		final = Image.alpha_composite(final, layer1)
		final = Image.alpha_composite(final, layer2)
		final = Image.alpha_composite(final, layer3)
		final = Image.alpha_composite(final, layer4)
		#create name
		if j+1 <10:
			beastnumber = "#000"+str(j+1)
		if j+1 > 9:
			beastnumber = "#00"+str(j+1)
		if j+1 > 99:
			beastnumber = "#0"+str(j+1)
		if j+1 > 999:
			beastnumber = "#"+str(j+1)


		#save a version without background, and then a version with background.

		final2 = Image.alpha_composite(final, layer5).save("nobg/"+beastnumber+".png")
		final3 = Image.alpha_composite(final, layer5)
		final4 = Image.alpha_composite(layer6, final3).save("background/"+beastnumber+".png")



#print results in terminal
print(pixelbeasts)
x = len(pixelbeasts)
print(x)
print(k)

#print results in csv
out=open("result.csv","w")
output=csv.writer(out)
for row in pixelbeasts:
	output.writerow(row)

out.close()
