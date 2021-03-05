"""Console script for interactive moco fastlog"""
import sys
import click
from os import environ
from datetime import datetime
from moco_wrapper import Moco
from moco_wrapper.util.response import ObjectResponse

@click.command()
def main(args=None):
    # load auth data from environment
    api_key = environ.get("MOCO_FASTLOG_API_KEY")
    domain = environ.get("MOCO_FASTLOG_DOMAIN")
    moco = Moco(auth={
        "domain": domain,
        "api_key": api_key
    })

    projects_avail = moco.Project.assigned().items
    for i, p in enumerate(projects_avail):
        click.echo("[{}]: {}".format(i, p.name))

    # retrieve projects
    project_index = click.prompt("> Which Project would you like to log time on?", type=int)
    project_selected = projects_avail[project_index]
    click.echo("Project \"{}\" selected".format(project_selected.name))

    # retrieve project tasks
    tasks_avail = moco.ProjectTask.getlist(project_selected.id).items
    for i, t in enumerate(tasks_avail):
        click.echo("[{}]: {}".format(i, t.name))
    tasks_index = click.prompt("> Which Task would you like to log time on?", type=int)
    task_selected = tasks_avail[tasks_index]

    # create activity for the task
    click.echo("Create Activity for Project \"{}\", Task \"{}\"".format(project_selected.name, task_selected.name))
    activity_description = click.prompt("Activity Description", type=str)
    activity_hours = click.prompt("Activity Time (Enter in Hours, 0.5 for 30m)", type=float)

    result = moco.Activity.create(
        activity_date=datetime.now(),
        project_id=project_selected.id,
        task_id=task_selected.id,
        hours=activity_hours,
        description=activity_description
    )

    if isinstance(result, ObjectResponse):
        click.echo("Activity created successfully")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
