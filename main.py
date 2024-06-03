def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	number_of_words = get_number_of_words(text)
	print(f"{number_of_words} words found in the document")
	character_dict_count = get_character_count_dict(text)
	print(f"The character count dictionary is: {character_dict_count}")

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

main()
