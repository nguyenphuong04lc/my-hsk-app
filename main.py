import json
import os
import random

# ==========================================
# NGÂN HÀNG TỪ VỰNG HSK 1 (Phân loại từ loại)
# ==========================================
lessons_data = {
    1: {"title": "Bài 1: AI小语，你好",
        "vocab": [("你好", "nǐ hǎo", "Xin chào", "phrase"), ("谢谢", "xièxie", "Cảm ơn", "phrase"),
                  ("再见", "zàijiàn", "Tạm biệt", "phrase"), ("不客气", "bú kèqi", "Không có gì", "phrase"),
                  ("您", "nín", "Ngài", "pronoun"), ("大家", "dàjiā", "Mọi người", "pronoun"),
                  ("老师", "lǎoshī", "Giáo viên", "noun"), ("学生", "xuéshēng", "Học sinh", "noun"),
                  ("你们", "nǐmen", "Các bạn", "pronoun")]},
    2: {"title": "Bài 2: 我叫李文",
        "vocab": [("叫", "jiào", "Gọi/Tên là", "verb"), ("什么", "shénme", "Cái gì", "pronoun"),
                  ("名字", "míngzi", "Tên", "noun"), ("我", "wǒ", "Tôi", "pronoun"), ("是", "shì", "Là", "verb"),
                  ("不", "bù", "Không", "adverb"), ("对不起", "duìbuqǐ", "Xin lỗi", "phrase"),
                  ("没关系", "méi guānxi", "Không sao", "phrase"), ("认识", "rènshi", "Quen biết", "verb"),
                  ("高兴", "gāoxìng", "Vui vẻ", "adj")]},
    3: {"title": "Bài 3: 我是中国人",
        "vocab": [("人", "rén", "Người", "noun"), ("中国", "Zhōngguó", "Trung Quốc", "noun"),
                  ("法国", "Fǎguó", "Pháp", "noun"), ("中文", "Zhōngwén", "Tiếng Trung", "noun"),
                  ("谁", "shéi", "Ai", "pronoun"), ("女朋友", "nǚpéngyou", "Bạn gái", "noun"),
                  ("哪", "nǎ", "Nào", "pronoun"), ("国", "guó", "Nước", "noun"), ("她", "tā", "Cô ấy", "pronoun"),
                  ("泰国", "Tàiguó", "Thái Lan", "noun"), ("的", "de", "Trợ từ sở hữu", "particle")]},
    4: {"title": "Bài 4: 我有两个孩子",
        "vocab": [("有", "yǒu", "Có", "verb"), ("多少", "duōshao", "Bao nhiêu", "pronoun"),
                  ("个", "gè", "Cái", "measure"), ("哥哥", "gēge", "Anh trai", "noun"),
                  ("呢", "ne", "Trợ từ", "particle"), ("没有", "méiyǒu", "Không có", "verb"),
                  ("家", "jiā", "Nhà", "noun"), ("几", "jǐ", "Mấy", "pronoun"), ("口", "kǒu", "Khẩu", "measure"),
                  ("爸爸", "bàba", "Bố", "noun"), ("妈妈", "māma", "Mẹ", "noun"), ("妹妹", "mèimei", "Em gái", "noun"),
                  ("和", "hé", "Và", "conj"), ("儿子", "érzi", "Con trai", "noun"),
                  ("孩子", "háizi", "Đứa trẻ", "noun"), ("女儿", "nǚ'ér", "Con gái", "noun"),
                  ("岁", "suì", "Tuổi", "measure"), ("今年", "jīnnián", "Năm nay", "noun")]},
    5: {"title": "Bài 5: 今天我休息",
        "vocab": [("今天", "jīntiān", "Hôm nay", "noun"), ("号", "hào", "Ngày", "noun"), ("月", "yuè", "Tháng", "noun"),
                  ("日", "rì", "Ngày", "noun"), ("星期", "xīngqī", "Tuần", "noun"),
                  ("休息", "xiūxi", "Nghỉ ngơi", "verb"), ("会", "huì", "Biết/Có thể", "verb"),
                  ("做饭", "zuò fàn", "Nấu cơm", "verb"), ("面条儿", "miàntiáor", "Mì", "noun"),
                  ("饺子", "jiǎozi", "Sủi cảo", "noun"), ("一些", "yīxiē", "Một ít", "pronoun"),
                  ("菜", "cài", "Món ăn", "noun"), ("下班", "xiàbān", "Tan làm", "verb"), ("新", "xīn", "Mới", "adj"),
                  ("电脑", "diànnǎo", "Máy tính", "noun"), ("真", "zhēn", "Thật", "adverb"),
                  ("好看", "hǎokàn", "Đẹp", "adj"), ("喜欢", "xǐhuan", "Thích", "verb")]},
    6: {"title": "Bài 6: 你的手机号是多少",
        "vocab": [("手机", "shǒujī", "Điện thoại", "noun"), ("电话", "diànhuà", "Điện thoại", "noun"),
                  ("明天", "míngtiān", "Ngày mai", "noun"), ("去", "qù", "Đi", "verb"),
                  ("哪儿", "nǎr", "Ở đâu", "pronoun"), ("想", "xiǎng", "Muốn", "verb"),
                  ("超市", "chāoshì", "Siêu thị", "noun"), ("买", "mǎi", "Mua", "verb"),
                  ("东西", "dōngxi", "Đồ vật", "noun"), ("些", "xiē", "Một ít", "measure"),
                  ("牛奶", "niúnǎi", "Sữa", "noun"), ("电影院", "diànyǐngyuàn", "Rạp chiếu phim", "noun"),
                  ("看", "kàn", "Xem", "verb"), ("电影", "diànyǐng", "Phim", "noun"), ("事", "shì", "Việc", "noun"),
                  ("上课", "shàngkè", "Lên lớp", "verb"), ("半", "bàn", "Rưỡi", "num"),
                  ("下课", "xiàkè", "Tan học", "verb"), ("家", "jiā", "Nhà", "noun"),
                  ("晚上", "wǎnshang", "Buổi tối", "noun")]},
    7: {"title": "Bài 7: 我晚上六点半下班",
        "vocab": [("现在", "xiànzài", "Bây giờ", "noun"), ("点", "diǎn", "Giờ", "measure"),
                  ("早上", "zǎoshang", "Sáng sớm", "noun"), ("上午", "shàngwǔ", "Buổi sáng", "noun"),
                  ("分", "fēn", "Phút", "measure"), ("课", "kè", "Bài học", "noun"),
                  ("下午", "xiàwǔ", "Buổi chiều", "noun"), ("见", "jiàn", "Gặp", "verb"),
                  ("电影院", "diànyǐngyuàn", "Rạp phim", "noun"), ("看", "kàn", "Xem", "verb"),
                  ("事", "shì", "Việc", "noun"), ("上班", "shàngbān", "Đi làm", "verb"),
                  ("店", "diàn", "Cửa hàng", "noun"), ("分钟", "fēnzhōng", "Phút", "measure"),
                  ("后", "hòu", "Sau", "noun")]},
    8: {"title": "Bài 8: 我爸爸也在医院工作",
        "vocab": [("房间", "fángjiān", "Căn phòng", "noun"), ("外", "wài", "Ngoài", "noun"),
                  ("只", "zhī", "Con (lượng từ)", "measure"), ("小", "xiǎo", "Nhỏ", "adj"),
                  ("猫", "māo", "Mèo", "noun"), ("没", "méi", "Không", "adverb"),
                  ("看见", "kànjiàn", "Nhìn thấy", "verb"), ("桌子", "zhuōzi", "Cái bàn", "noun"),
                  ("下", "xià", "Dưới", "noun"), ("漂亮", "piàoliang", "Xinh đẹp", "adj"),
                  ("学校", "xuéxiào", "Trường học", "noun"), ("书店", "shūdiàn", "Hiệu sách", "noun"),
                  ("前", "qián", "Trước", "noun"), ("能", "néng", "Có thể", "verb"), ("到", "dào", "Đến", "verb"),
                  ("午饭", "wǔfàn", "Bữa trưa", "noun")]},
    9: {"title": "Bài 9: 我明天上午在学校学习",
        "vocab": [("前边", "qiánbian", "Phía trước", "noun"), ("家", "jiā", "Nhà", "measure"),
                  ("那个", "nàge", "Cái đó", "pronoun"), ("外边", "wàibian", "Bên ngoài", "noun"),
                  ("椅子", "yǐzi", "Cái ghế", "noun"), ("上", "shàng", "Trên", "noun"),
                  ("本", "běn", "Quyển", "measure"), ("书", "shū", "Sách", "noun"), ("第", "dì", "Thứ", "prefix"),
                  ("学习", "xuéxí", "Học tập", "verb"), ("做", "zuò", "Làm", "verb"),
                  ("白天", "báitiān", "Ban ngày", "noun"), ("读书", "dúshū", "Đọc sách", "verb"),
                  ("朋友", "péngyou", "Bạn bè", "noun"), ("唱", "chàng", "Hát", "verb"),
                  ("歌", "gē", "Bài hát", "noun"), ("好听", "hǎotīng", "Hay", "adj"),
                  ("电视", "diànshì", "Tivi", "noun"), ("狗", "gǒu", "Chó", "noun"), ("玩", "wán", "Chơi", "verb")]},
    10: {"title": "Bài 10: 这儿的苹果真便宜",
         "vocab": [("杯子", "bēizi", "Cái cốc", "noun"), ("售货员", "shòuhuòyuán", "Nhân viên bán hàng", "noun"),
                   ("钱", "qián", "Tiền", "noun"), ("这些", "zhèxiē", "Những cái này", "pronoun"),
                   ("块", "kuài", "Đồng", "measure"), ("那些", "nàxiē", "Những cái kia", "pronoun"),
                   ("这儿", "zhèr", "Ở đây", "pronoun"), ("水果", "shuǐguǒ", "Hoa quả", "noun"),
                   ("少", "shǎo", "Ít", "adj"), ("斤", "jīn", "Cân", "measure"), ("苹果", "píngguǒ", "Táo", "noun"),
                   ("便宜", "piányi", "Rẻ", "adj")]},
    11: {"title": "Bài 11: 我读大学呢",
         "vocab": [("在", "zài", "Đang", "adverb"), ("读", "dú", "Học", "verb"), ("大学", "dàxué", "Đại học", "noun"),
                   ("大学生", "dàxuéshēng", "Sinh viên", "noun"), ("学", "xué", "Học", "verb"),
                   ("医", "yī", "Y khoa", "noun"), ("弟弟", "dìdi", "Em trai", "noun"),
                   ("起床", "qǐchuáng", "Thức dậy", "verb"), ("睡觉", "shuìjiào", "Ngủ", "verb"),
                   ("哪里", "nǎlǐ", "Ở đâu", "pronoun"), ("昨天", "zuótiān", "Hôm qua", "noun"),
                   ("问", "wèn", "Hỏi", "verb"), ("说", "shuō", "Nói", "verb"), ("要", "yào", "Muốn/Sẽ", "verb")]},
    12: {"title": "Bài 12: 昨天下雪了",
         "vocab": [("天气", "tiānqì", "Thời tiết", "noun"), ("天", "tiān", "Trời", "noun"),
                   ("下雨", "xià yǔ", "Mưa", "verb"), ("雨", "yǔ", "Mưa", "noun"),
                   ("有点儿", "yǒudiǎnr", "Hơi", "adverb"), ("觉得", "juéde", "Cảm thấy", "verb"),
                   ("冷", "lěng", "Lạnh", "adj"), ("雪", "xuě", "Tuyết", "noun"), ("来", "lái", "Đến", "verb"),
                   ("公司", "gōngsī", "Công ty", "noun"), ("生病", "shēngbìng", "Bị ốm", "verb"),
                   ("看病", "kànbìng", "Khám bệnh", "verb"), ("药", "yào", "Thuốc", "noun"),
                   ("回", "huí", "Về", "verb"), ("喝", "hē", "Uống", "verb"), ("热", "rè", "Nóng", "adj"),
                   ("水", "shuǐ", "Nước", "noun")]},
    13: {"title": "Bài 13: 请给我一杯茶",
         "vocab": [("可以", "kěyǐ", "Có thể", "verb"), ("问题", "wèntí", "Câu hỏi", "noun"),
                   ("卖", "mài", "Bán", "verb"), ("打电话", "dǎ diànhuà", "Gọi điện", "verb"),
                   ("一下", "yīxià", "Một chút", "measure"), ("服务员", "fúwùyuán", "Phục vụ", "noun"),
                   ("女士", "nǚshì", "Quý bà", "noun"), ("坐", "zuò", "Ngồi", "verb"), ("给", "gěi", "Cho", "verb"),
                   ("杯", "bēi", "Cốc", "measure"), ("早饭", "zǎofàn", "Bữa sáng", "noun"),
                   ("面包", "miànbāo", "Bánh mì", "noun"), ("鸡蛋", "jīdàn", "Trứng gà", "noun"),
                   ("茶", "chá", "Trà", "noun")]},
    14: {"title": "Bài 14: 我看了一个电影",
         "vocab": [("火车", "huǒchē", "Tàu hỏa", "noun"), ("中午", "zhōngwǔ", "Buổi trưa", "noun"),
                   ("开", "kāi", "Khởi hành", "verb"), ("有些", "yǒuxiē", "Một số", "pronoun"),
                   ("写", "xiě", "Viết", "verb"), ("都", "dōu", "Đều", "adverb"),
                   ("听见", "tīngjiàn", "Nghe thấy", "verb"), ("说话", "shuōhuà", "Nói chuyện", "verb"),
                   ("听", "tīng", "Nghe", "verb"), ("字", "zì", "Chữ", "noun"), ("汉语", "Hànyǔ", "Tiếng Hán", "noun"),
                   ("汉字", "Hànzì", "Chữ Hán", "noun"), ("明年", "míngnián", "Năm sau", "noun"),
                   ("中学", "zhōngxué", "Trung học", "noun"), ("小学", "xiǎoxué", "Tiểu học", "noun"),
                   ("上学", "shàngxué", "Đi học", "verb"), ("晚", "wǎn", "Muộn", "adj")]},
    15: {"title": "Bài 15: 大兴机场见",
         "vocab": [("爱", "ài", "Yêu", "verb"), ("哪个", "nǎge", "Cái nào", "pronoun"),
                   ("去年", "qùnián", "Năm ngoái", "noun"),
                   ("男朋友", "nánpéngyou", "Bạn trai", "noun"),
                   ("年", "nián", "Năm", "noun"), ("好玩儿", "hǎowánr", "Vui", "adj"),
                   ("西安", "Xī'ān", "Tây An", "noun"),
                   ("北京", "Běijīng", "Bắc Kinh", "noun"),
                   ("飞机", "fēijī", "Máy bay", "noun"),
                   ("小时", "xiǎoshí", "Giờ", "measure"),
                   ("家人", "jiārén", "Người nhà", "noun"),
                   ("时间", "shíjiān", "Thời gian", "noun"),
                   ("机场", "jīchǎng", "Sân bay", "noun"), ("接", "jiē", "Đón", "verb"),
                   ("住", "zhù", "Sống/Ở", "verb"), ("早", "zǎo", "Sớm", "adj")]}
}

# TỪ ĐIỂN CÂU DỊCH MẪU (Chuẩn ngữ pháp, thực tế, theo sát từng bài)
TRANSLATION_BANK = {
    1: [("Xin chào", "你好"), ("Cảm ơn", "谢谢"), ("Tạm biệt", "再见"), ("Không có gì", "不客气")],
    2: [("Tôi tên là Lý Văn", "我叫李文"), ("Tôi là học sinh", "我是学生"), ("Rất vui được gặp bạn", "很高兴认识你"),
        ("Xin lỗi", "对不起")],
    3: [("Tôi là người Trung Quốc", "我是中国人"), ("Cô ấy là bạn gái tôi", "她是我女朋友"),
        ("Bạn là người nước nào?", "你是哪国人？"), ("Tôi là người Pháp", "我是法国人")],
    4: [("Tôi có hai đứa con", "我有两个孩子"), ("Nhà tôi có 3 người", "我家有三口人"),
        ("Năm nay tôi 20 tuổi", "我今年二十岁"), ("Tôi có một người anh trai", "我有一个哥哥")],
    5: [("Hôm nay tôi nghỉ ngơi", "今天我休息"), ("Hôm nay là thứ mấy?", "今天星期几？"),
        ("Tôi biết nấu cơm", "我会做饭"), ("Máy tính này rất đẹp", "这个电脑真好看")],
    6: [("Ngày mai tôi đi siêu thị", "明天我去超市"), ("Bạn muốn mua gì?", "你想买什么？"),
        ("Tôi muốn uống sữa", "我想喝牛奶"), ("Điện thoại của tôi đâu?", "我的手机在哪儿？")],
    7: [("Bây giờ là mấy giờ?", "现在几点？"), ("Tôi 6h30 tan làm", "我六点半下班"),
        ("Chúng ta gặp nhau lúc 2h chiều nhé", "我们下午两点见吧"), ("Tôi có tiết học lúc 8h sáng", "我早上八点有课")],
    8: [("Bố tôi làm việc ở bệnh viện", "我爸爸在医院工作"), ("Trên bàn có một con mèo", "桌子上有一只小猫"),
        ("Bạn có thể đến không?", "你能到吗？"), ("Tôi ăn trưa ở trường", "我在学校吃午饭")],
    9: [("Ngày mai tôi học ở trường", "明天我在学校学习"), ("Trên ghế có một quyển sách", "椅子上有一本书"),
        ("Tôi thích đọc sách", "我喜欢读书"), ("Đây là cuốn sách thứ hai của tôi", "这是我的第二本书")],
    10: [("Táo ở đây rất rẻ", "这儿的苹果真便宜"), ("Cái cốc này bao nhiêu tiền?", "这个杯子多少钱？"),
         ("Tôi muốn mua hai cân táo", "我想买两斤苹果"), ("Những bông hoa này rất đẹp", "这些花很好看")],
    11: [("Tôi đang học đại học", "我在读大学呢"), ("Em trai tôi đang ngủ", "我弟弟在睡觉呢"),
         ("Bạn có đi siêu thị không?", "你去不去超市？"), ("Tôi không đi, tôi đang học bài", "我不去，我在学习呢")],
    12: [("Hôm qua trời mưa", "昨天下雨了"), ("Trời hôm nay rất lạnh", "今天天气很冷"), ("Tôi bị ốm rồi", "我生病了"),
         ("Bạn nên uống chút nước nóng", "你要喝点儿热水")],
    13: [("Cho tôi một cốc trà", "请给我一杯茶"), ("Tôi có thể hỏi một câu không?", "我可以问一下吗？"),
         ("Tôi muốn ăn bánh mì và trứng", "我想吃面包和鸡蛋"), ("Tôi cần một nửa", "我要一半")],
    14: [("Hôm qua tôi xem một bộ phim", "昨天我看了一个电影"), ("Mọi người đều nghe thấy rồi", "大家都听见了"),
         ("Tôi đã viết rất nhiều chữ Hán", "我写了很多汉字"),
         ("Năm sau con trai tôi học tiểu học", "明年我儿子上小学")],
    15: [("Tôi yêu Trung Quốc", "我爱中国"), ("Năm ngoái tôi đi Tây An", "去年我去了西安"),
         ("Bắc Kinh rất đẹp", "北京很漂亮"), ("Hẹn gặp ở sân bay nhé", "我们机场见吧")]
}


def generate_natural_questions(lesson_id, data):
    questions = []
    vocab = data['vocab']

    # Phân loại từ vựng
    nouns = [v for v in vocab if v[3] == "noun"]
    verbs = [v for v in vocab if v[3] == "verb"]
    adjs = [v for v in vocab if v[3] == "adj"]
    pronouns = [v for v in vocab if v[3] == "pronoun"]

    if not nouns: nouns = vocab
    if not verbs: verbs = vocab
    if not adjs: adjs = vocab
    if not pronouns: pronouns = vocab

    # Hàm hỗ trợ lấy đáp án sai (ĐÃ FIX LỖI VÒNG LẶP VÔ HẠN)
    def get_wrong_options(correct_item, pool, option_index):
        wrongs = []
        # 1. Cố gắng lấy từ danh sách pool trước
        for item in pool:
            if len(wrongs) >= 3: break
            if item[option_index] != correct_item[option_index] and item[option_index] not in wrongs:
                wrongs.append(item[option_index])

        # 2. Nếu pool quá ít, lấy bù từ toàn bộ từ vựng
        if len(wrongs) < 3:
            for item in vocab:
                if len(wrongs) >= 3: break
                if item[option_index] != correct_item[option_index] and item[option_index] not in wrongs:
                    wrongs.append(item[option_index])

        # 3. Nếu vẫn chưa đủ 3, tự động sinh từ rác để đảm bảo không bị treo
        fallback_words = ["Không có", "Khác", "Sai", "Chưa đúng"]
        idx = 0
        while len(wrongs) < 3:
            w = fallback_words[idx % len(fallback_words)]
            if w not in wrongs and w != correct_item[option_index]:
                wrongs.append(w)
            idx += 1

        return wrongs[:3]

    # 1. 30 câu Từ vựng
    for i in range(30):
        word, pinyin, meaning, _ = random.choice(vocab)
        options = [meaning] + get_wrong_options((word, pinyin, meaning), vocab, 2)
        random.shuffle(options)
        questions.append({
            "id": i + 1, "type": "meaning", "question": f"Từ '{word}' ({pinyin}) có nghĩa là gì?",
            "options": options, "answer": meaning, "explanation": f"'{word}' nghĩa là '{meaning}'."
        })

    # 2. 25 câu Pinyin
    for i in range(30, 55):
        word, pinyin, meaning, _ = random.choice(vocab)
        options = [pinyin, pinyin.replace('a', 'à').replace('i', 'ì'), pinyin.replace('n', 'm'),
                   pinyin.replace('o', 'ó').replace('u', 'ù')]
        unique_opts = list(set(options))
        while len(unique_opts) < 4: unique_opts.append(pinyin + str(random.randint(1, 9)))
        random.shuffle(unique_opts)
        questions.append({
            "id": i + 1, "type": "pinyin", "question": f"Cách đọc đúng của '{word}' là:",
            "options": unique_opts[:4], "answer": pinyin, "explanation": f"'{word}' đọc là {pinyin}."
        })

    # 3. 20 câu Điền từ vào câu
    for i in range(55, 75):
        template_type = random.choice(["S+V+N", "S+Adj", "S+是+N"])

        if template_type == "S+V+N":
            p = random.choice(pronouns)
            v = random.choice(verbs)
            n = random.choice(nouns)
            q_text = f"Điền từ thích hợp: {p[0]} ______ {n[0]}。 (Nghĩa: {p[2]} {v[2]} {n[2]})"
            correct_ans = v[0]
            options = [v[0]] + get_wrong_options(v, verbs, 0)
        elif template_type == "S+Adj":
            p = random.choice(pronouns)
            adj = random.choice(adjs)
            q_text = f"Điền từ thích hợp: {p[0]} 很 ______。 (Nghĩa: {p[2]} rất {adj[2]})"
            correct_ans = adj[0]
            options = [adj[0]] + get_wrong_options(adj, adjs, 0)
        else:
            p = random.choice(pronouns)
            n = random.choice(nouns)
            q_text = f"Điền từ thích hợp: {p[0]} ______ {n[0]}。 (Nghĩa: {p[2]} là {n[2]})"
            correct_ans = "是"
            options = ["是", "不", "有", "叫"]

        random.shuffle(options)
        questions.append({
            "id": i + 1, "type": "fill_blank", "question": q_text,
            "options": options[:4], "answer": correct_ans, "explanation": f"Đáp án đúng là '{correct_ans}'."
        })

    # 4. 15 câu Dịch câu (Sử dụng Kho câu mẫu thực tế của từng bài)
    current_trans_bank = TRANSLATION_BANK.get(lesson_id, TRANSLATION_BANK[1])

    for i in range(75, 90):
        # Lấy câu mẫu ngẫu nhiên trong kho của bài đó
        vn, zh = random.choice(current_trans_bank)

        # Tạo đáp án sai thông minh
        options = [zh]
        if len(zh) > 1:
            options.append(zh[::-1])  # Đảo ngược chữ
            options.append(f"是{zh[1:]}")
            options.append(f"我是不{zh[1:]}")
        else:
            options.extend(["我是", "不是我", "是我"])

        options = list(set(options))  # Loại bỏ trùng lặp
        while len(options) < 4:
            options.append(zh + "。")

        options = options[:4]
        random.shuffle(options)

        questions.append({
            "id": i + 1, "type": "translate", "question": f"Dịch câu sau sang tiếng Trung: '{vn}'",
            "options": options, "answer": zh, "explanation": f"Câu đúng là: {zh}"
        })

    # 5. 10 câu Phản xạ Ngữ pháp
    for i in range(90, 100):
        if lesson_id <= 5:
            q_text = "Chọn đại từ nhân xưng phù hợp để chào hỏi lịch sự: ______ 好！(Chào ngài)"
            correct_ans = "您"
            options = ["您", "你", "我", "他"]
        elif lesson_id <= 10:
            n = random.choice(
                [n for n in nouns if n[0] in ["书", "苹果", "杯子", "猫", "狗"]] + [("书", "shū", "Sách", "noun")])
            measure = "本" if n[0] == "书" else ("只" if n[0] in ["猫", "狗"] else "个")
            q_text = f"Chọn lượng từ đúng: 一 ______ {n[0]}"
            correct_ans = measure
            options = ["个", "本", "只", "口"]
        else:
            q_text = "Sắp xếp trật tự câu đúng: 1. 我 2. 喜欢 3. 中国菜"
            correct_ans = "1-2-3"
            options = ["1-2-3", "1-3-2", "2-1-3", "3-1-2"]

        questions.append({
            "id": i + 1, "type": "grammar", "question": q_text,
            "options": options, "answer": correct_ans, "explanation": f"Đáp án đúng là {correct_ans}."
        })

    random.shuffle(questions)
    for idx, q in enumerate(questions): q['id'] = idx + 1
    return questions


if not os.path.exists('hsk1_data'): os.makedirs('hsk1_data')

for lesson_id, data in lessons_data.items():
    questions = generate_natural_questions(lesson_id, data)
    lesson_json = {
        "lessonId": lesson_id, "lessonTitle": data['title'],
        "totalQuestions": len(questions), "questions": questions
    }
    with open(f"hsk1_data/lesson_{lesson_id}.json", 'w', encoding='utf-8') as f:
        json.dump(lesson_json, f, ensure_ascii=False, indent=4)
    print(f"Đã tạo: lesson_{lesson_id}.json")

print("=> HOÀN TẤT TẠO 1500 CÂU HỎI TỰ NHIÊN!")