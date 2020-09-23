# encoding: UTF-8

import sys

sys.path.append("lib")  # noqa

from lib.workflow import Workflow3, Workflow, ICON_WARNING


def err(wf, title, subtitle=""):
    # type: (Workflow, unicode, unicode) -> int
    """
    Show error text and exit
    :param wf: Workflow instance
    :param title: Error message title
    :param subtitle: Error description
    :return: Exit code
    """
    wf.add_item(title=title, subtitle=subtitle, icon=ICON_WARNING)
    wf.send_feedback()
    return 0


def main(wf):
    # type: (Workflow) -> int

    # Implement your workflow here
    wf.add_item(title="Hey it works", subtitle="You're ready to rock")
    wf.send_feedback()


if __name__ == "__main__":
    workflow = Workflow3()
    sys.exit(workflow.run(main))
