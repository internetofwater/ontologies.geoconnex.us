## Competency Questions

<!--
What datasets are available for a given watershed?
Which monitoring locations lie on a particular river?
What variables are measured at those locations?
What source dataset produced a derived feature?
Which evidence records support a wetland classification?
Which version of a dataset was used in an analysis?
Which organizations publish information about the same feature?

-->

## CQ-HYDRO-001

**Question:** Which NHDPlus flowlines belong to a specified GeoConnex mainstem?

**Use case:** A user needs to move between detailed NHDPlus hydrography and a persistent, named GeoConnex mainstem.

**Collections involved:**

- Mainstems
- NHDPlus flowlines

**Required concepts:**

- Mainstem
- NHDFlowline
- COMID
- Mainstem membership

**Expected relationship:**
`gcx-hydro:partOfMainstem`

**Currently answerable:** Partially

**Current limitation:** Membership may be available through lookup data but is not represented consistently in the published graph.

**Graph change potentially required:** Materialize the mainstem membership relationship and explicitly type both resources.

**Priority:** High

**Test:** A SPARQL query should return the mainstem associated with a known COMID.
