# 🌐 Sieci — Notatki SOC

## Adresy IP

| Typ | Do czego służy | Przykład |
|-----|---------------|---------|
| **Publiczny** | Identyfikuje urządzenie w Internecie | `89.64.12.44` |
| **Prywatny** | Identyfikuje urządzenie w sieci lokalnej (LAN) | `192.168.1.1` |

## Adres MAC

```
a4:c3:f0 : 85:ac:2d
└──────┘   └──────┘
Producent   Unikalny numer urządzenia
```

## Ping — ICMP

Ping używa pakietów ICMP do sprawdzenia jakości połączenia.

```bash
ping 192.168.1.254
# Wysłano: 6 pakietów | Odebrano: 6 | Utracono: 0 | Średni czas: 4.16 ms
```

## Rekordy DNS

| Rekord | Do czego służy |
|--------|---------------|
| **A** | Adres IPv4 |
| **AAAA** | Adres IPv6 |
| **CNAME** | Przekierowanie na inną domenę |
| **MX** | Serwer obsługujący e-maile |
| **TXT** | Weryfikacja domeny i antyspam |

## Jak działa DNS

```
Ty → Cache komputera → DNS ISP → Root DNS → Serwer TLD → Serwer domeny → ✅
```

> ⚠️ Twój ISP widzi każde zapytanie DNS. Możesz zmienić na `1.1.1.1` (Cloudflare).

## Metody HTTP i alerty SOC

| Metoda | Co robi |
|--------|---------|
| GET | Pobiera dane |
| POST | Wysyła nowe dane |
| PUT | Aktualizuje dane |
| DELETE | Usuwa dane |

> 🚨 Dużo POST na /login → **brute force** | Dużo DELETE od jednego IP → **podejrzane**

## Kody HTTP i alerty SOC

| Kod | Znaczenie |
|-----|----------|
| 200 | OK |
| 301/302 | Przekierowanie |
| 401 | Wymaga logowania |
| 403 | Brak uprawnień |
| 404 | Nie znaleziono |
| 500 | Błąd serwera |

> 🚨 Dużo 404 od jednego IP → **skanowanie** | Dużo 401/403 → **próba włamania**

## Nagłówki HTTP — SOC Alert

> 🚨 `User-Agent: python-requests` → może być skrypt/bot
> 🚨 Brak nagłówka `Host` → podejrzane
> 🚨 Dziwne `Cookie` → może być **session hijack**
