# Implementierungsplan: Drehmoment Digital (V3 Relaunch)

Dieser Plan vereint den inhaltlichen Fokus auf Struktur mit einer tiefgehenden optischen Überarbeitung (Premium Vibe) und einem chirurgischen Code-Refactoring im Ordner `website`.

## User Review Required
> [!IMPORTANT]
> Der Plan liegt jetzt extrem detailliert vor, inklusive aller visuellen Upgrades (Header, Footer, Bento-Box Layout). Bitte lies dir Punkt 2 (Visuelle Analyse) und Punkt 3 durch. Wenn das exakt deine Vision ist, gib mir dein "Go" und ich fange an zu coden!

---

## 1. Inhaltliche Strategie & Die 3 Zielgruppen

**Der Markt-Kontext:** KFZ-Betriebe kämpfen mit Personalmangel und schlechten Aufträgen.
**Unsere Positionierung:** Wir verkaufen **Struktur, Kontrolle und Filterung**. Wir bauen das "digitale Ladenlokal".
**Die Goldene Regel:** Wir formulieren ausschließlich positiv (kein Bashing von mobile.de etc.).

### Die 3 Fokus-Profile (Die neuen Abschnitte)
* **Profil A (Mietwerkstatt):** "Entspannter arbeiten, Zeit und Nerven sparen." (Buchungssystem)
* **Profil B (Mischbetrieb):** "Volle Flexibilität für euren Handel." (Unabhängigkeit von Portalen)
* **Profil C (Neueinsteiger):** "Wir bauen erst das Fundament, dann die Werbeschilder."

*(Diese Profile werden organisch in die neue "Folien-Reihenfolge" integriert).*

---

## 2. Visuelle Analyse & UI-Upgrades (Neu)

Basierend auf unserer Analyse sieht die Seite noch nicht nach "Weltagentur" aus. Das ändern wir:

### A. Der Header & Das Logo
* **Ist-Zustand:** Semi-Sticky, stottert beim Scrollen, Logo-Proportionen wirken "gequetscht", Buttons sind langweilig.
* **Upgrade:** Wir bauen einen echten "Frosted-Glass" (Milchglas) Header, der durchgehend sanft mitscrollt. Das Logo bekommt perfekte Abstände (`padding` statt `margin-top:-15px`). Die Buttons im Header bekommen weiche Hover-Mikroanimationen (Magnetic-Style).

### B. Das Leistungspaket (Lösung)
* **Ist-Zustand:** Einfache, langweilige Kacheln, die sehr klobig wirken.
* **Upgrade:** Wir ersetzen die Kacheln durch ein **Bento-Box Layout** (wie bei Apple). Asymmetrische, wunderschön abgerundete Flächen mit sanften Schatten, die viel edler und aufgeräumter wirken.

### C. Die Reihenfolge (User Journey)
Wir strukturieren die "Folien" (Abschnitte) logischer:
1. **Hero (Start):** Maximaler Impact.
2. **Die 3 Profile (Neu):** Der Nutzer findet sich sofort wieder (Mietwerkstatt / Handel / Starter).
3. **Problem / Agitation:** Warum man jetzt digitalisieren muss.
4. **Lösung (Bento-Box):** Unser System.
5. **Projekte / Proof:** Die Live-Demos.
6. **Footer & Kontakt.**

### D. Der Footer
* **Ist-Zustand:** Unstrukturiert, unübersichtlich.
* **Upgrade:** Ein massiver, pechschwarzer Footer mit riesiger "STARTEN WIR DURCH"-Typografie, klar abgegrenzten rechtlichen Links und einem absolut premium wirkenden Abschluss der Seite.

---

## 3. Technische Umsetzung (Chirurgischer Eingriff)

### A. Git-Sicherung
- Ein "Git-Tresor" wurde im Ordner `website` eingerichtet, der Live-Stand ist gesichert.

### B. CSS & Code-Sauberkeit (Non-Destruktiv)
- **Inline-Styles eliminieren:** Das komplette Panzertape im HTML wird restlos entfernt und zentralisiert.
- **Bucket-Aufteilung:** Das CSS wird sicher und professionell in 5 Buckets zerschnitten (`01_variables.css` bis `05_sections.css`), um künftige Fehler zu vermeiden.

### C. Backend (Cloudflare)
- Formular an `/functions/mail` anbinden und Spam-Schutz (Honeypot) ergänzen.

---

## 4. Verifizierungs-Plan
Nach dem chirurgischen CSS-Umbau und den visuellen Upgrades öffnen wir die Seite lokal. Wir prüfen das Layout, die fließenden Animationen und die neuen Texte, bevor wir jemals über ein Deployment sprechen.
