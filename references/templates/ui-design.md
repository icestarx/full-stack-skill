# UI Design Document Template (DESIGN.md)

```markdown
# Design System — [Project Name]

## Requirement and Acceptance Coverage

| REQ / AC IDs | User flow | Screens / components / states | Prototype or evidence | Status |
|---|---|---|---|---|
| | | | | Planned / Reviewed / Approved |

Every committed UX-affecting requirement and acceptance criterion must map to its
normal, alternate, error, permission, and recovery surfaces or an approved `N/A`.

## Product Context
- Product type, target users, industry/competitors

## Aesthetic Direction
- Style direction (editorial/minimalist/luxury/brutalist/...)
- Ornamentation level (minimal/intentional/expressive)
- Emotional positioning

## Information Architecture
- Sitemap
- Navigation structure (global/local/breadcrumbs)
- Page hierarchy (≤ 3 levels)

## Interaction Design
- Core user flow diagrams
- 6 interaction states coverage (normal/empty/loading/error/edge-case/interruption-recovery)
- Key page wireframes or prototype links

## Typography System
- Display: [Font] — [purpose/rationale]
- Body: [Font] — [purpose/rationale]
- UI/Labels: [Font]
- Data/Tables: [Font] (must support tabular-nums)
- Type scale (specific px/rem values)

## Color System
- Primary: [hex] — [usage]
- Secondary: [hex] — [usage]
- Neutral: [hex range] (cool/warm gray)
- Semantic: success/warning/error/info [hex]
- Dark mode strategy

## Spacing System
- Base unit: 4px / 8px
- Spacing scale: 2xs→3xl specific values
- Density: compact/comfortable/spacious

## Layout
- Grid system (columns/breakpoints)
- Max content width
- Border radius scale

## Motion
- Easing curves
- Duration scale (micro/short/medium/long)
- reduced-motion adaptation

## Component States
Each component covers: default | hover | focus | active | disabled | loading | error
```
