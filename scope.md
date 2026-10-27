# GeoConnex Ontology Scope

## Status

Draft version 0.2

## Purpose

The GeoConnex ontology will provide a modular, extensible, and machine-readable semantic model for GeoConnex reference features and their relationships. It will help people and software understand the structure and meaning of the GeoConnex graph, support reuse in downstream knowledge graphs, and enable reasoning where appropriate.

Ontology development will proceed incrementally by GeoConnex reference collection, with reusable concepts maintained in shared semantic modules.

Existing standards will be reused whenever they adequately represent GeoConnex concepts. New GeoConnex terms will be introduced only when existing vocabularies do not provide suitable concepts or properties.

## Problem Statement/Motivation

GeoConnex publishes reference features through APIs, JSON-LD, GeoJSON, RDF, and downloadable products. The semantic structure of these resources is not always represented consistently or documented formally.

Some feature types are inferred from collection names or IRI patterns rather than explicit RDF types. Some API fields are not represented in RDF, while other fields are inherited mechanically from source datasets without stable semantic definitions. The same concept may also be represented differently across collections.

This makes it harder for external users to:

- Understand the meaning and structure of the graph
- Integrate GeoConnex data seamlessly into other knowledge graphs
- Write reusable SPARQL queries across collections
- Apply reasoning consistently
- Distinguish stable GeoConnex concepts from source-specific attributes
- Understand relationships among reference-feature collections
- Track provenance, validity, replacement, and supersession

## Objectives

The project will:

1. Define shared GeoConnex concepts and relationships in reusable modules.
2. Document how individual reference collections apply those shared semantics.
3. Reuse established standards where they adequately represent GeoConnex concepts.
4. Make important feature types and relationships explicit in RDF.
5. Standardize stable properties that are currently absent or represented inconsistently.
6. Support external reuse with or without an inference engine.
7. Separate ontology semantics from collection-specific validation rules.
8. Document any changes required in the existing GeoConnex graph.
9. Preserve backward compatibility where practical.
10. Support extension through documented modeling and governance processes.

## Development Approach

Each reference collection will serve as a concrete modeling and testing unit. Work on a collection will begin with an inventory of its existing API, JSON-LD, GeoJSON, RDF, source documentation, and representative records.

Concepts used across collections will be defined once in shared modules. Collection profiles will document how those concepts are applied, including field mappings, usage requirements, SHACL constraints, examples, known limitations, and migration considerations.

Initial shared modules are expected to include:

- `gcx-core`: concepts and properties shared broadly across GeoConnex
- `gcx-hydro`: hydrographic-network features and relationships
- `gcx-region`: hydrologic, administrative, and other regional features

Detailed development procedures will be maintained separately from this scope document.

## Initial Scope

The first phase will model the related GeoConnex mainstems and NHDPlus flowlines collections as one vertical slice. Initial topics include:

- Explicit feature types
- Stable identifiers and names
- Relationships between mainstems and flowlines
- Immediate and transitive upstream network relationships
- Headwater network features
- Hydrography version and provenance
- Alignment with HY_Features and GeoSPARQL
- Mappings from current API and graph fields

After this hydrographic-network slice, work will expand to HUC12, county, and state reference collections.

Collection-specific competency questions will be maintained in `requirements/competency-questions.md`.

## Intended Users

The ontology and collection profiles are intended for:

- GeoConnex developers, maintainers, and data publishers
- Knowledge-graph and application developers
- Hydrologists and water-data practitioners
- Researchers integrating GeoConnex with other datasets
- AI systems interpreting GeoConnex resources
- Downstream projects such as NIDIS

## Modeling Principles

- **Reuse before invention:** Evaluate standards such as HY_Features, GeoSPARQL, SOSA/SSN, SKOS, PROV-O, OWL-Time, QUDT, and Dublin Core Terms before creating GeoConnex-specific terms.
- **Stable semantics rather than API mirroring:** Model meaningful, reusable concepts rather than mechanically reproducing every API field.
- **Shared semantics without collection silos:** Use collections as development units without creating isolated or conflicting ontologies.
- **Lightweight axioms:** Keep the ontology understandable and reusable; place most collection-specific validation requirements in SHACL.
- **Usable without reasoning:** Do not require GeoConnex or downstream users to operate an OWL reasoner.
- **Explicit provenance:** Document the origin of derived mappings, crosswalks, and network relationships.
- **Managed change:** Record effects on existing IRIs, data, APIs, transformations, and queries before adopting model changes.

## Relationship to the Existing Graph

The work will distinguish between the current deployed representation and the proposed target model. A separate crosswalk will record current fields and predicates, proposed ontology terms, reused standards, required graph changes, compatibility mappings, and effects on existing queries.

The crosswalk will be maintained in `inventory/current-graph-crosswalk.csv`. Significant modeling choices and their justifications will be maintained as decision records under `decisions/`.

## Out of Scope for the Initial Phase

The first phase will not:

- Model every GeoConnex collection
- Convert every API field into an ontology property
- Create an independent ontology for every collection
- Replace existing source ontologies
- Require an OWL reasoner
- Immediately migrate the complete deployed graph
- Resolve every historical identifier and versioning issue
- Define concepts used only by a single downstream project

## Deliverables

- Shared ontology modules
- Collection profiles
- Competency questions and SPARQL tests
- Current-to-target graph crosswalk
- Modeling-decision records
- SHACL shapes
- Example RDF records
- Human-readable documentation
- Graph-change and migration guidance

## Success Criteria

The initial phase will be successful when:

1. Mainstems and NHDPlus flowlines have explicit, documented semantic types.
2. Their identifiers and network relationships are represented consistently.
3. Shared semantics are reused across both collection profiles.
4. Competency questions are answered by tested example data and SPARQL queries.
5. Required graph changes and compatibility paths are documented.
6. The approach can be extended to additional reference collections.

## Open Decisions

The following decisions will be addressed in separate decision records:

- Whether the ontology is descriptive of the current graph, normative for future data, or both
- Which representation is authoritative when GeoJSON, JSON-LD, RDF, and source data differ
- The formal definition of a GeoConnex reference feature
- Alignment of mainstems and flowlines with HY_Features
- Which network relationships are asserted, inferred, or calculated at query time
- Backward-compatibility commitments for existing predicates and IRIs
- Governance, approval, versioning, and publication processes
