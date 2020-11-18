# Git Workflow

What is a Git Workflow? Git is a Version Control System -- for this project, we'll be following a set of guidelines on how we each contribute to the project using Git.

You can refer to this diagram for our general workflow:

![git diagram](https://raw.githubusercontent.com/grasshopperfund/grasshopperfund/705c1dd3fa65c3d299079e8e41117c8d4cf98f85/docs/images/git-flow-diagram.svg)

Things to notice:

* No direct commits to main
* Your work is done on a `feature` branch that you make
* The `feature` branch is made from the `dev` branch (switch to it before branching)
* When your done, make a Pull Request from your `feature` branch back to `dev`.

For more information about our workflow and Git, checkout this guide I made: [ICSSC @ UCI Git With the Flow](https://www.notion.so/Git-With-The-Flow-1c62521d9fb747a1ae9ce0f4ecf6bcdb)
