# vim: noexpandtab:syntax=make
CWD	=$(shell pwd)
PYTHON3_LIB_DIR ="/usr/lib/python3/dist-packages"
PYTHON3_MODULE_NAME=eda


clean:
	find . | grep -E "(__pycache__|\.pyc$\)" | xargs rm -rf
	rm -rf dist build
	rm -rf *.egg-info
	rm -rf ../*.orig.tar.gz
	rm -rf *.egg-info


links:
	make purge
	ln -s $(CWD)/$(PYTHON3_MODULE_NAME) $(PYTHON3_LIB_DIR)/$(PYTHON3_MODULE_NAME)


purge:
	rm -rf $(PYTHON3_LIB_DIR)/$(PYTHON3_MODULE_NAME)


bump:
	git add $(CWD)/$(PYTHON3_MODULE_NAME)/__init__.py
	git commit -m "bump version"


upload:
	python3 $(CWD)/setup.py sdist upload
	make clean


deb:
	dpkg-buildpackage -rfakeroot -b


devpackage:
	dpkg-buildpackage -rfakeroot -b -us -uc
