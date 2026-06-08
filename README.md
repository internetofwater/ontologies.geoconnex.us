# Geoconnex Alignment Recommendations

This folder contains a small alignment ontology:

- `geoconnex_ontology.ttl`

It turns the initial comparison of the Geoconnex class/property inventory against Schema.org and SawGraph into concrete Turtle axioms. The file is intentionally conservative: it recommends bridge axioms and cleanup notes without trying to replace SawGraph, HY_Features, GeoSPARQL, Schema.org, DCAT, SOSA/SSN, or QUDT.

The current TTL has coverage for every class and property in the provided inventory after normalizing `schema:` CURIEs, `http://schema.org/` IRIs, and HY_Features `/def/appschema/` IRIs to their recommended canonical forms.

## Design Goals

The main goal is to make Geoconnex graph data easier to query, validate, and discover across three overlapping audiences:

- hydrology and water knowledge graphs, where SawGraph, HY_Features, HyFO, GWML2, WBD, and NHDPlusV2 are the strongest fit;
- geospatial reasoning, where GeoSPARQL and Simple Features are the right formal geometry layer;
- web and dataset discovery, where Schema.org and DCAT are more visible to crawlers, catalogs, and general data users.

The TTL therefore treats Schema.org as a discovery layer, not as the only semantic model. It keeps hydrologic semantics anchored in SawGraph/HY_Features and spatial semantics anchored in GeoSPARQL.

## Important Cleanup Choices

The source CSVs contain mixed URI forms and a few type/property category issues.

Schema.org terms should be normalized to `https://schema.org/`. For example, `http://schema.org/Organization` and `schema:GeoCoordinates` should be treated as `https://schema.org/Organization` and `https://schema.org/GeoCoordinates` in exported RDF.

HY_Features terms should be normalized to SawGraph's namespace pattern:

```text
https://www.opengis.net/def/schema/hy_features/hyf/
```

The inventory also has some rows that are in the wrong list:

- `schema:governmentAgency` is a property, not a class.
- `schema:type` should generally not be used in RDF. Use `rdf:type`.
- `hyf:HY_IndirectPosition`, `hyf:HY_DistanceFromReferent`, and `hyf:HY_DistanceDescription` are class-like terms and should not be treated as properties.

## Property Classification

The TTL avoids generic `rdf:Property` declarations. Each property is classified as an `owl:ObjectProperty`, `owl:DatatypeProperty`, or `owl:AnnotationProperty` based on the recommended RDF object form.

Object properties are used when the value should be another resource. Examples include `schema:distribution`, `schema:publisher`, `schema:provider`, `schema:governmentAgency`, `schema:variableMeasured`, `schema:measurementMethod`, `schema:measurementTechnique`, `dcterms:conformsTo`, `qudt:hasUnit`, and `qudt:hasQuantityKind`.

Datatype properties are used when the value should be a literal. Examples include `schema:latitude`, `schema:longitude`, `schema:elevation`, `schema:polygon`, `schema:line`, `schema:coordinates`, `schema:encodingFormat`, `schema:temporalCoverage`, `schema:value`, `schema:unitCode`, `schema:unitText`, `schema:propertyID`, and `hyf:interpolative`.

URL-valued fields are modeled deliberately. `schema:contentUrl` and `schema:url` are object properties in this alignment because they work best as IRI objects and can then align cleanly to DCAT. If a source emits URL strings, normalize those strings to IRIs during RDF generation.

`schema:name` and `schema:description` are annotation properties because they are lightweight labels/descriptions rather than domain relations in this alignment layer.

`rdf:type` is not redeclared. It is the built-in RDF type predicate and should remain the predicate used for class membership.

## SawGraph Integration

The alignment ontology imports SawGraph's water ontology:

```turtle
owl:imports <http://purl.org/spatialai/spatial/water-full> .
```

SawGraph already adapts and extends HY_Features, HyFO, GWML2, WBD, NHDPlusV2, GeoSPARQL, and QUDT. That makes it a better hydrology backbone than a new Geoconnex-only class hierarchy.

The recommended pattern is:

- type hydrologic things as HY_Features or SawGraph-compatible classes;
- use GeoSPARQL geometry properties for spatial reasoning;
- add Schema.org metadata alongside those types for discovery.

One important network modeling choice is to keep immediate upstream/downstream relations separate from transitive closure relations. SawGraph models this distinction well. `hyf:downstreamWaterBody` should represent the immediate downstream relation, while NHDPlusV2-style closure properties can support reachability queries.

## Schema.org Integration

Schema.org is useful for search and general metadata, but several Schema.org classes and properties are intentionally broad. The TTL mostly uses `skos:closeMatch`, `rdfs:subPropertyOf`, and editorial notes instead of strong `owl:equivalentClass` claims.

For example, `schema:Dataset` is marked as close to `dcat:Dataset`, but not globally equivalent. In practice, Geoconnex dataset resources can be typed as both:

```turtle
ex:dataset a schema:Dataset, dcat:Dataset .
```

The same principle applies to measured values. `schema:PropertyValue` is close to `qudt:QuantityValue`, but it is broader and less formal. Use Schema.org for web-facing metadata and QUDT for unit-aware numeric semantics.

## Spatial Modeling

The TTL keeps Schema.org geography and GeoSPARQL geometry distinct:

- `schema:Place` is treated as a kind of `geo:Feature`.
- Simple Features geometry classes such as `sf:Point`, `sf:LineString`, and `sf:Polygon` are subclasses of `geo:Geometry`.
- `schema:GeoCoordinates` is close to `sf:Point`, but not equivalent.
- `schema:GeoShape` is close to `geo:Geometry`, but not equivalent.

This avoids accidentally treating a lightweight web metadata object as a fully specified spatial geometry.

The alignment uses `schema:geo` directly for Schema.org-facing coordinate or shape summaries. It does not mint a Geoconnex-specific subproperty of `schema:geo`.

For machine spatial reasoning, prefer:

```turtle
geo:hasGeometry / geo:defaultGeometry
geo:asWKT
```

For web discovery, keep:

```turtle
schema:geo
schema:latitude
schema:longitude
schema:polygon
schema:line
```

## Dataset and Distribution Modeling

The TTL bridges Schema.org dataset metadata to DCAT:

- `schema:DataDownload rdfs:subClassOf dcat:Distribution`
- `schema:distribution rdfs:subPropertyOf dcat:distribution`
- `schema:contentUrl rdfs:subPropertyOf dcat:downloadURL`
- `schema:encodingFormat skos:closeMatch dcat:mediaType`
- `schema:publisher rdfs:subPropertyOf dcterms:publisher`

This lets the same data support Schema.org-oriented discovery and DCAT-oriented catalog interoperability.

## Observations, Variables, and Units

The recommended measurement pattern combines Schema.org, SOSA/SSN, and QUDT:

- use `schema:variableMeasured` for web-discovery metadata;
- type formal observed variables as `sosa:ObservableProperty` or `qudt:QuantityKind`;
- use `qudt:hasUnit` with a QUDT unit IRI when possible;
- keep `schema:unitCode` or `schema:unitText` as lightweight labels or codes.

The TTL includes a union class, `geoconnex:MeasuredVariable`, so `schema:variableMeasured` can point to Schema.org property values, SOSA observable properties, or QUDT quantity kinds.

## How To Extend

Use this TTL as an alignment layer, not as the whole ontology. A practical next step is to generate a cleaned class/property inventory from the CSVs, then add:

- labels and definitions for any Geoconnex-specific terms;
- SHACL shapes for data validation;
- examples showing a catchment, flowpath, monitoring location, dataset, and measured variable;
- explicit mappings for any local Geoconnex predicates that are not already covered by Schema.org, HY_Features, GeoSPARQL, DCAT, SOSA/SSN, or QUDT.

The safest general rule is: use strong OWL equivalence only when two terms really have the same intended meaning in all contexts. Otherwise, prefer `rdfs:subClassOf`, `rdfs:subPropertyOf`, `skos:closeMatch`, or an editorial note.
