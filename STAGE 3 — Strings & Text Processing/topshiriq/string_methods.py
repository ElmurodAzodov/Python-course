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

# 2 - PAROLLARNI TEKSHIRISH TIZIMI
# Foydalanuvchi parollarining xavfsizlik darajasini tekshiruvchi dastur

print("=" * 60)
print("PAROLLARNI TEKSHIRISH TIZIMI".center(60))
print("=" * 60)

print("\nParol talablari:")
print("   • Kamida 8 belgi")
print("   • Kamida 1 ta katta harf")
print("   • Kamida 1 ta kichik harf")
print("   • Kamida 1 ta raqam")
print("   • Kamida 1 ta maxsus belgi (!@#$%^&*)")
print("   • 3 ta ketma-ket bir xil belgi bo'lmasligi kerak")
print("-" * 60)

# Yagona parol tekshirish
print("\n1. YAGONA PAROL TEKSHIRISH")
password = input("Parolni kiriting: ")

if password:
    score = 0
    checks = []
    missing = []
    
    # Uzunlik tekshirish
    if len(password) >= 8:
        score += 1
        checks.append("✓ Uzunlik (8+ belgi)")
    else:
        missing.append("✗ Uzunlik (kamida 8 belgi)")
    
    # Katta harf tekshirish
    has_upper = False
    for c in password:
        if c.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
        checks.append("✓ Katta harf")
    else:
        missing.append("✗ Katta harf")
    
    # Kichik harf tekshirish
    has_lower = False
    for c in password:
        if c.islower():
            has_lower = True
            break
    if has_lower:
        score += 1
        checks.append("✓ Kichik harf")
    else:
        missing.append("✗ Kichik harf")
    
    # Raqam tekshirish
    has_digit = False
    for c in password:
        if c.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1
        checks.append("✓ Raqam")
    else:
        missing.append("✗ Raqam")
    
    # Maxsus belgi tekshirish
    special_chars = "!@#$%^&*"
    has_special = False
    for c in password:
        if c in special_chars:
            has_special = True
            break
    if has_special:
        score += 1
        checks.append("✓ Maxsus belgi")
    else:
        missing.append("✗ Maxsus belgi")
    
    # Ketma-ket bir xil belgilar
    has_consecutive = False
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            has_consecutive = True
            break
    
    if not has_consecutive:
        score += 1
        checks.append("✓ Ketma-ket bir xil belgilar yo'q")
    else:
        missing.append("✗ 3 ta ketma-ket bir xil belgi bor")
    
    # Mustahkamlik darajasi
    if score >= 6:
        strength = "KUCHLI 🔒"
        color = "✅"
    elif score >= 4:
        strength = "O'RTA 🔐"
        color = "⚠️"
    else:
        strength = "ZAIF 🔓"
        color = "❌"
    
    # Natijalarni chiqarish
    print("\n" + "-" * 60)
    print("TEKSHIRUV NATIJALARI:")
    print("-" * 60)
    
    print(f"\nParol: {'*' * len(password)} ({len(password)} belgi)")
    print(f"Baholash: {score}/6")
    print(f"Mustahkamlik darajasi: {color} {strength}")
    
    print("\n✅ BAJARILGAN TALABLAR:")
    if checks:
        for check in checks:
            print(f"   {check}")
    else:
        print("   Hech qanday talab bajarilmagan")
    
    print("\n❌ BAJARILMAGAN TALABLAR:")
    if missing:
        for miss in missing:
            print(f"   {miss}")
    else:
        print("   Barcha talablar bajarilgan!")
    
    # Qo'shimcha statistika
    upper_count = sum(1 for c in password if c.isupper())
    lower_count = sum(1 for c in password if c.islower())
    digit_count = sum(1 for c in password if c.isdigit())
    special_count = sum(1 for c in password if c in special_chars)
    
    print("\n📊 QO'SHIMCHA STATISTIKA:")
    print(f"   • Katta harflar: {upper_count} ta")
    print(f"   • Kichik harflar: {lower_count} ta")
    print(f"   • Raqamlar: {digit_count} ta")
    print(f"   • Maxsus belgilar: {special_count} ta")
    
else:
    print("Xato: Parol kiritilmadi!")

# Bir nechta parollarni tekshirish
print("\n" + "=" * 60)
print("2. BIR NECHTA PAROLNI TEKSHIRISH")
print("=" * 60)
print("Parollarni vergul bilan ajratib yozing (masalan: parol1, parol2, parol3)")

passwords_input = input("\nParollarni kiriting: ")
password_list = [p.strip() for p in passwords_input.split(',') if p.strip()]

if password_list:
    print("\n" + "-" * 60)
    print("BARCHA PAROLLAR TAHLILI:")
    print("-" * 60)
    
    for i, pwd in enumerate(password_list, 1):
        print(f"\n{i}-PAROL:")
        print(f"   • Parol: {'*' * len(pwd)}")
        print(f"   • Uzunlik: {len(pwd)} belgi")
        
        # Tekshirishlar
        checks_passed = 0
        if len(pwd) >= 8:
            checks_passed += 1
        
        if any(c.isupper() for c in pwd):
            checks_passed += 1
        
        if any(c.islower() for c in pwd):
            checks_passed += 1
        
        if any(c.isdigit() for c in pwd):
            checks_passed += 1
        
        if any(c in "!@#$%^&*" for c in pwd):
            checks_passed += 1
        
        consecutive = False
        for j in range(len(pwd) - 2):
            if pwd[j] == pwd[j+1] == pwd[j+2]:
                consecutive = True
                break
        if not consecutive:
            checks_passed += 1
        
        # Darajani aniqlash
        if checks_passed >= 6:
            print(f"   • Daraja: KUCHLI 🔒 ({checks_passed}/6)")
        elif checks_passed >= 4:
            print(f"   • Daraja: O'RTA 🔐 ({checks_passed}/6)")
        else:
            print(f"   • Daraja: ZAIF 🔓 ({checks_passed}/6)")
        
        print(f"   • Katta harflar: {sum(1 for c in pwd if c.isupper())} ta")
        print(f"   • Raqamlar: {sum(1 for c in pwd if c.isdigit())} ta")
    
    # Umumiy statistika
    print("\n" + "-" * 60)
    print("UMUMIY STATISTIKA:")
    print(f"   • Jami parollar: {len(password_list)} ta")
    print(f"   • Eng uzun parol: {max(len(p) for p in password_list)} belgi")
    print(f"   • Eng qisqa parol: {min(len(p) for p in password_list)} belgi")
    
else:
    print("Xato: Parollar kiritilmadi!")

#=======================================================================================================
