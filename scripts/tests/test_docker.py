from pathlib import Path
from argparse import ArgumentParser
import sys
from typing import List
import subprocess
import shlex

from ..fetch_config import Config

def fetch_args() -> str:
    parser = ArgumentParser()
    parser.add_argument('tag', type=str)
    args = parser.parse_args()
    return args.tag

def run_tests(config: Config, tag: str, tests: List[Path]) -> int:
    if len(config.docker_repo) == 0 or len(config.docker_username) == 0:
        return 4
    for test in tests:
        docker_test = Path(f'/opt/acme/testing/docker/{test.name}')
        cmd = shlex.split(
            f'docker run --rm -v "{test}":{docker_test} --entrypoint '
            f'{docker_test} {config.docker_username}/{config.docker_repo}:'
            f'{tag}-test'
        )
        process = subprocess.run(cmd, stdout=sys.stdout, stderr=sys.stderr)
        if process.returncode != 0:
            return 5
    return 0

def main(config_path: Path, tests_path: Path, tag: str) -> int:
    if not tests_path.exists():
        return 1

    config = Config.load(config_path)
    if config is None:
        return 2

    tests_names = config.testing.get(tag, [])
    tests: List[Path] = []
    for test_name in tests_names:
        test = (tests_path / test_name).with_suffix('.sh')
        if not test.exists():
            return 3
        tests.append(test)

    return run_tests(config, tag, tests)

if __name__ == '__main__':
    root = Path(__file__).resolve().parent.parent.parent
    config = root / 'config.json'
    tests = root / 'tests/docker'
    tag = fetch_args()
    code = main(config, tests, tag)
    sys.exit(code)

