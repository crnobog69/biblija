import os

def latin_to_cyrillic(text):
    """
    Converts Serbian text from Latin to Cyrillic script.
    """
    # Definisanje mapa za zamenu slova
    latin_to_cyrillic_map = {
        'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 
        'đ': 'ђ', 'e': 'е', 'ž': 'ж', 'z': 'з', 'i': 'и', 
        'j': 'ј', 'k': 'к', 'l': 'л', 'lj': 'љ', 'm': 'м', 
        'n': 'н', 'nj': 'њ', 'o': 'о', 'p': 'п', 'r': 'р', 
        's': 'с', 't': 'т', 'ć': 'ћ', 'u': 'у', 'f': 'ф', 
        'h': 'х', 'c': 'ц', 'č': 'ч', 'dž': 'џ', 'š': 'ш'
    }

    # Specijalni digrafski karakteri imaju prednost
    special_digraphs = ['lj', 'nj', 'dž']
    
    result = []
    i = 0
    while i < len(text):
        # Provera specijalnih digrafskih karaktera
        found_digraph = False
        for digraph in special_digraphs:
            if text[i:].startswith(digraph):
                result.append(latin_to_cyrillic_map[digraph])
                i += len(digraph)
                found_digraph = True
                break
        
        if not found_digraph:
            # Konverzija običnih slova
            char = text[i].lower()
            if char in latin_to_cyrillic_map:
                # Zadržavanje originalne kapitalizacije
                converted_char = latin_to_cyrillic_map[char]
                result.append(converted_char.upper() if text[i].isupper() else converted_char)
            else:
                # Zadržavanje originalnih karaktera koji nisu slova
                result.append(text[i])
            i += 1

    return ''.join(result)

def convert_files_in_directory(input_dir, output_dir):
    """
    Конвертује текстуалне датотеке из латинице у ћирилицу у целом директоријуму.
    """
    # Креирање излазног директоријума ако не постоји
    os.makedirs(output_dir, exist_ok=True)

    # Обилазак свих датотека у улазном директоријуму
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.txt'):
                # Пуна путања улазне и излазне датотеке
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                output_folder = os.path.join(output_dir, relative_path)
                os.makedirs(output_folder, exist_ok=True)
                output_file_path = os.path.join(output_folder, file)

                # Читање и конвертовање садржаја датотеке
                try:
                    with open(input_file_path, 'r', encoding='utf-8') as input_file:
                        text = input_file.read()
                    
                    cyrillic_text = latin_to_cyrillic(text)

                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(cyrillic_text)
                    
                    print(f"Конвертована датотека: {input_file_path} -> {output_file_path}")

                except Exception as e:
                    print(f"Грешка при конвертовању датотеке {input_file_path}: {e}")

# Пример употребе
if __name__ == "__main__":
    input_directory = '.'  # Заменити са стварном путањом улазног директоријума
    output_directory = '.'  # Заменити са стварном путањом излазног директоријума
    convert_files_in_directory(input_directory, output_directory)