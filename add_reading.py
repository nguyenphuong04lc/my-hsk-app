import json
import os
import random

# Dữ liệu đọc hiểu mẫu cho một số bài (Bạn có thể mở rộng thêm)
READING_DATA = {
    "hsk1": {
        1: {
            "passage": "你好！我叫白家月。我是法国人。很高兴认识你。请问，你叫什么名字？",
            "q": [("白家月是哪国人？", ["法国人", "中国人", "泰国人", "英国人"], "法国人", "文中说：我是法国人。")]
        },
        2: {
            "passage": "我叫李文。我是中国人。你是哪国人？我也是中国人。对不起，没关系。",
            "q": [("李文是哪国人？", ["法国人", "中国人", "泰国人", "美国人"], "中国人", "文中说：我叫李文。我是中国人。")]
        },
        3: {
            "passage": "她是我女朋友。她叫安妮。她不是中国人，她是法国人。",
            "q": [("安妮是哪国人？", ["中国人", "法国人", "泰国人", "英国人"], "法国人",
                   "文中说：她不是中国人，她是法国人。")]
        },
        4: {
            "passage": "我家有四口人。爸爸、妈妈、一个哥哥和我。我没有妹妹。我今年二十岁。",
            "q": [("他家有几口人？", ["三口人", "四口人", "五口人", "六口人"], "四口人", "文中说：我家有四口人。")]
        },
        5: {
            "passage": "今天我休息。我不去上班。我在家做饭。我会做饺子。我喜欢吃饺子。",
            "q": [("今天他做什么？", ["去上班", "在家做饭", "去旅游", "去学校"], "在家做饭", "文中说：我在家做饭。")]
        }
        # Bạn có thể thêm các bài 6-15 tương tự ở đây
    },
    "hsk2": {
        1: {
            "passage": "在机场，王一雪接到了白家月和安妮。白家月说：“你们好，我叫白家月。”一飞打电话让我来接你们。后来家月发现行李不见了，我们去了服务台。",
            "q": [("王一雪去机场做什么？", ["去旅游", "接白家月", "送朋友", "买东西"], "接白家月",
                   "一飞打电话让我来接你们。")]
        },
        2: {
            "passage": "白家月和安妮想去北京大学。这儿有到那儿的公交车，但是车站有点儿远。白家月说：“我们还是打车去吧。”",
            "q": [
                ("她们怎么去北京大学？", ["坐公交车", "打车", "走路", "骑自行车"], "打车", "白家月说：我们还是打车去吧。")]
        }
    },
    "hsk3": {
        1: {
            "passage": "在机场，王一雪接到了白家月和安妮。一飞给我打电话了，让我来接你们。白家月发现行李不见了，李文带她去服务台，帮助她找到了行李。晚上，一雪姐带他们去吃了一家很好吃的中国菜。",
            "q": [("王一雪去机场做什么？", ["去旅游", "接白家月和安妮", "送朋友", "买东西"], "接白家月和安妮",
                   "一飞打电话让我来接你们。")]
        },
        2: {
            "passage": "在饭馆，白家月说：“飞了这么远，现在还真是又饿又渴。”她好久没喝中国茶，也没吃饺子了。她点了绿茶和饺子，王一雪点了很多好吃的菜。",
            "q": [("白家月现在觉得怎么样？", ["又累又困", "又饿又渴", "又冷又热", "很高兴"], "又饿又渴",
                   "白家月说：现在还真是又饿又渴。")]
        }
    }
}


def create_reading_questions(level_str, lesson_id):
    data = READING_DATA.get(level_str, {}).get(lesson_id)
    if not data:
        return None, []

    questions = []
    for q_text, options, answer, explanation in data["q"]:
        shuffled_options = random.sample(options, len(options))
        questions.append({
            "type": "reading",
            "question": q_text,
            "options": shuffled_options,
            "answer": answer,
            "explanation": explanation
        })
    return data["passage"], questions


def merge_data():
    for folder_name, level_str in [("hsk1_data", "hsk1"), ("hsk2_data", "hsk2"), ("hsk3_data", "hsk3")]:
        if not os.path.exists(folder_name): continue

        for filename in os.listdir(folder_name):
            if filename.endswith(".json"):
                filepath = os.path.join(folder_name, filename)
                try:
                    lesson_id = int(filename.replace("lesson_", "").replace(".json", ""))
                except:
                    continue

                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                passage, reading_qs = create_reading_questions(level_str, lesson_id)

                if passage:
                    data["readingPassage"] = passage
                    # Xóa các câu hỏi reading cũ (nếu chạy script nhiều lần)
                    data["questions"] = [q for q in data["questions"] if q.get("type") != "reading"]
                    # Thêm câu hỏi reading mới lên đầu
                    data["questions"] = reading_qs + data["questions"]
                    data["totalQuestions"] = len(data["questions"])

                    with open(filepath, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)
                    print(f"Đã cập nhật Đọc hiểu cho {folder_name}/{filename}")


if __name__ == "__main__":
    print("Đang thêm dữ liệu Đọc hiểu...")
    merge_data()
    print("Xong!")