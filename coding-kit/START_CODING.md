# Launch the coding workflow

Prepare your incident file using the [input template](examples/incident-template.json), then give the following instruction to an AI coordinator that can read local files and arrange fresh isolated coding contexts. Substitute your actual paths and model version. The coordinator may use the launcher; individual coding stages read only their assigned materials.

> Use this incident coding kit to code the incident in `my-incident.json`. Read `README.md` and `PROTOCOL.md` in full. Initialize a new run folder with the actual model version, then follow strict, lenient, reconcile, verify and final using `code_incidents.py`. Give each stage a fresh isolated context and only its assigned files, beginning with `TASK.md`. Strict and lenient must be independent. Save each raw response and submit it unchanged. Keep validation findings out of later coding contexts. Stop if a response is unusable, a required input cannot be read, or the platform cannot provide the required fresh contexts. Do not substitute a shared conversation for independent stages, fetch external sources, change the codebook, repair model answers or rerun for a cleaner result. Return the final record's location and each stage's saved/flagged/blocked status.

For a chat interface without a coordinator, run the commands in the [quick start](README.md) yourself, upload only each job's assigned files to a new conversation, and save its returned JSON before continuing. Five fresh conversations are needed for the complete workflow.

The included launcher prepares the materials and records responses. Connecting an API or an AI platform is the user's choice; the kit itself makes no model calls.
