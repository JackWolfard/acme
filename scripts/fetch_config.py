from __future__ import annotations
from pathlib import Path
from json import dumps, loads
from typing import Dict, List, Optional, Tuple
import sys
import traceback

class Config:

    latest: int
    stable: str
    releases: Dict[str,int]
    repo: str
    testing: Dict[str,List[str]]

    docker_username: str
    docker_repo: str
    
    def __init__(self, latest: int, stable: str, releases: Dict[str,int],
                 repo: str, testing: Optional[Dict[str,List[str]]] = None,
                 docker: Optional[Dict[str,str]] = None) -> None:
        self.latest = latest
        self.stable = stable
        self.releases = releases
        self.repo = repo
        self.testing = testing if testing is not None else {}
        self.docker_username = ''
        self.docker_repo = ''
        if docker is not None:
            self.docker_username = docker['username']
            self.docker_repo = docker['repo']
    
    @classmethod
    def load(cls, config: Path) -> Optional[Config]: 
        # load json
        config_json: Dict
        try:
            raw: str
            with config.open() as f:
                raw = f.read()
            config_json = loads(raw)
        except:
            return None
        # validate json
        latest: int
        stable: str
        releases: Dict[str,int]
        testing: Optional[Dict[str,List[str]]]
        docker: Optional[Dict[str,str]]
        repo: str
        try:
            latest = config_json['latest']
            assert type(latest) == int
            releases = config_json['releases']
            assert type(releases) == dict
            stable = config_json['stable']
            assert type(stable) == str
            assert releases.get(config_json['stable']) is not None
            repo = config_json['repo']
            assert type(repo) == str
            testing = config_json.get('testing')
            docker = config_json.get('docker')
        except:
            print(f'fetch_config.py: Config.load error '
                  f'{traceback.format_exc()}',
                  file=sys.stderr)
            return None
        return Config(latest, stable, releases, repo, testing=testing,
                      docker=docker)

    def to_json(self) -> str:
        out: List[Dict] = []
        out.append({
            'tag': 'latest',
            'revision': self.latest,
            'repo': self.repo
        })
        for release in self.releases:
            if release == self.stable:
                out.append({
                    'tag': 'stable',
                    'revision': self.releases[release],
                    'repo': self.repo
                })
            out.append({
                'tag': release,
                'revision': self.releases[release],
                'repo': self.repo
            })
        return dumps({'include': out})

def main(config_path: Path) -> Tuple[str,int]:
    out: Dict = {}
    if not config_path.exists():
        # can't find config
        print(f'fetch_config.py: can\'t find config ({config_path})',
              file=sys.stderr)
        return dumps(out), 1

    config: Optional[Config] = Config.load(config_path)
    if config is None:
        # bad config
        print(f'fetch_config.py: bad config ({config_path})', file=sys.stderr)
        return dumps(out), 2
    
    try:
        return config.to_json(), 0
    except:
        # issue converting to json
        print(f'fetch_config.py: json conversion error '
              f'{traceback.format_exc()}',
              file=sys.stderr)
        return dumps(out), 3
    
if __name__ == '__main__':
    config = Path(__file__).resolve().parent.parent / 'config.json'
    out, code = main(config)
    print(out)
    sys.exit(code)
