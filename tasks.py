from invoke.context import Context
from invoke.tasks import task


@task
def app(ctx: Context, prod: bool = False) -> None:
    """
    Run the FastAPI app.
    """
    cmds: list[str] = [
        "fastapi",
        "run" if prod else "dev",
        "fast_stack/app.py",
    ]
    ctx.run(" ".join(cmds), echo=True, pty=True)


@task(aliases=["docker"])
def container(
    ctx: Context, build: bool = False, run: bool = False, port: int = 8000
) -> None:
    """
    Build and run the Docker container.
    """
    if build:
        ctx.run("docker build -t faststack .", echo=True)
    if run:
        print(f"Running at...\nhttp://localhost:{port}\n")
        ctx.run(f"docker run --publish {port}:80 faststack", echo=True)
