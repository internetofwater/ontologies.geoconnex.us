import json
from pathlib import Path

from rdflib import Graph

# trivial script to convert ttl to json-ld and write it to stdout
# so that the geoconnex pipeline can consume it like a normal integration

def main():
    current_dir = Path(__file__).parent

    ttl_files = list(current_dir.glob("*.ttl"))
    if not ttl_files:
        raise Exception(f"No ttl files found in {current_dir}")

    for ttl_file in ttl_files:
        graph = Graph()
        graph.parse(ttl_file, format="turtle")

        # Serialize to JSON-LD
        jsonld = graph.serialize(format="json-ld")

        # Re-encode as compact one-line JSON 
        # this is since rdflib doesn't support writing compact JSON
        # as far as I can tell
        compact = json.dumps(
            json.loads(jsonld),
            separators=(",", ":"),
        )

        print(compact)


if __name__ == "__main__":
    main()
