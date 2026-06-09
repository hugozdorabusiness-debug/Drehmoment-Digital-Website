$newFooter = @"
<footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                
                <div class="footer-col" style="padding-right: 2rem;">
                    <img src="logo_transparent.png" alt="Drehmoment Digital" class="footer-logo" style="height: 140px; margin-bottom: 2rem;">
                    <p style="font-size: 1.1rem; line-height: 1.6;">Wir bringen deine Werkstatt auf die regionale Ideallinie. Pr&auml;zise, messbar, marktf&uuml;hrend.</p>
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
                    <h4>L&ouml;sungen</h4>
                    <ul>
                        <li><a href="neueinsteiger.html">Freie Werkst&auml;tten</a></li>
                        <li><a href="mischbetrieb.html">Werkstatt & Handel</a></li>
                        <li><a href="mietwerkstatt.html">Mietwerkstatt</a></li>
                        <li><a href="uebernahme.html">Betriebs&uuml;bergabe</a></li>
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
    </footer>
"@

Get-ChildItem -Filter *.html | ForEach-Object {
    $content = Get-Content -Raw $_.FullName
    $newContent = $content -replace '(?s)<footer class="site-footer">.*?</footer>', $newFooter
    if ($content -cne $newContent) {
        Set-Content -Path $_.FullName -Value $newContent -Encoding UTF8
        Write-Host "Updated $($_.Name)"
    } else {
        Write-Host "No footer found or already updated in $($_.Name)"
    }
}
