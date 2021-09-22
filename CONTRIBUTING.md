Contributing to this project
============================

This project is really welcoming to community contributions. If you are
so kind as to lend us a hand, please take a few minutes to read the 
following guidelines.

General guidelines
-----------------------------

A few tips to make your contribution more effective.

* Read the documentation before asking.
* Discuss with the community before staring your contribution.
* When submitting issues provide enough details.

Project development workflow
-----------------------------

This project's development workflow is organized on the lines of GitFlow [1] 
branching strategy, GitHub Flow [2] contribution revision policy and Semantic 
Versioning [2] release naming scheme. If not familiar with those protocols,
you may find useful to check the pointed references.

In a nutshell, the latest, possibly unstable, revision resides in branch 
_develop_.

To propose some change, first create an entry in the project's issue tracking
system. Please, chose an appropriate label whether it be a bug report,
a feature request, documentation suggestion etc. You may either assign the
issue to someone or leave it open for anyone to handle it.

If you decide to work on some issue (either by you or by someone else),
assign it you to, then branch off from _develop_, edit the code in your
local branch as needed and, when done, push it to the upstream repository
and create a pull/merge request referring to the issue it is meant to address.
Your PR shall be discussed and revised by the community. If eventually
accepted, it shall be merged back into _develop_.

Do not submit PRs before creating a corresponding issue. 

PR branches may be of varying types. Name it

* `fix/foo`          if its a bug fix
* `feature/foo`      if it implements a new feature
* `src/foo`          if it improves the source code but not functionality
* `doc/foo`          if it improves documentation

From time to time, when the development reaches an agreed upon level of
maturity, a new branch _release_ is derived from the _develop_. Only bug
fixes and source improvement are allowed in this branch. Eventually it shall
be merged into a pre-release branch and, finally, in the _main_ (or _master_)
branch as the new stable releases.

Releases are named based on SemVer scheme like `major.minor.patch-stage+review`.
Increments in `patch`, `minor` or `major` means, respectively, that API is
unchanged, extended or broken. Stage may be alpha, beta, rc for, respectively, 
incomplete, complete but untested, or release-candidate pre-releases; 
if omitted, it means a stable release. Field `review` is for successive
revisions of legacy stable releases.

You are strongly encouraged to write your contribution and communicate
with the developers and contributors community in English, if possible.
Do not mind at all if your current English skills are modest or incipient; 
no one expects otherwise --- your coding skills and willing to help matter 
more. Use a automatic translator if needed. Just don't name variable and 
functions in a language other than English.

If you are a developer and is assigned an issue, and you believe you are not
able to handle timely, please, try to reassign it to someone else.

If you don't have direct write access to the repository, you may still fork the
project and send pull requests.

References
----------

[1] https://nvie.com/posts/a-successful-git-branching-model/

[2] https://docs.github.com/en/get-started/quickstart/github-flow

[3] https://semver.org/
