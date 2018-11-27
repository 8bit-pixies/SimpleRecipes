js:
	cd simple_recipes; \
	python -m transcrypt -b -p .none -n $(py)

js_sources:= $(shell cd __target__ && find . -name *.js)


nd: 
	npx babel simple_recipes/__target__/$(py).js --out-file $(py).js


build:
	./build.sh $(py)


clean:
	rm -r -f *.js
	rm -r -f __target__/