import pdfplumber

# Thay tên file PDF của bạn vào đây
pdf_path = "Giáo trình HSK2 mới 3.0.pdf"

print(f"Đang đọc file: {pdf_path}...")
with pdfplumber.open(pdf_path) as pdf:
    # Chỉ đọc thử 5 trang đầu để kiểm tra
    for i in range(5):
        page = pdf.pages[i]
        text = page.extract_text()
        print(f"\n--- Trang {i+1} ---")
        if text:
            print(text[:500]) # In 500 ký tự đầu tiên
        else:
            print("[Không tìm thấy chữ - Có thể file này là ảnh scan]")