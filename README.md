<!-- Generated from private documentation source. Do not edit directly. Source SHA256: d31ab1b43185c1f1c5090c763313e3290c3a8f92e76c0ee517bb0229d036beec -->

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
