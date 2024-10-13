import json
import csv

def main():
    # Путь к JSON файлу
    json_file = './output/quiz.json'
    # Путь к выходному CSV файлу
    csv_file = './output/quiz.csv'

    # Чтение JSON файла
    with open(json_file, 'r', encoding='utf-8') as f:
        questions = json.load(f)

    # Открытие CSV файла для записи
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Создаем CSV writer с правильным экранированием
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

        # Запись строки настроек (если требуется)
        csv_writer.writerow(['settings', 'Тестирование', '', '40', 'minutes', '', '10', '80.0', '10.0', '', '', 'rand', '', '200.0'])

        # Обработка каждого вопроса
        for idx, question_item in enumerate(questions, start=1):
            question_text = question_item['question']
            answers = question_item['answers']

            # Определяем тип вопроса
            correct_answers_count = sum(1 for answer in answers if answer['correct'])
            question_type = 'single_choice' if correct_answers_count == 1 else 'multiple_choice'

            # Запись строки вопроса
            question_row = [
                'question',
                question_text,
                '',
                question_type,
                '1.00',
                f'{idx}.0',
                '1',
                '1.0',
                '', '', '', '', '', ''
            ]
            csv_writer.writerow(question_row)

            # Обработка вариантов ответа
            for answer_idx, answer_item in enumerate(answers, start=1):
                answer_text = answer_item['text']
                is_correct = '1' if answer_item['correct'] else '0'

                answer_row = [
                    'answer',
                    answer_text,
                    'text',
                    is_correct,
                    '0',
                    '',
                    str(answer_idx),
                    '', '', '', '', '', ''
                ]
                csv_writer.writerow(answer_row)

    print(f'Конвертация завершена. Файл {csv_file} создан.')

if __name__ == '__main__':
    main()
