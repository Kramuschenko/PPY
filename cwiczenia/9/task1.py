import wikipedia


def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


def get_article(title):
    try:
        page = wikipedia.page(title)
        return page.content
    except wikipedia.exceptions.PageError:
        return ""
    except wikipedia.exceptions.DisambiguationError:
        return ""


def calculate_average_letter_count():
    total_letter_count = 0
    article_count = 0

    title_generator = read_titles("small.txt")
    for title in title_generator:
        article = get_article(title)
        letter_count = len([char for char in article if char.isalpha()])
        total_letter_count += letter_count
        article_count += 1

    if article_count > 0:
        average_letter_count = total_letter_count / article_count
        return average_letter_count
    else:
        return 0


average_letters = calculate_average_letter_count()
print("Średnia liczba liter na artykuł:", average_letters)
