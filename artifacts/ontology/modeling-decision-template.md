# Modeling Decisions

Use this document as a template for recording ontology modeling decisions.
Assign each decision a permanent identifier and a descriptive title, such as
`MD-001: Representing HY_Features Figure 23`.

## 🧭 Decision index

Add each decision to this table. Keep its identifier unchanged even if its
title or status changes.

| ID | Decision | Status |
| --- | --- | --- |
| [MD-001](#md-001-descriptive-decision-title) | Descriptive decision title | Proposed |
| [MD-002](#md-002-another-decision-title) | Another decision title | Proposed |

### Status definitions

| Status | Meaning |
| --- | --- |
| **Proposed** | Under discussion and not yet approved |
| **Accepted** | Approved for implementation |
| **Deprecated** | Still documented but no longer recommended |
| **Superseded** | Replaced by another identified decision |

---

## MD-001: Descriptive decision title

Replace the placeholder title with a concise description of the decision. The
title should communicate the subject without requiring the reader to open the
section.

| Decision metadata | Value |
| --- | --- |
| **Status** | Proposed |
| **Decision type** | Ontology structure, vocabulary, alignment, validation, or another category |
| **Applies to** | Ontology, class, property, module, or specification |
| **Primary mechanism** | OWL/RDFS, SKOS, SHACL, or another mechanism |
| **Supporting mechanisms** | Supporting standards or technologies, if applicable |
| **Supersedes** | Decision ID or “None” |
| **Superseded by** | Decision ID or “None” |

> [!IMPORTANT]
> **Decision:** State the selected modeling approach in one or two sentences.

### Context

Describe the modeling problem, relevant requirements, and constraints. Explain
why a decision is required without arguing for a particular option yet.

Questions this section may answer:

- What needs to be represented?
- Which specifications or existing models apply?
- What ambiguity or interoperability problem exists?
- Who or what will consume the resulting data?

### Options considered

#### Option A: Name of option

Briefly describe the option.

**Advantages**

- Advantage one
- Advantage two

**Disadvantages**

- Disadvantage one
- Disadvantage two

#### Option B: Name of option

Briefly describe the alternative using the same comparison criteria.

**Advantages**

- Advantage one
- Advantage two

**Disadvantages**

- Disadvantage one
- Disadvantage two

### Decision

Describe the selected option precisely. Identify the ontology constructs,
namespaces, relationships, or validation mechanisms that implementations must
use.

### Rationale

Explain why the selected option best satisfies the requirements. This is the
**explanation-oriented** part of the record: it should help future maintainers
understand the reasoning and tradeoffs behind the decision.

### Implementation guide

Describe how to apply the decision. This is the **how-to-oriented** part of the
record, so use concrete, actionable steps.

1. Complete the first implementation step.
2. Complete the second implementation step.
3. Validate the result.

> [!TIP]
> Include a verification step so implementers can confirm that the decision
> has been applied correctly.

### Examples

Provide the smallest complete example that demonstrates the decision. Use a
language identifier on fenced code blocks so GitHub applies syntax
highlighting.

```turtle
ex:ExampleClass
    a owl:Class ;
    rdfs:label "Example class"@en .
```

If useful, include a counterexample:

```turtle
# Avoid this pattern because ...
ex:ExampleClass a skos:Concept .
```

### Consequences

#### Benefits

- Describe the semantic or operational benefit.
- Describe the interoperability or maintenance benefit.

#### Tradeoffs

- Describe added complexity or limitations.
- Describe any maintenance obligations.

#### Follow-up work

- [ ] Add or update ontology terms.
- [ ] Add SHACL validation shapes.
- [ ] Add competency questions or tests.
- [ ] Update related documentation.

### Reference

Use this section for the stable facts an implementer may need to look up.

| Modeling purpose | Selected mechanism |
| --- | --- |
| Primary semantics | Replace with the selected mechanism |
| Validation | Replace with the selected mechanism |
| Terminology alignment | Replace with the selected mechanism |

### References

- [Authoritative specification](https://example.org/)
- Related ontology or vocabulary
- Related issue, pull request, or earlier modeling decision

---

## MD-002: Another decision title

Copy the complete `MD-001` section above for each additional decision, assign
the next permanent identifier, and add the new entry to the decision index.

> [!CAUTION]
> Do not renumber existing decisions after they have been referenced in code,
> issues, pull requests, ontology annotations, or published documentation.

## Authoring guidance

- Use a descriptive title in addition to the decision number.
- Record one primary modeling question per decision.
- Keep the decision statement short and unambiguous.
- Separate rationale from implementation instructions.
- Include tradeoffs, not only benefits.
- Prefer authoritative specifications in the references.
- Update the status instead of deleting a historical decision.
- Mark replacements with `Supersedes` and `Superseded by` identifiers.

## Diátaxis alignment

This template applies the relevant Diátaxis modes within each decision record:

| Diátaxis mode | Template section |
| --- | --- |
| **Explanation** | Context, options considered, and rationale |
| **How-to guide** | Implementation guide |
| **Reference** | Metadata, examples, reference table, and sources |

Tutorials are intentionally excluded. A tutorial is an end-to-end learning
experience and should normally live in separate user documentation rather than
inside an architectural decision record.
