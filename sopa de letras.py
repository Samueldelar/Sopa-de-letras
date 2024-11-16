import json

class WordSearch:
    def __init__(self, letter_soup, words):
        # Convertir la sopa de letras y las palabras a mayúsculas
        self.letter_soup = [[char.upper() for char in row] for row in letter_soup]
        self.words = [word.upper() for word in words]
        self.rows = len(self.letter_soup)
        self.cols = len(self.letter_soup[0])
    
    def search_word(self, word):
        directions = [
            (0, 1), (0, -1), (1, 0), (-1, 0), 
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        word_len = len(word)
        
        def check_direction(x, y, dx, dy):
            for i in range(word_len):
                nx, ny = x + i * dx, y + i * dy
                if nx < 0 or nx >= self.rows or ny < 0 or ny >= self.cols:
                    return False
                if self.letter_soup[nx][ny] != word[i]:
                    return False
            return True
        
        for x in range(self.rows):
            for y in range(self.cols):
                if self.letter_soup[x][y] == word[0]:
                    for dx, dy in directions:
                        if check_direction(x, y, dx, dy):
                            return {"word": word, "found": True, "position": (x, y), "direction": (dx, dy)}
        return {"word": word, "found": False}

    def search_words(self):
        results = {word: self.search_word(word)["found"] for word in self.words}
        return results

    def generate_report(self, output_path):
        results = self.search_words()
        with open(output_path, 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, indent=4, ensure_ascii=False)
        print(f"Reporte generado en '{output_path}'")

def load_soup_and_words(file_path):
    with open(file_path, 'r') as f:
        content = f.read().splitlines()
    separator_index = content.index('---')
    letter_soup = [list(line) for line in content[:separator_index]]
    words = [line.strip() for line in content[separator_index + 1:]]
    return letter_soup, words

def main():
    # Rutas ajustadas según tu estructura de carpetas
    file_path = './SOPA/sopa.txt'  # Ruta relativa para la carpeta SOPA
    output_path = './RESPUESTA/resultados.json'  # Ruta relativa para la carpeta RESPUESTA
    
    letter_soup, words = load_soup_and_words(file_path)
    word_search = WordSearch(letter_soup, words)
    word_search.generate_report(output_path)

if __name__ == "__main__":
    main()
