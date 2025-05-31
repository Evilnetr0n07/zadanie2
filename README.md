# Zadanie 2 – Budowa i publikacja obrazu Dockera z multi-architekturą oraz skanowaniem CVE

##Autor
Marek Zając

## Opis projektu

Repozytorium zawiera aplikację napisaną w Go oraz Dockerfile umożliwiający zbudowanie obrazu kontenera.

Celem zadania było przygotowanie pipeline'u GitHub Actions, który:

- buduje obraz Dockera dla dwóch architektur: `linux/amd64` oraz `linux/arm64`,
- wykorzystuje cache budowania obrazu przechowywane w publicznym repozytorium DockerHub,
- skanuje obraz pod kątem luk bezpieczeństwa (CVE) za pomocą Trivy,
- publikuje obraz tylko, gdy nie wykryto luk o wysokim lub krytycznym poziomie zagrożenia,
- publikuje obraz do publicznego repozytorium GitHub Container Registry (GHCR).

## Struktura repozytorium

- `main.go` – źródła aplikacji w Go
- `Dockerfile` – dwustopniowy build obrazu z multiarchitekturą
- `.github/workflows/docker-image.yml` – definicja pipeline'u GitHub Actions
- `templates/` – folder z szablonami HTML (jeśli dotyczy)

## Konfiguracja pipeline'u GitHub Actions

Workflow `docker-image.yml` realizuje następujące kroki:

1. Checkout kodu źródłowego.
2. Pobranie metadanych do generowania tagów (SHA skrócony i semver na podstawie tagu Git).
3. Konfiguracja QEMU i Buildx do multiarch buildów.
4. Logowanie do GitHub Container Registry (GHCR) i DockerHub (cache).
5. Budowanie obrazu z cache pobieranym i zapisywanym w publicznym repozytorium DockerHub (`zadanie2-cache`), co przyspiesza kolejne buildy.
6. Skanowanie obrazu narzędziem Trivy pod kątem luk krytycznych i wysokich.
7. Publikacja obrazu do GHCR tylko jeśli nie wykryto krytycznych zagrożeń.

## Tagowanie obrazów i cache

- Obrazy tagowane są automatycznie przez `docker/metadata-action`:
- `sha-<skrót_SHA>` — jednoznaczna identyfikacja buildów,
- `semver` — na podstawie tagów git w formacie `vX.Y.Z`.

- Cache builda przechowywany jest w publicznym repozytorium DockerHub `${{ vars.DOCKERHUB_USERNAME }}/zadanie2-cache`, umożliwiając szybkie budowanie na różnych maszynach.

## Wybór narzędzia do skanowania CVE

Użyto **Trivy** ze względu na:

- prostą integrację w CI/CD,
- automatyczne aktualizacje baz CVE,
- możliwość ustawienia progów zagrożeń,
- szerokie wsparcie i popularność w społeczności DevOps.

## Uruchomienie pipeline

- Wypchnięcie taga git w formacie `vX.Y.Z` automatycznie uruchamia pipeline i buduje oraz publikuje obraz.
- Możliwe jest także ręczne uruchomienie workflow w GitHub UI lub z CLI:

```bash
gh workflow run docker-image.yml
```
