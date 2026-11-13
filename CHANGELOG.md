# Changelog

## 3.2.0

- Added the `template_version` front-matter key.
- Front-matter keys renamed: `name` -> `full_name`, `institution` -> `affiliation_name`.
  `status` and `research` were removed from front matter; the status now appears as a
  bold line in the body, research area is `research_area`, and `slug` was added.
- Body heading `Research Interests` renamed to `Research Focus`.
- Education entries now read `- <degree> — <institution> (<years>)` (em dash,
  institution before the years). Previously `- <degree>, <institution> (<years>)`.
- The contact block is rendered only when contact details are published; otherwise
  no `## Contact` section and no `contact_email` key appear.
- Generated pages end with the provenance comment above; the old HTML footer
  `<!-- orbit-profile 2.x | generated from team-memory -->` was removed.
