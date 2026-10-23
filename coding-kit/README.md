# Code your own incidents

Use this kit to code an incident with your chosen AI system. You provide the incident account and source reports; the kit provides the definitions, instructions and five-stage workflow.

## 1. Open the kit

Unzip the package and open the `coding-kit` folder in an AI coding agent that can read files, run Python and start separate AI contexts. The launcher uses Python 3.10 or later.

## 2. Add your incident

Save your incident narrative and available source reports in the folder. Include the report titles and source URLs where available. Supply the actual text: the launcher does not download articles from links.

Start with one incident. The agent can organize your material using the included [input template](examples/incident-template.json).

## 3. Give the agent this instruction

> Read START_CODING.md and PROTOCOL.md. Put the incident narrative and reports I provide into my-incident.json using the input template. Set up the Python environment described in the protocol and record the actual model version. Run the five-stage coding workflow, using a fresh context for each stage and only its assigned files. Save the answers unchanged. Return the final coding file and explain any flagged or blocked stages.

The workflow produces two independent codings, reconciles their differences, checks the result, and records the final decisions. The launcher prepares the files and saves responses; your AI system performs the coding.

## 4. Read the result

The final coding is saved at:

```text
runs/<run-name>/results/final/record.json
```

It contains the selected categories, supporting passages and reasons. Earlier answers and check findings remain in the same run folder. Review the coding against the sources; passing a file check does not establish that every judgment is correct.

For another incident, supply new material and use a new run folder.

## Reference material

Read the [codebook](CODEBOOK.md) for definitions and the [coding manual](materials/CODING_MANUAL.md) for evidence rules. The [protocol](PROTOCOL.md) includes terminal commands if you prefer to prepare and submit each stage yourself.

The kit uses the experiment's frozen v0.9.5 codebook. You can also apply its definitions manually, recording categories, evidence and reasons yourself.

Scripts are MIT-licensed. The codebook, protocol and other written materials use CC BY-NC-SA 4.0; see [licensing details](../LICENSE-CONTENT.md).
