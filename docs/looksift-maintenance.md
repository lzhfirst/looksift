# Maintaining the public Looksift Skill

The public bundle contains the runtime instructions, portable Python helpers,
numbered bilingual style records and pinned official Qwen prompt templates.
See [installation and checks](installation.md) for setup and local validation.

The Looksift website remains the discovery and style-selection product. This
Skill writes prompts and does not run production queues or generate images.

Keep root SKILL.md as the single canonical entry. Preserve the workflow,
preference semantics, first-use logo, selected-language interaction and complete
prompt delivery. Missing effective drawing information requires clarification
across all subjects; applicable current or explicit ongoing completion permission
is reused. Style numbers refer to exact records, never list positions.

Library updates must use confirmed source changes. Preserve four-digit IDs and
all surviving bilingual fields. Removed IDs leave gaps; do not renumber, guess
replacements, or infer retirement from generation outcomes. Verify styles.json,
individual records and the library manifest together before publishing an update.

Keep official template originals, their pinned manifest and upstream license
unchanged. The package LICENSE covers the project; the official template folder
retains its own license and attribution. Style records retain their source URLs.

Runtime preference data belongs outside this bundle. Never commit user profiles,
SQLite databases, credentials, production queues, local host configuration or
private chat transcripts. Public documentation may include explicitly selected,
reviewed generated examples with source and model credits; do not copy the
production asset directories wholesale. Tests use isolated roots and explicit test profiles.
Candidates are not automatic defaults, and successful persistence must be checked
before telling the user a preference was saved.

Before release, verify the public package independently of the production
checkout. Check all relative Markdown links, every index record, official file
hashes and the preference helper. Agent text reviews and passing local tests do
not establish generated-image similarity or identical behavior across hosts.
