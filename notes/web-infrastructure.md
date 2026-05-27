# 🌍 Infrastruktura Webowa — Notatki SOC

## Komponenty

| Pojęcie | Co to jest |
|---------|-----------|
| **Load Balancer** | Rozdziela ruch między wiele serwerów. Jeśli serwer padnie — przełącza. |
| **CDN** | Kopie plików na serwerach na całym świecie — dostajesz z najbliższego. |
| **WAF** | Blokuje hakerów, boty i ataki DDoS przed serwerem. |
| **Baza danych** | MySQL, MongoDB, PostgreSQL — przechowuje dane aplikacji. |

## Wirtualizacja

| | VM | Kontener |
|-|----|---------|
| System OS | Własny, pełny | Dzieli z hostem |
| Czas startu | Minuty | Sekundy |
| Użycie | Testowanie malware, inny OS | Szybkie wdrożenia |

## Chmura — modele usług

| Model | Analogia | Przykład |
|-------|---------|---------|
| IaaS | Puste mieszkanie — zarządzasz wszystkim | AWS EC2 |
| PaaS | Umeblowane mieszkanie — skupiasz się na aplikacji | Google App Engine |
| SaaS | Hotel — używasz przez przeglądarkę | Gmail, Zoom |

## Serwery WWW

- Apache, Nginx, IIS — nasłuchują połączeń i serwują pliki
- Jeden serwer może hostować wiele domen (Virtual Host)
- Treść statyczna = pliki bez zmian | Dynamiczna = generowana w locie

> ⚠️ Backend przetwarza dane użytkownika — błędy prowadzą do **SQL Injection**, **XSS**
