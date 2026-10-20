# Modeling Decision: Representing HY_Features Figure 23

| Decision metadata | Value |
| --- | --- |
| **Scope** | OGC HY_Features Figure 23 |
| **Status** | Recommended |
| **Primary model** | OWL/RDFS class hierarchy |
| **Complementary models** | SKOS concept schemes and SHACL shapes |

> [!IMPORTANT]
> **Decision:** Model the formal feature types in Figure 23 as an OWL/RDFS
> class hierarchy. Use SKOS for classification and terminology alignment, and
> use SHACL for validation.

## 🧭 How this document is organized

This decision record uses the applicable parts of the
[Diátaxis documentation framework](https://diataxis.fr/):

| Diátaxis mode | Use in this document | Go to |
| --- | --- | --- |
| **Explanation** | Understand why Figure 23 represents class semantics | [Why Figure 23 is a class hierarchy](#explanation-why-figure-23-is-a-class-hierarchy) |
| **How-to guide** | Apply the decision to an ontology | [Apply the modeling decision](#how-to-apply-the-modeling-decision) |
| **Reference** | Select the correct RDF mechanism | [Mechanism by modeling purpose](#reference-mechanism-by-modeling-purpose) |

> [!NOTE]
> Diátaxis tutorials are learning-oriented, end-to-end lessons. This modeling
> decision does not include one because its purpose is to record and apply an
> architectural decision, not teach RDF from first principles.

## Decision at a glance

Model the formal feature types in Figure 23 of OGC HY_Features as an OWL/RDFS class hierarchy. Use SKOS for code lists, user-facing classifications, and mappings to external terminology. Use SHACL to implement the UML cardinalities and constraints.

In short:

- **OWL/RDFS** defines what a hydrologic feature *is* and supports inheritance.
- **SKOS** describes how features are categorized or mapped across vocabularies.
- **SHACL** validates whether feature data satisfies structural constraints.

This hybrid design most closely preserves the semantics of the OGC conceptual model while supporting discovery, terminology alignment, and data validation.

## Explanation: why Figure 23 is a class hierarchy

The HY_Features specification says that `HY_HydroFeature` is “specialized into more specific feature types.” These feature types inherit properties, associations, cardinalities, and constraints. Those are class semantics, not merely vocabulary organization.

Representing the types as OWL/RDFS classes provides two important capabilities:

1. A reasoner can infer membership in broader feature types.
2. Specialized feature types can carry their own relationships and validation rules.

For example, `HY_DendriticCatchment` has single-outflow and single-lower-catchment constraints in the conceptual model. These constraints should normally be implemented with SHACL, possibly supplemented by OWL.

The HY_Features conformance requirements also treat the Figure 23 elements as feature types and require implementations to retain their mandatory properties and associations.

## How-to: apply the modeling decision

### 1. Define the formal feature types as classes

Declare `HY_HydroFeature` and its specialized types as OWL classes. Connect each specialized type to its parent with `rdfs:subClassOf`.

```turtle
hyf:HY_HydroFeature a owl:Class .

hyf:HY_Catchment
    a owl:Class ;
    rdfs:subClassOf hyf:HY_HydroFeature .

hyf:HY_HydroNexus
    a owl:Class ;
    rdfs:subClassOf hyf:HY_HydroFeature .

hyf:HY_CatchmentRealization
    a owl:Class ;
    rdfs:subClassOf hyf:HY_HydroFeature .

hyf:HY_DendriticCatchment
    a owl:Class ;
    rdfs:subClassOf hyf:HY_Catchment .
```

### 2. Type feature instances with the most specific applicable class

```turtle
ex:catchment123 a hyf:HY_DendriticCatchment .
```

A reasoner can then infer:

```turtle
ex:catchment123
    a hyf:HY_Catchment,
      hyf:HY_HydroFeature .
```

> [!TIP]
> Type an instance with the most specific known class. The class hierarchy
> allows a reasoner to infer its broader types.

### 3. Use SKOS for classification values

Use SKOS when a value classifies a feature without changing the feature's structural model. Appropriate uses include:

- hydro-location types;
- drainage-pattern categories;
- name-usage types;
- organizational classifications;
- locally defined feature categories; and
- mappings among USGS, WMO, Geoconnex, and project terminology.

```turtle
ex:HydroFeatureTypeScheme
    a skos:ConceptScheme ;
    skos:prefLabel "Hydrologic feature categories"@en .

ex:stream
    a skos:Concept ;
    skos:inScheme ex:HydroFeatureTypeScheme ;
    skos:prefLabel "Stream"@en ;
    skos:broader ex:watercourse .

ex:feature123
    a hyf:HY_HydroFeature ;
    ex:featureType ex:stream .
```

Here, `ex:stream` is a classification value. Assigning it does not automatically give `ex:feature123` additional properties or constraints.

### 4. Define associations as object properties

Represent relationships among hydrologic features with OWL object properties. Keep these associations separate from SKOS semantic relations such as `skos:broader`.

### 5. Validate constraints with SHACL

Translate the conceptual model's cardinalities and data-quality requirements into SHACL shapes. Use OWL axioms only where their open-world semantics match the intended inference behavior.

### 6. Add terminology crosswalks

Use SKOS mapping properties such as `skos:exactMatch` and `skos:closeMatch` to connect classification concepts across external vocabularies. Do not use these properties as substitutes for class equivalence or subclass relationships.

## Reference: mechanism by modeling purpose

| Modeling purpose | RDF mechanism |
| --- | --- |
| Formal HY_Features types from Figure 23 | OWL/RDFS classes |
| Specialization and inheritance | `rdfs:subClassOf` |
| Associations between features | OWL object properties |
| Cardinality and data-quality validation | SHACL shapes |
| Code lists and descriptive categories | SKOS concept schemes |
| Crosswalks between external vocabularies | `skos:exactMatch`, `skos:closeMatch`, and related mapping properties |

## Reference: choosing between a class and a concept

Use an **OWL/RDFS class** when membership changes what can be inferred or validated about a resource. Use a **SKOS concept** when the value labels, organizes, or maps a resource without introducing structural semantics.

Ask these questions:

1. Does membership imply inherited properties, associations, or constraints? If yes, use a class.
2. Is the term primarily a code-list value, category, or vocabulary mapping? If yes, use a SKOS concept.
3. Does the model need both formal semantics and a searchable vocabulary view? If yes, dual typing may be appropriate, with the caution below.

## Caution: dual typing

A formal class may also be represented as a SKOS concept when a searchable vocabulary view is required:

```turtle
hyf:HY_Catchment
    a owl:Class, skos:Concept ;
    rdfs:subClassOf hyf:HY_HydroFeature ;
    skos:broader hyf:HY_HydroFeature ;
    skos:inScheme ex:HYFeatureTypeScheme .
```

> [!CAUTION]
> `rdfs:subClassOf` and `skos:broader` express different relationships and
> must be maintained consistently. Introduce dual typing only when the
> vocabulary view serves a clear user or application requirement.

## Sources

- OGC HY_Features, section 7.3 and Figure 23
- OGC HY_Features conformance requirements
