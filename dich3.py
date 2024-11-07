from deep_translator import GoogleTranslator
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

input_file = "questions.txt"
output_file = "output_vietnamese.txt"

# Kiểm tra nếu file đầu ra tồn tại, nếu không, tạo file rỗng
if not os.path.exists(output_file):
    open(output_file, "w", encoding='utf-8').close()

# Đọc các dòng đã dịch sẵn trong file đầu ra (nếu có)
translated_lines = []
try:
    with open(output_file, "r", encoding='utf-8') as f:
        translated_lines = f.readlines()
except FileNotFoundError:
    pass  # Nếu file không tồn tại, sẽ bắt đầu dịch mới hoàn toàn

translated_count = len(translated_lines)

# Đọc file đầu vào
with open(input_file, "r", encoding='utf-8') as infile:
    lines = infile.readlines()

# Lấy những dòng chưa được dịch
lines_to_translate = lines[translated_count:]

# Hàm dịch một dòng văn bản
def translate_line(line):
    line = line.strip()
    try:
        translated_line = GoogleTranslator(source='en', target='vi').translate(line)
        return translated_line
    except Exception as e:
        print(f"Lỗi khi dịch dòng: {line}. Lỗi: {e}")
        return None

# Dịch các dòng song song với đa luồng
with ThreadPoolExecutor(max_workers=5) as executor:  # Bạn có thể điều chỉnh số luồng (max_workers) tùy theo nhu cầu
    futures = {executor.submit(translate_line, line): line for line in lines_to_translate}
    with open(output_file, "a", encoding='utf-8') as outfile:
        for i, future in enumerate(as_completed(futures)):
            result = future.result()
            if result:
                outfile.write(result + "\n")
                print(f"Dòng {i + translated_count} đã dịch: {result}")

print("Quá trình dịch hoàn tất.")
