# 1 - MATN TAHLIL QILISH DASTURI
# Foydalanuvchi kiritgan matn ustida keng qamrovli tahlil o'tkazuvchi dastur

print("=" * 60)
print("MATN TAHLIL QILISH DASTURI".center(60))
print("=" * 60)

# Foydalanuvchidan matn kiritish
text = input("\nMatnni kiriting: ")

if text:
    # So'zlar soni
    words = text.split()
    words_count = len(words)
    
    # Gaplar soni (nuqta, undov, so'roq belgilariga qarab)
    sentences = text.replace('!', '.').replace('?', '.').split('.')
    sentences = [s for s in sentences if s.strip()]  # Bo'sh gaplarni olib tashlash
    sentences_count = len(sentences)
    
    # Belgilar soni
    chars_count = len(text)
    
    # Bo'sh joysiz belgilar soni
    chars_without_spaces = len(text.replace(' ', ''))
    
    # Eng ko'p qatnashgan so'zni topish
    word_frequency = {}
    for word in words:
        word_lower = word.lower().strip('.,!?;:()"\'')
        if word_lower:
            word_frequency[word_lower] = word_frequency.get(word_lower, 0) + 1
    
    most_common_word = ""
    max_word_count = 0
    for word, count in word_frequency.items():
        if count > max_word_count:
            max_word_count = count
            most_common_word = word
    
    # Eng ko'p qatnashgan harfni topish
    letter_frequency = {}
    for char in text.lower():
        if char.isalpha():  # Faqat harflarni olish
            letter_frequency[char] = letter_frequency.get(char, 0) + 1
    
    most_common_letter = ""
    max_letter_count = 0
    for letter, count in letter_frequency.items():
        if count > max_letter_count:
            max_letter_count = count
            most_common_letter = letter
    
    # Tinish belgilarini ro'yxatga olish
    punctuation_marks = '.,!?;:-—(){}[]"\''
    punctuation_list = []
    for char in text:
        if char in punctuation_marks:
            punctuation_list.append(char)
    
    # Matnni teskari tartibda chiqarish
    reversed_text = text[::-1]
    
    # So'zlarning birinchi harfini katta qilish
    capitalized_words = []
    for word in words:
        if word:
            capitalized_words.append(word[0].upper() + word[1:].lower() if len(word) > 1 else word.upper())
    capitalized_text = ' '.join(capitalized_words)
    
    # Raqamlar yig'indisi
    digit_sum = 0
    digits_found = []
    for char in text:
        if char.isdigit():
            digit_sum += int(char)
            digits_found.append(char)
    
    # Unli va undosh harflarni guruhlash
    unli_harflar = "aeiouAEIOU" + "o'u O'U"  # O'zbekcha unli harflar
    unlilar = []
    undoshlar = []
    
    for char in text:
        if char.isalpha():
            if char in unli_harflar or char.lower() in "o'u" and "'" in text:  # O'zbekcha unli harflar uchun
                unlilar.append(char)
            else:
                undoshlar.append(char)
    
    # Natijalarni chiqarish
    print("\n" + "=" * 60)
    print("MATN TAHLILI NATIJALARI".center(60))
    print("=" * 60)
    
    print(f"\n📊 ASOSIY MA'LUMOTLAR:")
    print(f"   • So'zlar soni: {words_count}")
    print(f"   • Gaplar soni: {sentences_count}")
    print(f"   • Belgilar soni: {chars_count}")
    print(f"   • Bo'sh joysiz belgilar: {chars_without_spaces}")
    
    print(f"\n🏆 ENG KO'P QATNASHGANLAR:")
    print(f"   • So'z: '{most_common_word}' - {max_word_count} marta")
    print(f"   • Harf: '{most_common_letter}' - {max_letter_count} marta")
    
    print(f"\n🔢 RAQAMLAR:")
    print(f"   • Raqamlar: {', '.join(digits_found) if digits_found else 'Topilmadi'}")
    print(f"   • Raqamlar yig'indisi: {digit_sum}")
    
    print(f"\n✍️ HARFLAR TAHLILI:")
    print(f"   • Unli harflar ({len(unlilar)} ta): {''.join(unlilar[:50])}{'...' if len(unlilar) > 50 else ''}")
    print(f"   • Undosh harflar ({len(undoshlar)} ta): {''.join(undoshlar[:50])}{'...' if len(undoshlar) > 50 else ''}")
    
    print(f"\n🔣 TINISH BELGILARI:")
    print(f"   • {len(punctuation_list)} ta: {', '.join(set(punctuation_list))}")
    
    print(f"\n🔄 MATNNING TESKARI KO'RINISHI:")
    print(f"   {reversed_text[:200]}{'...' if len(reversed_text) > 200 else ''}")
    
    print(f"\n📝 BIRINCHI HARFI KATTA SO'ZLAR:")
    print(f"   {capitalized_text[:200]}{'...' if len(capitalized_text) > 200 else ''}")
    
    print("\n" + "=" * 60)
else:
    print("Xato: Matn kiritilmadi!")

#===================================================================================================
