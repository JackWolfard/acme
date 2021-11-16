[![Build][build-shield]][build-action]
[![Docker version][docker-version-shield]][docker-repo]
[![Docker image size][docker-image-shield]][docker-repo]
[![Docker stars][docker-stars-shield]][docker-repo]
[![Docker pulls][docker-pulls-shield]][docker-repo]

# ACME Cross-Assembler Docker Distribution

This [repository][repo] serves as a [Docker][docker] distribution of
[ACME][acme] at [jackwolfard/acme][docker-repo] by leveraging
[GitHub Actions][github-actions] to build the trunk of the
[SVN repository][acme-svn].

## Reference

ACME is available at `/bin/acme` and can be called from CLI as `acme`.

## Tags

- `latest`: Trunk of SVN repository
- `stable`: Latest stable release
- `0.97`: Release 0.97
- `0.96`: Latest stable 0.96.x release
- `0.96.5`: Release 0.96.5
- `0.95`: Latest stable 0.95.x release
- `0.95.8`: Release 0.95.8
- `0.94`: Latest stable 0.94.x release
- `0.94.12`: Release 0.94.12

[acme]: https://sourceforge.net/projects/acme-crossass/
[acme-svn]: https://sourceforge.net/p/acme-crossass/code-0/HEAD/tree/
[github-actions]: https://github.com/features/actions
[docker]: https://www.docker.com/
[docker-repo]: https://hub.docker.com/r/jackwolfard/acme
[repo]: https://github.com/JackWolfard/acme
[build-shield]: https://img.shields.io/github/workflow/status/jackwolfard/acme/build-containers?label=build&logo=github&style=flat-square
[build-action]: https://github.com/jackwolfard/acme/actions?workflow=build-containers
[docker-version-shield]: https://img.shields.io/docker/v/jackwolfard/acme?sort=semver&style=flat-square
[docker-image-shield]: https://img.shields.io/docker/image-size/jackwolfard/acme?sort=semver&style=flat-square
[docker-stars-shield]: https://img.shields.io/docker/stars/jackwolfard/acme?style=flat-square
[docker-pulls-shield]: https://img.shields.io/docker/pulls/jackwolfard/acme?style=flat-square
