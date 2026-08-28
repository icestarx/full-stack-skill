# Documentation Organization and Versioning

Read this reference when initializing project documentation, starting a major
version, or deciding where a lifecycle artifact belongs. It describes generated
project documentation, not this skill package's own `references/` directory.

## Two Version Axes

Do not use release folders as product baselines.

- A **major-version baseline** owns the effective product, UX, engineering,
  quality, and operations model for a long-lived product line.
- A **release record** owns the scope and delivery evidence for one minor, patch,
  prerelease, or deployment event within that product line.

## Recommended Layout

```text
docs/
├── README.md
├── shared/
│   ├── domain-glossary.md
│   ├── domain-rules/
│   ├── engineering-standards/
│   └── compliance/
├── versions/
│   ├── v1/
│   │   ├── manifest.md
│   │   ├── product/
│   │   │   ├── capability-tree.md
│   │   │   └── requirements/
│   │   ├── ux/
│   │   ├── engineering/
│   │   │   ├── architecture.md
│   │   │   ├── adr/
│   │   │   ├── api/
│   │   │   └── data/
│   │   ├── quality/
│   │   └── operations/
│   └── v2/
│       └── ...
├── changes/
│   └── CHG-2026-001-short-name/
│       ├── work-item.md
│       └── verification.md
├── releases/
│   ├── v1/1.8.0/
│   └── v2/2.0.0/
│       ├── manifest.md
│       ├── change-set.md
│       ├── plan.md
│       ├── verification.md
│       ├── deployment.md
│       ├── release-notes.md
│       └── retrospective.md
└── traceability/
    ├── ledger.json
    ├── ledger.md                 # Optional generated/small-project view
    ├── coverage/
    │   ├── v1.md
    │   └── v2.md
    └── exceptions.md
```

Adapt names to an existing project convention instead of creating a parallel tree.
Keep `docs/README.md` as the navigation entry point: list active/supported version
lines, current releases, authoritative documents, owners, and document status.

For medium/large projects, validate `ledger.json` with the provided traceability
schema/script. Markdown-only ledgers are a small-project fallback or generated view.

## Active Change Records

A change record coordinates four-track work that has not yet become baseline truth
or a release event. It references affected requirements, decisions, tasks, code,
verification, and target release without copying their contents. Use
`references/templates/change-work-item.md`; add a verification record from
`references/templates/verification-evidence.md` when CI or the tracker does not
already provide equivalent durable evidence.

One change may produce several PRs or releases, and one release may contain several
changes. Link them explicitly. After closure, retain the record for audit or archive
it according to project policy; never treat it as the current product baseline.

## Baseline Composition

Every `versions/<major>/manifest.md` declares one mode:

- **Independent**: the major version owns its changed product/UX/engineering
  definitions and imports only explicitly shared material. Prefer this for large
  product-model or architecture changes.
- **Derived**: the major version explicitly reuses selected documents from one
  immediate parent at a pinned source revision and replaces others. Use only when
  the unchanged surface is substantial and the resolved baseline remains easy to
  understand without following a live mutable parent.

Rules:

1. Never mechanically copy a previous major version's full document set.
2. Promote material intended to evolve jointly across supported lines to `shared/`.
   Derived reuse is only for immutable parent content pinned by revision; it must
   never be an unpinned dependency on a mutable V1 document.
3. Never edit a prior major version to describe new-version behavior.
4. Allow at most one declared parent. Flatten the manifest's resolved document
   list with each document's source baseline and pinned revision so readers never
   traverse `V4 → V3 → V2 → V1` inheritance chains.
5. When a requirement changes meaning, create a new ID and link it with
   `supersedes`; do not silently redefine an ID used by a released baseline.
6. A generated, immutable resolved snapshot may be attached to a release for
   audit or offline reading. It is a build artifact, not an editable source.
7. A manifest cannot contain the commit hash of the same commit that first contains
   that value. `baseline source revision` pins the listed content; release tooling
   may publish the manifest revision or resolved snapshot digest afterward.

Use `references/templates/version-manifest.md` for a baseline manifest.

## Release Records

A release record references its major-version baseline and contains only delivery
scope, deltas, plans, verification, deployment evidence, and learning. It must not
contain copied PRD, UX, or architecture baselines.

The release manifest pins:

- version line, release identifier, baseline manifest, and immutable baseline source revision;
- included requirement and acceptance-criterion IDs;
- PRs/commits, build and artifact identifiers;
- test/approval evidence, deployment environments, flags, and production signals.

Use `references/templates/release-manifest.md`. Git tags or immutable commit SHAs
provide historical reconstruction; a mutable `latest` folder does not.

## Document Ownership and Metadata

Version-owned product and engineering documents describe the effective current
state for that version line. Release documents describe events. Shared documents
must name an owner and list the supported version lines.

Each maintained document should record, directly or through its manifest:

- authoritative status and owner;
- version line and lifecycle status;
- last verified date or change;
- requirement, decision, or release IDs it governs;
- superseded document or ID when applicable.

When several major versions are supported in parallel, change each affected
baseline explicitly. Never assume a fix or policy change applies to every line.
