# Run Neo4j In A Docker Container
This GitHub Custom Action runs Neo4j in a Docker container.
It also allows users to add any of the plugin supported by the
[Neo4j documentation](https://neo4j.com/docs/operations-manual/current/docker/plugins/#docker-plugins-neo4jplugins).
Neo4j is a powerful graph database.

## Inputs
### neo4j-version
**Optional** The version of the
[Neo4j image](https://hub.docker.com/_/neo4j/tags)
to run. Defaults to `latest`.

### neo4j-plugins
**Optional** Comma separated list of plugins to use. 
The 
[Neo4j documentation](https://neo4j.com/docs/operations-manual/current/docker/plugins/#docker-plugins-neo4jplugins).
describes the available plugins.

## Outputs

### docker_container

The ID of the created docker image.

## Example usage
```yaml
uses: afoley587/setup-neo4j-with-plugins
with:
  neo4j-version: 'community-bullseye'
  neo4j-plugins: 'apoc,graph-data-science'
```

See 
[test cases](https://github.com/afoley587/setup-neo4j-with-plugins/blob/main/.github/workflows/test.yml)
for more examples.

## License
This action is licensed under the 
[MIT License](https://github.com/afoley587/setup-neo4j-with-plugins/blob/main/LICENSE).