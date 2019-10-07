print("Moin Moin")
name = input("Name bidde: ")
print("Das merke ich mir", name)

anzahl = int(input("Wie viel Zigaretten rauchst Du am Tag? "))
anzahlmonat = anzahl * 30
anzahljahr = anzahl * 365
print("Das sind", anzahlmonat, "im Monat", "und", anzahljahr, "im Jahr,")
uebertrieben = 30
gelogen = 10

if anzahl <= gelogen:
    print("erzähl mir kein Scheiss, Du rauchst mehr!")
    print(name, "erzähl meinem Programm keinen Unsinn.")

elif anzahl <= uebertrieben:
    print("so hätte ich Dich auch eingeschätzt.")
    print("Weniger rauchen", name,
          "weil eine Zigarette so viel Feinstaub erzeugt wie eine 10km Autofahrt.")

elif anzahl > uebertrieben:
    print("Deeeega ganz schön viel!")
    print("In jedem Fall weniger rauchen", name)
