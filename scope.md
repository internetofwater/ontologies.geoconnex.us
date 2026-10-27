# Geoconnex Ontology Scope

## Status

Draft version 0.1

## Purpose

The Geoconnex ontology will provide a modular, extensible, and machine-readable semantic model for Geoconnex reference features and their relationships. It will help people and software understand the structure and meaning of the Geoconnex graph, support reuse in downstream knowledge graphs, and enable reasoning where appropriate.

Ontology development will proceed incrementally by Geoconnex reference collection, with reusable concepts maintained in shared semantic modules.

Existing standards will be reused whenever they adequately represent Geoconnex concepts. New GeoConnex terms will be introduced only when existing vocabularies do not provide suitable concepts or properties.

## Problem Statement/Motivation

GeoConnex publishes reference features through APIs, JSON-LD, GeoJSON, RDF, and downloadable products. The semantic structure of these resources is not always represented consistently or documented formally.

Some feature types are inferred from collection names or IRI patterns rather than explicit RDF types. Some API fields are not represented in RDF, while other fields are inherited mechanically from source datasets without stable semantic definitions. The same concept may also be represented differently across collections.

This makes it harder for external users to:

- Understand the meaning and structure of the graph
- Integrate Geoconnex data (seamlessly?) into other knowledge graphs
- Write reusable SPARQL queries across collections
- Apply reasoning consistently
- Distinguish stable GeoConnex concepts from source-specific attributes
- Understand relationships among reference-feature collections
- Track provenance, validity, replacement, and supersession

## Objectives

The ontology initiative will:

1. Model Geoconnex incrementally using individual reference collections as manageable units of work.
2. Define shared concepts and relationships in reusable ontology modules.
3. Define collection-specific usage requirements and mappings in collection profiles.
4. Align GeoConnex concepts with existing standards where appropriate.
5. Make important feature types explicit through `rdf:type`.
6. Standardize stable properties currently represented inconsistently.
7. Document the semantic meaning of important API and graph fields.
8. Support external reuse with or without an inference engine.
9. Separate ontology semantics from collection-specific validation rules.
10. Document graph changes required to adopt the ontology.
11. Preserve backward compatibility where practical.
12. Provide examples, competency questions, and validation tests.
13. Establish a process for extending and governing the ontology.

## Development Approach

### Collection-driven development

Each reference collection will provide a concrete modeling and testing unit. Work on a collection will begin with its deployed data rather than with an abstract class hierarchy.

For each collection, the project will:

1. Inventory its API, JSON-LD, GeoJSON, RDF, and downloadable fields.
2. Record representative examples and source documentation.
3. Define collection-specific competency questions.
4. Identify concepts shared with other collections.
5. Place reusable semantics in the appropriate shared module.
6. Define collection usage requirements in a collection profile.
7. Create SHACL shapes for collection-specific validation.
8. Record differences between the current graph and the proposed model.
9. Test example data against competency questions and shapes.
10. Document migration and backward-compatibility requirements.

### Shared semantic modules

Shared modules will define terms intended for reuse across multiple collections. Initial candidates are:

- `gcx-core`: concepts and properties shared broadly across Geoconnex
- `gcx-hydro`: hydrographic-network features and relationships
- `gcx-region`: hydrologic, administrative, statistical, and other regions

Module boundaries will be based on semantic cohesion and reuse, not merely on API organization.

### Collection profiles

A collection profile will specify how a particular Geoconnex collection applies the shared ontology. A profile may include:

- Classes applicable to collection records
- Required and optional properties
- Identifier expectations
- API-field-to-RDF mappings
- Source-specific attributes
- Controlled vocabularies
- SHACL constraints
- Example records
- Competency questions
- Known data limitations
- Current graph differences
- Migration requirements

Collection profiles will not redefine the meaning of shared ontology terms.

## Initial Scope

The first development phase will focus on the related mainstems and NHDPlus flowlines collections. These collections will be treated as one vertical modeling slice because their definitions, identifiers, and network relationships depend on each other.

### Mainstems profile

The initial profile will address:

- GeoConnex reference mainstems
- Mainstem identifiers and names
- Headwater network features
- Outlet network features, if required
- Relationships between mainstems and flowlines
- Mainstem provenance and source hydrography
- Current JSON-LD and GeoJSON field mappings

### NHDPlus flowlines profile

The initial profile will address:

- NHDPlus flowlines
- NHDPlusV2 COMIDs
- GNIS names and identifiers
- Immediate upstream network relationships
- Transitive upstream network relationships
- Mainstem membership
- Headwater relationships
- Hydrography version and provenance
- Superseded or replaced identifiers, where available

### Regional profiles

After the initial hydrographic-network slice, development will proceed to:

1. HUC12 and related hydrologic-unit collections
2. Counties and county equivalents
3. States and equivalent administrative regions

Regional profiles will address identifiers, nesting, geometry, spatial relationships, provenance, and mappings to external authorities.

## Initial Competency Area

The first ontology release should support questions such as:

- Which NHDPlus flowlines belong to a specified GeoConnex mainstem?
- To which mainstem does a specified flowline belong?
- What is the immediate upstream feature of a specified flowline?
- Which flowlines are transitively upstream of a specified flowline?
- What is the headwater network feature of a mainstem?
- What COMID and GNIS name identify a flowline?
- Which reference mainstem corresponds to a boundary-crossing flowline?
- Which upstream flowlines are potential surface-water sources for a service area?

The complete inventory will be maintained in `requirements/competency-questions.md`.

## Intended Users

The ontology and collection profiles are intended to support:

- GeoConnex developers and maintainers
- GeoConnex data publishers
- Knowledge-graph developers
- Hydrologists and water-data practitioners
- Application developers
- Researchers integrating GeoConnex with other datasets
- AI systems and agents interpreting GeoConnex resources
- Downstream projects such as NIDIS

## Modeling Principles

### Reuse before invention

Existing standards will be evaluated before introducing GeoConnex-specific terms. Likely standards include HY_Features, GeoSPARQL, SOSA/SSN, SKOS, PROV-O, OWL-Time, QUDT, and Dublin Core Terms.

### Stable semantics rather than API mirroring

The ontology will not mechanically convert every API field into an ontology property. Stable and meaningful concepts will receive formal semantic terms. Implementation-specific or source-specific fields may be retained in collection profiles as source attributes with appropriate provenance.

### Shared semantics without collection silos

Reference collections provide implementation boundaries, but they will not become isolated ontologies that independently redefine shared concepts. Cross-collection concepts will be defined once in a shared module and applied through profiles.

### Lightweight ontology axioms

The ontology will provide sufficient structure to make the graph understandable and reusable without imposing unnecessary logical restrictions. Validation requirements and collection-specific cardinality rules will generally be represented using SHACL rather than strong OWL axioms.

### Usable without reasoning

The ontology may support inference, but its usefulness will not depend on GeoConnex operating a reasoner. Important types and relationships may be materialized when doing so improves usability and query performance.

### Explicit provenance

Derived mappings, crosswalks, network relationships, and source-specific attributes should retain sufficient provenance to explain how they were produced.

### Backward compatibility

Existing GeoConnex IRIs and predicates should not be changed without documenting effects on current data, queries, and users. Deprecated terms may remain available through mappings or redirects where appropriate.

## Out of Scope for the Initial Phase

The initial phase will not attempt to:

- Model every GeoConnex reference-feature collection
- Convert every API field into an ontology property
- Produce an independent ontology for every collection
- Replace existing source ontologies
- Define all observation and monitoring-data concepts
- Require GeoConnex to operate an OWL reasoner
- Encode all collection validation requirements as OWL axioms
- Immediately migrate the complete deployed graph
- Resolve every historical identifier and versioning issue
- Define application-specific concepts belonging exclusively to NIDIS

## Relationship to the Existing Graph

The work will distinguish clearly between:

1. The current deployed representation of each collection
2. The proposed target semantic representation

For each collection field and proposed ontology term, the project will record:

- Current API and source fields
- Current RDF classes and predicates
- Example values
- Proposed semantic representation
- Reused external standards
- Required graph changes
- Backward-compatibility mappings
- ETL, JSON-LD context, or API changes
- Effects on existing SPARQL queries

The crosswalk will be maintained in `inventory/current-graph-crosswalk.csv`.

## Proposed Deliverables

The project will produce:

- Ontology requirements and scope documentation
- Reference-collection inventory
- Competency-question inventory
- Current-to-target term crosswalk
- Modeling-decision records
- Shared Turtle ontology modules
- Collection profiles
- Human-readable documentation
- SHACL shapes
- Example RDF records
- SPARQL competency-query tests
- Graph-change and migration documentation
- Versioning and governance guidance

## Success Criteria

The initial phase will be successful when:

1. The mainstems and NHDPlus flowlines profiles answer their competency questions.
2. Shared semantics are defined once and reused across both collections.
3. Mainstems and flowlines have explicit, documented semantic types.
4. Mainstem membership and upstream-network relationships have unambiguous definitions.
5. Important source identifiers are represented consistently.
6. The model clearly identifies reused and GeoConnex-specific terms.
7. Collection profiles document required fields and current mappings.
8. Required graph changes and compatibility paths are documented.
9. SHACL validation and SPARQL tests demonstrate the intended model.
10. The workflow can be applied to HUC12, county, state, and later collections.

## Open Questions

1. Is the ontology primarily descriptive of the current graph or normative for future GeoConnex data?
2. Which representation is authoritative when JSON-LD, GeoJSON, source data, and RDF differ?
3. What is the formal definition of a GeoConnex reference feature?
4. How should GeoConnex mainstems align with HY_Features?
5. How should NHDPlus flowlines align with HY_Features?
6. Which network relationships should be asserted, inferred, or calculated at query time?
7. Which requirements belong in shared modules versus collection profiles?
8. What backward-compatibility commitments apply to existing predicates and IRIs?
9. Who approves ontology terms, collection profiles, and releases?
10. Where will the ontology, profiles, shapes, and documentation be published?
11. How will ontology changes be coordinated with changes to the deployed graph?
12. Can profiles and graph changes be released one collection at a time?

## Initial Modeling Decision

GeoConnex ontology development will proceed incrementally by reference collection. Reusable semantics will be defined in shared domain modules, while collection-specific requirements, source mappings, validation constraints, examples, and migration notes will be maintained as collection profiles. This approach preserves alignment with deployed GeoConnex products without creating isolated ontologies for each collection.
