# Technology Selection Guide

> Read this reference when at **Step 4 (Technical Planning)** or whenever a technology choice is needed.

## Default Choices

When choosing technology, consider: team expertise, ecosystem maturity, performance requirements, and long-term maintenance. Here are sensible defaults:

| Problem | Default Choice | When to Deviate |
|---------|---------------|-----------------|
| Web app | Next.js + TypeScript | Astro for content, Svelte for perf |
| Mobile (cross-platform) | React Native (Expo) | Flutter for pixel-perfect, embedded |
| Mobile (Apple only) | SwiftUI | UIKit for complex custom interactions |
| Mobile (Android only) | Jetpack Compose | XML-based for legacy codebases |
| Desktop (cross-platform) | Tauri | Electron for larger teams, WPF for Windows-only |
| API server | FastAPI (Python) or Hono (TS) | Go for high-throughput, Rust for systems |
| Database | PostgreSQL | MongoDB for document-first, DynamoDB for serverless |
| Cache | Redis | In-memory for single-instance |
| Queue | BullMQ (Node) or Celery (Python) | Kafka for event streaming at scale |
| Hosting | Vercel/Railway for apps, VPS for services | AWS/GCP when you need their managed services |
| Auth | Lucia (TS) or Ory (self-hosted) | Auth0/Clerk for managed, Keycloak for enterprise |
| Observability | OpenTelemetry + Grafana | Datadog for managed, Sentry for error tracking |

These are starting points, not dogma. The right choice depends on context.

## Selection Principles

- **Start simple.** Monolith first, microservices when you have a reason. Modular monolith is the sweet spot for most applications.
- **Domain-driven boundaries.** Organize code around business domains, not technical layers.
- **Data flow.** Make data flow explicit. Event-driven for async communication, request-response for synchronous. CQRS when read/write patterns diverge.
- **Integration patterns.** Idempotency keys for at-least-once delivery. Outbox pattern for reliable event publication. Saga for distributed transactions. Circuit breaker for external service calls.
- **Document decisions.** Architecture Decision Records (ADRs) for significant choices. Document the why, not the what — code already tells you what.

## Cross-Platform Strategy

When a product spans web, mobile, and desktop:

- **Shared business logic.** Type definitions, validation, calculations, and API clients should be shared. A validation rule implemented three times is three places to fix a bug.
- **Platform-specific UI.** Share logic, not pixels — unless using a framework deliberately designed for cross-platform rendering (Flutter, React Native).
- **API versioning.** Mobile clients can't be force-upgraded. APIs must support old client versions.
- **Feature flags.** Ship features dark, enable per-platform, roll back without a deploy.
