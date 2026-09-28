# Looksift 2.0

**English** · [简体中文](README.zh-CN.md)

**Find a visual style. Bring your own idea. Get a prompt built for it.**

Looksift is a Skill for turning a new creative brief into detailed Qwen Image 2.1 prompts. Browse the [Looksift gallery](https://looksift.com), choose a numbered style or a reference image, and describe what you want to make. Your Agent connects the chosen visual treatment to your subject, composition and constraints.

The result is a complete prompt you can take to your image-generation workflow. Looksift handles prompt preparation; image generation happens in the tool you choose.

**Version 2.0 · 4,012 styles · English / 简体中文 documentation**

[Download the installation ZIP](https://github.com/lzhfirst/looksift/releases/download/v2.0.0/looksift-2.0.zip) · [Release notes and checksums](https://github.com/lzhfirst/looksift/releases/tag/v2.0.0)

[Explore styles](https://looksift.com) · [Get started](#quick-start) · [See image examples](#a-look-inside-the-style-library) · [Read complete case prompts](docs/examples.md) · [Official Qwen project](https://github.com/QwenLM/Qwen-Image-2.1)

## Why Looksift exists

Finding an image you like is often easier than describing what makes it work. A name such as “watercolor” or “cinematic” leaves many decisions unresolved: how edges break, where detail concentrates, how materials respond to light, and how color holds the composition together.

Copying an example prompt creates another problem. Its people, setting and layout can follow the style into a completely different brief. A landscape request can inherit a portrait's composition; a new product can acquire objects that only belonged to the reference.

Looksift gives the Agent a structured way to read a visual style, understand your intended picture, and write a new prompt around both.

| When the work gets stuck | How Looksift helps |
| --- | --- |
| “I know the look, but I cannot describe it.” | Reads concrete style traits: marks, texture, form, edges, light and color relationships. |
| A copied prompt keeps bringing back the old subject. | Separates reusable visual treatment from the original scene. |
| A short brief leaves too much to guess. | Asks for useful missing information or permission to develop secondary details. |
| The conversation keeps asking the same questions. | Reuses choices already settled within the current request and applicable explicit preferences. |
| A translation changes the scene or the words inside the image. | Keeps the versions aligned and preserves requested visible text. |
| A reference is available, but its style is hard to express in words. | Provides a reference-based route with clear image roles and a new scene description. |

## What 2.0 provides

- **Two clear workflows.** Use an exact library number for text-to-image, or prepare a prompt for a style reference supplied at generation time.
- **A bundled library of 4,012 styles.** Numbered records include reusable style descriptions, complete scene examples and source information. Once installed, reading a bundled record does not require fetching its source page.
- **Scene-aware prompt development.** The Agent connects subjects, actions, spatial relationships, lighting and framing into a coherent picture.
- **Questions only where they matter.** Missing effective drawing information is handled for every kind of subject, including landscapes, products, posters, people and animals.
- **Control over creative additions.** You can complete the brief yourself, delegate secondary details, or require the Agent to stay strictly within supplied content.
- **Composition for the chosen frame.** A new aspect ratio calls for a corresponding composition, rather than just changing a number at the end.
- **Language-aware delivery.** Ordinary conversation follows your chosen language. Prompt delivery can include English and your selected language, with explicit single-language requests respected.
- **Local preferences.** Explicit defaults can be remembered. Repeated choices remain candidates until you actually authorize them as defaults.
- **Official template resources.** The bundle preserves the selected Qwen Image 2.1 text-to-image and editing prompt templates, their source revision and upstream license.
- **Structured output when requested.** JSON delivery follows the selected official template schema for integration into a separate workflow.

## A look inside the style library

The library spans visual approaches rather than one fixed subject: painted surfaces, line-based illustration, photographic light, mixed-media texture, dimensional materials and more. The examples below show six existing library generation results.

| Architectural texture · 0046 | Nature illustration · 0048 | Monochrome atmosphere · 0057 |
| :---: | :---: | :---: |
| ![Weathered carved-stone courtyard viewed through a shaded colonnade](assets/examples/0046.png) | ![Rabbit among blue and golden flowers on a warm ivory ground](assets/examples/0048.png) | ![Monochrome coastal path leading toward a jagged sea stack and radiating light](assets/examples/0057.png) |
| Mineral surfaces, repeated forms and natural light. | Fine directional marks, transparent washes and open paper. | Strong tonal separation, selective edges and mist. |

| Mixed-media landscape · 0064 | Handcrafted dimensions · 0109 | Dramatic comic painting · 1813 |
| :---: | :---: | :---: |
| ![Blue-grey waterside landscape assembled from weathered rectangular layers](assets/examples/0064.png) | ![Handcrafted figure holding a pale cup while seated in an armchair](assets/examples/0109.png) | ![Dark-haired woman beside a window glowing with orange city light](assets/examples/1813.png) |
| Scraped color, visible seams and layered depth. | Rounded forms, tactile surfaces and soft staged light. | Broken painted texture, deep shadows and luminous accents. |

**Image provenance:** These are existing Qwen Image 2.1 INT8 library samples. They illustrate the corresponding stored scene prompts; they are not a claim that the Skill generates images by itself or that every new subject will reproduce the same result. Each selected image has been matched to its library prompt. [Open the case notes, full prompts and source credits](docs/examples.md).

### What a style number represents

A number selects one exact record. Its reusable description explains the visual methods, while its complete example shows those methods in a particular scene. The example subject is not a required ingredient for your next image.

For instance, the dramatic light and painted texture of style 1813 can inform a new scene without carrying over the woman, dress or city window from its example. Your brief determines the new subject and setting. Exact source colors are retained when you ask for them; otherwise the Agent adapts color relationships to your new scene within the creative scope you have allowed.

Numbers are identifiers, not rankings or positions in a list. Gaps are intentional when records are retired. Use a number present in the installed library; an unavailable number must be clarified rather than silently replaced.

## Quick start

### 1. Install the complete Skill

Use an Agent host that supports `SKILL.md` skills, can read the bundled files, and can run local Python. The included helpers require Python 3.9 or later and use only the standard library.

Download and extract the [Looksift 2.0 installation ZIP](https://github.com/lzhfirst/looksift/releases/download/v2.0.0/looksift-2.0.zip). Install the enclosed **complete `looksift` folder** using your host's supported skill installation mechanism. If your host supports GitHub-based installation, use [this repository](https://github.com/lzhfirst/looksift) and its root Skill. Keep `SKILL.md` at the installed bundle root and preserve the nested directories. Copying only the entry document leaves out the style records and templates the Skill needs.

Reload or refresh skills in your host after installation or an update. Model weights and an image-generation service are not included in the Skill package; choose your image-generation environment separately.

### 2. Choose how the style will be supplied

| | A — Direct text-to-image | B — Generate with a style reference |
| --- | --- | --- |
| Style input | An exact Looksift style number. | A reference image supplied to the drawing tool when generating. |
| What you provide to the Agent | Method A, your number, your new theme and known constraints. | Method B, your new theme and known constraints; a number is optional. |
| Reference upload during prompt preparation | Not required. | Not required for ordinary style-reference prompt preparation. |
| What the drawing tool receives | The completed text prompt. | The completed prompt together with the selected reference image. |
| Template basis | Qwen Image 2.1 text-to-image. | Qwen Image 2.1 editing. |

If you only provide a theme, Looksift asks which method you want. A number or an attachment alone does not silently choose a workflow.

### 3. Give your new brief

You can start with an idea and refine it in conversation. If you already know the key choices, provide them together.

**Example request for method A:**

> Use Looksift, method A, style 0048. Create a square image of one red fox resting beside a small cluster of ferns. Show the whole fox, with its tail curled around its paws and plenty of open space around the silhouette. Use a warm ivory background and soft daylight. No text. You may complete secondary details while keeping the subject and layout. Reply in English.

**Example request for method B:**

> Use Looksift, method B. I will upload a style reference when generating. Create a wide image of a solitary lighthouse on a low rocky island at dawn, viewed from a calm sea. Keep the lighthouse on the right and leave open water on the left. No people or lettering. Use 16:9. You may develop secondary details, but the eventual reference should supply visual style only. Reply in English.

These are ready-to-try request examples, not claims that those new scenes have already been rendered. The image gallery above has its own recorded scene prompts.

### 4. Resolve any meaningful gaps

The Agent retains what you have already supplied and asks one necessary unresolved item at a time. That might be a missing style number, a consequential scene detail, the aspect ratio or how you want missing details handled.

You do not need to complete a rigid questionnaire. A short, precise brief can be sufficient; a long list of vague adjectives may still need clarification. Missing information is judged by whether it affects the intended picture.

### 5. Take the prompt to your drawing tool

Copy the completed prompt into your chosen Qwen Image 2.1 workflow and use the confirmed frame. For method B, attach the selected reference there as well. A reference mentioned in the conversation is not automatically sent to the drawing model.

Inspect the result and describe any changes you want. If the frame changes, Looksift should recompose the description for the new frame while retaining your settled subject and constraints.

## What the prompt delivery contains

Ordinary delivery contains a complete scene description: the requested subject, relevant actions and relationships, composition, visual treatment, materials, lighting and environment. Exact requested words inside the image remain unchanged.

By default, you receive a complete English prompt plus a complete equivalent in your selected communication language. When that language is English, one complete English version serves both roles. You can explicitly request a single language. A short usage note states the chosen ratio and, for reference-based generation, reminds you to attach the reference.

**The language switch at the top of this repository changes the documentation language. It does not set your Agent's conversation language or prompt-output preference.**

If you need machine-readable output, request JSON explicitly. Text-to-image uses `rewritten_prompt` and `wh_ratio`; editing adds `ratio_follow`, with exactly one ratio field populated. JSON-only delivery contains the official object without introductory text or an extra translation field. The detailed schemas and pinned originals are explained in the [template guide](skills/looksift/references/qwen-image-2.1-official/README.md).

## Preferences that stay under your control

You can ask the Agent to remember a default, such as a preferred aspect ratio, communication language or permission to complete secondary details. Current explicit requests take priority over older defaults.

Repeated user choices can be tracked as candidates, but repetition is not permission to make them permanent. A temporary choice applies to the current request. An Agent's own creative decisions do not become your habits.

Preference data is stored locally outside the distributable bundle. It is not included in the public repository. There is no built-in cloud or cross-device synchronization, and shared machines need a reliable profile for each user. Replacing the Skill does not automatically erase separately stored preferences. See the [preference guide](skills/looksift/references/user-preferences.md) for the behavior and controls.

## What is in the package

```text
looksift/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── assets/examples/
├── docs/
│   ├── examples.md
│   └── examples.zh-CN.md
└── skills/looksift/
    ├── WORKFLOW.md
    ├── scripts/
    │   ├── lookup_style.py
    │   └── preferences.py
    └── references/
        ├── styles.json
        ├── styles/
        ├── library-manifest.json
        ├── user-preferences.md
        └── qwen-image-2.1-official/
```

The root [SKILL.md](SKILL.md) is the canonical entry. The [workflow](skills/looksift/WORKFLOW.md) carries the detailed operating rules. Exact library counts belong to the [library manifest](skills/looksift/references/library-manifest.json), so they can be checked against the installed release.

## Frequently asked questions

**Does Looksift generate images?**  
It delivers prompts. Rendering is performed by your separate image-generation tool. No paid generation request is launched automatically by this Skill.

**Do I need a style number every time?**  
Method A needs a valid exact number. Method B can prepare a style-reference prompt without one.

**Must I upload the reference before the Agent can help?**  
For ordinary method B prompt preparation, you can supply it later to the drawing tool. A task asking the Agent to inspect an existing image, edit a particular canvas or preserve specific visual evidence may require that image during the conversation.

**Will a reference's people or background appear in my new image?**  
The prompt assigns a style-only reference to visual treatment and describes your new content separately. Final behavior still depends on the drawing model and the supplied inputs.

**Can I use the prompts with another model?**  
The wording can be tried elsewhere, but the templates and stated target are Qwen Image 2.1. Other models may interpret the same prompt differently; cross-model equivalence is not promised.

**Is this the official Qwen prompt-enhancement model?**  
Looksift supplies official template resources to your host Agent. It does not itself run Qwen's separately released prompt-enhancement checkpoints.

**Does it guarantee the exact same style?**  
No. A well-formed prompt does not establish visual equivalence. Judge the generated image, the chosen reference and the actual settings together.

**Does the English homepage force English conversation?**  
No. Documentation, conversation and requested prompt language are separate choices.

## Websites and source resources

| Resource | What it is for |
| --- | --- |
| [Looksift](https://looksift.com) | The project's style gallery: browse, compare and choose available style examples and references. |
| [Official Qwen Image 2.1 repository](https://github.com/QwenLM/Qwen-Image-2.1) | Upstream model documentation and image-generation resources. |
| [Pinned template sources](skills/looksift/references/qwen-image-2.1-official/manifest.json) | Exact source revision, original links and checksums used by this bundle. |
| [Midlibrary](https://midlibrary.io) | Source references for records that identify Midlibrary provenance; individual case pages retain their source links. |

Looksift is a separate project. Links and credits identify resources and provenance; they do not imply an official affiliation or endorsement.

## License and credits

Project code and documentation are provided under the [MIT license](LICENSE). Bundled Qwen template originals retain their [upstream license](skills/looksift/references/qwen-image-2.1-official/LICENSE). Source references retain their own provenance; the project license does not relicense third-party source artworks. The case images are generated library outputs, with model and source credits listed on the [examples page](docs/examples.md).
