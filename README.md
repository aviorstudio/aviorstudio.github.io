<!-- Generated from private documentation source. Do not edit directly. Source SHA256: 5ddd7d4887dd1186520a6ea5ff043f91fc4d63e560b78e3f2282b0ce3fe4ed68 -->

# aviorstudio.github.io

Static redirect to [Avior Studio](https://www.avior.studio/).

Install [mise](https://mise.jdx.dev/) and run `mise install`, then run `mise run check`. Use `mise tasks ls` to inspect the applicable stages.

## Contributor verification

Tool versions and native tasks live in `mise.toml`. Prepare the pinned helper source and run the complete gate:

```sh
git clone https://github.com/nicodes/tools.git .ci-tools
git -C .ci-tools checkout --detach 091101094fedf5ce2e67c339c1c9c842d6a662dc
mise install
mise run check
```

Native build and test commands retain source and output checks, with receipts in `.artifacts/verification`. Existing product release rules and artifacts remain owned by this repository. End users install the product’s published distribution.

## Contributor task interface

Contributor tool versions and task entry points live in the native Mise configuration. Use `mise run lint` for source checks, `mise run test` for the applicable behavioral tests, and `mise run check` for the complete supported gate. `mise run clean` removes declared generated outputs while preserving source, credentials and retained data. This package has no application development service.
