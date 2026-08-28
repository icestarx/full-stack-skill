# Change Work Item Template

Use this as the shared state for the four tracks. Keep it concise and link to
canonical detail instead of copying PRDs, designs, test reports, or release records.

````markdown
# CHG-[YYYY]-[NNN] — [Outcome]

> **Mode**: New product / Feature change / Bug fix / Maintenance / Incident
> **Risk**: Low / Medium / High — [Rationale]
> **Version line / release target**: [v2 / 2.1.0 or TBD]
> **State**: `proposed / ready / in_progress / merge_ready / release_ready / observing / closed / blocked / cancelled`
> **Prior state**: [Required when blocked]
> **Owner**: [Name or role]
> **Baseline manifest**: [Path or TBD for a new baseline]
> **Traceability ledger**: [Path or tracker]

## Outcome and Boundaries

- Problem / intended outcome:
- Origin IDs (`REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS`):
- In scope:
- Non-goals:
- Success and failure signals:

## Impact and Risk

| Surface | Current behavior | Intended change | Compatibility / failure risk | Owner |
|---|---|---|---|---|
| Product / UX | | | | |
| API / events / integrations | | | | |
| Data / migration | | | | |
| Security / permissions | | | | |
| Operations / support | | | | |

## Track Status

| Track | Owner | State | Current evidence | Blocker / next decision |
|---|---|---|---|---|
| Product | | | | |
| Engineering | | | | |
| Verification | | | | |
| Delivery & Learning | | | | |

Track state is one of `not_applicable`, `planned`, `active`, `blocked`,
`evidence_ready`, or `accepted`.

## Vertical Slices

| Slice / TASK IDs | User or risk-reduction outcome | Dependencies | Code/contracts | Verification | Release strategy | State |
|---|---|---|---|---|---|---|
| | | | | | | |

## Decisions and Exceptions

| ID / date | Decision or exception | Rationale / risk | Owner | Review / expiry |
|---|---|---|---|---|
| | | | | |

## Session Handoff

- Last known repository state / commit:
- Completed since previous handoff:
- Commands run and results:
- Open blockers or stale evidence:
- Next smallest ready action:

## Closure

- Merge, PR, build, and release evidence:
- Observation window and result:
- Baseline/ledger updates:
- Follow-up `BUG/TECH/SEC/OPS/REQ/RULE/NFR` items:
- Temporary flags/adapters cleanup owner and date:
````
