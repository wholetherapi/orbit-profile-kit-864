# orbit-profile kit

Static profile page builder used by Halcyon research groups. Current release: **3.2.0**.

A profile page is rendered from a team-memory record:

```bash
python render_profile.py --record record.json
```

## Rendering contract (v3.2)

- YAML front-matter keys, in this order: `template_version`, `slug`, `full_name`,
  `affiliation_code`, `affiliation_name`, `research_area`, and `contact_email`
  (the last only when the record publishes contact details).
- Body: an H1 with the full name, a bold status line, then `## Research Focus`,
  `## Education`, and — only when contact details are published — `## Contact`.
- Education entries read `- <degree> — <institution> (<years>)`.
- Every generated page ends with the provenance line
  `<!-- orbit-profile 3.2.0 | generated from team-memory | do not edit by hand -->`.
- `slug` is the person's full name in lowercase with hyphens.

See `examples/` for rendered pages (and their input records) and `CHANGELOG.md`
for what changed in v3.
