# Data Types
## User Story
**Title**: Short description of user story

**Description**: Detailed description of user story

**Priority**: MoSCow priority

![Must Have](https://img.shields.io/badge/_-Must%20Have-red?style=for-the-badge)
![Should Have](https://img.shields.io/badge/_-Should%20Have-orange?style=for-the-badge)
![Could Have](https://img.shields.io/badge/_-Could%20Have-yellow?style=for-the-badge)

## Task

**Title**: Description of task

**Status**: The status of the task

![Todo](https://img.shields.io/badge/_-Todo-BF4A8A?style=for-the-badge)
![in Progress](https://img.shields.io/badge/_-In%20Progress-D19821?style=for-the-badge)
![In Review](https://img.shields.io/badge/_-In%20Review-1F6EEB?style=for-the-badge)
![Done](https://img.shields.io/badge/_-Done-238636?style=for-the-badge)

**Sprint**: The sprint this task belongs to, if it has no sprint it is an unplanned task.

**Assignees**: The user responsible for the task

**Linked Pull requests**:  The pull request this tasks belongs to

**Completion Date**: The date this task was completed

# Pages
## User Stories
These are all user stories / features that need to be developed eventually.
They aren't affected by sprints and are simply descriptions of features.

## Backlog
All unplanned tasks.

## Overview
All tasks per sprint grouped by user story.

## Burndown Chart
Overview of the completion date of all tasks grouped by sprint sorted on completion date.

## Current Sprint
All tasks for the current sprint per user (or all users) where each column represents one of the four statuses.
Contains roughly the same data as the Overview.

# Usage

> [!IMPORTANT]
> Don't forget to set the label to either `User Story` or `Task` when creating an issue.
> Unlabelled issues will show up on every tab to prevent the issue from disappearing upon creation.


## Definition of status
### Todo
A task is in the `Todo` stage when the assigned user hasn't started working on this task yet.

### In Progress
A task is in the `In Progress` stage when this task is being worked on.

### In Review
A task is in the `In Review` stage when the assigned user thinks they are done with the task and have requested a review of the linked PR.

> [!NOTE]
> When changes are requested in the PR review the status will be reset to `In Progress` until a new review is requested.

### Done
A task is in the `Done` stage and ONLY in this stage if the PR is merged.

## Rules
Follow these rules when using the board to avoid problems and to ensure a smooth development process.

- Every PR must be linked to a task, and no more than 1 PR per task. If a task requires multiple PRs the task needs to be split up into smaller tasks.

- Upon completion of a task the `Completion Date` field must be set to the day the PR was merged.

- No negligence! Keep the project clean by using consistent capitalisation and update references when something has changed.
