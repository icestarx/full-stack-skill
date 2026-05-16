# Frontend Design Document Template

```markdown
# Frontend Design — [Project Name]

## 1. Frontend Tech Stack
| Layer | Choice | Version | Rationale |
|-------|--------|---------|-----------|
| Framework | Next.js / Vue / Svelte / ... | | |
| UI Library | shadcn/ui / Ant Design / ... | | |
| State Mgmt | Zustand / Jotai / Pinia / ... | | |
| Data Fetching | TanStack Query / SWR / tRPC / ... | | |
| Styling | Tailwind / CSS Modules / ... | | |
| Build Tool | Vite / Turbopack / ... | | |
| Testing | Vitest + Playwright / Jest + Cypress | | |
| Type System | TypeScript / PropTypes | | |

## 2. Component Architecture
### Component Layers
```
pages/          ← Page-level components (route entries)
├── layouts/    ← Layout components (nav/sidebar/footer)
├── features/   ← Feature components (by business domain)
├── shared/     ← Shared components (UI primitives)
└── templates/  ← Template components (page skeletons)
```

### Component Design Principles
- Compound Components for complex widgets
- Container/Presentational separation for data loading
- One component per file, styles/tests/types colocated

## 3. State Management
| State Category | Management | Tool |
|----------------|------------|------|
| Server state | Cache + auto revalidation | TanStack Query |
| Client state | Lightweight store | Zustand |
| URL state | Search params / route segments | next/navigation |
| Form state | Form library | React Hook Form |

- Never duplicate server state into client stores
- Prefer derived values over redundant computed state

## 4. Route Design
| Route | Page | Auth Required | Notes |
|-------|------|---------------|-------|
| / | Home | No | Landing page |
| /login | Login | No | |
| /dashboard | Dashboard | Yes | Post-login home |
| ... | | | |

## 5. Rendering Strategy
| Page Type | Rendering | Rationale |
|-----------|-----------|-----------|
| Landing | SSG / ISR | SEO critical |
| Dashboard | CSR | Authenticated content |
| Dynamic content | SSR | Real-time data |

## 6. Styling Architecture
- Design tokens → CSS custom properties
- Utility classes (spacing/typography) + component-scoped styles
- No inline styles (except dynamic values)
- Theme switching strategy

## 7. Frontend Project Structure
```
src/
├── app/            # Route pages
├── components/     # Components (organized by feature domain)
├── hooks/          # Custom hooks
├── lib/            # Utility functions
├── styles/         # Global styles + tokens
├── types/          # Type definitions
└── test/           # Test utilities + E2E
```

## 8. Performance Strategy
- LCP < 2.5s, INP < 200ms, CLS < 0.1
- Image optimization (WebP/AVIF, lazy loading)
- Code splitting (route-based + dynamic import)
- Font loading strategy (font-display: swap, preload critical fonts)
- Bundle budget: landing < 150KB, app < 300KB

## 9. Accessibility Strategy
- Semantic HTML
- ARIA labels + keyboard navigation
- Focus management (modals/route transitions)
- reduced-motion support
- Color contrast ≥ AA

## 10. Frontend Security
- CSP (Content Security Policy)
- XSS prevention (no unsanitized HTML)
- CSRF token management
- Third-party script SRI
- No sensitive data in frontend storage
```
