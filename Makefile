.PHONY: all generate clean

default_python_interpreter = python
ifeq "$(PYTHON_INTERPRETER)" ""
	pythoni := $(default_python_interpreter)
else
	pythoni := $(PYTHON_INTERPRETER)
endif

all: clean generate
generate:
	@echo "Generating code..."
	docker run --rm -v "$$(pwd):/local" \
		--user $(shell id -u):$(shell id -g) \
		openapitools/openapi-generator-cli:v5.2.0 generate -v \
		-i /local/spec/openapi.yaml \
		-g python \
		-o /local/generated \
		-c /local/open-api-conf.yaml

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
	$(pythoni) -m pytest
