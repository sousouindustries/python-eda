# vim: noexpandtab:syntax=make
CWD	=$(shell pwd)
PYTHON3_LIB_DIR ="/usr/lib/python3/dist-packages"
PYTHON3_MODULE_NAME=saga


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
