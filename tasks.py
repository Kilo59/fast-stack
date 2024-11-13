from invoke.tasks import task
from invoke.context import Context


@task
def app(ctx: Context, prod: bool = False):
    """
    Run the FastAPI app.
    """
    cmds: list[str] = [
        "fastapi", "run" if prod else "dev", "fast_stack/app.py",
    ]
    ctx.run(" ".join(cmds), echo=True, pty=True)
