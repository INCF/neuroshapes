# Download

Neuroshapes schemas are tested using a [shacl workbench](https://github.com/BlueBrain/sbt-nexus-workbench) which is a SBT plugin that helps in the development of SHACL schemas in JSON-LD format.
Please follow these steps to run the tests and download the schemas:

* [Install sbt](https://www.scala-sbt.org/1.0/docs/Setup.html)
* Clone the INCF/neuroshapes repository and run the tests

```shell
# Go to home
cd  ~

# Clone the repository
git clone https://github.com/INCF/neuroshapes.git

cd neuroshapes

# Run 'sbt'
sbt

# Run 'test'
test

# Export all the locally defined schemas to the dir /tmp/my-schemas using <http://localhost:8080/v0> as base uri 
exportSchemas http://localhost:8080/v0 /tmp/my-schemas

# Schemas can be defined in modules that are imported by local modules. The collectResources command can be run to collect all schemas and contexts defined in this project classpath

## Collect schemas
collectResources http://localhost:8080/v1 /tmp/my-schemas schemas

## Collect everything defined
collectResources http://localhost:8080/v1 /tmp/my-schemas all



```
