# Testing the ACME Docker image

The [ACME subversion][acme-svn] distribution provides several tests located in
the `testing` folder. Run `scripts/docker/tests/run.sh` after building the image
w/ `scripts/docker/tests/build.sh` to execute these tests against the
[Docker image][docker-repo].

## Tests

All scripts assume to be placed in the `testing/docker` directory inside of the
container.

- `tests/cpus.sh`: Compiles code for several architectures and compares to an
  expected output.
- `tests/errors.sh`: Checks for errors from the compiler
- `tests/warnings.sh`: Checks for warnings from the compiler

[acme-svn]: https://sourceforge.net/p/acme-crossass/code-0/HEAD/tree/
[docker-repo]: https://hub.docker.com/r/jackwolfard/acme
