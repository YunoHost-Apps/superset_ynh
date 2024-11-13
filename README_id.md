<!--
N.B.: README ini dibuat secara otomatis oleh <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Ini TIDAK boleh diedit dengan tangan.
-->

# Apache Superset untuk YunoHost

[![Tingkat integrasi](https://dash.yunohost.org/integration/superset.svg)](https://ci-apps.yunohost.org/ci/apps/superset/) ![Status kerja](https://ci-apps.yunohost.org/ci/badges/superset.status.svg) ![Status pemeliharaan](https://ci-apps.yunohost.org/ci/badges/superset.maintain.svg)

[![Pasang Apache Superset dengan YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Baca README ini dengan bahasa yang lain.](./ALL_README.md)*

> *Paket ini memperbolehkan Anda untuk memasang Apache Superset secara cepat dan mudah pada server YunoHost.*  
> *Bila Anda tidak mempunyai YunoHost, silakan berkonsultasi dengan [panduan](https://yunohost.org/install) untuk mempelajari bagaimana untuk memasangnya.*

## Ringkasan

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


**Versi terkirim:** 4.1.0~ynh1

## Tangkapan Layar

![Tangkapan Layar pada Apache Superset](./doc/screenshots/explore.jpg)

## Dokumentasi dan sumber daya

- Website aplikasi resmi: <https://superset.apache.org/>
- Dokumentasi admin resmi: <https://superset.apache.org/docs/intro>
- Depot kode aplikasi hulu: <https://github.com/apache/superset>
- Gudang YunoHost: <https://apps.yunohost.org/app/superset>
- Laporkan bug: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Info developer

Silakan kirim pull request ke [`testing` branch](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Untuk mencoba branch `testing`, silakan dilanjutkan seperti:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
atau
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Info lebih lanjut mengenai pemaketan aplikasi:** <https://yunohost.org/packaging_apps>
