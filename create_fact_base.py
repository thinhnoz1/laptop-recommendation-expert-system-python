import csv
import json

csvfile = open("laptops.csv", newline='')
reader = csv.DictReader(csvfile)
i =0

laptop_list = []

with open('facts.json', 'w') as outfile:
	for row in reader:
		row['id'] = i
		i = i+1
		row['comments'] = row['comments'].replace('\n',' ')
		id = int(row['id'])
		brand = str(row['brand'])
		model = str(row['model'])
		ram = int(row['ram'])
		hd_type = str(row['hd_type'])
		hd_size = int(row['hd_size'])
		screen_size = float(row['screen_size'])
		price = int(row['price'])
		processor_brand = str(row['processor_brand'])
		processor_model = str(row['processor_model'])

		clock_speed = 0.0
		if row['clock_speed']:
			clock_speed = float(row['clock_speed'])
		
		graphic_card_brand = "0"
		if row['graphic_card_brand']:
			graphic_card_brand = str(row['graphic_card_brand'])
		
		graphic_card_size = 0
		if row['graphic_card_size']:
			graphic_card_size = int(row['graphic_card_size'])
		
		os = str(row['os'])

		weight = 0.0
		if row['weight']:
			weight = float(row['weight'])

		comments = str(row['comments'])

		laptop_list.append({"id": id, "brand": brand, "model": model, "ram": ram,
							"hd_type": hd_type, "hd_size": hd_size, "screen_size": screen_size,
							"price": price, "processor_brand": processor_brand,
							"processor_model": processor_model, "clock_speed": clock_speed,
							"graphic_card_brand": graphic_card_brand, "graphic_card_size": graphic_card_size,
							"os": os, "weight": weight, "comments": comments })
	
	json.dump(laptop_list, outfile)