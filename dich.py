from deep_translator import GoogleTranslator

# Đường dẫn tới file tiếng Anh và file đầu ra
input_file = "questions.txt"  # Đường dẫn tới file tiếng Anh
output_file = "output_vietnamese.txt"  # Đường dẫn tới file tiếng Việt

# Mở file tiếng Anh để đọc và file tiếng Việt để ghi
with open(input_file, "r", encoding='utf-8') as infile, open(output_file, "w", encoding='utf-8') as outfile:
    for line in infile:
        line = line.strip()  # Loại bỏ khoảng trắng ở đầu và cuối dòng
        if line:  # Kiểm tra nếu dòng không trống
            # Dịch dòng sang tiếng Việt
            translated_line = GoogleTranslator(source='en', target='vi').translate(line)
            # Ghi vào file đầu ra
            outfile.write(translated_line + "\n")

print(f"Đã dịch xong và lưu vào '{output_file}'.")
