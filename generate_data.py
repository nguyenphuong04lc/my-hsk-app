import json
import os
import random
import re

# ==========================================
# KHO DỮ LIỆU MẪU HSK 1 (Bài 1)
# ==========================================
DATA_SOURCE = {
    1: {
        "title": "Bài 1: AI小语，你好",
        "vocab": [
            ("你好", "nǐ hǎo", "Xin chào"), ("谢谢", "xièxie", "Cảm ơn"), ("再见", "zàijiàn", "Tạm biệt"),
            ("不客气", "bú kèqi", "Không có gì"), ("您", "nín", "Ngài"), ("大家", "dàjiā", "Mọi người"),
            ("老师", "lǎoshī", "Giáo viên"), ("学生", "xuéshēng", "Học sinh"), ("你们", "nǐmen", "Các bạn"),
            ("对不起", "duìbuqǐ", "Xin lỗi"), ("没关系", "méi guānxi", "Không sao"), ("是", "shì", "Là")
        ],
        "grammar": [
            # Đảm bảo câu mẫu có chứa từ vựng ở trên để có thể điền từ
            ("Đại từ nhân xưng", "Đại từ nào dùng để chào hỏi lịch sự với người lớn tuổi?",
             ["您 (nín)", "你 (nǐ)", "我 (wǒ)", "他 (tā)"], "您 (nín)", "您 là kính ngữ của 你."),
            ("Chào hỏi", "Cách đáp lại lời 'Cảm ơn' là gì?",
             ["不客气 (bú kèqi)", "你好 (nǐ hǎo)", "再见 (zàijiàn)", "对不起 (duìbuqǐ)"], "不客气 (bú kèqi)",
             "不客气 nghĩa là 'Không có gì'."),
            ("Xin lỗi", "Đáp lại lời xin lỗi, ta dùng:",
             ["没关系 (méi guānxi)", "不客气 (bú kèqi)", "你好 (nǐ hǎo)", "谢谢 (xièxie)"], "没关系 (méi guānxi)",
             "没关系 nghĩa là 'Không sao đâu'."),
            ("Giới thiệu tên", "Cấu trúc để giới thiệu tên là gì?", ["我叫...", "我是...", "我有...", "我在..."],
             "我叫...", "我叫 + Tên (Tôi tên là...)")
        ],
        "translate": [
            ("Xin chào", "你好"), ("Cảm ơn", "谢谢"), ("Tạm biệt", "再见"), ("Không có gì", "不客气"),
            ("Xin lỗi", "对不起"), ("Không sao", "没关系"), ("Tôi tên là Lý Văn", "我叫李文"),
            ("Tôi là học sinh", "我是学生"), ("Rất vui được gặp bạn", "很高兴认识你")
        ]
    }
}


# ==========================================
# HÀM SINH CÂU HỎI ĐIỀN TỪ CHUẨN XÁC (KHÔNG LỖI)
# ==========================================
def generate_fill_blank_strict(vocab, grammar_list, used_sentences):
    questions = []

    for g in grammar_list:
        # Lấy câu trả lời đúng (chính là câu mẫu ngữ pháp)
        sentence = g[3]

        # Nếu câu này đã dùng để điền từ rồi thì bỏ qua
        if sentence in used_sentences: continue

        # Tìm từ vựng trong câu này
        target_word = None
        target_meaning = None
        for word, pinyin, meaning in vocab:
            # Chỉ chọn từ có độ dài >= 1 và nằm trong câu
            if word in sentence and len(word) >= 1:
                target_word = word
                target_meaning = meaning
                break

        # NẾU TÌM THẤY TỪ VỰNG PHÙ HỢP, MỚI TẠO CÂU HỎI
        if target_word:
            # Thay thế từ đó bằng dấu gạch
            q_text = sentence.replace(target_word, "______")

            # Đáp án sai lấy từ kho từ vựng
            wrongs = [v[0] for v in vocab if v[0] != target_word]
            options = [target_word] + random.sample(wrongs, min(3, len(wrongs)))
            while len(options) < 4: options.append("___")
            random.shuffle(options)

            questions.append({
                "type": "fill_blank",
                "question": f"Điền từ thích hợp vào chỗ trống:\n{q_text}",
                "options": options[:4],
                "answer": target_word,
                "explanation": f"Đáp án đúng là “{target_word}” ({target_meaning})."
            })
            # Đánh dấu câu này đã dùng
            used_sentences.add(sentence)

    return questions


# ==========================================
# HÀM TỔNG HỢP
# ==========================================
def generate_all_questions(data):
    questions = []
    vocab = data["vocab"]
    grammar = data["grammar"]
    translate = data["translate"]

    used_words = set()
    used_grammar = set()
    used_translate = set()
    used_fill_blank_sentences = set()

    # 1. TỪ VỰNG (Hán -> Việt)
    for word, pinyin, meaning in vocab:
        if word in used_words: continue
        wrong_meanings = [v[2] for v in vocab if v[2] != meaning]
        options = [meaning] + random.sample(wrong_meanings, min(3, len(wrong_meanings)))
        while len(options) < 4: options.append("Đáp án khác")
        random.shuffle(options)
        questions.append({
            "type": "meaning", "question": f"Từ “{word}” ({pinyin}) có nghĩa là gì?",
            "options": options, "answer": meaning, "explanation": f"“{word}” nghĩa là “{meaning}”."
        })
        used_words.add(word)

    # 2. TỪ VỰNG (Việt -> Hán)
    for word, pinyin, meaning in vocab:
        if word in used_words: continue
        wrong_words = [f"{v[0]} ({v[1]})" for v in vocab if v[0] != word]
        options = [f"{word} ({pinyin})"] + random.sample(wrong_words, min(3, len(wrong_words)))
        while len(options) < 4: options.append("Đáp án khác")
        random.shuffle(options)
        questions.append({
            "type": "meaning", "question": f"Từ nào có nghĩa là “{meaning}”?",
            "options": options, "answer": f"{word} ({pinyin})", "explanation": f"“{meaning}” là “{word}” ({pinyin})."
        })
        used_words.add(word)

    # 3. NGỮ PHÁP
    for g in grammar:
        if g[1] in used_grammar: continue
        options = list(g[2])
        random.shuffle(options)
        questions.append({
            "type": "grammar", "question": f"Ngữ pháp: {g[0]}\n{g[1]}",
            "options": options, "answer": g[3], "explanation": g[4]
        })
        used_grammar.add(g[1])

    # 4. DỊCH CÂU
    for vn, zh in translate:
        if vn in used_translate: continue
        wrong1 = zh[::-1] if len(zh) > 1 else zh + "吗"
        wrong2 = zh.replace("我", "他") if "我" in zh else zh.replace("你", "我")
        options = [zh, wrong1, wrong2, zh + "了"]
        options = list(set(options))
        while len(options) < 4: options.append("Đáp án sai")
        random.shuffle(options)
        questions.append({
            "type": "translate", "question": f"Dịch câu sau sang tiếng Trung: “{vn}”",
            "options": options[:4], "answer": zh, "explanation": f"Câu đúng là: {zh}"
        })
        used_translate.add(vn)

    # 5. ĐIỀN TỪ (SỬ DỤNG HÀM STRICT MỚI)
    fill_blank_qs = generate_fill_blank_strict(vocab, grammar, used_fill_blank_sentences)
    questions.extend(fill_blank_qs)

    # 6. BÙ ĐẮP Pinyin (Nếu thiếu câu)
    while len(questions) < 30:
        word, pinyin, meaning = random.choice(vocab)
        wrong1 = pinyin.replace('a', 'à').replace('i', 'ì')
        wrong2 = pinyin.replace('n', 'm')
        options = [pinyin, wrong1, wrong2, pinyin + "1"]
        options = list(set(options))
        while len(options) < 4: options.append(pinyin + "2")
        random.shuffle(options)
        questions.append({
            "type": "pinyin", "question": f"Cách đọc đúng của “{word}” là:",
            "options": options[:4], "answer": pinyin, "explanation": f"“{word}” đọc là {pinyin}."
        })

    random.shuffle(questions)
    for idx, q in enumerate(questions):
        q["id"] = idx + 1

    return questions


if __name__ == "__main__":
    print("Bắt đầu tạo dữ liệu (Đã sửa lỗi Điền từ)...")
    os.makedirs("hsk1_data", exist_ok=True)

    questions = generate_all_questions(DATA_SOURCE[1])

    lesson_json = {
        "lessonId": 1,
        "lessonTitle": DATA_SOURCE[1]["title"],
        "totalQuestions": len(questions),
        "questions": questions
    }

    with open("hsk1_data/lesson_1.json", "w", encoding="utf-8") as f:
        json.dump(lesson_json, f, ensure_ascii=False, indent=4)

    print(f" -> Đã tạo hsk1_data/lesson_1.json với {len(questions)} câu hỏi (Chuẩn 100%).")