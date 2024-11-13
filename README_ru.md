<!--
Важно: этот README был автоматически сгенерирован <https://github.com/YunoHost/apps/tree/master/tools/readme_generator>
Он НЕ ДОЛЖЕН редактироваться вручную.
-->

# Apache Superset для YunoHost

[![Уровень интеграции](https://dash.yunohost.org/integration/superset.svg)](https://ci-apps.yunohost.org/ci/apps/superset/) ![Состояние работы](https://ci-apps.yunohost.org/ci/badges/superset.status.svg) ![Состояние сопровождения](https://ci-apps.yunohost.org/ci/badges/superset.maintain.svg)

[![Установите Apache Superset с YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=superset)

*[Прочтите этот README на других языках.](./ALL_README.md)*

> *Этот пакет позволяет Вам установить Apache Superset быстро и просто на YunoHost-сервер.*  
> *Если у Вас нет YunoHost, пожалуйста, посмотрите [инструкцию](https://yunohost.org/install), чтобы узнать, как установить его.*

## Обзор

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


**Поставляемая версия:** 4.1.0~ynh1

## Снимки экрана

![Снимок экрана Apache Superset](./doc/screenshots/explore.jpg)

## Документация и ресурсы

- Официальный веб-сайт приложения: <https://superset.apache.org/>
- Официальная документация администратора: <https://superset.apache.org/docs/intro>
- Репозиторий кода главной ветки приложения: <https://github.com/apache/superset>
- Магазин YunoHost: <https://apps.yunohost.org/app/superset>
- Сообщите об ошибке: <https://github.com/YunoHost-Apps/superset_ynh/issues>

## Информация для разработчиков

Пришлите Ваш запрос на слияние в [ветку `testing`](https://github.com/YunoHost-Apps/superset_ynh/tree/testing).

Чтобы попробовать ветку `testing`, пожалуйста, сделайте что-то вроде этого:

```bash
sudo yunohost app install https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
или
sudo yunohost app upgrade superset -u https://github.com/YunoHost-Apps/superset_ynh/tree/testing --debug
```

**Больше информации о пакетировании приложений:** <https://yunohost.org/packaging_apps>
