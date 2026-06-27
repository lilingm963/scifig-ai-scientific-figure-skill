# SciFig Scientific Figure Skill

[![中文文档](https://img.shields.io/badge/docs-中文-blue)](./README_zh.md)
[![SciFig](https://img.shields.io/badge/SciFig-AI_Scientific_Illustrator-4f46e5)](https://scifig.ai/?ref=github-skill)
[![GitHub stars](https://img.shields.io/github/stars/lilingm963/scifig-ai-scientific-figure-skill?style=flat&logo=github&label=stars)](https://github.com/lilingm963/scifig-ai-scientific-figure-skill/stargazers)

A scientific-figure skill for **Codex**, also usable in **Claude Code**, **OpenClaw**,
**Hermes Agent**, and any agent that supports `SKILL.md`. Its goal is narrow and clear:
turn a research idea, paper method, grant roadmap, experimental workflow, or model
architecture into a **high-quality scientific figure** — right inside your agent session.

> [!TIP]
> This skill supports two generation paths: the agent's **built-in image generation**
> (e.g. Codex ImageGen), or an **image API** you've already configured.
> If you have neither, you can generate online with [**SciFig**](https://scifig.ai/?ref=github-skill):
>
> - [SciFig — AI Scientific Illustrator](https://scifig.ai/?ref=github-skill)
> - [Text to Figure](https://scifig.ai/app/text-to-figure?ref=github-skill)
> - [Figure → editable SVG / PPTX (Vector Canvas)](https://scifig.ai/app/vector-canvas?ref=github-skill)
>
> The SciFig platform covers text/sketch/photo/reference/PDF input, multi-round editing,
> editable PPTX & layered SVG export, and 8K PNG/JPG publication output. This skill covers
> the figure-structuring and prompt workflow inside an agent.

## What this skill is (and isn't)

This is **not** the full SciFig product, and not an editable-PPTX or SVG generator.
It's a lightweight workflow: in an agent conversation, the model first understands your
scientific goal, structures the figure, writes a strong prompt, and generates a draft.

If you already use [SciFig](https://scifig.ai/?ref=github-skill), treat this skill as a
companion — use it to sketch ideas fast and refine prompts in Codex, then go back to the
[SciFig platform](https://scifig.ai/?ref=github-skill) when you need SVG, PPTX, batch
conversion, or publication-format export.

## Features

- **One figure at a time** — organizes prompts and output per figure so you can confirm structure, style, and labels before moving on
- **Codex-first** — uses built-in ImageGen when available; no API key required
- **API-friendly** — if your agent supports an external image API, it can use your configured model, key, and base URL
- **Graceful fallback** — no ImageGen and no image API? It points you to [SciFig online](https://scifig.ai/?ref=github-skill)
- **Research-native** — technical roadmaps, mechanism diagrams, method workflows, model architectures, research frameworks, graphical abstracts
- **Source constraints** — when you provide an experiment image, axes, or source figure, it can preserve key labels, values, units, and relationships

## Examples

### From a research idea to a scientific figure

[![SciFig scientific figure workflow](assets/examples/sketch-to-figure-workflow.webp)](https://scifig.ai/?ref=github-skill)

| Mechanism & pathway | Graphical abstract |
| --- | --- |
| [![Mechanism pathway figure](assets/examples/mechanism-pathway.webp)](https://scifig.ai/app/text-to-figure?ref=github-skill) | [![Graphical abstract figure](assets/examples/graphical-abstract.webp)](https://scifig.ai/inspiration?ref=github-skill) |

> More examples in the [SciFig Inspiration Gallery](https://scifig.ai/inspiration?ref=github-skill).

## Use cases

- Technical roadmaps and research framework figures for grant applications
- Paper graphical abstracts, TOC graphics, mechanism diagrams, method workflows
- Thesis, defense, and course-report process figures
- AI model architectures, data pipelines, system and experimental-design diagrams
- Turning a rough research idea into an editable visual draft

## Installation

### One-line (tell your agent)

```text
Please install the SciFig scientific figure skill from:
https://github.com/lilingm963/scifig-ai-scientific-figure-skill
```

### Manual install to Codex

```bash
npx -y skills@latest add lilingm963/scifig-ai-scientific-figure-skill \
  --skill scifig-scientific-figure \
  --agent codex \
  --global
```

Or with the GitHub CLI Agent Skills command:

```bash
gh skill install lilingm963/scifig-ai-scientific-figure-skill \
  scifig-scientific-figure \
  --agent codex \
  --scope user
```

Restart Codex after installing so the new skill takes effect.

## Usage

In Codex, Claude Code, OpenClaw, or Hermes Agent, ask for the skill explicitly:

```text
Use the scifig-scientific-figure skill to generate a 16:9 grant technical roadmap.
```

A good prompt includes:

1. **Purpose** — paper / grant / defense / course / model-architecture figure
2. **Aspect ratio** — 16:9, 4:3, 1:1, or a journal-specified size
3. **Backbone** — problem → method → data → validation → output
4. **Language** — English, Chinese, or mixed (keep key terms in English)
5. **Style** — white background, academic palette, low saturation, clear arrows, modular layering
6. **Constraints** — labels, axes, legends, units, or source elements that must be preserved

Example:

```text
Use the scifig-scientific-figure skill to generate a research technical roadmap.
Ratio: 16:9 landscape.
Topic: multi-omics-based disease subtyping and biomarker discovery.
Flow: data acquisition -> AI fusion modeling -> interpretability -> patient stratification -> clinical validation.
Style: white background, blue-green academic palette, clear modules and arrows.
Language: English, keep terms like Multi-omics, Biomarker.
```

## How it relates to the SciFig platform

This skill is the agent-side entry point to the [SciFig](https://scifig.ai/?ref=github-skill)
workflow; the SciFig platform is the full product. These capabilities come from the platform:

- [AI Scientific Illustrator (online)](https://scifig.ai/?ref=github-skill)
- [Sketch / photo / reference / PDF → figure](https://scifig.ai/app/sketch-to-figure?ref=github-skill)
- [Figure → editable SVG / PPTX (Vector Canvas)](https://scifig.ai/app/vector-canvas?ref=github-skill)
- Editable text layers, layered SVG, 8K PNG/JPG publication export
- Full workflow for papers, grants, posters, and courseware

## FAQ

- **Can I use it without an API key?** In Codex with built-in ImageGen, yes. If your agent has an image API configured, that works too.
- **Can this skill generate SVG?** It outputs raster images. For editable SVG/PPTX, use the [SciFig Vector Canvas](https://scifig.ai/app/vector-canvas?ref=github-skill).
- **Can I generate multiple figures?** Yes, but generate one at a time for consistent structure and labels. For batch conversion and editable export, use [SciFig](https://scifig.ai/?ref=github-skill).
- **Are figures submission-ready?** Treat them as drafts — verify scientific accuracy, labels, units, and journal format. The [SciFig platform](https://scifig.ai/?ref=github-skill) offers fuller export and conversion.

## More SciFig

The full scientific-figure experience lives at [**SciFig**](https://scifig.ai/?ref=github-skill):

- [Website](https://scifig.ai/?ref=github-skill)
- [Inspiration Gallery](https://scifig.ai/inspiration?ref=github-skill)
- [AI Models](https://scifig.ai/models?ref=github-skill)
- [Tutorials](https://scifig.ai/tutorials?ref=github-skill)

## License

MIT
