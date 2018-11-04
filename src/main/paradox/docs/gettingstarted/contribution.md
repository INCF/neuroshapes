# How to contribute

We would love for you to contribute to the Neuroshapes familly of data models and help make them even better than they are now!
As a contributor, find in the next sections the guidelines we would like you to follow.

## Got a Question or a Problem?
Please do not hesitate to open an issue [here](https://github.com/INCF/neuroshapes/issues) and join the INCF neuroshapes SIG at [INCF Special Interest Group on Neuroshapes](https://www.incf.org/activities/standards-and-best-practices/incf-special-interest-groups/incf-sig-on-neuroshapes-open).

## Found a Bug?
If you find a bug in the source code of any tools, in any schema or vocabulary in this repository, you can help us fix it by
[submitting an issue](#submit-issue) to our [GitHub Repository](https://github.com/INCF/neuroshapes). Even better, you can
[submit a Pull Request](#submit-pr) with a fix.

## Missing a Feature or a data model?
You can *request* them by [submitting an issue](#submit-issue) to our GitHub
Repository. If you would like to *implement* a new feature or *propose* a new data model specification, please submit an issue with a proposal for your work first, to be sure it can be implemented and most importantly, to trigger discussions and enable collaborations with interested people.
Please consider what kind of change it is:

* For **a Data Model Specification Proposal or Extension**, first open an issue and outline your proposal so that it can be discussed.

* **Data examples implementing/illustrating an existing Data Model** can be directly [submitted as a Pull Request](#submit-pr). For example different atlas releases conformant to the 
[atlas registration prov pattern](https://github.com/INCF/neuroshapes/blob/master/provpatterns/assets/atlas-registration-prov-template.svg) can be submitted.

* For a **Major Feature** related to the tools and scripts made available in this repository, first open an issue and outline your proposal so that it can be
discussed. This will also allow us to better coordinate our efforts, prevent duplication of work,
and help you to craft the change so that it is successfully accepted into the project.


* **Small Features** can be crafted and directly [submitted as a Pull Request](#submit-pr).

## Submission Guidelines
### Submitting an Issue
Before you submit an issue, please search the issue tracker, maybe an issue for your problem already
exists and the discussion might inform you of workarounds readily available.
We want to fix all the issues as soon as possible, but before fixing a bug we need to reproduce and
confirm it. In order to reproduce bugs we will need as much information as possible, and preferably
be in touch with you to gather information.

### Submitting a Data Model Specification
Before you submit your proposal consider the following guidelines:

* Please join the [INCF Special Interest Group (SIG) on Neuroshapes](https://www.incf.org/activities/standards-and-best-practices/incf-special-interest-groups/incf-sig-on-neuroshapes-open) before sending pull requests.
  Proposals are managed and reviewed by members of that INCF SIG.
 
* Open an issue and outline your proposal so that it can be discussed.




### Submitting a Pull Request (PR)
Before you submit your Pull Request (PR) consider the following guidelines:

* Please join the [INCF SIG on Neuroshapes]() before sending Pull requests.
  Proposals are managed and reviewed by members of that INCF SIG.


* Clone the Neuroshapes github repository:

```shell
    # Go to home
    cd  ~
    
    # Clone the repository
    git clone https://github.com/INCF/neuroshapes.git
    
    cd neuroshapes
    
```
    
* Make your changes in a new git branch:

     ```shell
     git checkout -b my-fix-branch master
     ```
* Create your patch, **including appropriate test cases**.

* Run the full test suite, and ensure that all tests pass.

    ```shell
    # Run 'sbt'
    sbt
    
    # Run 'test'
    test
    
    # Exit
    exit
    
    ```
* Commit your changes using a descriptive commit message.

     ```shell
     git commit -a
     ```
  Note: the optional commit `-a` command line option will automatically “add” and “rm” edited files.

* Push your branch to GitHub:

    ```shell
    git push origin my-fix-branch
    ```
* In GitHub, send a pull request to the `master` branch.

* If we suggest changes then:
  * Make the required updates.
  * Re-run the test suites to ensure tests are still passing.
  * Rebase your branch and force push to your GitHub repository (this will update your Pull Request):
    ```shell
    git rebase master -i
    git push -f
    ```
That’s it! Thank you for your contribution!
#### After your pull request is merged
After your pull request is merged, you can safely delete your branch and pull the changes
from the main (upstream) repository:
* Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:
    ```shell
    git push origin --delete my-fix-branch
    ```

* Check out the master branch:

    ```shell
    git checkout master -f
    ```

* Delete the local branch:
    ```shell
    git branch -D my-fix-branch
    ```

* Update your master with the latest upstream version:
    ```shell
    git pull --ff upstream master
    ```
    
## Join the INCF Neuroshape SIG

Join the [INCF Special Interest Group on Neuroshapes](https://www.incf.org/activities/standards-and-best-practices/incf-special-interest-groups/incf-sig-on-neuroshapes-open).
