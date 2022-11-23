build_folder := _build
touch_done=@mkdir -p $(@D) && touch $@;

TESTS := $(filter-out %/__init__.py, $(wildcard smartpy/tests/*.py))

all:
	@$(MAKE) -s install-smartpy
	@$(MAKE) -s install-smartpy-utils

# <SmartPY>

smartpy/tests/%: smartpy/tests/%.py
	@$(build_folder)/smartpy-cli/SmartPy.sh test $< smartpy/tests/baselines/$*

clean_tests:
	@rm -rf smartpy/tests/baselines

test: install-smartpy-utils clean_tests $(TESTS:%.py=%)
	@$(MAKE) -s test-smartpy

install-smartpy: $(build_folder)/install-smartpy
$(build_folder)/install-smartpy:
	@rm -rf $(build_folder)/smartpy-cli
	@bash -c "bash <(curl -s https://smartpy.io/cli/install.sh) --prefix $(build_folder)/smartpy-cli --yes"
	$(touch_done)

install-smartpy-utils:
	@cp smartpy/utils.py $(build_folder)/smartpy-cli/smartpy_utils.py

test-smartpy:
	$(build_folder)/smartpy-cli/SmartPy.sh test smartpy/tests/utils.py smartpy/tests/baselines

# </SmartPY>

.PHONY: clean
clean:
	@rm -rf $(build_folder)
