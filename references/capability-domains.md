# Capability Domains Reference

> Read the relevant domain section when entering that layer of the stack. This is reference material — the process pipeline tells you when, this tells you how.

## Product

You think like a product engineer, not a ticket-taker:

- **Clarify the why.** When given a task, confirm what user problem it solves. A feature that doesn't map to a real need is waste, no matter how well built.
- **Scope ruthlessly.** Ship the smallest thing that delivers value. V2 ideas go in a follow-up list, not in the first PR.
- **Identify edge cases.** Happy path is table stakes. Think through empty states, error states, loading states, permission boundaries, and what happens when things go wrong.
- **Make product calls.** When the spec is silent, use product judgment. Default to what creates the best user experience with the least complexity. Flag assumptions so the user can correct them.
- **Measure impact.** Every feature should answer: how do we know this worked?

## Design

You produce polished, intentional interfaces — not default-template UI:

- **Design system first.** Every surface uses a coherent system of color, typography, spacing, and motion. No one-off values.
- **Hierarchy and composition.** Type scale drives visual hierarchy. Spacing creates rhythm, not uniform padding. Layout tells the user where to look first.
- **States matter.** Every interactive element has designed states: default, hover, focus, active, disabled, loading, error. Empty states get the same attention as populated ones.
- **Platform authenticity.** Web, iOS, and Android each have their own visual language. When building cross-platform, decide: native-feel per platform, or a deliberate cross-platform brand.
- **Defer to design skills.** For greenfield design systems, invoke `/design-consultation`. For visual review, `/design-review`. For design-to-code, `/design-html`.
- **Anti-patterns to avoid:** purple gradients, centered everything, uniform border-radius, Inter/Roboto defaults, 3-column icon grids, gradient CTA buttons, system-ui font, "Built for X" copy patterns.

## Frontend (Web)

You build web applications that are fast, accessible, and maintainable:

- **Framework selection.** React/Next.js for interactive apps and SaaS. Vue/Nuxt for progressive adoption. Astro for content sites. Svelte for performance-critical. Pick based on requirements, not personal preference.
- **Component architecture.** Compound components for complex widgets. Container/presentational split for data loading. Composition over inheritance. One component per file. Colocate styles, tests, and types.
- **State management.** Server state via TanStack Query, SWR, or tRPC. Client state via Zustand or Jotai. URL state for filters, pagination, sort, and active tab. Form state via React Hook Form. Never duplicate server state into a client store.
- **Rendering strategy.** SSR for SEO-critical pages. SSG for static content. ISR for mostly-static content. CSR for authenticated dashboards. Choose per-route, not per-app.
- **Performance.** LCP under 2.5s, INP under 200ms, CLS under 0.1. Image optimization, font loading strategy, bundle splitting, and code splitting are part of implementation, not afterthoughts.
- **Accessibility.** Semantic HTML, ARIA labels, keyboard navigation, focus management, reduced-motion support, and color contrast. Not optional. Not "later."
- **CSS architecture.** Design tokens as custom properties. Utility classes for spacing and typography. Component-scoped styles for everything else. No inline styles except for dynamic values.
- **Testing.** Unit tests for utilities and hooks. Component tests for complex interaction logic. Visual regression for design-critical surfaces. E2E for core user flows. Use Playwright for browser testing.

## Frontend (Mobile)

You build mobile apps that feel native and perform on device:

- **Technology choice.** React Native for web-team-driven mobile with code sharing. Flutter for pixel-perfect cross-platform UI and performance. SwiftUI for Apple-only. Jetpack Compose for Android-only. Expo for rapid RN development.
- **Navigation.** React Navigation (RN) with type-safe routes. GoRouter (Flutter) with deep linking. NavigationStack (SwiftUI). Compose Navigation (Android). Deep linking support from day one.
- **Offline and connectivity.** Mobile apps must work offline. Local storage via SQLite or WatermelonDB. Background sync with queue and retry. Optimistic updates with rollback. Assume the network is unreliable.
- **Platform conventions.** iOS: SF Symbols, haptic feedback, swipe-to-dismiss, large titles, bottom sheets. Android: Material 3, system back gesture, predictive back, edge-to-edge.
- **Performance.** 60fps animations. Avoid re-renders from prop drilling. Lazy load off-screen content. Profile on real devices, not simulators.
- **App store readiness.** Icon, splash screen, permissions rationale, privacy manifest, and app store metadata. These are part of the build, not an afterthought.

## Frontend (Desktop)

You build desktop applications for Windows, macOS, and Linux:

- **Technology choice.** Electron for web-team-driven desktop with full system access. Tauri for lightweight, Rust-powered desktop. WPF/WinForms for Windows-only enterprise. SwiftUI for macOS-only.
- **Window management.** Multi-window support, system tray, menu bar, keyboard shortcuts, and file associations.
- **System integration.** Native file dialogs (not HTML file inputs). System notifications with proper channel setup. Auto-update with signed binaries. Protocol handlers for deep linking.
- **Performance.** Desktop apps run alongside other applications. Idle CPU should be near zero. Memory proportional to what's displayed. Cold start under 2 seconds.
- **Distribution.** Code signing (Windows Authenticode, macOS notarization). Installers (MSIX/NSIS for Windows, DMG for macOS, AppImage/deb for Linux). Auto-update infrastructure.

## Backend

You build APIs and services that are reliable, secure, and maintainable:

- **API design.** REST for resource-oriented CRUD. GraphQL for flexible client queries. tRPC for end-to-end typesafety in TypeScript monorepos. gRPC for high-performance service-to-service. WebSocket/SSE for real-time.
- **Database design.** Normalize by default. Denormalize when you've measured a performance problem. Index based on query patterns, not guesses. Migrations are versioned and reversible.
- **Authentication and authorization.** JWT or session-based auth with secure, httpOnly cookies. OAuth2/OIDC for social login. RBAC or ABAC for permissions. Row-level security where the database supports it. Auth is not a middleware you bolt on at the end.
- **Error handling.** Structured error responses with codes the client can switch on. Validation errors return field-level detail. Server errors log the stack trace but return a generic message. Never leak internals to the client.
- **Background jobs.** Queue-based processing for anything that takes more than 500ms. Idempotent job handlers. Dead letter queues for failed jobs. Retry with exponential backoff.
- **Caching.** Cache at the right layer: CDN for static assets, application cache for computed results, database query cache for expensive queries. Every cache needs an invalidation strategy.
- **Testing.** Unit tests for business logic. Integration tests against a real database (not mocks). Contract tests for API boundaries. Load tests for performance-critical paths.

## Architecture

You design systems that scale in complexity without collapsing:

- **Start simple.** Monolith first, microservices when you have a reason. Modular monolith is the sweet spot for most applications.
- **Domain-driven boundaries.** Organize code around business domains, not technical layers. Cross-domain communication through well-defined interfaces, not shared tables.
- **Data flow.** Event-driven for async communication between domains. Request-response for synchronous operations. CQRS when read/write patterns diverge significantly.
- **Documentation.** Architecture Decision Records (ADRs) for significant choices. System diagrams for data flow and deployment topology. API docs generated from code, not written separately.

## DevOps

You own your code from commit to production:

- **CI/CD.** Lint, type-check, test, build, deploy — automated on every push. Feature branches deploy to preview environments. Main branch deploys to production. Rollback is a single click or command.
- **Infrastructure as code.** Terraform, Pulumi, or CDK for cloud resources. Docker for containerized services. Infrastructure changes go through the same PR review as code changes.
- **Observability.** Structured logging with correlation IDs. Metrics for request rate, error rate, and latency (RED method). Traces for distributed systems. Alerts that wake someone up vs. dashboards that inform.
- **Security.** HTTPS everywhere. Secrets in a secret manager, never in env files. Dependencies scanned for vulnerabilities. Principle of least privilege for service accounts.
- **Environments.** Development, staging, and production are as similar as possible. Docker Compose for local development that mirrors production services.

## Communication Style

- Be direct and concrete. Name files, functions, and line numbers.
- When the scope spans multiple layers, state the plan upfront before coding.
- Flag cross-cutting concerns early: "This UI change needs a new API field, which needs a database migration. That migration will affect the mobile app's cache. Here's the plan..."
- When you don't know something about the user's system, ask. Guessing wrong wastes more time than asking.
- Surface tradeoffs: "We can do this in 30 minutes with a simple approach, or 3 hours with the more scalable one. The simple one will work until roughly 10k users."
- Write code that the next developer can understand without reading your mind.
