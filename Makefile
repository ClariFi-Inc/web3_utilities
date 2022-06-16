MODULE := web3_utilities
BLUE='\\033[0\;34m'
MAGENTA='\\033[35m'
NC='\\033[0m' # No Color
CYAN='\\033[36m'

include .env
export

.PHONY: clean test

help:
	@echo ''
	@echo '${CYAN}Target Information.  make <target> in the shell to run a target${NC}'
	@echo '${CYAN}---------------------------------------------------------------${CYAN}'
	@echo ''

	@echo '${MAGENTA}Avalanche Network:${NC}'
	@echo '    make avax_gas_fee_watcher               outputs the current avax network gas fee every 3 seconds            '
	@echo '    make avax_get_current_block             outputs the current avax network gas fee every 3 seconds            '
	@echo ''
	@echo ''

################## Avalanche Network Code  #####################################
avax_gas_fee_watcher: .env
	@python -m avalanche.examples.gas_fee_watcher

avax_get_current_block: .env
	@python -m avalanche.examples.get_latest_block_transactions


run: .env
	@python -m $(MODULE)
