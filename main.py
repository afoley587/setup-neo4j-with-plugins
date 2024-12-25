import argparse
import subprocess
import sys

from typing import List, Tuple


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Setup Neo4j Actions",
        description="Sets up Neo4j within a GitHub Action",
    )
    parser.add_argument(
        "-t", "--tag", help="Neo4j docker tag to run.", default="latest", type=str
    )
    parser.add_argument(
        "-p",
        "--plugins",
        help="Comma separated list of Neo4j plugins to install",
        default="",
        nargs="?",
        type=str,
    )
    return parser.parse_args()


def run_docker_container(tag: str, plugins: List[str]) -> Tuple[str, int]:
    cmd = [
        "docker",
        "run",
        "-d",
    ]

    if len(plugins) > 0:
        plugins_fmt = "[" + ",".join([f'"{p}"' for p in plugins]) + "]"
        cmd += ["-e", f"NEO4J_PLUGINS={plugins_fmt}"]

    cmd += ["-e", "NEO4J_AUTH=none", f"docker.io/neo4j:{tag}"]

    try:
        # Run the Docker command and capture the return code
        result = subprocess.run(
            cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return result.stdout.decode().strip(), result.returncode
    except subprocess.CalledProcessError as e:
        # Capture and log the error if the command fails
        print(f"Error running Docker command: {e.stderr.decode()}")
        return "", e.returncode


def main():
    args = parse_args()

    tag = args.tag.strip().lower()

    plugins = args.plugins

    if args.plugins:
        plugins = args.plugins.strip().lower().split(",")
    else:
        plugins = []

    container, rc = run_docker_container(tag, plugins)
    return container, rc


if __name__ == "__main__":
    container, rc = main()

    if rc == 0:
        print(container)

    sys.exit(rc)
