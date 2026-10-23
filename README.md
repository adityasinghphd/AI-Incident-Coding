# AI Incident Coding

Research materials and a reusable kit for coding AI incident evidence with a risk taxonomy. The taxonomy separates five dimensions: Cause, Vector, Proximal harm, Distal harm, and Challenges. Coding connects selected concepts to source passages, reasons and supported relationships between harms.

## Read about the work

Start with the [overview](00-start-here.md), then explore:

1. [The risk taxonomy prototype](01-what-we-are-coding.md)
2. [Where our incident evidence comes from](02-where-the-incidents-come-from.md)
3. [How we code an incident](03-how-we-code-an-incident.md)
4. [What we have learned so far](04-what-we-have-learned-so-far.md)
5. [How we code mitigations](05-how-we-code-mitigations.md)
6. [Validation and expansion](06-validation-and-expansion.md)

The historical baseline covers 1,597 processed AIID records, including 1,567 development cases. The documents also describe a separate 116-entry model comparison and human validation study. Held-out model answers are not distributed here.

## Code your own incidents

Follow the [getting-started guide](coding-kit/README.md). The kit includes the [codebook](coding-kit/CODEBOOK.md), [coding manual](coding-kit/materials/CODING_MANUAL.md), [protocol](coding-kit/PROTOCOL.md), five stage prompts, output schemas, an input template and a Python launcher. Supply your own incident narrative and saved source reports, and choose the AI system that will perform the coding.

The launcher prepares each stage's materials and saves the returned answers. It makes no model or API calls. The kit uses the frozen v0.9.5 incident instrument; this repository is a research draft, and the reliability study is intended to assess how consistently it can be applied.

Markdown files can be read directly on GitHub. The matching HTML reading copies open locally after downloading the repository; open `index.html` for the document overview.

## Licensing

This repository uses separate licenses, according to the material:

| Material | License |
| --- | --- |
| Python launcher and library scripts, JSON output schemas, input template, dependency file and software build helpers if present | [MIT](LICENSE) |
| Codebook in every format, including `coding-kit/materials/VALID_CONCEPTS.json`; coding manual, written protocol, stage prompts, explanatory documents and figures | [CC BY-NC-SA 4.0](LICENSE-CONTENT.md) |

The repository's MIT license applies to the software listed above. It does not license the codebook or other research materials under MIT. HTML reading copies have the same license as the documents they render.

For reuse of research materials under CC BY-NC-SA 4.0, credit Aditya Singh, link to this repository and the license, and identify modifications. Shared adaptations must follow that license's ShareAlike terms. Commercial permissions for protected research materials require a separate arrangement with the rights holder. Third-party materials retain their own applicable terms.
