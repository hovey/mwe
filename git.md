# Git

hello world!

## Git for Windows

- [ ] Download [Git for Windows](https://gitforwindows.org)
  * As of 2023-10-01, we recommended `Git-2.42.0.2-64-bit.exe`
    * sha-256: bd9b41641a258fd16d99beecec66132160331d685dfb4c714cea2bcc78d63bdb

```bash
# Use powershell to check the sha value
PS C:\Users\UserName> Get-fileHash C:\Users\UserName\Downloads\Git-2.42.0.2-64-bit.exe

# The results should appear as follows:
Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          bd9b41641a258fd16d99beecec66132160331d685dfb4c714cea2bcc78d63bdb       C:\Users\UserName\Downloads\Git-2.42.0.2-64-bit.exe
```

## Git for macOS

- [ ] Install [xcode](https://apps.apple.com/us/app/xcode/id497799835?mt=12) from the App Store.
  * From the terminal `xcode-select install`.
  * This will install git 
    * Alternatively, for brew users, `brew install git` can be used, but xcode is still the recommended option.

As of 2023-10-09, the version of Git for macOS is as follows:

```bash
s1060600:~ chovey$ git --version
git version 2.39.2 (Apple Git-143)
```

## Configure Name and Email

Set the Git global user name and email.  We recommend using the Git Bash shell on Windows, and a standard Bash shell on macOS and Linux.  

```bash
git config --global user.name "your full name here"
git config --global user.email "your email here"

# example
git config --global user.name "John Doe"
git config --global user.email "john.doe@gmail.com"
```

See also [Multi-User Configuration](#multi-user-configuration) for advanced user settings.

## ssh

The local machine can be configured to easily communicate with the repo through the 
use of ssh public/private pairs.

```bash
# If the ~/.ssh folder already exists, be careful not to make new public/private key pairs that may overwrite existing pairs.

# The following instructions whether or not the ~/.ssh folder already exists, and will
# overwrite any existing pairs with the same name.

# On Windows, we recommend using the Git Bash shell.  For macOS and Linux, we recommend  the Bash shell

cd ~  # from the home directory
ssh-keygen -t ecdsa-sha2-nistp256

Generating public/private ecdsa-sha2-nistp256 key pair.

Enter file in which to save the key (~/.ssh/id_ecdsa):
Created directory '~/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in ~/.ssh/id_ecdsa
Your public key has been saved in ~/.ssh/id_ecdsa.pub
The key fingerprint is:
SHA256:XXXXXXXXXXXXXXXXXXXXXXXXXX user_name@machine_name
The key's randomart image is:
+---[ECDSA 256]---+
| xx.3.2.2.       |
| xx.   ...   ..  |
| ..  k           |
| ..  k           |
| xx.   ...   ..  |
| // xx... .. ..  |
+----[SHA256]-----+
```

Start the ssh-agent 
```bash
eval "$(ssh-agent -s)"    # required on macOS and Linux, but we found it was not required on Windows
```

For macOS, Chad had to complete the following extra steps:

```bash
ssh-add --apple-use-keychain ~/.ssh/id_ecdsa

# update the .ssh/config file
# from
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ecdsa

# to
Host github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ecdsa
Host cee-gitlab.sandia.gov
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ecdsa
```

On the GitLab repo, in the top right corner, select the User Profile icon, then select `Edit proile`, on the left panel, open the sidebar (if it is minimized), select `SSH Keys`.

Copy the contents of the public key file, `id_ecdsa.pub`, to cee-gitlab on the User Settings > SSH Keys page

Test that the connection to the repo works:

```bash
s1060600:.ssh chovey$ ssh -T git@cee-gitlab.sandia.gov

...
<--snip-->
...

Welcome to GitLab, @chovey!
s1060600:.ssh chovey$
```

## Cloning Repositories

Clone a repo:

```bash
git clone git@cee-gitlab.sandia.gov:some_repo/repo_name.git
```

## Git LFS

What is Git LFS?

* Git Large File Storage (LFS) is an extension for Git that provides versioning of large files.
Using Git LFS allows users to keep their repository a manageable size, makes the 
repo clone and fetch steps faster, all while keeping the same familiar Git workflow, 
with the same level of permissions control.
* The [Git LFS Tutorial](https://github.com/git-lfs/git-lfs/wiki/Tutorial) provides a nice
walk through.

The Git LFS server is already built into GitHub and GitLab, so only the Git LFS client
needs to be installed on one's local machine.

- [ ] Install the [Git LFS Client](https://git-lfs.com)

After installation, set up Git LFS on your local user account:

```bash
git lfs install  # this step only needs to be done once per user account

# example
chovey@s1060600/Users/chovey> git lfs install
Git LFS initialized.
```

Verify the version of Git LFS is 2.0 or later:

```bash
chovey@s1060600/Users/chovey/demo/exodus> git lfs version
git-lfs/3.4.0 (GitHub; darwin amd64; go 1.20.6)
```

Verify that these four additional hooks are installed:

```bash
# example
chovey@s1060600/Users/chovey/demo/.git/hooks> ll
total 152
# new hooks after 'git lfs install'
-rwxr-xr-x@ 1 chovey  351B Oct  5 10:27 post-checkout*
-rwxr-xr-x@ 1 chovey  347B Oct  5 10:27 post-commit*
-rwxr-xr-x@ 1 chovey  345B Oct  5 10:27 post-merge*
-rwxr-xr-x@ 1 chovey  341B Oct  5 10:27 pre-push*
# preexisting hooks
-rwxr-xr-x@ 1 chovey  478B Oct  3 15:46 applypatch-msg.sample*
-rwxr-xr-x@ 1 chovey  896B Oct  3 15:46 commit-msg.sample*
-rwxr-xr-x@ 1 chovey  4.6K Oct  3 15:46 fsmonitor-watchman.sample*
-rwxr-xr-x@ 1 chovey  189B Oct  3 15:46 post-update.sample*
-rwxr-xr-x@ 1 chovey  424B Oct  3 15:46 pre-applypatch.sample*
-rwxr-xr-x@ 1 chovey  1.6K Oct  3 15:46 pre-commit.sample*
-rwxr-xr-x@ 1 chovey  416B Oct  3 15:46 pre-merge-commit.sample*
```

Select the file types for Git LFS to manage, for example, we set Git LFS to manage 
`.stl` and `.g` (Exodus) files:

```bash
git lfs track "*.stl"
Tracking "*.stl"

git lfs track "*.g"
Tracking "*.g"

# example
chovey@s1060600/Users/chovey/demo> git lfs track "*.stl"
Tracking "*.stl"
chovey@s1060600/Users/chovey/demo> git lfs track "*.g"
Tracking "*.g"
```

A new file called `.gitattributes` will appear in the repo:

```bash
# example
chovey@s1060600/Users/chovey/demo> vim .gitattributes

*.stl filter=lfs diff=lfs merge=lfs -text
*.g filter=lfs diff=lfs merge=lfs -text
```

Add the `.gitattributes` file to the repo:

```bash
git add .gitattributes  # add, then commit and push

# example
git commit -m 'gitattributes as part of lfs'; git push
...

# finally add some geometry files
chovey@s1060600/Users/chovey/demo/exodus> ll
total 28504
-rw-r-----@ 1 chovey  9.3M Dec 16  2020 some_file_1.g
-rw-r-----@ 1 chovey  2.8M Dec 16  2020 some_file_2.g
-rw-r-----@ 1 chovey  1.8M Dec 16  2020 some_file_3.g
chovey@s1060600/Users/chovey/demo/exodus> git add *.g
chovey@s1060600/Users/chovey/demo/exodus> git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   some_file_1.g
	new file:   some_file_1.g
	new file:   some_file_1.g

chovey@s1060600/Users/chovey/demo/exodus> git commit -m 'exodus files via LFS'
[main b296382] exodus files via LFS
 3 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 demo/exodus/some_file_1.g
 create mode 100644 demo/exodus/some_file_2.g
 create mode 100644 demo/exodus/some_file_3.g
chovey@s1060600/Users/chovey/demo/exodus> git push
```

Note the presence of the "**LSF**" next to the file name on the repo.

Finally, run `git lfs ls-files` to see a list of Git LFS tracked files:

```bash
# example
chovey@s1060600/Users/chovey/demo/exodus> git lfs ls-files
87d7c1afaa * exodus/some_file_1.g
17227d9ff8 * exodus/some_file_2.g
107844a776 * exodus/some_file_3.g
```

Note: The git-lfs service on the HPC is installed as a module.  Use `module load` as follows:

```bash
# formerly: module load git-lfs/git-lfs
module load aue/git-lfs
git lfs install
```

## Most-Used Git Commands

Below are the  most-used Git commands:

```bash
git clone repo_resource_name.git   # example: git clone git@cee-gitlab.sandia.gov:some_repo/repo_name.git
git status                         # shows which files on the local differ from the repo server

git pull                           # update local to match current state of repo server

git diff <filename.ext>            # shows updates from repo version to local version
git add <filename.ext>             # example: git add README.md

git commit -m "your message here"  # example: git commit -m "update README.md with most-used commands"
git push                           # items staged from the commit are pushed up to the repo
```

## Git Branch

Branches are created, typically off the `main` branch, to isolate updates while keeping the main branch in an always-deployable state.   In general, branches are a recommended best practice, but overuse or failure to merge the branch back into `main` within reasonble time intervals (e.g., weeks) can result in branches that are impossible to merge back into `main`, by virtue of `main` evolving signficant since the time the branch was created.  

Below are some commonly used Git branch commands, shown by way of example:

```bash
# show existing branches
> git branch

    # example
    > git branch  # show existing branches, '*' is current branch
      develop
      feature/dat-to-yaml
      feature/square_root
    * main
      yml_refactor


# change branches
> git checkout <branch_name>

    # example
    > git checkout yml_refactor
    Switched to branch 'yml_refactor'
    Your branch is up to date with 'origin/yml_refactor'.
    > git branch  # show existing branches, '*' is current branch
      develop
      feature/dat-to-yaml
      feature/square_root
      main
    * yml_refactor


# create a new branch
> git branch <new_branch_name>

    # example
    > git branch json_testing  # creates the new branch

    > git branch  # shows existing branches
      develop
      feature/dat-to-yaml
      feature/square_root
    * main
      json_testing
      yml_refactor

    > git branch json_refactor  # switch to the json_refactor branch


# tell GitLab try track a new branch
> git push origin <new_branch_name>  # let GitLab track the local branch

    # example
    > git push origin json_refactor


# sync GitLab's new branch to your local new branch
> git push --set-upstream origin <new_branch_name>

    # example
    > git push --set-upstream origin yaml_testing
    Branch 'yaml_testing' set up to track remote branch 'yaml_testing' from 'origin'.


# develop new code on new branch
    # example
    > vim new_file.json  # develop content
    > git add new.json
    > git commit -m 'proposed new json content'
    > git push


# create a merge request on the GitLab GUI (not done locally)

# After the GitLab repo owner does the merge 
# then delete the local branch ...

# move to the main branch, then delete a branch
> git checkout main
> git branch --delete <branch_name>

    # examples
    > git checkout main
    > git branch --delete feature/json_refactor
    > git branch -d gui_experiment  # -d is equivalent to --delete
```

## Git Rebase

```sh
git checkout main
git pull

git checkout my-branch-name
git fetch origin
git rebase origin/main

# resolve any conflicts, check if conflicts with
git status

# after resolving, stage the changes
git add resolve-files

# then continue with the rebase
git rebase --continue

# if there are more conflicts, repeat above as necessary, then
git push origin my-branch-name
```

## Distribution

The distribution steps will tag the code state as a release version, with a
semantic version number, build the code as a wheel file, and publish to the wheel
file as a release to GitLab.

### Git Tag

View existing tags, if any,

```bash
git tag
```

Create a tag.  Tags can be *lightweight* or *annotated*.
Annotated tags are recommended since they store tagger name, email, date, and
message information.  Create an annotated tag:

```bash
# example of an annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"
```

Push the tag to the repo

```bash
# example continued
git push origin v1.0.0
```

Verify the tag appears on the repo, found on the Code > Tags section.

### Build

Ensure that `setuptools` and `build` are installed,

```bash
pip install setuptools build
```

Navigate to the project directory, where the `pyproject.toml` file is located
and create a wheel distribution.

```bash
# generates a .whl file in the dist directory
python -m build --wheel
```

## Multi-User Configuration

*Optional*

* This example uses Chad's local machine `s1060600` to setup a Git user name and email 
  * for his open source repository work (default), and
  * for his Sandia work (folder specific)
    * for example, with cee-gitlab for work on the Pygators engine repository.

On `s1060600`, update the Git global `~/.gitconfig` file:

```bash
# from
[user]
  name = Chad Hovey
  email = chad.hovey@stanfordalumni.org

# to
[user]
  name = Chad Hovey
  email = chad.hovey@stanfordalumni.org
[includeIf "gitdir:~/pygators/engine/"]
  path = ~/pygators/engine/.gitconfig
```

Then, in the `~/pygators/engine/.gitconfig` file, create a specific user name and email:

```bash
[user]
  name = Chad Brian Hovey
  email = chovey@sandia.gov
```

**Warning:**  Do not check your local `.gitconfig` folder into the repo, as it can the overwrite others' local `.gitconfig` when they pull the repo.  The `.gitignore` file in the repo should help to avoid checking in your personal `.gitconfig` file, since the `.gitignore` file indicates to ignore `.gitconfig` files.
