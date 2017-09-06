# Lab 2

## Some useful configuration

### Setting up Visual Studio Code as the default editor for git

There are many times when git will pop open an editor, we'll set up that editor to be Visual Studio code.

Setting it up ([thanks to this stack overflow answer](https://stackoverflow.com/questions/30024353/how-to-use-visual-studio-code-as-default-editor-for-git))

- Run `git config --global core.editor "code --wait"`
- Now running `git config --global -e` in the command line opens up the config options in VS Code.
- In the config options add

```
[diff]
    tool = default-difftool
[difftool "default-difftool"]
    cmd = code --wait --diff $LOCAL $REMOTE
```

### Bash prompt customization

We can customize the shell by adding to the `~/.bashrc` file. `~/.bashrc` is a bash script which is run whenever you open the terminal.

Two useful utilities for git:

- [git-completion.bash](https://github.com/git/git/blob/master/contrib/completion/git-completion.bash)
- [git-prompt.sh](https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh)

Copy these files into your home directory and add a `.` to the beginning of the names (e.g. `.git-completion.bash`), this will hide it. Then open up `~/.bashrc` and add

```
source $HOME/.git-completion.bash
source $HOME/.git-prompt.sh
PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '
```

`source` runs the specified file. For instance, after changing `~/.bashrc` if you enter `source ~/.bashrc` into the command line, it will run the `~/.bashrc` file and you should see your terminal prompt change.


## Reading
### Reading Assignment
Be sure to do the assignment associated with [this week's reading](https://berkeley-stat159-f17.github.io/stat159-f17/_static/ref/millman-perez.pdf). It's up on bcourses now. After reading write two paragraph-length responses

1. Summarizing the reading
2. Exploring something that interests you (e.g. one aspect in particular, something you disagree with)

### Programming Reading
Read chapter 1 of [Effective Computation in Physics](http://proquest.safaribooksonline.com/book/physics/9781491901564) to brush up on/learn command line basics. We won't be going over those in class/lab.