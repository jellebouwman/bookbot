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

def get_character_count_dict(text):
	lower_case_text = text.lower()
	character_count_dict = {}

	for char in lower_case_text:
		if char in character_count_dict:
			character_count_dict[char] += 1
		else:
			character_count_dict[char] = 1
	return character_count_dict

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

def print_report(book_path, word_count, sorted_char_dict):
	print(f"--- Begin report of {book_path} ---")
	print(f"{word_count} words found in the document \n")

	for char in sorted_char_dict:
		print(f"The '{char['char']}' character was found {char['count']} times")

	print(f"--- End report of {book_path} ---")


main()
