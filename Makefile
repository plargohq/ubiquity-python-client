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
	cp -r generated/ubiquity/ubiquity_openapi_client ubiquity/
	
clean_generated:
	@echo "Cleaning up 'generated' folder..."
	rm -rf generated

clean_library:
	@echo "Cleaning up generated library at 'ubiquity/ubiquity_client'..."
	rm -rf ubiquity/ubiquity_client

clean: clean_generated clean_library
