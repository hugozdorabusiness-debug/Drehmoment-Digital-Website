import os
import re

new_footer = """<footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                
                <div class="footer-col" style="padding-right: 2rem;">
                    <img src="logo_transparent.png" alt="Drehmoment Digital" class="footer-logo" style="height: 140px; margin-bottom: 2rem;">
                    <p style="font-size: 1.1rem; line-height: 1.6;">Wir bringen deine Werkstatt auf die regionale Ideallinie. Präzise, messbar, marktführend.</p>
                </div>

                <div class="footer-col">
                    <h4>Navigation</h4>
                    <ul>
                        <li><a href="index.html">Startseite</a></li>
                        <li><a href="index.html#warum-wir">Philosophie</a></li>
                        <li><a href="index.html#loesung">Unser System</a></li>
                        <li><a href="deep-dive.html">Der Hebel</a></li>
                        <li><a href="index.html#prozess">Ablauf</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h4>Lösungen</h4>
                    <ul>
                        <li><a href="neueinsteiger.html">Freie Werkstätten</a></li>
                        <li><a href="mischbetrieb.html">Werkstatt & Handel</a></li>
                        <li><a href="mietwerkstatt.html">Mietwerkstatt</a></li>
                        <li><a href="uebernahme.html">Betriebsübergabe</a></li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h4>Kontakt</h4>
                    <ul>
                        <li><a href="https://wa.me/491633778849" target="_blank">0163 - 377 88 49</a></li>
                        <li><a href="mailto:kontakt@drehmoment-digital.de">kontakt@drehmoment-digital.de</a></li>
                        <li><br>Made along the A40 / NRW.</li>
                    </ul>
                </div>

                <div class="footer-col">
                    <h4>Rechtliches</h4>
                    <ul>
                        <li><a href="impressum.html">Impressum</a></li>
                        <li><a href="datenschutz.html">Datenschutz</a></li>
                        <li><a href="agb.html">AGB</a></li>
                    </ul>
                </div>

            </div>

            <div style="text-align: center; margin-top: 3rem; padding-bottom: 2rem; color: #475569; font-size: 0.95rem; font-weight: 500; letter-spacing: 1px;">
                &copy; 2026 DREHMOMENT DIGITAL. ALL RIGHTS RESERVED.
            </div>
        </div>
    </footer>"""

count = 0
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the existing footer block
        new_content, num_subs = re.subn(r'<footer class="site-footer">.*?</footer>', new_footer, content, flags=re.DOTALL)
        
        if num_subs > 0:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
            count += 1
        else:
            print(f"No footer found in {filename}")

print(f"Successfully updated footer in {count} files.")
