# 💻 System Operacyjny — Notatki SOC

## 19 — System Operacyjny — Co to Jest

> OS = niewidzialny menedżer komputera. Działa między Tobą, aplikacjami a sprzętem.

| Funkcja | Co to znaczy |
|---------|-------------|
| Uruchamia programy | Otwiera i zamyka aplikacje |
| Zarządza pamięcią | Pilnuje żeby programy sobie nie przeszkadzały |
| Obsługuje urządzenia | Klawiatura, mysz, ekran |
| Zarządza plikami | Zapisuje i odczytuje dane z dysku |

---

## 20 — Pięć Obowiązków OS

| # | Obowiązek | SOC Alert |
|---|-----------|----------|
| 1 | **Zarządzanie procesami** | Nieznany proces = możliwy **malware** |
| 2 | **Zarządzanie pamięcią (RAM)** | Gdy brakuje → pamięć wirtualna (dysk) |
| 3 | **Zarządzanie plikami** | Uprawnienia "tylko do odczytu" chronią pliki systemowe |
| 4 | **Zarządzanie użytkownikami** | Nieautoryzowane konto = **kompromitacja systemu** |
| 5 | **Zarządzanie urządzeniami** | OS automatycznie rozpoznaje nowy sprzęt |

---

## 21 — Przestrzeń Jądra vs Przestrzeń Użytkownika

| | Przestrzeń jądra | Przestrzeń użytkownika |
|-|-----------------|----------------------|
| Dostęp do sprzętu | ✅ Pełny | ❌ Tylko przez syscall |
| Kto działa | Kernel i sterowniki | Wszystkie aplikacje |
| Błąd = | Crash całego systemu | Pada tylko ta aplikacja |

```
Aplikacja → Syscall → Kernel sprawdza → Kernel wykonuje → Wynik wraca
```

> 🚨 **Kernel exploit** = atak na jądro = pełne przejęcie maszyny — najgroźniejszy typ ataku!

---

## 22 — OS jako Fundament Bezpieczeństwa

| Mechanizm | Co robi | SOC Alert |
|-----------|---------|----------|
| **Uwierzytelnianie** | Weryfikuje kim jesteś | Wiele nieudanych logowań = **brute force** |
| **Uprawnienia** | Kontroluje co możesz robić | Zwykły user z uprawnieniami admina = **eskalacja uprawnień** |
| **Izolacja** | Każdy program w swoim "pudełku" | Wirus w przeglądarce nie sięga do plików systemowych |
| **Ochrona systemu** | Blokuje zmiany w krytycznych plikach | Malware ma utrudnione nadpisanie plików |

**Ściągawka:**

| Pojęcie | Co to znaczy |
|---------|-------------|
| **OS** | Menedżer całego komputera |
| **Kernel** | Serce OS — pełna władza nad sprzętem |
| **Syscall** | Sposób w jaki aplikacja prosi kernel o pomoc |
| **Kernel exploit** | Atak na jądro = pełne przejęcie systemu |
| **Eskalacja uprawnień** | Zdobycie wyższych uprawnień niż dozwolone |
