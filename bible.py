def get_scripture():
	with open('static/dnstrunv', encoding='utf-8') as f:
		lines = f.readlines()

	scripture = []
	for line in lines:

		# parse a record
		sp = line.split('#')

		data = {}
		data['order'] = int(sp[0])
		data['book'] = sp[1].strip()
		data['chapter'] = int(sp[2])
		data['verse'] = int(sp[3])
		data['content'] = sp[4]

		# save
		scripture.append(data)

	# sort
	scripture = sorted(scripture, key=lambda data: data['order'])

	return scripture

def main():
	scripture = get_scripture()

	for s in scripture[:50]:
		print(s)

if __name__ == '__main__':
	main()
