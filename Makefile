.PHONY: all generate clean

default_openapi_jar_path = openapi-generator-cli-5.2.0.jar
ifeq "$(OPENAPI_GENERATOR_JAR_PATH)" ""
	openapi_jar_path := $(default_openapi_jar_path)
else
	openapi_jar_path := $(OPENAPI_GENERATOR_JAR_PATH)
endif

all: clean generate
generate:
	@echo "Generating code..."
	java -jar $(openapi_jar_path) generate -v -i spec/openapi.yaml -c open-api-conf.yaml -g python -o generated 
	mv generated/ubiquity_openapi_client src
	
clean:
	@echo "Cleaning up..."
	rm -rf generated
	rm -rf src/ubiquity_openapi_client
