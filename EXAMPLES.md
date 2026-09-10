# EXAMPLES — эталон вывода (одна заявка от начала до конца)

## A. Вакансия (сжатая выжимка после шага 1)

Zencoder · Senior Software Engineer · Europe, Remote · EN. Стек TypeScript + Kotlin. Требуют: 10+ лет, backend Java/Kotlin/TypeScript, product mindset, ownership, «deep familiarity with AI assistants», startup-среда, плюс — real-time collaborative systems. Канал: форма Greenhouse (CV + cover letter + свободный вопрос про AI-инструменты). Решения по умолчанию: язык EN; локация «remote»; работодатель полный; годы и Kotlin не объявлять; письмо (форма).

## B. JSON для render_cv.py (как есть, целиком)

```json
{
  "lang": "en",
  "name": "Ivan Shabanov",
  "title": "Senior Software Engineer",
  "tail": "TypeScript / Node.js / React · AI Coding Agents, MCP & LLM Systems · Product-minded IC",
  "location": "Yerevan, Armenia (GMT+4) · Remote · B2B contract or EOR · Full overlap with EU hours",
  "contacts": [
    {
      "label": "ivan@ishbnv.dev",
      "href": "mailto:ivan@ishbnv.dev"
    },
    {
      "label": "+374 77 719 518",
      "href": "tel:+37477719518"
    },
    {
      "label": "linkedin.com/in/ishbnv",
      "href": "https://www.linkedin.com/in/ishbnv"
    },
    {
      "label": "github.com/ishbnv",
      "href": "https://github.com/ishbnv"
    },
    {
      "label": "ishbnv.dev",
      "href": "https://ishbnv.dev"
    }
  ],
  "summary": "Senior Software Engineer with 4+ years of production TypeScript and 3 years building with LLMs, the last two spent turning AI coding agents into a team capability: project rules for Claude Code, custom MCP servers over the codebase and internal APIs, an agentic pre-review stage and hands-on training, after which a typical CRUD module with tests went from ~2 h to ~40 min. Makes decisions on data and starts things without being asked: replaced a human lead channel with an LLM agent after a 3-month controlled comparison (revenue from ~$47K to ~$141K/month), cut LLM API costs 10× with a confidence-based cascade nobody had asked for, and led a 3-engineer team to a credit-report product that was profitable in its first week. Builds real-time features end to end: WebSocket status updates over Kafka events, live queues, chat.",
  "jobs": [
    {
      "company": "Alfa-Dengi (Alfa-Bank ecosystem)",
      "engagement": "via GIDFINANCE",
      "role": "Senior Full-Stack Engineer · Tech Lead",
      "dates": "Sep 2024 – Present · 2 yrs · Remote",
      "blurb": "Consumer lending product in the ecosystem of one of Russia's largest private banks; delivered via outsourcing partner GIDFINANCE. Cross-functional product team; I ship e2e features from the backend to the interface.",
      "bullets": [
        "Made AI coding agents a team-level capability: wrote the **project rules for Claude Code** (architecture conventions, style, what an agent must never touch), built **custom MCP servers** exposing the database schema, task tracker and docs to agents, added an **agentic pre-review stage** ahead of human review and trained the team; a typical CRUD module with tests now takes **~40 min instead of ~2 h** and pull requests reach reviewers clean.",
        "Launched a credit-report product that **turned profitable in its first week** (net profit **+40%**, EPC doubled from **~$1.9 to ~$3.8**) by cutting scope to the minimum testable flow, co-designing the funnel with marketing and leading 3 engineers through technical design, the API contract, the NBKI credit-bureau integration and a Node.js backend over a **6M-row** scoring dataset; rolled out to two more brands after A/B tests.",
        "Enabled marketers to launch automated push campaigns **with zero engineering involvement** (**~$80K/month** generated) by building a status-driven campaign builder on NestJS and React with per-status frequency caps and daily per-user limits built into the builder.",
        "**Eliminated notification loss** under peak load by moving notification delivery and domain-event processing to **Apache Kafka**; live application-status updates and notifications reach the UI over **WebSocket** on top of those events.",
        "Cut load time of a 100K-row lead-scoring table (9K+ new leads/day) from **8 s to under 1 s** by reworking the data-access path: server-side pagination, PostgreSQL query and index optimisation, caching."
      ]
    },
    {
      "company": "Appbooster",
      "engagement": "",
      "role": "Full-Stack Engineer (contract)",
      "dates": "Nov 2023 – Aug 2024 · 10 mos · Remote",
      "blurb": "Mobile-app marketing platform: ~100 employees, 10,000+ apps promoted for clients in 26 countries.",
      "bullets": [
        "Grew the task-and-rewards product to **1,000 daily active users in 3 months** by owning the full cycle: React user dashboard for paid tasks and proof submission, chatbot re-engagement notifications and a **live verification queue** for admins.",
        "Made **100% of payouts auditable** and screened out duplicate and faked proofs by modelling the full task lifecycle from pick-up to payout behind a moderation queue with anti-fraud rules, processing **hundreds of completions a day**."
      ]
    },
    {
      "company": "SODA",
      "engagement": "",
      "role": "Full-Stack Engineer",
      "dates": "Aug 2022 – Oct 2023 · 1 yr 3 mos · Remote",
      "blurb": "Lead-generation agency for residential developers and law firms (~60 employees). Owned the client-server side: APIs, database, interfaces.",
      "bullets": [
        "**Tripled monthly channel revenue from ~$47K to ~$141K** and cut lead response time from ~8 min to **under 30 s** with an LLM assistant that talks to leads in real time; a 3-month controlled comparison (humans / humans + AI / AI only) settled the decision to move the channel fully to AI.",
        "**Cut LLM API costs 10×** on my own initiative by prototyping, measuring and shipping a model cascade: a cheap model handles routine leads and escalates to a stronger one only on low confidence.",
        "Migrated a legacy PHP monolith to **Node.js/TypeScript microservices** (Express, PostgreSQL): service decomposition, business-logic and API migration.",
        "Lifted conversion **~1.5×** on SPA sites receiving paid ad traffic by raising Lighthouse Performance from **58 to 87** through Core Web Vitals work."
      ]
    }
  ],
  "oss": {
    "text": "**vk-ai-bot-platform** (MIT) — multi-tenant LLM chatbot platform with real-time conversation handling: OpenRouter API, per-community prompt versioning, token-aware context windows, multi-step re-engagement workflows on BullMQ, event deduplication, admin analytics. TypeScript, Fastify, Drizzle ORM, PostgreSQL, Redis, React, Docker Compose, GitHub Actions.",
    "href": "https://github.com/ishbnv/vk-ai-bot-platform"
  },
  "skills": [
    [
      "AI Coding Agents & LLM Systems",
      "Claude Code (project rules, reusable skills, agentic pre-review), MCP (Model Context Protocol) custom servers, AI code review, AI agents and tool interface design, LLM APIs (Anthropic API, OpenAI API, OpenRouter), prompt engineering, context engineering, model cascading and routing, LLM evaluation against human baselines, cost/latency optimisation, AI chatbots"
    ],
    [
      "Languages",
      "TypeScript, JavaScript (ES6+), Node.js, SQL"
    ],
    [
      "Backend",
      "NestJS, Express, Fastify, REST APIs, GraphQL, WebSocket and real-time updates, Prisma ORM, microservices, event-driven architecture (Apache Kafka, BullMQ), domain-driven design, software architecture and system design"
    ],
    [
      "Frontend",
      "React, Next.js, Redux Toolkit, Ant Design, Feature-Sliced Design, Vite, Webpack, Core Web Vitals"
    ],
    [
      "Data & Infrastructure",
      "PostgreSQL, Redis, Apache Kafka, Docker, Kubernetes, AWS, GitLab CI/CD, GitHub Actions, OpenTelemetry, Grafana"
    ],
    [
      "Product & Process",
      "product discovery with marketing and sales, scope cutting to a testable v1, A/B tests and controlled experiments, code review, Agile/Scrum, technical documentation, mentoring and team training"
    ]
  ],
  "education": [
    "Southern Federal University — Applied Informatics, 2022–2024",
    "English — professional working proficiency (daily in a distributed team) · Russian — native"
  ]
}
```

Команда: `python3 render_cv.py cv.json Ivan_Shabanov_Senior_Software_Engineer_Zencoder.pdf --keywords "Senior Software Engineer,TypeScript,Claude Code,MCP,AI agents,product,real-time,WebSocket,software architecture"`

## C. JSON для render_letter.py (письмо после самопроверки по STYLE_GUIDE §7)

```json
{
  "name": "IVAN SHABANOV",
  "line1": "ivan@ishbnv.dev · +374 77 719 518 · linkedin.com/in/ishbnv · github.com/ishbnv · ishbnv.dev",
  "line2": "Yerevan, Armenia (GMT+4) · Remote · Full overlap with EU hours",
  "date": "3 September 2026",
  "to": [
    "Zencoder — Hiring Team",
    "Re: Senior Software Engineer, Europe (Remote)"
  ],
  "paragraphs": [
    "Dear Hiring Team,",
    "I am applying for the Senior Software Engineer role. I use coding agents every day, and for the last two years part of my job has been making them work for a whole team.",
    "At Alfa-Dengi, a consumer-lending marketplace, AI tooling was a personal habit, different for every engineer. The project rules for Claude Code came first, including what an agent must never touch: production migrations and anything that moves money or scoring. Internal MCP servers followed, so agents get the database schema and the task tracker from a tool instead of guessing at our data model. The last piece was an agent pre-review stage in front of every human review, so pull requests arrive clean and reviewers spend their time on logic. Then I trained the team. A typical CRUD module with tests now takes about forty minutes where it used to take roughly two hours. I also know where agents fail in a real codebase, and I suspect that is the more useful half of this experience for you.",
    "At SODA, a lead-generation agency, the question was whether to keep human chat managers once an LLM assistant answered leads within thirty seconds instead of eight minutes. Over three months I ran the channel in three modes on the same metrics, and the assistant on its own won every month. The channel moved to it and revenue tripled. Later I saw that every lead was going to the top model. No one had asked for a fix; I prototyped a cascade in my own time, measured quality and cost, and API costs dropped tenfold.",
    "I have shipped real-time features before: application-status updates over WebSocket on top of Kafka events, and a live verification queue for moderators. My production stack is all TypeScript: Node.js on NestJS and Express, React, PostgreSQL, Kafka, Kubernetes.",
    "I work remotely from Yerevan, GMT+4, which overlaps the full European working day.",
    "Which part of the agent loop do your users trust least today, the plan or the verification?"
  ],
  "closing": [
    "Kind regards,",
    "Ivan Shabanov"
  ]
}
```

## D. Пример Telegram-сообщения (русская вакансия, отклик в TG)

```
Добрый день! Пишу по вакансии Senior Frontend Developer (React).

Четыре года пишу на React и TypeScript, последние два года в Альфа-Деньгах, маркетплейсе потребительского кредитования.

Ближе всего к вашим задачам три вещи. Дашборд скоринга лидов на 100 тыс. строк грузился 8 секунд, теперь меньше секунды: сначала профилирование, потом серверная пагинация и виртуализация строк. Живые статусы заявок и уведомления приходят в интерфейс по WebSocket поверх событий Kafka. Визуальный редактор кампаний, в котором маркетологи собирают кампании сами, без разработчика, и он приносит около $80K в месяц.

Claude Code в ежедневной работе два года. Настроил правила проекта и написал MCP-серверы под нашу базу и таск-трекер. Потом поставил агентную проверку PR перед код-ревью и обучил команду. Типовой CRUD-модуль с тестами стал занимать около 40 минут вместо двух часов.

Из вашего стека работал с PostgreSQL, Redis и Kubernetes.

Резюме прикладываю. Работаю удалённо из Еревана, GMT+4, рабочий день полностью пересекается с Москвой и Европой. Готов созвониться на этой неделе в любой день.

Иван Шабанов · github.com/ishbnv
```

## E. Формат сводки в чате (после файлов)

**Zencoder — Senior Software Engineer.** Метч: AI-процесс команды попадает в центр вакансии (Claude Code, MCP, агентное пре-ревью), product mindset подтверждён кейсами с измерением; против — 10+ лет при 4+ и Kotlin, которого нет. Решения: EN, шапка remote, работодатель с Alfa-Bank, годы и Kotlin не упоминаются. В CV первым идёт буллет про AI-процесс, навыки открываются блоком «AI Coding Agents & LLM Systems», добавлен real-time (WebSocket-статусы поверх Kafka, живая очередь верификации). Не закрыто: Kotlin/Java, 10 лет. Проверить перед отправкой: цифра «с 2 ч до 40 мин» — оценка, на интервью подавать с «about»; если пробовали Zencoder или Cursor, добавьте одну фразу в ответ формы.
