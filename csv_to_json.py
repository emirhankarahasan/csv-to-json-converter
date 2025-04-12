import csv
import json

csv_file = "strings.csv"
json_file = "strings_tr.json"

try:
    with open(csv_file, "r", encoding="cp1254") as f:
        reader = csv.DictReader(f)
        print("✅ CSV dosyası başarıyla açıldı.")
        print(f"🔍 Bulunan başlıklar: {reader.fieldnames}")
        
        data = {}
        missing_translations = []  # Eksik çevirileri tutacak liste
        for row in reader:
            key = row.get("key")
            tr = row.get("tr_text")
            
            if key:
                if tr:  # Eğer Türkçe çeviri varsa
                    data[key] = tr
                else:  # Eğer Türkçe çeviri yoksa
                    missing_translations.append(key)

    # JSON dosyasını oluştur
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"🎉 Dönüştürme tamamlandı → {json_file}")

    # Eksik çevirileri yazdır
    if missing_translations:
        print("\n❌ Eksik Çeviriler:")
        for key in missing_translations:
            print(f" - {key}")
    else:
        print("✅ Tüm çeviriler mevcut!")

except KeyError as e:
    print(f"❌ HATA: '{e.args[0]}' başlığı CSV dosyanda bulunamadı.")
    print("Lütfen ilk satırın şu şekilde olduğundan emin ol: ")
    print("key,text,tr_text")

except FileNotFoundError:
    print(f"❌ HATA: {csv_file} bulunamadı. Dosya ismini ve dizini kontrol et.")
