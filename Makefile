.PHONY: all generate clean

default_openapi_jar_path = openapi-generator-cli.jar
ifeq "$(OPENAPI_GENERATOR_JAR_PATH)" ""
	openapi_jar_path := $(default_openapi_jar_path)
else
	openapi_jar_path := $(OPENAPI_GENERATOR_JAR_PATH)
endif

all: clean generate
generate:
	@echo "Generating code..."
	java -jar $(openapi_jar_path) generate -v -i spec/openapi.yaml -c open-api-conf.yaml -g python -o generated 
	/bin/cp -r generated/docs . # use /bin/cp to prevent aliasing from cp to cp -i
	cp -r generated/ubiquity/ubiquity_openapi_client ubiquity/ # don't do this for the generated library to not overwrite code by mistake
	
clean_generated:
	@echo "Cleaning up 'generated' folder..."
	rm -rf generated

clean_library:
	@echo "Cleaning up generated library at 'ubiquity/ubiquity_openapi_client'..."
	rm -rf ubiquity/ubiquity_openapi_client

clean: clean_generated clean_library

.PHONY: test
test: clean_generated
	pytest
