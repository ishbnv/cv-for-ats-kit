# MASTER_FACTS — единый источник правды о кандидате (Иван Шабанов)

> Версия 1.0 · 3 сентября 2026. Всё, что можно писать в CV, письмах и сообщениях, берётся ТОЛЬКО отсюда.
> Если вакансия требует факт, которого здесь нет, — его не выдумывают, а называют пробелом в итоговой сводке.
> Обновлять файл, а не память чата: новый факт → сюда, потом в проект.

## 0. Правила правды

- Факт можно использовать, если он есть в разделах 1–10. Формулировку менять можно, число и смысл — нет.
- Числа из раздела 6 «Канон цифр» — единственно допустимые. Оценочные цифры подаются со смягчением («about», «roughly», «около»).
- Раздел 5 «Не заявлять» важнее любого требования вакансии.
- Привязка факта к месту работы фиксирована в разделе 4; не переносить факт между работами.

## 1. Шапка

- Имя: EN «Ivan Shabanov» · RU «Иван Шабанов»
- Контакты (все — кликабельные ссылки): ivan@ishbnv.dev (mailto:ivan@ishbnv.dev) · +374 77 719 518 (tel:+37477719518) · linkedin.com/in/ishbnv (https://www.linkedin.com/in/ishbnv) · github.com/ishbnv (https://github.com/ishbnv) · ishbnv.dev (https://ishbnv.dev)
- Строка локации, вариант «релокация» (офисные или гибридные вакансии в EU/UK/Израиле):
  EN «Yerevan, Armenia (GMT+4) · Open to relocation (EU / UK / Israel) · Remote-ready, full EU overlap»
  RU «Ереван, Армения (GMT+4) · Готов к релокации (EU / UK / Израиль) · Удалённо, полное совпадение с рабочим днём EU»
- Строка локации, вариант «remote» (удалённые вакансии):
  EN «Yerevan, Armenia (GMT+4) · Remote · B2B contract or EOR · Full overlap with EU hours»
  RU «Ереван, Армения (GMT+4) · Удалённо · B2B-контракт / EOR / ИП · Полное совпадение с рабочим днём EU и МСК»
- Строка локации под конкретный город (офисная вакансия в одном городе): «Yerevan, Armenia (GMT+4) · Ready to relocate to <City>, <Country> · Remote until relocation, full EU overlap» / «Ереван, Армения (GMT+4) · Готов к переезду в <Город> · До переезда удалённо». Список стран, куда релокация подтверждена: EU (включая Кипр, Нидерланды, Германию, Польшу, Чехию, Эстонию), UK, Израиль.
- Наименование текущего работодателя: полное «Alfa-Dengi (Alfa-Bank ecosystem) via GIDFINANCE» (по умолчанию) или нейтральное «Alfa-Dengi via GIDFINANCE» (для компаний с жёстким санкционным комплаенсом, по запросу пользователя). Строка о компании — дословно как в резюме (см. §3), без чисел по составу команды.
- Состав команд (сколько человек, сколько инженеров в SODA или в Альфа-Деньгах) в документах НЕ указывать — кандидат расскажет на интервью. Единственное число про команду, которое остаётся: «возглавил команду из 3 инженеров» на продукте кредитных отчётов.
- Опыт всего: «4+ years» (авг. 2022 — наст. время). Никогда не писать «5+», «6+», «8+».
- Стаж LLM-систем: 3 года (с 2023). AI coding agents в командном процессе: 2 года.

## 2. Позиционирование (пресеты A–F): заголовок, хвост, summary

### A · Senior Full-Stack Engineer
- title: EN «Senior Full-Stack Engineer» · RU «Senior Full-Stack Engineer»
- tail: EN «TypeScript / Node.js / React · Fintech & AI Agents» · RU «TypeScript / Node.js / React · Финтех и AI-агенты»
- теги для отбора буллетов (по приоритету): FS, BE, LEAD, AI, FIN, GROWTH; лимит буллетов: Alfa 5, Appbooster 3, SODA 4; порядок блоков навыков: core → backend → frontend → ai → infra → process; open-source: да
- summary EN: Senior Full-Stack Engineer with 4+ years shipping revenue-critical products in fintech and marketing tech on TypeScript, Node.js (NestJS) and React. Led a 3-engineer team to launch a credit-report product that turned profitable in its first week (+40% net profit); built an AI lead-processing channel that tripled monthly revenue to ~$141K. Owns features end to end: data model, API, UI, CI/CD, observability.
- summary RU: Senior Full-Stack Engineer, 4+ года разработки продуктов с прямым влиянием на выручку в финтехе и маркетинговых платформах: TypeScript, Node.js (NestJS), React. Возглавил команду из 3 инженеров, запустившую продукт кредитных отчётов, который окупился за первую неделю (+40% к чистой прибыли); построил AI-канал обработки лидов, утроивший месячную выручку до ~$141K. Закрывает фичи целиком: модель данных, API, интерфейс, CI/CD, наблюдаемость.

### B · Senior Backend Engineer
- title: EN «Senior Backend Engineer» · RU «Senior Backend Engineer»
- tail: EN «Node.js / TypeScript · Kafka, PostgreSQL, Kubernetes · Fintech» · RU «Node.js / TypeScript · Kafka, PostgreSQL, Kubernetes · Финтех»
- теги для отбора буллетов (по приоритету): BE, FIN, LEAD, AI, FS, GROWTH; лимит буллетов: Alfa 5, Appbooster 2, SODA 4; порядок блоков навыков: core → backend → infra → ai → frontend → process; open-source: да
- summary EN: Senior Backend Engineer with 4+ years building high-load Node.js/TypeScript services in fintech: NestJS, PostgreSQL, Redis, Apache Kafka, Kubernetes. Cut a 100K-row scoring query from 8 s to under 1 s, eliminated message loss at peak load with Kafka, and designed the GitLab CI/CD → Kubernetes pipeline with OpenTelemetry tracing. Led a 3-engineer team on a credit-bureau integration that was profitable in week one.
- summary RU: Senior Backend Engineer, 4+ года высоконагруженных сервисов на Node.js/TypeScript в финтехе: NestJS, PostgreSQL, Redis, Apache Kafka, Kubernetes. Ускорил запрос по 100 тыс. строк скоринга с 8 с до <1 с, устранил потери сообщений на пике через Kafka, спроектировал пайплайн GitLab CI/CD → Kubernetes с трейсингом OpenTelemetry. Руководил командой из 3 инженеров на интеграции с бюро кредитных историй, окупившейся за неделю.

### C · AI / LLM Engineer
- title: EN «AI Engineer» · RU «AI Engineer»
- tail: EN «LLM Systems, AI Agents, MCP · TypeScript / Node.js» · RU «LLM-системы, AI-агенты, MCP · TypeScript / Node.js»
- теги для отбора буллетов (по приоритету): AI, FS, BE, LEAD, GROWTH, FIN; лимит буллетов: Alfa 5, Appbooster 2, SODA 4; порядок блоков навыков: ai → core → backend → frontend → infra → process; open-source: да
- summary EN: AI Engineer with 4+ years of production TypeScript/Node.js and 3 years shipping LLM systems: a model cascade that cut cost per lead 10×, an AI assistant that tripled channel revenue to ~$141K/month, and custom MCP servers adopted by a fintech engineering team. Covers the full loop: prompt and routing design, cost/latency optimisation, evaluation against human baselines, integration into React/NestJS products.
- summary RU: AI Engineer, 4+ года production-разработки на TypeScript/Node.js и 3 года запуска LLM-систем: каскад моделей, снизивший стоимость лида в 10 раз; AI-ассистент, утроивший выручку канала до ~$141K в месяц; собственные MCP-серверы, внедрённые в инженерную команду финтех-продукта. Полный цикл: дизайн промптов и роутинга, оптимизация стоимости и задержки, сравнение с человеческим бейзлайном, интеграция в продукты на React/NestJS.

### D · Tech Lead / Lead Engineer
- title: EN «Tech Lead / Senior Full-Stack Engineer» · RU «Tech Lead / Senior Full-Stack Engineer»
- tail: EN «TypeScript / Node.js / React · Fintech» · RU «TypeScript / Node.js / React · Финтех»
- теги для отбора буллетов (по приоритету): LEAD, FS, BE, AI, FIN, GROWTH; лимит буллетов: Alfa 5, Appbooster 2, SODA 4; порядок блоков навыков: leadership → core → backend → ai → frontend → infra → process; open-source: нет
- summary EN: Tech Lead and Senior Full-Stack Engineer with 4+ years in product teams and 2 years leading delivery: owned technical design, API contracts and user flows for a 3-engineer team that launched a profitable credit-report product in one week (+40% net profit). Introduced AI-agent workflows (Claude, MCP) across the team and built the CI/CD, tracing and alerting stack the team ships on.
- summary RU: Tech Lead и Senior Full-Stack Engineer, 4+ года в продуктовых командах, 2 года руководства разработкой: отвечал за техническое проектирование, контракты API и пользовательские сценарии команды из 3 инженеров, которая за неделю вывела в прибыль продукт кредитных отчётов (+40% к чистой прибыли). Внедрил в команду AI-агентов (Claude, MCP) и построил стек CI/CD, трейсинга и алертинга, на котором команда релизится.

### E · Fintech Software Engineer
- title: EN «Senior Software Engineer» · RU «Senior Software Engineer»
- tail: EN «Fintech · TypeScript / Node.js / React · PostgreSQL, Kafka» · RU «Финтех · TypeScript / Node.js / React · PostgreSQL, Kafka»
- теги для отбора буллетов (по приоритету): FIN, BE, FS, LEAD, AI, GROWTH; лимит буллетов: Alfa 5, Appbooster 2, SODA 4; порядок блоков навыков: core → backend → infra → frontend → ai → process; open-source: нет
- summary EN: Senior Software Engineer with 4+ years shipping revenue-critical fintech products on TypeScript, Node.js (NestJS), PostgreSQL and Apache Kafka. Led a 3-engineer team through an NBKI credit-bureau integration and a credit-report product that was profitable in its first week (+40% net profit, EPC doubled); made 100% of payouts auditable with a moderation queue and anti-fraud rules. Owns features end to end: data model, API, UI, CI/CD, observability.
- summary RU: Senior Software Engineer, 4+ года разработки финтех-продуктов с прямым влиянием на выручку: TypeScript, Node.js (NestJS), PostgreSQL, Apache Kafka. Провёл команду из 3 инженеров через интеграцию с бюро НБКИ и запуск продукта кредитных отчётов, окупившегося за первую неделю (+40% к чистой прибыли, EPC ×2); сделал 100% выплат проверяемыми через очередь модерации с антифрод-правилами. Закрывает фичи целиком: модель данных, API, интерфейс, CI/CD, наблюдаемость.

### F · Growth / MarTech Engineer
- title: EN «Senior Full-Stack Engineer» · RU «Senior Full-Stack Engineer»
- tail: EN «Growth & MarTech · TypeScript / Node.js / React» · RU «Growth и MarTech · TypeScript / Node.js / React»
- теги для отбора буллетов (по приоритету): GROWTH, FS, AI, BE, LEAD, FIN; лимит буллетов: Alfa 5, Appbooster 3, SODA 4; порядок блоков навыков: core → frontend → backend → ai → infra → process; open-source: да
- summary EN: Senior Full-Stack Engineer with 4+ years shipping growth and marketing products on TypeScript, Node.js (NestJS) and React. Built a push-campaign builder that marketers run without engineers (~$80K/month), grew a task-and-rewards product to 1,000 DAU in 3 months, and tripled a lead channel's revenue to ~$141K/month with an AI assistant. Owns features end to end: data model, API, UI, CI/CD, observability.
- summary RU: Senior Full-Stack Engineer, 4+ года разработки growth- и маркетинговых продуктов: TypeScript, Node.js (NestJS), React. Построил конструктор push-кампаний, которым маркетологи пользуются без разработчиков (~$80K в месяц), вырастил продукт заданий до 1 000 DAU за 3 месяца, утроил выручку лид-канала до ~$141K в месяц с помощью AI-ассистента. Закрывает фичи целиком: модель данных, API, интерфейс, CI/CD, наблюдаемость.

## 3. Опыт: факты и банк буллетов (теги FS BE AI LEAD FIN GROWTH)

### Alfa-Dengi (Alfa-Bank ecosystem) / Альфа-Деньги (экосистема Альфа-Банка)
- название нейтральное: EN «Alfa-Dengi» · RU «Альфа-Деньги»; форма: «via GIDFINANCE» / «через GIDFINANCE»
- роль: EN «Senior Full-Stack Engineer · Tech Lead» · RU «Senior Full-Stack Engineer · Tech Lead»
- даты: EN «Sep 2024 – Present · 2 yrs · Remote» · RU «сент. 2024 – наст. время · 2 года · удалённо»
- строка о компании EN (как в резюме, менять нельзя): Consumer lending product in the ecosystem of one of Russia's largest private banks; delivered via outsourcing partner GIDFINANCE. Cross-functional product team; I ship e2e features from the backend to the interface.
- строка о компании RU (как в резюме): Продукт потребительского кредитования в экосистеме одного из крупнейших частных банков России; проект реализуется через аутсорс-партнёра GIDFINANCE. Кросс-функциональная команда; реализую e2e-фичи от бэкенда до интерфейса.
- строка о компании (нейтральный вариант, только по запросу пользователя) EN: Consumer-lending marketplace (loan showcases, credit scoring, credit reports) with 9K+ new leads a day. Cross-functional product team; contract engagement via GIDFINANCE.
- RU: Маркетплейс потребительского кредитования (витрины займов, кредитный скоринг, кредитные отчёты), 9 тыс.+ новых лидов в день. Кросс-функциональная команда; контракт через GIDFINANCE.

Буллеты (EN / RU):

1. [FS BE LEAD FIN]
   EN: Launched a credit-report product that **turned profitable in its first week** (net profit **+40%**, EPC doubled from **~$1.9 to ~$3.8**) by leading a 3-engineer team through technical design, user flows, the API contract, the NBKI credit-bureau integration and a Node.js backend querying a **6M-row** scoring dataset.
   RU: Вывел в прибыль продукт кредитных отчётов **за первую неделю** (**+40%** к чистой прибыли, EPC вырос с **~$1.9 до ~$3.8**), возглавив команду из 3 инженеров: техническое проектирование, пользовательские сценарии, контракт API, интеграция с бюро НБКИ, бэкенд на Node.js с поиском по скоринговому датасету на **6 млн строк**.

2. [FS GROWTH]
   EN: Enabled marketers to launch automated push campaigns **with zero engineering involvement** (**~$80K/month** generated) by building a status-driven campaign builder on NestJS and React.
   RU: Дал маркетологам возможность запускать автоматические push-кампании **без участия разработчиков** (кампании приносят **~$80K в месяц**), построив конструктор кампаний по статусам заявок на NestJS и React.

3. [BE] (needs: confirm)
   EN: Cut load time of a 100K-row lead-scoring table (9K+ new leads/day) from **8 s to under 1 s** by reworking the data-access path: server-side pagination, PostgreSQL query and index optimisation, caching.
   RU: Ускорил загрузку таблицы скоринга лидов на 100 тыс. строк (9 тыс.+ новых лидов в день) с **8 с до <1 с**, переработав путь доступа к данным: серверная пагинация, оптимизация запросов и индексов PostgreSQL, кэширование.

4. [BE]
   EN: **Eliminated notification loss** under peak load by moving notification delivery and domain-event processing to **Apache Kafka**.
   RU: **Устранил потери уведомлений** на пиковых нагрузках, переведя доставку уведомлений и обработку доменных событий на **Apache Kafka**.

5. [AI LEAD]
   EN: Introduced AI-agent workflows across the engineering team: built **custom MCP servers** over the codebase and internal APIs, integrated Claude into daily development and ran hands-on training on agentic workflows and AI code review.
   RU: Внедрил агентные AI-воркфлоу в инженерную команду: написал **собственные MCP-серверы** для кодовой базы и внутренних API, встроил Claude в ежедневную разработку, провёл обучение агентным воркфлоу и AI-код-ревью.

6. [BE LEAD]
   EN: Designed and built the delivery and observability stack the team ships on: **GitLab CI/CD into Kubernetes**, OpenTelemetry tracing, Grafana alerting.
   RU: Спроектировал и построил стек деплоя и наблюдаемости, на котором релизится команда: **GitLab CI/CD в Kubernetes**, трейсинг OpenTelemetry, алертинг в Grafana.

7. [FS FIN] (needs: metric)
   EN: Increased loan approvals by **[X%]** by personalising microloan-brand showcases to each user's loan history.
   RU: Увеличил количество одобрений займов на **[X%]**, персонализировав витрины МФО-брендов под кредитную историю пользователя.

### Appbooster / Appbooster
- название нейтральное: EN «Appbooster» · RU «Appbooster»
- роль: EN «Full-Stack Engineer (contract)» · RU «Full-Stack Engineer (контракт)»
- даты: EN «Nov 2023 – Aug 2024 · 10 mos · Remote» · RU «нояб. 2023 – авг. 2024 · 10 мес. · удалённо»
- строка о компании EN: Mobile-app marketing platform: ~100 employees, 10,000+ apps promoted for clients in 26 countries.
- строка о компании RU: Платформа мобильного маркетинга: ~100 сотрудников, 10 000+ приложений в продвижении для клиентов из 26 стран.

Буллеты (EN / RU):

1. [FS GROWTH]
   EN: Grew the task-and-rewards product to **1,000 daily active users in 3 months** by owning the full cycle: React user dashboard for paid tasks and proof submission, chatbot re-engagement notifications and the admin verification queue.
   RU: Вырастил продукт заданий с вознаграждениями до **1 000 активных пользователей в день за 3 месяца**, отвечая за полный цикл: React-кабинет платных заданий и сдачи пруфов, уведомления чат-бота для возврата в продукт, админ-очередь верификации.

2. [BE FIN]
   EN: Made **100% of payouts auditable** and screened out duplicate and faked proofs by modelling the full task lifecycle from pick-up to payout behind a moderation queue with anti-fraud rules, processing **hundreds of completions a day**.
   RU: Сделал **100% выплат проверяемыми** и отсёк дубли и поддельные пруфы, смоделировав полный жизненный цикл задания от взятия до выплаты за очередью модерации с антифрод-правилами (**сотни выполнений в день**).

3. [GROWTH]
   EN: Enabled paid channels to be judged by **retained active users instead of installs** by shipping UTM and referrer attribution alongside activity and return-rate metrics.
   RU: Перевёл оценку платных каналов **с установок на удержанных активных пользователей**, запустив атрибуцию по UTM и рефереру вместе с метриками активности и возвращаемости.

### SODA / СОДА
- название нейтральное: EN «SODA» · RU «СОДА»
- роль: EN «Full-Stack Engineer» · RU «Full-Stack Engineer»
- даты: EN «Aug 2022 – Oct 2023 · 1 yr 3 mos · Remote» · RU «авг. 2022 – окт. 2023 · 1 год 3 мес. · удалённо»
- строка о компании EN: Lead-generation agency for residential developers and law firms (~60 employees). Owned the client-server side: APIs, database, interfaces.
- строка о компании RU: Агентство лидогенерации для застройщиков и юридических компаний (~60 сотрудников). Отвечал за клиент-серверную часть: API, база данных, интерфейсы.

Буллеты (EN / RU):

1. [AI LEAD GROWTH FS FIN]
   EN: **Tripled monthly channel revenue from ~$47K to ~$141K** and cut lead response time from ~8 min to **under 30 s** by leading the AI lead-processing assistant and running a 3-month controlled comparison (humans / humans + AI / AI only) that moved the channel fully to AI.
   RU: **Утроил месячную выручку канала с ~$47K до ~$141K** и сократил время ответа лиду с ~8 мин до **<30 с**, возглавив разработку AI-ассистента обработки лидов и проведя 3-месячное контролируемое сравнение (люди / люди + ИИ / только ИИ), по итогам которого канал полностью перевели на ИИ.

2. [AI BE]
   EN: **Cut cost per processed lead 10×** by designing an LLM model cascade: a cheap model handles routine leads and escalates to a stronger model only on low confidence.
   RU: **Снизил стоимость обработки лида в 10 раз**, спроектировав каскад LLM-моделей: дешёвая модель обрабатывает типовые лиды и эскалирует к сильной только при низкой уверенности.

3. [BE]
   EN: Migrated a legacy PHP monolith to **Node.js/TypeScript microservices** (Express, PostgreSQL): service decomposition, business-logic and API migration.
   RU: Перевёл легаси-монолит на PHP в **микросервисы на Node.js/TypeScript** (Express, PostgreSQL): декомпозиция, перенос бизнес-логики и API.

4. [FS GROWTH]
   EN: Lifted conversion **~1.5×** on SPA sites receiving paid ad traffic by raising Lighthouse Performance from **58 to 87** through Core Web Vitals work.
   RU: Поднял конверсию SPA-сайтов под платный трафик **в ~1,5 раза**, повысив Lighthouse Performance с **58 до 87** за счёт работы с Core Web Vitals.

5. [FS]
   EN: Removed manual lead hand-off by building a React integration hub syncing the agency CRM with partner developers' CRM systems.
   RU: Убрал ручную передачу лидов, построив React-хаб интеграций между CRM агентства и CRM-системами партнёров-застройщиков.

## 4. Подтверждённые дополнительные факты и их привязка

Всё ниже подтверждено кандидатом 3 сентября 2026. Использовать только с указанной привязкой.

Alfa-Dengi (сент. 2024 — наст. время)
- На продукте кредитных отчётов вёл команду из 3 инженеров (это единственное допустимое число о команде). Общий размер команды и число инженеров в документах не называть.
- Кредитный продукт: срезал скоуп до минимального проверяемого сценария (суммы займов в истории заявок вынес из v1), воронку проектировал вместе с маркетингом; продукт окупился в первую неделю; после A/B-тестов раскатан ещё на два бренда. Кто и сколько человек наполняли бэклог — в документах не писать.
- Конструктор push-кампаний = визуальный редактор с канвасом: шаги drag-and-drop, ветвления по статусам заявок, условный контент; document model: нормализованный стор на Redux Toolkit с иммутабельными обновлениями, черновики отдельно от опубликованной версии, undo/redo, автосохранение; лимиты частоты по статусам и дневные лимиты на пользователя настраиваются в самом редакторе; ~$80K/месяц; маркетологи работают без разработчика.
- Real-time: живые статусы заявок и уведомления в UI по WebSocket поверх событий Kafka; живые данные в таблице скоринга.
- Таблица скоринга 100K строк, 9K+ лидов/день: с 8 с до <1 с (from 8 s to under 1 s). Подтверждено: профилирование до оптимизации, серверная пагинация, оптимизация запросов/индексов PostgreSQL, виртуализация строк на клиенте (в DOM только видимое окно), фильтры сохранены. Курсорная пагинация, ключи/TTL кеша — НЕ подтверждены, не писать.
- Kafka: перевод доставки уведомлений и доменных событий на Apache Kafka устранил потери сообщений на пиках (массовые рассылки по статусам поверх обычного потока); события стали воспроизводимыми. Топология (топики, партиционирование по userId, consumer groups, идемпотентность) и «до этого были Redis-очереди» — НЕ подтверждены, не писать.
- Деплой: GitLab CI/CD в self-managed Kubernetes-кластер на 5 нод, OpenTelemetry-трейсинг, Grafana-алертинг. Спроектировал пайплайн; кластер — «self-managed», без утверждения, что построил его сам.
- AI-процесс команды: правила проекта для Claude Code (архитектурные конвенции, стиль, границы: prod-миграции, всё про деньги и скоринг — агенту нельзя); переиспользуемые скиллы с автопроверкой; внутренние MCP-серверы (схема БД, таск-трекер, документация); стадия агентного пре-ревью перед человеческим код-ревью; обучение команды. Результат: типовой CRUD-модуль с тестами с ≈2 ч до ≈40 мин / from ~2 h to ~40 min (ОЦЕНКА — только со смягчением). «Продавал пилотом на одном модуле», «до этого копипаста в веб-чат» — НЕ подтверждены.
- Инцидент с залпом push-уведомлений (до ~15 статусных апдейтов, скачок отписок, фикс лимитами) — рассказывать ТОЛЬКО на прямой вопрос про факап на интервью. В CV, письмах и сообщениях — нет.

Appbooster (нояб. 2023 — авг. 2024, контракт)
- Продукт заданий с вознаграждениями (engagement-механика: задания, награды, возврат в продукт): рост до 1 000 DAU за 3 месяца; React-кабинет заданий и пруфов на нормализованном сторе с optimistic updates; уведомления чат-бота; живая (real-time) очередь верификации для админов.
- Жизненный цикл задания от взятия до выплаты как асинхронный workflow за очередью модерации с антифрод-правилами: 100% выплат проверяемы, дубли и поддельные пруфы отсекаются; сотни выполнений в день.
- UTM/referrer-атрибуция с метриками активности и возвращаемости (оценка каналов по удержанным пользователям вместо установок).

SODA (авг. 2022 — окт. 2023)
- AI-ассистент обработки лидов: ответ <30 с против ~8 мин у человека; 3-месячное сравнение помесячно в трёх режимах (люди / люди + ИИ / только ИИ) на одинаковых метриках; «только ИИ» выигрывал стабильно; канал полностью переведён на ассистента; выручка канала с ~$47K до ~$141K/мес (from ~$47K to ~$141K/month); чат с лидом в реальном времени.
- Каскад моделей: инициатива без запроса; прототип на n8n в своё время; дешёвая модель первой, эскалация при неуверенности; API-косты ↓ в 10 раз без потери качества, заметной бизнесу; ушёл в прод как основная архитектура. Как именно определялась «неуверенность» — НЕ зафиксировано; в текстах не описывать, на интервью готовить.
- Миграция PHP-монолита в микросервисы Node.js/TypeScript (Express, PostgreSQL, REST API): декомпозиция, перенос бизнес-логики и API.
- SPA-сайты под платный трафик: Lighthouse Performance с 58 до 87 (from 58 to 87), конверсия ≈ ×1,5 (ОЦЕНКА — «about»); профилирование до оптимизации, Core Web Vitals; пиксель-точная вёрстка по макетам Figma, тёмная тема, адаптив под экраны — подтверждены как практика кандидата, привязка к сайтам СОДЫ допустима.
- React-хаб интеграций CRM агентства с CRM партнёров-застройщиков.

Инструменты и практики (без привязки к конкретной работе, подтверждены)
- Тестирование: Playwright, Cypress, Vitest, Jest, Supertest, React Testing Library, Storybook (stories для React-компонентов).
- Облако: AWS (EC2, поднятие и конфигурирование серверов, S3, networking, деплой) и Yandex Cloud в проде.
- API/архитектура: OpenAPI/Swagger, BFF (backend for frontend), REST, GraphQL, WebSocket, микросервисы, event-driven (Kafka, BullMQ), DDD, системный дизайн.
- Безопасность: OWASP Top 10 как практика: валидация входных данных, авторизация, rate limits, секреты и токены — шифрование at rest (в open-source: AES-256-GCM), антифрод-правила.
- AI: Anthropic API, OpenAI API, OpenRouter; MCP-серверы; Claude Code — единственный AI-инструмент для кода (Cursor/Windsurf/Codex — не заявлять, если пользователь не скажет иначе).

## 5. НЕ заявлять (даже если вакансия требует)

- Python в проде — нет. Допустима только готовность: «готов работать с Python (FastAPI/Django) в стеке проекта», и только если вакансия сама допускает Node.js-основной опыт.
- Kotlin, Java, Go, Elastic, MySQL — не упоминать вообще.
- LangChain, LangSmith, DeepAgents, fine-tuning/RL — нет. Формулировка при необходимости: «агенты собраны напрямую на Anthropic/OpenAI API и MCP, трейсинг собственный».
- Chromium internals, Chrome DevTools Protocol, Puppeteer, Selenium — нет (Playwright — да).
- Образование: Южный федеральный университет, Прикладная информатика, 2022–2024 — степень НЕ завершена: писать только программу и годы, без «B.Sc./M.Sc.». МФТИ/ВШЭ/МГУ, Codeforces, олимпиады — нет.
- Стаж: только «4+ years». Разрыв с требованием вакансии (5+, 6+, 8+, 10+) в CV и письмах не обсуждать, если пользователь не попросит назвать прямо.
- Деньги, которых нет в каноне (§6): $75K/mo, $150K/mo, $230K/mo, $22M, $7.5M, «millions of rubles a week» — нет.
- Нельзя писать про инцидент с пушами (см. §4) и про «scaling 3M → 200M».

## 6. Канон цифр (STAR-банк v9, 21.08.2026)

Точные, можно защитить:
- Кредитный продукт: окупился за первую неделю; чистая прибыль +40%; EPC ×2 (с ~$1.9 до ~$3.8 / from ~$1.9 to ~$3.8); A/B ещё на два бренда; датасет скоринга 6 млн строк; команда 3 инженера.
- Push-кампании: ~$80K/мес; без участия разработчиков.
- Таблица: 100K строк; 9K+ лидов/день; с 8 с до <1 с (from 8 s to under 1 s).
- Kafka: ноль потерь сообщений на пиках.
- Kubernetes: self-managed, 5 нод.
- Appbooster: 1 000 DAU за 3 месяца; сотни выполнений в день; 100% выплат проверяемы; 10 000+ приложений, 26 стран, ~100 сотрудников.
- SODA: с ~$47K до ~$141K/мес (×3) / from ~$47K to ~$141K/month; <30 с против ~8 мин; API-косты ↓10×; Lighthouse: с 58 до 87 (from 58 to 87); ~60 сотрудников.
Оценочные (со смягчением «about / roughly / около»):
- CRUD-модуль с тестами: с ≈2 ч до ≈40 мин / from ~2 h to ~40 min.
- Конверсия после Lighthouse: ≈ ×1,5 (≈ +50%).

## 7. Открытый исходный код

- vk-ai-bot-platform (MIT, github.com/ishbnv/vk-ai-bot-platform): мультитенантная платформа AI-чатботов для сообществ VK; TypeScript, Fastify 5, Drizzle ORM, BullMQ, PostgreSQL 16, Redis 7, React 19 + Mantine, OpenRouter API; двухуровневая дедупликация callback-событий; контекстные окна с учётом токенов и лимитами на сообщество; AES-256-GCM шифрование VK-токенов at rest; гибридный режим с внешними rule-based ботами; nudge-сценарии с учётом рабочих часов и эскалацией (макс. 2); админ-панель с JWT, онбордингом сообществ, версионированием промптов, аналитикой; двуязычный UI; first-click атрибуция партнёрских ссылок; Docker Compose (prod/dev), GitHub Actions CI/CD. 0 звёзд, 2 коммита — не называть «популярным».
- В профиле GitHub также gidfinance-identity (TypeScript) и три форкнутых стартера — их не упоминать.

## 8. Open-source строка

- EN: **vk-ai-bot-platform** (MIT) — multi-tenant AI chatbot platform: OpenRouter LLM API, per-community prompt versioning, token-aware context windows, multi-step re-engagement workflows on BullMQ, event deduplication, admin analytics. TypeScript, Fastify, Drizzle ORM, PostgreSQL, Redis, React, Docker Compose, GitHub Actions.
- RU: **vk-ai-bot-platform** (MIT) — мультитенантная платформа AI-чатботов: LLM через OpenRouter API, версионирование промптов по сообществам, контекстные окна с учётом токенов, многошаговые сценарии возврата на BullMQ, дедупликация событий, админ-панель с аналитикой. TypeScript, Fastify, Drizzle ORM, PostgreSQL, Redis, React, Docker Compose, GitHub Actions.
- ссылка: https://github.com/ishbnv/vk-ai-bot-platform

## 9. Банк навыков (блоки; порядок задаёт пресет или вакансия)

- core — EN «Languages»: TypeScript, JavaScript (ES6+), Node.js, SQL
  RU «Языки»: TypeScript, JavaScript (ES6+), Node.js, SQL
- backend — EN «Backend»: NestJS, Express, Fastify, REST APIs, GraphQL, WebSocket, Prisma ORM, microservices, event-driven architecture, domain-driven design, system design
  RU «Бэкенд»: NestJS, Express, Fastify, REST API, GraphQL, WebSocket, Prisma ORM, микросервисы, событийно-ориентированная архитектура, DDD, системный дизайн
- ai — EN «AI Engineering»: LLM integration (Anthropic API, OpenAI API, OpenRouter), AI agents, agentic workflows, MCP (Model Context Protocol) — custom servers, prompt engineering, model cascading and routing, cost/latency optimisation, LLM evaluation, AI chatbots, Claude Code, AI code review
  RU «AI Engineering»: интеграция LLM (Anthropic API, OpenAI API, OpenRouter), AI-агенты, агентные воркфлоу, MCP (Model Context Protocol) — собственные серверы, промпт-инжиниринг, каскады и роутинг моделей, оптимизация стоимости и задержки, оценка качества LLM, AI-чат-боты, Claude Code, AI-код-ревью
- frontend — EN «Frontend»: React, Next.js, Redux Toolkit, Ant Design, Feature-Sliced Design, Vite, Webpack, Core Web Vitals, Lighthouse
  RU «Фронтенд»: React, Next.js, Redux Toolkit, Ant Design, Feature-Sliced Design, Vite, Webpack, Core Web Vitals, Lighthouse
- infra — EN «Data & Infrastructure»: PostgreSQL, Redis, Apache Kafka, BullMQ, Docker, Kubernetes, AWS, GitLab CI/CD, GitHub Actions, OpenTelemetry, Grafana
  RU «Данные и инфраструктура»: PostgreSQL, Redis, Apache Kafka, BullMQ, Docker, Kubernetes, AWS, GitLab CI/CD, GitHub Actions, OpenTelemetry, Grafana
- process — EN «Testing & Process»: Playwright (E2E), Vitest, Jest, Supertest, code review, Agile/Scrum, technical documentation, mentoring
  RU «Тестирование и процессы»: Playwright (E2E), Vitest, Jest, Supertest, код-ревью, Agile/Scrum, техническая документация, менторинг
- leadership — EN «Leadership»: technical design and API contracts, delivery planning for a 3-engineer team, code review, mentoring, hands-on team training (AI agents, MCP)
  RU «Лидерство»: техническое проектирование и контракты API, планирование поставки для команды из 3 инженеров, код-ревью, менторинг, обучение команды (AI-агенты, MCP)

## 10. Образование и языки

- EN: Southern Federal University — Applied Informatics, 2022–2024 | English — professional working proficiency (daily in a distributed team) · Russian — native
- RU: Южный федеральный университет — Прикладная информатика, 2022–2024 | Английский — профессиональный рабочий уровень (ежедневно в распределённой команде) · Русский — родной

## 11. Решения по умолчанию (не спрашивать пользователя, применять)

- Язык документов = язык вакансии. Русская вакансия → CV и сообщение по-русски; английская → по-английски. Название должности — дословно из вакансии (кроме случая, когда в названии стоит незаявляемая технология, напр. «(React / Node.js / Python)»: тогда без неё, а готовность — в summary).
- Локация: удалённая вакансия → строка «remote»; офис/гибрид в одном городе → строка «переезд в <город>»; несколько стран EU/UK/IL → строка «релокация». Страна не из списка §1 → сказать в сводке, локацию оставить «remote».
- Работодатель: полное наименование с Alfa-Bank. Нейтральное — только если пользователь просил или компания заявляет sanctions-compliance явно.
- Канал отклика: форма/почта → cover letter (PDF); Telegram → сообщение до 150 слов (текст, без PDF письма); и CV всегда.
- Разрыв по стажу и отсутствие Python/Kotlin: не объявлять первым; исключение — вакансия сама пишет «готовность изучать X» (тогда одной фразой их же словами).
- Open-source строка: включать для AI-, fullstack- и frontend-ролей; выключать для backend/infra, если не влезает.
- Уточняющие вопросы пользователю задавать только при блокере: вакансия требует факт, которого нет в §1–10 и без которого отклик бессмысленен, или локация вне списка. Во всех остальных случаях — решать по умолчанию и перечислить принятые решения в сводке.

## 12. Комплаенс и предупреждения

- Alfa-Bank под санкциями EU/US; у компаний с жёстким комплаенсом (Nebius, Deel и т.п.) название банка может вызвать вопросы. Нейтральный вариант — по решению пользователя.
- Вакансии с признаками «серого» финтеха (платёжный роутинг для «одного клиента», оплата в USDT, отклик только через личный Telegram, NDA-компания в trading/betting): в сводке напомнить проверить юрисдикцию и лицензию на первом созвоне.

