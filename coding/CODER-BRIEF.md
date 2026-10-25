# Coder brief (identical for Coder A and Coder B)

You are one of two independent coders. You will never see the other coder's work.

## Inputs
1. The codebook: `study/prereg/PREREGISTRATION.md`, sections 2 and 4. Apply it literally.
2. The product dossiers: every `study/dossiers/*.md` except `TEMPLATE.md` and the `_scratch_*` folders.
3. The standards evidence: `study/research/standards_evidence.md`.

You may open URLs cited in a dossier to check a quotation. You may not search for new evidence. If the dossier lacks evidence for a function, code what the dossier supports. "No documented evidence" means 0 or 1 as the codebook says. It does not mean the coder fills the gap from memory.

Do not read any other file in `/Users/mudaberjamshaid/megagoals/o1/christensen-paper/` or its parents, including the `research/` notes other than standards_evidence.md and any earlier classification. Do not use prior knowledge of a product to raise a code above what the cited evidence supports.

## Task 1: products
For each dossier, assign F1 to F5 (0, 1 or 2) and SUFF (1 only if the sufficiency rule is met, else 0). Write:
- `<outdir>/codes.csv` with header `slug,F1,F2,F3,F4,F5,SUFF`, one row per dossier, slug = dossier filename without `.md`.
- `<outdir>/reasons.md`: for each product and function, one line giving the code and the dossier quotation (or its absence) that decides it.

## Task 2: standards
For each standard in standards_evidence.md (LTI, OneRoster, Open Badges, Common Cartridge, QTI, CASE, CLR, EDU-API, Caliper, LIS), assign the **highest verifiability level a receiving system can reach for that standard's main information**, as defined in PREREGISTRATION.md section 2: 1 = V1 syntactic only, 2 = V2 provenance, 3 = V3 referent checkable against an independent source of truth the receiver can reach. Write `<outdir>/standards.csv` with header `standard,V,reason`. Do not look up or consider certification counts. Code the nature of the information, not how popular the standard is.

## Output rules
Plain text, no em dashes. When unsure between two codes, choose the lower one and say why in reasons.md.
