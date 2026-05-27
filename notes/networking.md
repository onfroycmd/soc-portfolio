# 🌐 Sieci — Notatki SOC

## 01 — IDS

**IDS** (Intrusion Detection System) = system wykrywający nieautoryzowany dostęp do sieci lub systemu.

- Wykrywanie nieautoryzowanych urządzeń w sieci
- Wykrywanie nieautoryzowanego dostępu do plików

---

## 02 — Adresy IP

| Typ | Do czego służy | Przykład |
|-----|---------------|---------|
| **Publiczny** | Identyfikuje urządzenie w Internecie | `89.64.12.44` |
| **Prywatny** | Identyfikuje urządzenie w sieci lokalnej (LAN) | `192.168.1.1` |

---

## 03 — Adres MAC

```
a4:c3:f0 : 85:ac:2d
└──────┘   └──────┘
Producent   Unikalny numer urządzenia
```

---

## 04 — Ping — ICMP

Ping używa pakietów **ICMP** do sprawdzenia jakości połączenia.

```bash
ping 192.168.1.254
# Wysłano: 6 | Odebrano: 6 | Utracono: 0 | Średni czas: 4.16 ms
```

---

## 05 — Rekordy DNS

| Rekord | Do czego służy |
|--------|---------------|
| **A** | Adres IPv4 |
| **AAAA** | Adres IPv6 |
| **CNAME** | Przekierowanie na inną domenę |
| **MX** | Serwer obsługujący e-maile |
| **TXT** | Weryfikacja domeny i antyspam |

---

## 06 — Jak działa DNS

```
Ty → Cache komputera → DNS ISP → Root DNS → Serwer TLD → Serwer domeny → ✅
```

| Typ DNS | Rola |
|---------|------|
| **Rekurencyjny** | Szuka odpowiedzi w Twoim imieniu |
| **Autorytatywny** | Zna oficjalną, prawdziwą odpowiedź |

> ⚠️ Twój ISP widzi każde zapytanie DNS. Możesz zmienić na `1.1.1.1` (Cloudflare).

---

## 07 — Budowa URL

```
http://user:password@tryhackme.com:80/view-room?id=1#task3
  │       │              │          │      │       │    │
Schemat  Użytk.        Domena     Port  Ścieżka  Query Fragment
```

| Część | Przykład | Co oznacza |
|-------|---------|-----------|
| Schemat | `http://` | Protokół (HTTP, HTTPS, FTP) |
| Host | `tryhackme.com` | Adres serwera |
| Port | `:80` | HTTP=80, HTTPS=443 |
| Ścieżka | `/view-room` | Konkretna strona |
| Query | `?id=1` | Dodatkowe parametry |
| Fragment | `#task3` | Konkretne miejsce na stronie |

---

## 08 — Żądanie HTTP

```http
GET / HTTP/1.1
Host: tryhackme.com
User-Agent: Mozilla/5.0 Firefox/87.0
Referer: https://tryhackme.com/
```

| Linia | Co oznacza |
|-------|-----------|
| `GET / HTTP/1.1` | Pobierz stronę główną, wersja HTTP 1.1 |
| `Host` | Której domeny chcesz |
| `User-Agent` | Jakiej przeglądarki używasz |
| `Referer` | Skąd przychodzisz |

---

## 09 — Odpowiedź HTTP

```http
HTTP/1.1 200 OK
Server: nginx/1.15.8
Content-Type: text/html
Content-Length: 98
```

---

## 10 — Metody HTTP

| Metoda | Co robi |
|--------|---------|
| **GET** | Pobiera dane |
| **POST** | Wysyła nowe dane |
| **PUT** | Aktualizuje dane |
| **DELETE** | Usuwa dane |

> 🚨 Dużo POST na /login → **brute force**
> 🚨 Dużo DELETE od jednego IP → **podejrzane**
> 🚨 PUT na plik systemowy → **próba nadpisania pliku**

---

## 11 — Kody HTTP

| Zakres | Znaczenie |
|--------|----------|
| **2xx** | ✅ Sukces |
| **3xx** | ➡️ Przekierowanie |
| **4xx** | ❌ Błąd klienta |
| **5xx** | 💥 Błąd serwera |

| Kod | Znaczenie |
|-----|----------|
| 200 | OK |
| 301 | Przekierowanie trwałe |
| 401 | Wymaga logowania |
| 403 | Brak uprawnień |
| 404 | Nie znaleziono |
| 500 | Błąd serwera |

> 🚨 Dużo 404 od jednego IP → **skanowanie**
> 🚨 Dużo 401/403 → **próba włamania**

---

## 12 — Nagłówki HTTP

**Nagłówki żądania:**

| Nagłówek | Co robi |
|----------|---------|
| `Host` | Której strony chcesz |
| `User-Agent` | Jaka przeglądarka/program |
| `Cookie` | Dane zapisane przez serwer |

**Nagłówki odpowiedzi:**

| Nagłówek | Co robi |
|----------|---------|
| `Set-Cookie` | Serwer zapisuje ciasteczko |
| `Content-Type` | Typ zwracanej zawartości |

> 🚨 `User-Agent: python-requests` → może być skrypt/bot
> 🚨 Dziwne `Cookie` → może być **session hijack**
