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

def query(book, chapter):
	# get scripture
	scripture = get_scripture()

	# filter by book and chapter
	query = list(filter(lambda data: data['book'] == book and data['chapter'] == chapter, scripture))

	# concat the verses
	text = ''
	for q in query:
		text += '{}:{} {}\n'.format(q['chapter'], q['verse'], q['content'])

	return text

def main():
	print(query('Matt', 13))

if __name__ == '__main__':
	main()
