from docx import Document
import json
import re

# Открываем загруженный документ
doc_path = "./input/quiz-3.docx"
document = Document(doc_path)

data = []
question = None
answers = []

question_pattern = re.compile(r'^\d+\.\s?')
question_pattern_2 = re.compile(r'^\?\?.\s?')
answer_list_pattern = re.compile(r'^[а-яА-Я]\)\s?')

# Парсинг документа
for paragraph in document.paragraphs:
    text = paragraph.text.strip()

    # Если текст пустой, пропускаем
    if not text:
        continue

    # Проверяем, если это начало нового вопроса
    if question_pattern_2.match(text) or question_pattern.match(text):
        # Если текущий вопрос уже был, добавляем его в данные
        if question and answers:
            data.append({"question": question, "answers": answers})
            answers = []

        # Начинаем новый вопрос
        # Удаляем номер вопроса из текста
        text = question_pattern.sub("", text)
        text = question_pattern_2.sub("", text)
        question = text
    else:
        # Определяем правильный ответ (если выделен жирным)
        correct = any(run.bold for run in paragraph.runs)
        # Удаляем нумерацию из вопроса
        text = answer_list_pattern.sub("", text)
        answers.append({"text": text, "correct": correct})

# Добавляем последний вопрос, если он не был добавлен
if question and answers:
    data.append({"question": question, "answers": answers})

# Генерация JSON
json_output = json.dumps(data, ensure_ascii=False, indent=4)

# Сохраняем JSON в файл
output_path = "./output/quiz.json"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(json_output)