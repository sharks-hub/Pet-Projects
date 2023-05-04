import openai

def get_genre():
    while True:
        genre = input("Enter song genre (country, pop, rap): ").lower()
        if genre in ["country", "pop", "rap"]:
            return genre
        else:
            print("Invalid genre. Please choose from country, pop, or rap.")

def get_keywords():
    keywords = []
    for i in range(3):
        keyword = input(f"Enter keyword {i + 1}: ")
        keywords.append(keyword)
    return keywords

def generate_lyrics(genre, keywords):
    prompt = f"Write a {genre} song with the following structure: opener, chorus, verse, chorus, close. The song should include these keywords: {', '.join(keywords)}.\n\n"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def main():
    genre = get_genre()
    keywords = get_keywords()
    lyrics = generate_lyrics(genre, keywords)
    print("\nGenerated song lyrics:\n")
    print(lyrics)

if __name__ == "__main__":
    main()
