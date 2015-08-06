SASSOPTS=--scss --style expanded

default: generate

generate: generate-sass generate-html generate-svg

generate-html:
	bin/assemble.py

generate-svg:
	(cd graphviz && bash makeall.sh)

generate-sass:
	sass --update ${SASSOPTS} .

force-sass:
	sass --update ${SASSOPTS} --force .

watch-sass:
	sass --watch  ${SASSOPTS} .
