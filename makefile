# vim:fdm=marker

# Constants                                                                 {{{1
# ==============================================================================

# Targets                                                                   {{{1
# ==============================================================================

.PHONY: help
help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "$(COLOR_BLUE)%-18s$(COLOR_NONE) %s\n", $$1, $$2}'

.PHONY: setup-environment
setup-environment: ## Setup the environment
	@echo 'Setting environment variables'
	@export SPOTIPY_CLIENT_ID="${SECRET_SPOTIFY_CLIENT_ID}"
	@export SPOTIPY_CLIENT_SECRET="${SECRET_SPOTIFY_CLIENT_SECRET}"

.PHONY: insinuate-ssh-cert
insinuate-ssh-cert: ## Add the SSH certificate
	@echo 'Setting environment variables'
	export SPOTIPY_CLIENT_ID := $SECRET_SPOTIFY_CLIENT_ID
	export SPOTIPY_CLIENT_SECRET := $$SECRET_SPOTIFY_CLIENT_SECRET

