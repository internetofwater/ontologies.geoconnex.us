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

## Relationship to the Existing Graph

The work will distinguish between the current deployed representation and the proposed target model. A separate crosswalk will record current fields and predicates, proposed ontology terms, reused standards, required graph changes, compatibility mappings, and effects on existing queries.

The crosswalk will be maintained in `inventory/current-graph-crosswalk.csv`. Significant modeling choices and their justifications will be maintained as decision records under `decisions/`.

## Open Decisions

The following decisions will be addressed in separate decision records:

- Whether the ontology is descriptive of the current graph, normative for future data, or both
- Which representation is authoritative when GeoJSON, JSON-LD, RDF, and source data differ
- The formal definition of a GeoConnex reference feature
- Alignment of mainstems and flowlines with HY_Features
- Which network relationships are asserted, inferred, or calculated at query time
- Backward-compatibility commitments for existing predicates and IRIs
- Governance, approval, versioning, and publication processes
