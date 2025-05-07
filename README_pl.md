<!--
To README zostało automatycznie wygenerowane przez <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Nie powinno być ono edytowane ręcznie.
-->

# Apache Superset dla YunoHost

[![Poziom integracji](https://apps.yunohost.org/badge/integration/superset)](https://ci-apps.yunohost.org/ci/apps/superset/)
![Status działania](https://apps.yunohost.org/badge/state/superset)
![Status utrzymania](https://apps.yunohost.org/badge/maintained/superset)

[![Zainstaluj Apache Superset z YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Przeczytaj plik README w innym języku.](./ALL_README.md)*

> *Ta aplikacja pozwala na szybką i prostą instalację Apache Superset na serwerze YunoHost.*  
> *Jeżeli nie masz YunoHost zapoznaj się z [poradnikiem](https://yunohost.org/install) instalacji.*

## Przegląd

Superset is a modern data exploration and data visualization platform. Superset can replace or augment proprietary business intelligence tools for many teams. Superset integrates well with a variety of data sources.

Superset provides:

- A no-code interface for building charts quickly
- A powerful, web-based SQL Editor for advanced querying
- A lightweight semantic layer for quickly defining custom dimensions and metrics
- Out of the box support for nearly any SQL database or data engine
- A wide array of beautiful visualizations to showcase your data, ranging from simple bar charts to geospatial visualizations
- Lightweight, configurable caching layer to help ease database load
- Highly extensible security roles and authentication options
- An API for programmatic customization
- A cloud-native architecture designed from the ground up for scale

*-- Superset's Github repository*


**Dostarczona wersja:** 4.1.2~ynh1

## Zrzuty ekranu

![Zrzut ekranu z Apache Superset](./doc/screenshots/explore.jpg)

## Dokumentacja i zasoby

- Oficjalna strona aplikacji: <https://superset.apache.org/>
- Oficjalna dokumentacja dla administratora: <https://superset.apache.org/docs/intro>
- Repozytorium z kodem źródłowym: <https://github.com/apache/superset>
- Sklep YunoHost: <https://apps.yunohost.org/app/superset>
- Zgłaszanie błędów: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Informacje od twórców

Wyślij swój pull request do [gałęzi `testing`](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Aby wypróbować gałąź `testing` postępuj zgodnie z instrukcjami:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
lub
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Więcej informacji o tworzeniu paczek aplikacji:** <https://yunohost.org/packaging_apps>
