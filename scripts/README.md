# ⚙️ Scripts

Skrypty do automatyzacji pracy SOC analityka.

| Skrypt | Co robi | Status |
|--------|---------|--------|
| [port-scanner.py](./port-scanner.py) | Skanuje otwarte porty na danym IP | ✅ |
| *(wkrótce)* ioc-checker.py | Sprawdza IP/hash w VirusTotal | ⬜ |

---

## port-scanner.py

**Cel:** Sprawdzenie które porty są otwarte na danym hoście — podstawowy rekonesans sieci.

**Narzędzie:** Python — biblioteka `socket`

**Skanowane porty:**

| Port | Usługa |
|------|--------|
| 21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 3389 | RDP |
| 8080 | HTTP alternatywny |

**Wyniki testu na `192.168.1.1` (router lokalny):**

[OTWARTY]  Port 53 — DNS
[OTWARTY]  Port 80 — HTTP (panel admina routera)
[OTWARTY]  Port 443 — HTTPS
**Wnioski:** Router lokalny wystawia DNS, HTTP i HTTPS — typowa konfiguracja. 
Otwarte porty 80/443 oznaczają dostępny panel administracyjny.
