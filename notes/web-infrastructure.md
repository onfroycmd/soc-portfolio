# 🌍 Infrastruktura Webowa — Notatki SOC

## 13 — Front End vs Back End

| Typ | Gdzie działa | Widoczne |
|-----|-------------|---------|
| **Front End** | Przeglądarka | ✅ TAK |
| **Back End** | Serwer | ❌ NIE |

---

## 14 — Podstawowe tagi HTML

| Tag | Rola |
|-----|------|
| `<html>` | Główny pojemnik |
| `<head>` | Informacje o stronie (niewidoczne) |
| `<body>` | Treść strony |
| `<h1>` | Nagłówek |
| `<p>` | Akapit |
| `class` | Do stylizacji CSS |
| `id` | Unikalny identyfikator elementu |

---

## 15 — Infrastruktura Webowa

| Pojęcie | Co to jest |
|---------|-----------|
| **Load Balancer** | Rozdziela ruch między serwery. Jeśli jeden padnie — przełącza. |
| **CDN** | Kopie plików na serwerach na świecie — dostajesz z najbliższego. |
| **WAF** | Blokuje hakerów, boty i DDoS przed serwerem. |
| **Baza danych** | MySQL, MongoDB, PostgreSQL |
| **Round-Robin** | Load balancer wysyła po kolei: 1→2→3→1→2→3 |
| **Health Check** | Load balancer sprawdza czy serwery działają |

---

## 16 — Serwery WWW

| Pojęcie | Opis |
|---------|------|
| **Serwer WWW** | Apache, Nginx, IIS — nasłuchuje i serwuje pliki |
| **Virtual Host** | Jeden serwer obsługuje wiele domen |
| **Treść statyczna** | Pliki serwowane bez zmian (obrazy, CSS) |
| **Treść dynamiczna** | Generowana w locie przez backend |

> ⚠️ Backend przetwarza dane użytkownika — błędy = **SQL Injection**, **XSS**

---

## 17 — Wirtualizacja

**VM vs Kontener:**

| | VM | Kontener |
|-|----|---------|
| System OS | Własny, pełny | Dzieli z hostem |
| Czas startu | Minuty | Sekundy |
| Użycie | Testowanie malware, inny OS | Szybkie wdrożenia |

**Hypervisor:**

| Typ | Działa na | Przykłady |
|-----|----------|----------|
| Typ 1 | Sprzęcie bezpośrednio | VMware ESXi, Hyper-V |
| Typ 2 | Systemie operacyjnym | VirtualBox, VMware Workstation |

> 🔒 Izolowane środowisko VM = bezpieczne testowanie malware

---

## 18 — Chmura Obliczeniowa

| Model | Analogia | Przykład |
|-------|---------|---------|
| **IaaS** | Puste mieszkanie — zarządzasz wszystkim | AWS EC2 |
| **PaaS** | Umeblowane mieszkanie — skupiasz się na aplikacji | Google App Engine |
| **SaaS** | Hotel — używasz przez przeglądarkę | Gmail, Zoom |

**Dostawcy:**

| Firma | Dla kogo |
|-------|---------|
| **AWS** | Największy, globalny |
| **Azure** | Korporacje, chmury hybrydowe |
| **Google Cloud** | AI i analiza danych |
