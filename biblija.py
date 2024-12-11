import os
from bs4 import BeautifulSoup

def extract_text_from_html(file_path, output_path):
    try:
        # Учитавање HTML датотеке
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Парсирање HTML-а
        soup = BeautifulSoup(html_content, 'html.parser')

        # Проналажење <div> елемента са ID-јем 'textBody'
        text_body = soup.find('div', id='textBody')

        if text_body:
            # Извлачење чистог текста
            extracted_text = text_body.get_text(separator='\n').strip()

            # Чување текста у .txt датотеку
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(extracted_text)

            return f"Текст је успешно извучен и сачуван у: {output_path}"
        else:
            return f"Елемент са ID-јем 'textBody' није пронађен у датотеци {file_path}."

    except Exception as e:
        return f"Дошло је до грешке са датотеком {file_path}: {e}"

def process_all_html_files(input_dir, output_dir):
    try:
        # Обилазак свих датотека у датом директоријуму
        for root, _, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.htm') or file.endswith('.html'):
                    input_file_path = os.path.join(root, file)

                    # Креирање путање за излазну датотеку
                    relative_path = os.path.relpath(root, input_dir)
                    output_folder = os.path.join(output_dir, relative_path)
                    os.makedirs(output_folder, exist_ok=True)
                    output_file_path = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.txt")

                    # Обрада HTML датотеке
                    result = extract_text_from_html(input_file_path, output_file_path)
                    print(result)

    except Exception as e:
        print(f"Дошло је до грешке током обраде: {e}")

# Пример употребе
input_directory = '.'  # Замените са стварном путањом
output_directory = '.'  # Замените са стварном путањом
process_all_html_files(input_directory, output_directory)
