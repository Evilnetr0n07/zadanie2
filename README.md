## Tagowanie i cache

Obrazy oznaczane są tagiem `latest` oraz wysyłane do:

- `ghcr.io/<user>/zadanie1-app:latest` – główny obraz aplikacji
- Cache buildera zapisywany jest w:
  - `docker.io/<user>/zadanie1-cache:cache`

Zastosowano `mode=max`, aby maksymalnie wykorzystywać wspólne warstwy. Dzięki temu przebudowy są szybsze, a obrazy mniejsze.

Źródło: [Docker BuildKit cache reference](https://docs.docker.com/build/cache/backends/)

## Skanowanie CVE

Zastosowano **Trivy**, ponieważ:
- Jest darmowy, open source, bezpośrednio zintegrowany z GH Actions.
- Pozwala zablokować publikację, jeśli występują krytyczne CVE.

Źródło: [Trivy GitHub Action](https://github.com/aquasecurity/trivy-action)

