# 💻 System Operacyjny — Notatki SOC

## OS jako menedżer komputera

> OS działa między Tobą, aplikacjami a sprzętem. Bez niego komputer to kupka plastiku.

| Funkcja OS | Co to znaczy |
|-----------|-------------|
| Zarządzanie procesami | Uruchamia i zamyka aplikacje |
| Zarządzanie pamięcią (RAM) | Każda aplikacja dostaje swój obszar |
| Zarządzanie plikami | Wie gdzie leży każdy plik |
| Zarządzanie użytkownikami | Twoje pliki niewidoczne dla innych kont |
| Zarządzanie urządzeniami | Automatycznie rozpoznaje mysz, pendrive |

## Kernel vs Przestrzeń użytkownika

| | Przestrzeń jądra | Przestrzeń użytkownika |
|-|-----------------|----------------------|
| Dostęp do sprzętu | ✅ Pełny | ❌ Tylko przez syscall |
| Kto działa | Kernel i sterowniki | Wszystkie aplikacje |
| Błąd = | Crash całego systemu | Pada tylko ta aplikacja |

```
Aplikacja → Wywołanie systemowe (syscall) → Kernel sprawdza → Kernel wykonuje → Wynik
```

## Mechanizmy bezpieczeństwa OS

| Mechanizm | SOC Alert |
|-----------|----------|
| Uwierzytelnianie | Wiele nieudanych logowań = **brute force** |
| Uprawnienia | Zwykły user z uprawnieniami admina = **eskalacja uprawnień** |
| Izolacja procesów | Wirus w przeglądarce nie sięga do plików systemowych |
| Ochrona systemu | Malware ma utrudnione nadpisanie plików systemowych |

> 🚨 **Kernel exploit** = atak na jądro = pełne przejęcie maszyny — najgroźniejszy typ ataku!
