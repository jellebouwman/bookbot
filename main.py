def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	number_of_words = get_number_of_words(text)
	character_dict_count = get_character_count_dict(text)
	sorted_character_list = sort_character_dict(character_dict_count)

	print_report(book_path, number_of_words, sorted_character_list)

def get_book_text(path):
	with open(path) as f:
		return f.read()

def get_number_of_words(text):
	return len(text.split())

def test_get_number_of_words():
	assert get_number_of_words("some text with five words") == 5
	assert get_number_of_words("sometextwithnospaces") == 1
	assert get_number_of_words("") == 0

def get_character_count_dict(text):
	lower_case_text = text.lower()
	character_count_dict = {}

	for char in lower_case_text:
		if char in character_count_dict:
			character_count_dict[char] += 1
		else:
			character_count_dict[char] = 1
	return character_count_dict

def test_get_character_count_dict():
	assert get_character_count_dict("a") == {"a": 1}
	assert get_character_count_dict("aa") == {"a": 2}
	assert get_character_count_dict("ab") == {"a": 1, "b": 1}
	assert get_character_count_dict("aA") == {"a": 2}
	assert get_character_count_dict("aAa") == {"a": 3}
	assert get_character_count_dict("a b =") == {"a": 1, "b": 1, " ": 2, "=": 1}

# Refactors a dict of character keys and count values to a sorted
# list of dicts that contain keys for the character and counts
# also filters out non-alphabetic characters
def sort_character_dict(character_dict):
	character_count_list = []

	def sort_on(dict):
		return dict["count"]

	for char, count in character_dict.items():
		if char.isalpha():
			character_count_list.append({"char": char, "count": count})

	character_count_list.sort(reverse=True, key=sort_on)

	return character_count_list

def test_sort_character_dict():
	assert sort_character_dict({"a": 1}) == [{"char": "a", "count": 1}]
	assert sort_character_dict({"a": 2}) == [{"char": "a", "count": 2}]
	assert sort_character_dict({"a": 1, "b": 1}) == [{"char": "a", "count": 1}, {"char": "b", "count": 1}]
	assert sort_character_dict({" ": 1, "1": 1}) == []

# Prints a report of the books's word count and character count
def print_report(book_path, word_count, sorted_char_dict):
	print(f"--- Begin report of {book_path} ---")
	print(f"{word_count} words found in the document \n")

	for char in sorted_char_dict:
		print(f"The '{char['char']}' character was found {char['count']} times")

	print(f"--- End report of {book_path} ---")

def test_print_report():
	assert print_report("books/frankenstein.txt", 1, [{"char": "a", "count": 1}]) == None

main()
