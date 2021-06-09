# Terraform-LocalStack

The purpose of this repository is to show how one can integrate the TF Testsuite, LocalStack and Jenkins.
It can verify Terraform code against Localstack in an automated fashion as described in the Jenkins file.

# Dependencies

- [Terraform-Testsuite](https://hub.docker.com/repository/docker/wirelab/terraform-testrunner)
- [LocalStack](https://hub.docker.com/r/localstack/localstack)
- [Jenkins](https://www.jenkins.io/)

# Content Overview

- **.gitignore**

Defines a list of excluded content committed to source code.

- **Jenkinsfile**

Defines pipeline steps.

- **LICENSE**

MIT license file.

- **main.tf**

Example Terraform file creating a single resource.

- **README.md**

This file.

- **versions.tf**

Declares the Terraform and AWS provider version.

- **tests/**

Folder where the unit test files are stored.

    - **__init__.py**
    Required file for the tests to run.

    - **e2e_tests.py**
    Python unit tests.

# How to use

In order to execute the Jenkins pipeline a job needs to pre-exist on the Jenkins server
however configuring this is out of the scope of this document.

To start experimenting clone this repo to the local machine `git clone git@github.com:david-wirelab/tf-localstack.git`.
Create a Jenkins job and point Git SCM to the Github repository.
Trigger a build and the pipeline will run to completion running one test as defined in `tests/e2e_test.py`.
