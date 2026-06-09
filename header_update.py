import os
import re

html_files = {
    'index.html': {'active': []},
    'deep-dive.html': {'active': ['nav-hebel']},
    'neueinsteiger.html': {'active': ['nav-zielgruppen', 'sub-neueinsteiger'], 'back_btn': True},
    'mischbetrieb.html': {'active': ['nav-zielgruppen', 'sub-mischbetrieb'], 'back_btn': True},
    'mietwerkstatt.html': {'active': ['nav-zielgruppen', 'sub-mietwerkstatt'], 'back_btn': True}
}

# deep-dive needs back button too!
html_files['deep-dive.html']['back_btn'] = True

header_template = """    <!-- ================== HEADER ================== -->
    <header class="site-header">
        <div class="header-inner">
            <div class="header-left">
{back_btn_html}
                <a href="index.html" class="logo-link">
                    <img src="./drehmoment_digital_transparent-removeb ohne supslogan.png" alt="Drehmoment Digital Logo" class="header-logo-img">
                </a>
            </div>
            <nav class="nav-links">
                <a href="index.html">Start</a>
                <a href="index.html#warum-wir">Warum wir?</a>
                <a href="deep-dive.html" class="nav-hebel{act_hebel}">Der Hebel</a>
                
                <div class="nav-dropdown">
                    <a href="index.html#zielgruppen" class="dropdown-trigger nav-zielgruppen{act_ziel}">Für wen?</a>
                    <div class="dropdown-menu">
                        <a href="neueinsteiger.html" class="sub-neueinsteiger{act_neu}">Der Neueinsteiger</a>
                        <a href="mischbetrieb.html" class="sub-mischbetrieb{act_misch}">Werkstatt & Handel</a>
                        <a href="mietwerkstatt.html" class="sub-mietwerkstatt{act_miet}">Mietwerkstätten</a>
                    </div>
                </div>
                
                <a href="index.html#prozess">Prozess</a>
                <a href="index.html#loesung">System</a>
                <a href="index.html#projekte">Projekte</a>
            </nav>
            <div class="cta-nav">
                <a href="index.html#kontakt" class="btn-primary">JETZT KONTAKT AUFNEHMEN &rarr;</a>
            </div>
            <button class="mobile-nav-toggle" aria-label="Menü öffnen"><span></span><span></span><span></span></button>
        </div>
    </header>"""

back_html = """                <a href="javascript:history.back()" class="back-btn" title="Zurück">
                    <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
                    Zurück
                </a>"""

for file, config in html_files.items():
    if not os.path.exists(file): continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    b_html = back_html if config.get('back_btn') else ""
    act_h = " active" if "nav-hebel" in config['active'] else ""
    act_z = " active" if "nav-zielgruppen" in config['active'] else ""
    act_n = " active" if "sub-neueinsteiger" in config['active'] else ""
    act_m = " active" if "sub-mischbetrieb" in config['active'] else ""
    act_mi = " active" if "sub-mietwerkstatt" in config['active'] else ""
    
    new_header = header_template.format(
        back_btn_html=b_html,
        act_hebel=act_h, act_ziel=act_z, act_neu=act_n, act_misch=act_m, act_mi=act_mi
    )
    
    # regex replace header
    # From <header class="site-header"> to </header>
    new_content = re.sub(r'<!-- =* HEADER =* -->\s*<header class="site-header">.*?</header>', new_header, content, flags=re.DOTALL)
    # also try without comments
    new_content = re.sub(r'<header class="site-header">.*?</header>', new_header, new_content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated {file}")
