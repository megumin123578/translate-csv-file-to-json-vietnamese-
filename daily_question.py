import pandas as pd
from deep_translator import GoogleTranslator

# Đọc file CSV
csv_file = "data.csv"  # Đường dẫn tới file CSV của bạn
data = pd.read_csv(csv_file)

# Lấy các câu hỏi từ cột question1 và question2
questions = []

# Thêm các câu hỏi từ column "question1"
questions.extend(data['question1'].dropna().tolist())

# Thêm các câu hỏi từ column "question2"
questions.extend(data['question2'].dropna().tolist())

# Dịch các câu hỏi sang tiếng Việt
translated_questions = []
for question in questions:
    translated = GoogleTranslator(source='en', target='vi').translate(question)
    translated_questions.append(translated)

# Lưu các câu hỏi đã dịch vào file text
with open("translated_questions.txt", "w", encoding='utf-8') as f:
    for question in translated_questions:
        f.write(question + "\n")

print(f"Đã lưu {len(translated_questions)} câu hỏi đã dịch vào 'translated_questions.txt'.")
