def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	number_of_words = get_number_of_words(text)
	print(f"{number_of_words} words found in the document")

def get_book_text(path):
	with open(path) as f:
		return f.read()

def get_number_of_words(text):
	return len(text.split())

main()
