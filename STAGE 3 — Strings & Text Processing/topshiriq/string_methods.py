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

# 3 - MATNLARNI QAYTA ISHLASH GENERATORI
# Berilgan matnlar ro'yxatini turli usullarda qayta ishlovchi dastur

print("=" * 70)
print("MATNLARNI QAYTA ISHLASH GENERATORI".center(70))
print("=" * 70)

# Matnlar ro'yxati
matnlar = [
    "  python dasturlash tili  ",
    "2024 YIL DASTURLASH YILI",
    "string metodlari: upper(), lower()",
    "telefon: +998901234567"
]

print("\n📄 BERILGAN MATNLAR:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    print(f"{i}. '{matn}'")

print("\n" + "=" * 70)
print("QAYTA ISHLASH NATIJALARI".center(70))
print("=" * 70)

# 1. Katta harflarga o'tkazish
print("\n1. KATTA HARFLARGA O'TKAZISH:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    print(f"{i}. {matn.upper()}")

# 2. Kichik harflarga o'tkazish
print("\n2. KICHIK HARFLARGA O'TKAZISH:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    print(f"{i}. {matn.lower()}")

# 3. Birinchi harfni katta qilish
print("\n3. BIRINCHI HARFNI KATTA QILISH:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    print(f"{i}. {matn.strip().capitalize()}")

# 4. Har bir so'zning birinchi harfini katta qilish
print("\n4. HAR SO'ZNING BIRINCHI HARFINI KATTA QILISH:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    print(f"{i}. {matn.title()}")

# 5. Ortibcha bo'shliqlarni tozalash
print("\n5. ORTIQCHA BO'SHLIQLARNI TOZALASH:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    print(f"{i}. '{matn.strip()}'")

# 6. Markazlashtirilgan holda chiqarish
print("\n6. MARKAZLASHTIRILGAN HOLDА CHIQARISH:")
print("-" * 70)
max_uzunlik = max(len(matn) for matn in matnlar)
for i, matn in enumerate(matnlar, 1):
    print(f"{i}. {matn.center(max_uzunlik + 10)}")

# 7. Matnlarni uzunligi bo'yicha saralash
print("\n7. MATNLARNI UZUNLIGI BO'YICHA SARALASH:")
print("-" * 70)
saralangan = sorted(matnlar, key=len)
for i, matn in enumerate(saralangan, 1):
    print(f"{i}. '{matn}' - {len(matn)} belgi")

# 8. Matnlardan faqat raqamlarni ajratib olish
print("\n8. FAQAT RAQAMLARNI AJRATIB OLISH:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    raqamlar = ''
    for belgi in matn:
        if belgi.isdigit():
            raqamlar += belgi
    print(f"{i}. {raqamlar if raqamlar else 'Raqam topilmadi'}")

# 9. Matnlardan faqat harflarni ajratib olish
print("\n9. FAQAT HARFLARNI AJRATIB OLISH:")
print("-" * 70)
for i, matn in enumerate(matnlar, 1):
    harflar = ''
    for belgi in matn:
        if belgi.isalpha():
            harflar += belgi
    print(f"{i}. {harflar if harflar else 'Harf topilmadi'}")

# 10. Matnlarni berilgan kalit so'z bo'yicha filtrlash
print("\n10. KALIT SO'Z BO'YICHA FILTRLASH:")
print("-" * 70)
kalit_soz = input("Kalit so'zni kiriting: ").strip().lower()

if kalit_soz:
    print(f"\n'{kalit_soz}' so'zi qatnashgan matnlar:")
    topildi = False
    for i, matn in enumerate(matnlar, 1):
        if kalit_soz in matn.lower():
            print(f"{i}. {matn}")
            topildi = True
    if not topildi:
        print("Hech qanday matn topilmadi")

# Qo'shimcha: O'zingiz matn qo'shish
print("\n" + "=" * 70)
print("O'ZINGIZ MATN QO'SHISH".center(70))
print("=" * 70)

yangi_matn = input("\nYangi matn kiriting: ").strip()
if yangi_matn:
    matnlar.append(yangi_matn)
    print(f"\n✅ Matn qo'shildi! Jami matnlar soni: {len(matnlar)}")
    
    print("\nYANGILANGAN MATNLAR RO'YXATI:")
    print("-" * 70)
    for i, matn in enumerate(matnlar, 1):
        print(f"{i}. '{matn}'")

#=====================================================================================

# 4 - SHAXSIY MA'LUMOTLARNI ANONIMLASHTIRISH
# Matn tarkibidagi shaxsiy ma'lumotlarni topib, ularni maxfiylashtiruvchi dastur

print("=" * 70)
print("SHAXSIY MA'LUMOTLARNI ANONIMLASHTIRISH".center(70))
print("=" * 70)

# Misol matn
original = "Mening ishim Ali Valiyev. Email: ali@mail.com, tel: +998901234567, Kredit karta: 1234-5678-9012-3456, IP: 192.168.1.1:8000"

print("\n📄 ASL MATN:")
print("-" * 70)
print(original)

# Anonimlashtirilgan matn
anonim = original
topilganlar = []

print("\n" + "=" * 70)
print("ANIMLASHTIRISH JARAYONI".center(70))
print("=" * 70)

# 1. Email manzillarni aniqlash va anonimlashtirish
print("\n1. EMAIL MANZILLAR:")
print("-" * 70)

# Email qidirish
email_boshlanishi = original.find('@')
if email_boshlanishi != -1:
    # Email boshlanishini topish
    email_oxiri = email_boshlanishi
    while email_oxiri < len(original) and original[email_oxiri] not in ' .,;:':
        email_oxiri += 1
    
    # Email boshini topish
    email_boshi = email_boshlanishi
    while email_boshi > 0 and original[email_boshi-1] not in ' .,;:@':
        email_boshi -= 1
    
    email = original[email_boshi:email_oxiri]
    print(f"   • Topildi: {email}")
    topilganlar.append(f"Email: {email}")
    
    # Anonimlashtirish
    anonim = anonim.replace(email, "***@***.***")

# 2. Telefon raqamlarini aniqlash va anonimlashtirish
print("\n2. TELEFON RAQAMLARI:")
print("-" * 70)

# Telefon qidirish (oddiy usul)
telefon_index = original.find('+998')
if telefon_index != -1:
    telefon_oxiri = telefon_index
    while telefon_oxiri < len(original) and original[telefon_oxiri].isdigit() or original[telefon_oxiri] == '+':
        telefon_oxiri += 1
    
    telefon = original[telefon_index:telefon_oxiri]
    print(f"   • Topildi: {telefon}")
    topilganlar.append(f"Telefon: {telefon}")
    
    # Anonimlashtirish
    anonim = anonim.replace(telefon, "+998*********")

# 3. Ism-familyalarni aniqlash va anonimlashtirish
print("\n3. ISM-FAMILYALAR:")
print("-" * 70)

# Ism-familya qidirish (katta harf bilan boshlangan so'zlar)
words = original.split()
ism_familya = ""
for i in range(len(words) - 1):
    if words[i][0].isupper() and words[i+1][0].isupper():
        ism_familya = words[i] + " " + words[i+1]
        break

if ism_familya:
    print(f"   • Topildi: {ism_familya}")
    topilganlar.append(f"Ism-familya: {ism_familya}")
    
    # Anonimlashtirish (bosh harflar)
    ism_bosh = ism_familya[0] + "."
    familya_bosh = ism_familya.split()[1][0] + "."
    anonim = anonim.replace(ism_familya, ism_bosh + familya_bosh)

# 4. Kredit karta raqamlarini aniqlash va anonimlashtirish
print("\n4. KREDIT KARTA RAQAMLARI:")
print("-" * 70)

# Kredit karta qidirish (xxxx-xxxx-xxxx-xxxx formati)
karta_index = original.find('1234-5678-9012-3456')
if karta_index != -1:
    karta = "1234-5678-9012-3456"
    print(f"   • Topildi: {karta}")
    topilganlar.append(f"Kredit karta: {karta}")
    
    # Anonimlashtirish (oxirgi 4 ta raqam qoldiriladi)
    anonim = anonim.replace(karta, "****-****-****-3456")

# 5. IP manzillarni aniqlash va anonimlashtirish
print("\n5. IP MANZILLAR:")
print("-" * 70)

# IP qidirish (oddiy usul)
ip_index = original.find('192.168.1.1:8000')
if ip_index != -1:
    ip = "192.168.1.1:8000"
    print(f"   • Topildi: {ip}")
    topilganlar.append(f"IP manzil: {ip}")
    
    # Anonimlashtirish
    anonim = anonim.replace(ip, "***.***.*.*:***")

print("\n" + "=" * 70)
print("ANIMLASHTIRILGAN MATN".center(70))
print("=" * 70)
print(f"\n{anonim}")

print("\n" + "=" * 70)
print("ANIMLASHTIRISH HISOBOTI".center(70))
print("=" * 70)

print(f"\n📊 TOPILGAN MAXFIY MA'LUMOTLAR:")
print("-" * 70)
for i, malumot in enumerate(topilganlar, 1):
    print(f"{i}. {malumot}")

print(f"\n📈 STATISTIKA:")
print(f"   • Jami topilgan ma'lumotlar: {len(topilganlar)} ta")
print(f"   • Anonimlashtirilgan matn uzunligi: {len(anonim)} belgi")
print(f"   • Asl matn uzunligi: {len(original)} belgi")

# Qo'shimcha: O'zingiz matn kiritish
print("\n" + "=" * 70)
print("O'ZINGIZ MATN KIRITISH".center(70))
print("=" * 70)

oz_matn = input("\nMatn kiriting: ").strip()
if oz_matn:
    print(f"\nSiz kiritgan matn: {oz_matn}")
    print("(Hozircha faqat misol matn anonimlashtirildi)")

#=========================================================================================

# 5 - PALINDROM VA ANAGRAMMA ANALIZATORI
# Matnlar to'plamida palindrom va anagrammalarni topuvchi dastur

print("=" * 70)
print("PALINDROM VA ANAGRAMMA ANALIZATORI".center(70))
print("=" * 70)

# Matn kiritish
text = input("\nMatnni kiriting: ").strip()

if text:
    # Matnni so'zlarga ajratish
    words = text.split()
    
    # So'zlarni tozalash (tinish belgilaridan)
    clean_words = []
    for word in words:
        clean_word = ''
        for char in word:
            if char.isalnum():  # Harf yoki raqam bo'lsa
                clean_word += char
        if clean_word:
            clean_words.append(clean_word)
    
    print("\n" + "=" * 70)
    print("TAHLIL NATIJALARI".center(70))
    print("=" * 70)
    
    # 1. Palindromlarni tekshirish
    print("\n1. PALINDROM SO'ZLAR:")
    print("-" * 70)
    
    palindromes = []
    for word in clean_words:
        word_lower = word.lower()
        if word_lower == word_lower[::-1] and len(word) > 1:
            palindromes.append(word)
    
    if palindromes:
        print(f"   • Topilgan palindromlar ({len(palindromes)} ta):")
        for p in palindromes:
            print(f"     - {p}")
    else:
        print("   • Palindrom so'z topilmadi")
    
    # 2. Anagrammalarni tekshirish
    print("\n2. ANAGRAMMA JUFTLIKLAR:")
    print("-" * 70)
    
    # Har bir so'z uchun tartiblangan harflar
    sorted_words = []
    for word in clean_words:
        word_lower = word.lower()
        sorted_word = ''.join(sorted(word_lower))
        sorted_words.append((word, sorted_word))
    
    # Anagramma juftliklarni topish
    anagram_pairs = []
    used = set()
    
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if i != j and sorted_words[i][1] == sorted_words[j][1]:
                pair = (sorted_words[i][0], sorted_words[j][0])
                if pair not in anagram_pairs and (pair[1], pair[0]) not in anagram_pairs:
                    anagram_pairs.append(pair)
    
    if anagram_pairs:
        print(f"   • Topilgan anagramma juftliklar ({len(anagram_pairs)} ta):")
        for a1, a2 in anagram_pairs:
            print(f"     - '{a1}'  ↔  '{a2}'")
    else:
        print("   • Anagramma juftlik topilmadi")
    
    # 3. Eng uzun palindrom
    print("\n3. ENG UZUN PALINDROM:")
    print("-" * 70)
    
    if palindromes:
        longest = max(palindromes, key=len)
        print(f"   • '{longest}' - {len(longest)} harf")
    else:
        print("   • Palindrom topilmadi")
    
    # 4. Eng ko'p anagrammasi bo'lgan so'z
    print("\n4. ENG KO'P ANAGRAMMASI BO'LGAN SO'Z:")
    print("-" * 70)
    
    # Anagramma guruhlarini yaratish
    anagram_groups = {}
    for word, sorted_word in sorted_words:
        if sorted_word in anagram_groups:
            if word not in anagram_groups[sorted_word]:
                anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    
    # Eng katta guruhni topish
    max_group = []
    for group in anagram_groups.values():
        if len(group) > len(max_group):
            max_group = group
    
    if len(max_group) > 1:
        print(f"   • So'zlar: {', '.join(max_group)}")
        print(f"   • {len(max_group)} ta anagramma")
    else:
        print("   • Anagramma guruhlari topilmadi")
    
    # 5. Harf chastotasi bo'yicha guruhlash
    print("\n5. HARF CHASTOTASI BO'YICHA GURUHLASH:")
    print("-" * 70)
    
    letter_groups = {}
    for word in clean_words:
        word_lower = word.lower()
        # Harflarni sanash
        letter_count = {}
        for letter in word_lower:
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) + 1
        
        # Chastota kalitini yaratish
        freq_key = ''
        for letter in sorted(letter_count.keys()):
            freq_key += f"{letter}{letter_count[letter]}"
        
        if freq_key in letter_groups:
            if word not in letter_groups[freq_key]:
                letter_groups[freq_key].append(word)
        else:
            letter_groups[freq_key] = [word]
    
    # Bir xil harf chastotasiga ega so'zlar
    similar_freq = []
    for group in letter_groups.values():
        if len(group) > 1:
            similar_freq.append(group)
    
    if similar_freq:
        print(f"   • Bir xil harf chastotasiga ega so'zlar ({len(similar_freq)} guruh):")
        for i, group in enumerate(similar_freq[:3], 1):
            print(f"     {i}. {', '.join(group)}")
        if len(similar_freq) > 3:
            print(f"     ... va yana {len(similar_freq) - 3} ta guruh")
    else:
        print("   • Bir xil harf chastotasiga ega so'zlar topilmadi")
    
    # 6. Vizual ko'rinish
    print("\n6. VIZUAL KO'RINISH:")
    print("-" * 70)
    
    # Palindromlar uchun
    print("\n   PALINDROMLAR:")
    for word in clean_words:
        word_lower = word.lower()
        if word_lower == word_lower[::-1] and len(word) > 1:
            print(f"   🔴 {word}  ←→  {word[::-1]}")
    
    # Bir nechta so'zlar uchun palindrom tekshirish
    print("\n   TEKSHIRISH UCHUN:")
    for word in clean_words[:5]:  # Faqat birinchi 5 ta so'z
        word_lower = word.lower()
        if len(word) > 1:
            if word_lower == word_lower[::-1]:
                print(f"   ✅ {word} - palindrom")
            else:
                print(f"   ❌ {word} - palindrom emas")

else:
    print("Xato: Matn kiritilmadi!")

# Qo'shimcha: Alohida so'z tekshirish
print("\n" + "=" * 70)
print("ALOHIDA SO'Z TEKSHIRISH".center(70))
print("=" * 70)

word = input("\nSo'zni kiriting: ").strip().lower()
if word:
    # Palindrom tekshirish
    if word == word[::-1]:
        print(f"✅ '{word}' - PALINDROM")
    else:
        print(f"❌ '{word}' - palindrom EMAS")
    
    # So'zning teskari ko'rinishi
    print(f"🔄 Teskari ko'rinishi: '{word[::-1]}'")