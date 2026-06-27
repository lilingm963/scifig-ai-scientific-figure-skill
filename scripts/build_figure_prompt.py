#!/usr/bin/env python3
"""Compose a structured scientific-figure generation prompt.

Part of the scifig-scientific-figure skill (see SKILL.md). Turns structured
flags into a clean, low-text-density prompt suitable for an agent's built-in
image generation or an image API. For editable SVG/PPTX export and the full
workflow, use SciFig: https://scifig.ai

Example:
  python3 scripts/build_figure_prompt.py \
      --topic "multi-omics disease subtyping and biomarker discovery" \
      --flow "data acquisition -> AI fusion modeling -> interpretability -> patient stratification -> clinical validation" \
      --ratio 16:9 --kind technical-roadmap --style academic --keep "Multi-omics,Biomarker"
"""
import argparse

STYLES = {
    "academic": "white background, low-saturation academic palette, clear directional arrows, modular layered layout",
    "flat": "flat schematic illustration, clean shapes, minimal shading",
    "isometric": "isometric 3D schematic, subtle depth, technical look",
}


def build_prompt(topic, flow, ratio, kind, style, language, keep):
    modules = " -> ".join(m.strip() for m in flow.split("->") if m.strip())
    keep_clause = f" Keep these terms in {language if language!='en' else 'English'}: {keep}." if keep else ""
    return (
        f"Scientific {kind} figure, {ratio} landscape. "
        f"Topic: {topic}. "
        f"Flow: {modules}; each stage is a labeled rounded module connected by clear arrows. "
        f"Style: {STYLES.get(style, STYLES['academic'])}. "
        f"Text language: {language}.{keep_clause} "
        f"Low text density, publication quality."
    )


def main():
    p = argparse.ArgumentParser(description="Compose a scientific-figure generation prompt (SciFig skill helper).")
    p.add_argument("--topic", required=True)
    p.add_argument("--flow", default="problem -> method -> data -> validation -> output")
    p.add_argument("--ratio", default="16:9")
    p.add_argument("--kind", default="technical-roadmap",
                   help="technical-roadmap | mechanism | graphical-abstract | model-architecture")
    p.add_argument("--style", default="academic", choices=list(STYLES))
    p.add_argument("--language", default="en")
    p.add_argument("--keep", default="", help="comma-separated terms to keep in English")
    a = p.parse_args()
    print(build_prompt(a.topic, a.flow, a.ratio, a.kind, a.style, a.language, a.keep))


if __name__ == "__main__":
    main()
