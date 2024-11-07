from deep_translator import GoogleTranslator

input_file = "questions.txt"  
output_file = "output_vietnamese.txt"  


with open(output_file, "r", encoding='utf-8') as f:
    translated_lines = f.readlines()
translated_count = len(translated_lines)


with open(input_file, "r", encoding='utf-8') as infile, open(output_file, "a", encoding='utf-8') as outfile:
    for i, line in enumerate(infile):
        if i < translated_count:  
            continue
        line = line.strip()  
        if line:  
            try:
                
                translated_line = GoogleTranslator(source='en', target='vi').translate(line)
                if translated_line:
                    outfile.write(translated_line + "\n")  
                    print(f"{i} Đã tạo: {translated_line}")
                else:
                    print(f"Không thể tạo dòng: {line}")
            except Exception as e:
                print(f"Lỗi khi tạo dòng: {line}. Lỗi: {e}")

print("Quá trình tạo data tiếp tục hoàn tất.")
